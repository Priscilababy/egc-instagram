# -*- coding: utf-8 -*-
"""Posteo 2026-10-23 · Jabalina: el largo pesa mucho más que el diámetro. Formato CONEXIÓN (gráfico).
Fuente: conocimiento/23 (PAT7, tabla de resistencias; valores relativos, orientativos) y 06 (40 Ω, 770.3.2)."""
import sys
from placa import *

s = encabezado('JABALINA: EL LARGO', 'PESA MÁS QUE EL DIÁMETRO')

BASE, ALTO_MAX, AN = 800, 400, 100
# resistencia relativa (100 % = primera jabalina de cada grupo), de la tabla de la ficha 23
largo = [('1,5 m', 35.2), ('3 m', 19.4), ('4,5 m', 13.7), ('6 m', 10.6)]
diam = [('1/2&quot;', 20.0), ('5/8&quot;', 19.4), ('3/4&quot;', 18.9)]

def barras(items, x0, color):
    out = ''
    ref = items[0][1]
    for i, (et, v) in enumerate(items):
        pct = int(100 * v / ref + 0.5)
        h = int(ALTO_MAX * v / ref)
        x = x0 + i * (AN + 30)
        out += f'<rect x="{x}" y="{BASE-h}" width="{AN}" height="{h}" rx="8" fill="{color}" stroke="{NAVY}" stroke-width="4"/>'
        out += texto(x + AN/2, BASE - h - 14, f'{pct} %', 34, NAVY, 'middle')
        out += texto(x + AN/2, BASE + 46, et, 34, NAVY, 'middle')
    return out

s += texto(70, 268, 'MÁS LARGO', 38)
s += texto(70, 312, 'diámetro fijo: 5/8&quot;', 32, NAVY, negrita=False)
s += texto(640, 268, 'MÁS DIÁMETRO', 38)
s += texto(640, 312, 'largo fijo: 3 m', 32, NAVY, negrita=False)
s += barras(largo, 70, AMARILLO)
s += barras(diam, 640, '#C9CFD7')
s += f'<line x1="50" y1="{BASE}" x2="1030" y2="{BASE}" stroke="{NAVY}" stroke-width="5"/>'
s += texto(540, 905, 'Resistencia relativa: 100 % = jabalina de partida', 32, NAVY, 'middle', negrita=False)

s += mensaje(['Pasar de 1,5 m a 3 m: baja ~45 %.', 'De 1/2&quot; a 3/4&quot;: baja ~5 %.', 'Se mide: 40 Ω como máximo.'], y=950)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-23-jabalina-largo-diametro.png'
guardar(s, salida)
