# -*- coding: utf-8 -*-
"""
Publica en Instagram los posteos COMERCIALES de EGC cuya fecha y hora ya llegaron.
Lo corre GitHub Actions (.github/workflows/publicar-comerciales.yml). No usa Metricool.

Cola: comerciales/posts/AAAA-MM-DD-HHMM-slug.jpg + .txt (hora de Buenos Aires).
La placa .jpg la genera comerciales/generar_placas.py desde comerciales/placas/<mismo nombre>.py.
Registro: comerciales/publicados.md (una línea por posteo publicado o fallido).
Clave: secreto IG_TOKEN (token de Instagram, nunca en el repositorio).
"""
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

IG_USER_ID = '17841433372262211'  # @egc_eletric_global_cost
RAW = 'https://raw.githubusercontent.com/Priscilababy/egc-instagram/main/comerciales/posts/'
AQUI = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(AQUI, 'posts')
REGISTRO = os.path.join(AQUI, 'publicados.md')
BA = dt.timezone(dt.timedelta(hours=-3))
NOMBRE = re.compile(r'^(\d{4}-\d{2}-\d{2})-(\d{2})(\d{2})-[a-z0-9-]+$')


def pedir(metodo, url, datos=None):
    cuerpo = urllib.parse.urlencode(datos).encode() if datos else None
    req = urllib.request.Request(url, data=cuerpo, method=metodo)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{e.code}: {e.read().decode()[:500]}')


def ya_registrados():
    if not os.path.exists(REGISTRO):
        return set()
    return set(re.findall(r'`([^`]+)`', open(REGISTRO, encoding='utf-8').read()))


def registrar(linea):
    nuevo = not os.path.exists(REGISTRO)
    with open(REGISTRO, 'a', encoding='utf-8') as f:
        if nuevo:
            f.write('# Posteos comerciales publicados\n\n')
        f.write(linea + '\n')


def api(token):
    # Token de Instagram (empieza con IG) -> graph.instagram.com; token de Meta (EAA...) -> graph.facebook.com
    return 'https://graph.instagram.com/v21.0' if token.startswith('IG') else 'https://graph.facebook.com/v21.0'


def publicar(token, base):
    API = api(token)
    txt = open(os.path.join(POSTS, base + '.txt'), encoding='utf-8').read().rstrip()
    if len(txt) > 2200:
        raise RuntimeError(f'texto de {len(txt)} caracteres (máximo 2200)')
    url_img = RAW + base + '.jpg'
    for _ in range(6):  # la imagen tiene que estar online
        try:
            with urllib.request.urlopen(url_img, timeout=30) as r:
                if r.status == 200:
                    break
        except Exception:
            pass
        time.sleep(15)
    else:
        raise RuntimeError(f'la imagen no responde: {url_img}')
    cont = pedir('POST', f'{API}/{IG_USER_ID}/media', {'image_url': url_img, 'caption': txt, 'access_token': token})['id']
    for _ in range(20):
        estado = pedir('GET', f'{API}/{cont}?fields=status_code&access_token={token}').get('status_code')
        if estado == 'FINISHED':
            break
        if estado == 'ERROR':
            raise RuntimeError('Instagram rechazó la imagen')
        time.sleep(10)
    pub = pedir('POST', f'{API}/{IG_USER_ID}/media_publish', {'creation_id': cont, 'access_token': token})['id']
    link = pedir('GET', f'{API}/{pub}?fields=permalink&access_token={token}').get('permalink', '')
    return link


def main():
    token = os.environ.get('IG_TOKEN', '').strip()
    if not token:
        sys.exit('Falta el secreto IG_TOKEN')
    if os.environ.get('PRUEBA') == '1':
        d = pedir('GET', f'{api(token)}/{IG_USER_ID}?fields=username&access_token={token}')
        print('Conexión OK con Instagram:', d.get('username'))
        return
    ahora = dt.datetime.now(BA)
    hechos = ya_registrados()
    pendientes = []
    for f in sorted(os.listdir(POSTS)):
        base, ext = os.path.splitext(f)
        m = NOMBRE.match(base)
        if ext != '.jpg' or not m or base in hechos:
            continue
        cuando = dt.datetime.strptime(f'{m[1]} {m[2]}:{m[3]}', '%Y-%m-%d %H:%M').replace(tzinfo=BA)
        # solo lo que ya llegó y no tiene más de 12 h de atraso (no publicar cosas viejas de golpe)
        if cuando <= ahora <= cuando + dt.timedelta(hours=12):
            pendientes.append(base)
    if not pendientes:
        print('Nada para publicar ahora.')
        return
    base = pendientes[0]  # uno por corrida, para no amontonar
    hora = ahora.strftime('%Y-%m-%d %H:%M')
    try:
        link = publicar(token, base)
        registrar(f'- {hora} · PUBLICADO · `{base}` · {link}')
        print('Publicado:', base, link)
    except Exception as e:
        registrar(f'- {hora} · ERROR · `{base}` · {str(e)[:300]}')
        print('ERROR:', base, e)
        sys.exit(1)


if __name__ == '__main__':
    main()
