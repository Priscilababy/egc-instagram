# -*- coding: utf-8 -*-
"""Portada del blog: tiras LED y fuentes de 12 V (fichas 01, 07, 10)."""
import sys
from placa import *

s = encabezado('TIRAS LED Y', 'FUENTES DE 12 V')

def flecha(x, y1, y2):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-18}" stroke="{NAVY}" stroke-width="8"/>'
            f'<path d="M{x-20},{y2-22} L{x+20},{y2-22} L{x},{y2} z" fill="{NAVY}"/>')

s += caja(60, 230, 600, 220, 'LADO 220 V')
s += texto(85, 350, 'Diferencial de 30 mA', 36) + texto(85, 400, 'La llave corta la fase', 36)
s += flecha(360, 450, 510)
s += caja(60, 510, 600, 250, 'FUENTE 12 V')
s += texto(85, 630, 'Primario y secundario', 36) + texto(85, 675, 'separados.', 36)
s += texto(85, 725, 'Nunca autotransformador.', 36, ROJO)
s += flecha(360, 760, 820)
s += caja(60, 820, 600, 220, 'LADO 12 V')
s += texto(85, 940, 'Más de 3 m de cable:', 36) + texto(85, 990, 'es parte de la instalación', 34)

# Caños separados
s += caja(700, 230, 320, 810, 'CAÑOS', 36)
for x in (790, 930):
    s += f'<rect x="{x-45}" y="330" width="90" height="630" rx="12" fill="#F6F8FA" stroke="{GRIS}" stroke-width="5"/>'
s += cable([(766, 345), (766, 945)], CAST) + cable([(790, 345), (790, 945)], CEL) + cable_pe([(814, 345), (814, 945)])
s += cable([(918, 345), (918, 945)], RET, punteado=True) + cable([(942, 345), (942, 945)], RET2, punteado=True)
s += texto(790, 1012, '220 V', 34, NAVY, 'middle') + texto(930, 1012, '12 V', 34, NAVY, 'middle')

s += mensaje(['12 V y 220 V, en caños separados'], y=1070, tam=40, ancho=700)
s += firma()

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
