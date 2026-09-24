# -*- coding: utf-8 -*-
"""
Biblioteca de placas EGC para Instagram (1080 x 1350, formato 4:5).

Uso típico (ver ejemplo_ventilador.py y ejemplo_neutros.py):

    from placa import *
    s = encabezado('VENTILADOR DE TECHO', 'CON LUZ')
    s += tablero()                     # ID 30 mA · IT 10 A · N · PE
    s += cable([(440,363),(440,450),(260,450),(260,503)], CAST)
    ...
    s += firma()
    guardar(s, '../posts/2026-09-25-tema.png')

Reglas de diseño (NO romperlas):
- Texto mínimo 32 px. Títulos 58-64 px. Rótulos principales 40-60 px.
- Logo EGC siempre abajo a la izquierda (firma()).
- Colores AEA (Tabla 770.10.XIII): fase castaño; celeste SOLO neutro; verde-amarillo SOLO PE.
  Retornos y viajeros: color NO reservado, punteado (RET gris, RET2 violeta).
  No dibujar retornos en negro ni rojo: son colores de fase (ver conocimiento/03).
- Nada de texto que se superponga. Revisar el PNG antes de publicar.
"""
import base64
import os
import shutil
import subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
ANCHO, ALTO = 1080, 1350

# Paleta
NAVY = '#132B47'      # encabezado y contornos
AMARILLO = '#F2B90F'  # franja y acentos
CAST = '#7B4A21'      # fase (castaño)
CEL = '#5BC4F0'       # neutro (celeste)
CEL_TXT = '#2A8FD0'   # texto del neutro
VERDE = '#22A04B'     # PE
AMAR_PE = '#F2CE1A'   # franja amarilla del PE
RET = '#6E6E6E'       # retorno / viajero (gris: color no reservado)
RET2 = '#8E44AD'      # segundo retorno / viajero (violeta: color no reservado)
NEG = '#1E1E1E'       # negro = fase S (L2). No usar para retornos
ROJO = '#D7141A'      # chip "MAL" y alertas. No usar para retornos (rojo = fase T)
VERDE_OK = '#1E8E48'  # "bien"
GRIS = '#8A95A3'
W = 12                # grosor de cable

FUENTE = "Liberation Sans, DejaVu Sans, Arial, sans-serif"


def encabezado(linea1, linea2=None, linea2_amarilla=True):
    """Encabezado azul con título en 1 o 2 líneas y tarjeta blanca de fondo."""
    s = (f'<rect width="{ANCHO}" height="{ALTO}" fill="#ECEFF2"/>'
         f'<rect width="{ANCHO}" height="180" fill="{NAVY}"/>'
         f'<rect y="180" width="{ANCHO}" height="8" fill="{AMARILLO}"/>')
    if linea2:
        s += f'<text x="50" y="96" font-size="60" font-weight="bold" fill="#FFF">{linea1}</text>'
        color2 = AMARILLO if linea2_amarilla else '#FFF'
        s += f'<text x="50" y="160" font-size="60" font-weight="bold" fill="{color2}">{linea2}</text>'
    else:
        s += f'<text x="50" y="120" font-size="64" font-weight="bold" fill="#FFF">{linea1}</text>'
    s += '<rect x="30" y="210" width="1020" height="1020" rx="28" fill="#FFF" stroke="#DDE2E8" stroke-width="3"/>'
    return s


def tablero(id_txt='ID 30 mA', it_txt='IT 10 A'):
    """Fila del tablero. Salidas: IT abajo en (440,363), N en (700,363), PE en (920,363)."""
    return (f'<rect x="45" y="228" width="990" height="150" rx="16" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
            f'<rect x="60" y="243" width="240" height="120" rx="10" fill="#FFF" stroke="{NAVY}" stroke-width="4"/>'
            f'<text x="180" y="318" font-size="42" font-weight="bold" fill="{NAVY}" text-anchor="middle">{id_txt}</text>'
            f'<line x1="300" y1="303" x2="320" y2="303" stroke="{NAVY}" stroke-width="4"/>'
            f'<rect x="320" y="243" width="240" height="120" rx="10" fill="#FFF" stroke="{NAVY}" stroke-width="4"/>'
            f'<text x="440" y="318" font-size="42" font-weight="bold" fill="{NAVY}" text-anchor="middle">{it_txt}</text>'
            f'<rect x="620" y="243" width="160" height="120" rx="10" fill="#FFF" stroke="{CEL_TXT}" stroke-width="4"/>'
            f'<text x="700" y="325" font-size="60" font-weight="bold" fill="{CEL_TXT}" text-anchor="middle">N</text>'
            f'<rect x="820" y="243" width="200" height="120" rx="10" fill="#FFF" stroke="{VERDE}" stroke-width="4"/>'
            f'<text x="920" y="325" font-size="60" font-weight="bold" fill="{VERDE}" text-anchor="middle">PE</text>')


def cable(puntos, color, punteado=False):
    """Cable como polilínea. puntos = [(x,y), ...]."""
    p = ' '.join(f'{x},{y}' for x, y in puntos)
    dash = ' stroke-dasharray="28 16"' if punteado else ''
    return (f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{W}"'
            f' stroke-linejoin="round"{dash}/>')


def cable_pe(puntos):
    """Conductor de protección verde-amarillo."""
    p = ' '.join(f'{x},{y}' for x, y in puntos)
    return (f'<polyline points="{p}" fill="none" stroke="{AMAR_PE}" stroke-width="{W}" stroke-linejoin="round"/>'
            f'<polyline points="{p}" fill="none" stroke="{VERDE}" stroke-width="{W}" stroke-dasharray="22 22" stroke-linejoin="round"/>')


def borne(x, y, color):
    """Borne cuadrado de 34 px centrado en (x,y)."""
    return f'<rect x="{x-17}" y="{y-17}" width="34" height="34" rx="5" fill="{color}"/>'


def caja(x, y, w, h, titulo, tam=36):
    """Caja blanca con cabecera azul (para llaves, aparatos, etc.). Cabecera de 72 px."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
            f'<path d="M{x},{y+20} a20,20 0 0 1 20,-20 h{w-40} a20,20 0 0 1 20,20 v52 h-{w} z" fill="{NAVY}"/>'
            f'<text x="{x + w/2}" y="{y+50}" font-size="{tam}" font-weight="bold" fill="#FFF" text-anchor="middle">{titulo}</text>')


def texto(x, y, t, tam=40, color=NAVY, ancla='start', negrita=True):
    peso = ' font-weight="bold"' if negrita else ''
    return f'<text x="{x}" y="{y}" font-size="{tam}"{peso} fill="{color}" text-anchor="{ancla}">{t}</text>'


def ancho_texto(t, tam, negrita=True):
    """Ancho en px de un texto con Liberation Sans (Pillow si está; si no, estimación conservadora)."""
    try:
        from PIL import ImageFont
        archivo = 'LiberationSans-Bold.ttf' if negrita else 'LiberationSans-Regular.ttf'
        return ImageFont.truetype(os.path.join(AQUI, 'fuentes', archivo), tam).getlength(t)
    except Exception:
        return len(t) * tam * 0.62


def mensaje(lineas, x=60, y=890, ancho=None, tam=40):
    """Recuadro amarillo con la idea clave (máx. 3 líneas cortas). El ancho se ajusta a la línea más larga."""
    if ancho is None:
        ancho = int(max(ancho_texto(l, tam) for l in lineas) + 2 * 26 + 10)
    alto = 50 + 60 * len(lineas)
    s = f'<rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="18" fill="#FFF6D6" stroke="{AMARILLO}" stroke-width="4"/>'
    for i, l in enumerate(lineas):
        s += texto(x + 26, y + 65 + 60 * i, l, tam)
    return s


def chip(x, y, t, color, tam=40):
    """Etiqueta de color (p. ej. 'MAL' en rojo, 'BIEN' en verde)."""
    ancho = 36 + int(tam * 0.68) * len(t)
    return (f'<rect x="{x}" y="{y}" width="{ancho}" height="{tam + 18}" rx="14" fill="{color}"/>'
            f'<text x="{x+14}" y="{y + tam + 1}" font-size="{tam}" font-weight="bold" fill="#FFF">{t}</text>')


def firma(pie='AEA 90364'):
    """Logo EGC abajo a la izquierda + referencia abajo a la derecha."""
    with open(os.path.join(AQUI, 'logo-egc-light.png'), 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    # logo 520x223 -> 250 x 107
    return (f'<image x="50" y="1238" width="250" height="107" href="data:image/png;base64,{b64}"'
            f' xlink:href="data:image/png;base64,{b64}" preserveAspectRatio="xMinYMid meet"/>'
            f'<text x="1030" y="1305" font-size="32" font-weight="bold" fill="{GRIS}" text-anchor="end">{pie}</text>')


def svg(cuerpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" font-family="{FUENTE}">'
            f'{cuerpo}</svg>')


# ─────────────────────────── Render ───────────────────────────

def _fuentes():
    d = os.path.join(AQUI, 'fuentes')
    return [os.path.join(d, f) for f in os.listdir(d) if f.lower().endswith('.ttf')]


def _con_resvg(svg_txt, png):
    import resvg_py  # pip install resvg-py
    out = resvg_py.svg_to_bytes(svg_string=svg_txt, font_files=_fuentes(), skip_system_fonts=False)
    if isinstance(out, str):          # algunas versiones devuelven base64
        out = base64.b64decode(out)
    elif isinstance(out, list):
        out = bytes(out)
    with open(png, 'wb') as f:
        f.write(out)


def _con_cairosvg(svg_txt, png):
    import cairosvg  # pip install cairosvg (requiere libcairo2)
    cairosvg.svg2png(bytestring=svg_txt.encode('utf-8'), write_to=png, output_width=ANCHO, output_height=ALTO)


def _con_rsvg(svg_txt, png):
    if not shutil.which('rsvg-convert'):  # apt-get install -y librsvg2-bin
        raise RuntimeError('rsvg-convert no instalado')
    tmp = png[:-4] + '.svg'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(svg_txt)
    subprocess.run(['rsvg-convert', '-w', str(ANCHO), '-h', str(ALTO), '-o', png, tmp], check=True)


def _con_playwright(svg_txt, png):
    from playwright.sync_api import sync_playwright  # pip install playwright
    html = f'<!doctype html><html><body style="margin:0">{svg_txt}</body></html>'
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': ANCHO, 'height': ALTO})
        pg.set_content(html)
        pg.wait_for_timeout(500)
        pg.screenshot(path=png)
        b.close()


def guardar(cuerpo, png):
    """Arma el SVG y lo convierte a PNG probando varios motores. Devuelve el motor usado."""
    os.makedirs(os.path.dirname(os.path.abspath(png)), exist_ok=True)
    s = svg(cuerpo)
    errores = []
    for nombre, fn in (('resvg', _con_resvg), ('cairosvg', _con_cairosvg),
                       ('rsvg-convert', _con_rsvg), ('playwright', _con_playwright)):
        try:
            fn(s, png)
            if os.path.getsize(png) > 10_000:
                print(f'PNG generado con {nombre}: {png}')
                return nombre
        except Exception as e:  # probar el siguiente motor
            errores.append(f'{nombre}: {e}')
    raise RuntimeError('No se pudo renderizar el PNG:\n' + '\n'.join(errores))
