# -*- coding: utf-8 -*-
"""
Placas COMERCIALES de EGC (1080 x 1350). Estilo propio, distinto de las técnicas:
negro + rojo + blanco (colores de marca). Mismas reglas: texto >= 32 px, logo abajo a la izquierda.

    from comercial import *
    s = cabecera('DEL TABLERO', 'AL UNIFILAR EN PDF')
    s += paso(1, 300, 'Cargás cada circuito', 'Potencia y largo. Nada más.')
    s += cta()
    guardar(s, '../comerciales/posts/AAAA-MM-DD-slug.png')
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'generador'))
from placa import ANCHO, ALTO, texto, ancho_texto, firma, guardar  # noqa: F401

NEGRO = '#141414'
ROJO_EGC = '#D7141A'
GRIS_T = '#4A4A4A'
FONDO = '#F4F4F4'


def cabecera(linea1, linea2=None, etiqueta=None):
    """Franja negra con título blanco (1 o 2 líneas) y raya roja. etiqueta = chip rojo opcional (ej. 'NUEVO')."""
    s = (f'<rect width="{ANCHO}" height="{ALTO}" fill="{FONDO}"/>'
         f'<rect width="{ANCHO}" height="250" fill="{NEGRO}"/>'
         f'<rect y="250" width="{ANCHO}" height="12" fill="{ROJO_EGC}"/>')
    y1 = 125 if linea2 else 165
    if etiqueta:
        w = int(ancho_texto(etiqueta, 32) + 36)
        s += (f'<rect x="50" y="30" width="{w}" height="48" rx="10" fill="{ROJO_EGC}"/>'
              f'<text x="68" y="66" font-size="32" font-weight="bold" fill="#FFF">{etiqueta}</text>')
        y1 += 20
    s += f'<text x="50" y="{y1}" font-size="66" font-weight="bold" fill="#FFF">{linea1}</text>'
    if linea2:
        s += f'<text x="50" y="{y1 + 78}" font-size="66" font-weight="bold" fill="{ROJO_EGC}">{linea2}</text>'
    return s


def paso(n, y, titulo, detalle=None):
    """Paso numerado: círculo rojo con número, título negro (44 px) y detalle gris (36 px)."""
    s = (f'<circle cx="105" cy="{y}" r="44" fill="{ROJO_EGC}"/>'
         f'<text x="105" y="{y + 17}" font-size="48" font-weight="bold" fill="#FFF" text-anchor="middle">{n}</text>'
         + texto(175, y + 2 if detalle else y + 15, titulo, 44, NEGRO))
    if detalle:
        s += texto(175, y + 50, detalle, 36, GRIS_T, negrita=False)
    return s


def tilde(y, t, tam=40):
    """Línea con tilde roja (beneficio)."""
    return (f'<path d="M70,{y - 14} l16,16 l30,-34" fill="none" stroke="{ROJO_EGC}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
            + texto(140, y, t, tam, NEGRO))


def cta(linea='PROBALA 30 DÍAS GRATIS', sub='Sin tarjeta · link en la bio', y=1040):
    """Botón rojo con el llamado a la acción y una línea debajo."""
    w = int(ancho_texto(linea, 50) + 90)
    x = (ANCHO - w) / 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="104" rx="52" fill="{ROJO_EGC}"/>'
            f'<text x="{ANCHO/2}" y="{y + 69}" font-size="50" font-weight="bold" fill="#FFF" text-anchor="middle">{linea}</text>'
            + texto(ANCHO / 2, y + 160, sub, 36, GRIS_T, 'middle', negrita=False))


def pie():
    return firma('egc.globalepika.net.ar')


def salida(cuerpo, script):
    """Guarda la placa como JPG (Instagram solo acepta JPEG) en comerciales/posts/<mismo nombre>.jpg."""
    import os
    from PIL import Image
    base = os.path.splitext(os.path.basename(script))[0]
    posts = os.path.join(os.path.dirname(os.path.abspath(script)), '..', 'posts')
    png = os.path.join(posts, base + '.png')
    guardar(cuerpo, png)
    Image.open(png).convert('RGB').save(os.path.join(posts, base + '.jpg'), 'JPEG', quality=92)
    os.remove(png)
    print('JPG listo:', base + '.jpg')
