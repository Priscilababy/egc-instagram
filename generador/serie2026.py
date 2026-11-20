# -*- coding: utf-8 -*-
"""Estilo "serie especial" para placas destacadas (AEA 770 edición 2026).
Fondo azul profundo, acentos amarillos, tarjetas translúcidas. Usa el render de placa.py."""
import base64
import os
from placa import guardar, ancho_texto, AQUI, ANCHO, ALTO

NAVY = '#132B47'
NAVY_D = '#0A1626'
AMA = '#F2B90F'
AMA_L = '#FFD34D'
CIAN = '#5BC4F0'
VERDE = '#2FBF6A'
ROJO = '#FF4D4F'
BLANCO = '#FFFFFF'
TXT2 = '#C9D6E6'   # texto secundario sobre oscuro


def _chk(t, tam, max_w, negrita=True):
    w = ancho_texto(t, tam, negrita)
    if w > max_w:
        raise ValueError(f'Texto demasiado ancho ({w:.0f} > {max_w}): {t}')
    if tam < 32:
        raise ValueError(f'Texto menor a 32 px: {t}')


def t(x, y, s, tam=40, color=BLANCO, ancla='start', negrita=True, max_w=None, extra=''):
    if max_w:
        _chk(s, tam, max_w, negrita)
    peso = ' font-weight="bold"' if negrita else ''
    return (f'<text x="{x}" y="{y}" font-size="{tam}"{peso} fill="{color}" '
            f'text-anchor="{ancla}"{extra}>{s}</text>')


def defs():
    return f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#16345A"/><stop offset="0.55" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_D}"/>
</linearGradient>
<radialGradient id="glow" cx="0.85" cy="0.12" r="0.55">
  <stop offset="0" stop-color="{AMA}" stop-opacity="0.32"/><stop offset="1" stop-color="{AMA}" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glow2" cx="0.05" cy="0.95" r="0.5">
  <stop offset="0" stop-color="{CIAN}" stop-opacity="0.18"/><stop offset="1" stop-color="{CIAN}" stop-opacity="0"/>
</radialGradient>
<linearGradient id="ama" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="{AMA_L}"/><stop offset="1" stop-color="{AMA}"/>
</linearGradient>
<linearGradient id="vidrio" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.13"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.05"/>
</linearGradient>
<pattern id="grid" width="54" height="54" patternUnits="userSpaceOnUse">
  <path d="M54,0 L0,0 0,54" fill="none" stroke="#FFFFFF" stroke-opacity="0.05" stroke-width="2"/>
</pattern>
<filter id="sombra" x="-20%" y="-20%" width="140%" height="140%">
  <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.35"/>
</filter>
<filter id="brillo" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="18"/>
</filter>
</defs>'''


def fondo(n, total, titulo1, titulo2):
    s = defs()
    s += f'<rect width="{ANCHO}" height="{ALTO}" fill="url(#bg)"/>'
    s += f'<rect width="{ANCHO}" height="{ALTO}" fill="url(#grid)"/>'
    s += f'<rect width="{ANCHO}" height="{ALTO}" fill="url(#glow)"/>'
    s += f'<rect width="{ANCHO}" height="{ALTO}" fill="url(#glow2)"/>'
    # marca de agua
    s += (f'<text x="1110" y="1205" font-size="330" font-weight="bold" fill="none" stroke="#FFFFFF" '
          f'stroke-opacity="0.06" stroke-width="3" text-anchor="end">2026</text>')
    # franja diagonal
    s += f'<path d="M820,0 L1080,0 L1080,26 L846,26 z" fill="url(#ama)"/>'
    # pastilla de serie
    s += f'<rect x="60" y="60" width="580" height="58" rx="29" fill="url(#ama)"/>'
    s += t(350, 101, "SERIE ESPECIAL · AEA 770 · 2026", 32, NAVY, "middle", max_w=550)
    s += t(1020, 102, f'{n:02d}/{total:02d}', 40, BLANCO, 'end', extra=' fill-opacity="0.55"')
    # título
    s += t(60, 225, titulo1, 78, BLANCO, max_w=960)
    s += t(60, 312, titulo2, 78, AMA, max_w=960)
    s += f'<rect x="60" y="342" width="140" height="10" rx="5" fill="url(#ama)"/>'
    return s


def tarjeta(x, y, w, h, borde=None, rx=28, relleno='url(#vidrio)'):
    b = f' stroke="{borde}" stroke-width="3"' if borde else ' stroke="#FFFFFF" stroke-opacity="0.16" stroke-width="2"'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{relleno}"{b} filter="url(#sombra)"/>'


def pie(ref='AEA 90364-7-770'):
    with open(os.path.join(AQUI, 'logo-egc-light.png'), 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    s = f'<rect x="50" y="1222" width="290" height="104" rx="22" fill="#FFFFFF" filter="url(#sombra)"/>'
    s += (f'<image x="70" y="1228" width="250" height="92" href="data:image/png;base64,{b64}" '
          f'xlink:href="data:image/png;base64,{b64}" preserveAspectRatio="xMidYMid meet"/>')
    s += t(1030, 1268, ref, 32, TXT2, 'end')
    s += t(1030, 1310, 'Guardalo para la obra', 32, AMA, 'end')
    return s


def rayo(cx, cy, esc=1.0, color=None):
    color = color or 'url(#ama)'
    p = [(8, -46), (-24, 6), (0, 6), (-12, 46), (26, -12), (2, -12), (14, -46)]
    pts = ' '.join(f'{cx + x * esc},{cy + y * esc}' for x, y in p)
    return f'<polygon points="{pts}" fill="{color}"/>'
