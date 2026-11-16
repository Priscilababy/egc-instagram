# -*- coding: utf-8 -*-
"""Portada del blog: cuándo se aplica la AEA 90364-7-771 (fichas 14, 01 y 49)."""
import sys
from placa import *

s = encabezado('¿770 O 771?', 'OFICINAS Y LOCALES')

filas = [
    (['VIVIENDA', 'hasta 63 A y 10 kA'], '770', CAST),
    (['OFICINA', 'o LOCAL'], '771', NAVY),
    (['VIVIENDA FUERA', 'del alcance de la 770'], '771', NAVY),
]
y = 250
for (l1, l2), norma, col in filas:
    s += f'<rect x="60" y="{y}" width="640" height="170" rx="20" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
    s += texto(95, y + 75, l1, 46) + texto(95, y + 130, l2, 36, '#4A5563', negrita=False)
    # flecha
    s += (f'<line x1="710" y1="{y+85}" x2="790" y2="{y+85}" stroke="{NAVY}" stroke-width="10"/>'
          f'<polygon points="790,{y+60} 830,{y+85} 790,{y+110}" fill="{NAVY}"/>')
    s += f'<rect x="845" y="{y+20}" width="175" height="130" rx="20" fill="{col}"/>'
    s += texto(932, y + 107, norma, 64, '#FFF', 'middle')
    y += 205

s += mensaje(['La 771 (2006) sigue vigente.', 'En vivienda común manda la 770.'], y=900)
s += texto(60, 1180, 'Oficinas: grados por superficie.', 36, '#4A5563', negrita=False)
s += firma('AEA 90364-7-771')
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog-771.png')
