# -*- coding: utf-8 -*-
"""2026-11-04 · Varios circuitos en el mismo caño (ficha 07, 770.10.3.8.2). Formato CONEXIÓN."""
import sys
from placa import *

s = encabezado('VARIOS CIRCUITOS', 'EN UN MISMO CAÑO')

# Caño con 3 circuitos (cada uno: fase, neutro, PE)
s += texto(540, 262, 'UN SOLO CAÑO', 36, NAVY, 'middle')
s += f'<rect x="340" y="276" width="400" height="250" rx="40" fill="#EEF1F5" stroke="{NAVY}" stroke-width="6"/>'
for i, y in enumerate((338, 400, 462)):
    s += cable([(190, y - 18), (890, y - 18)], CAST)
    s += cable([(190, y), (890, y)], CEL)
    s += cable_pe([(190, y + 18), (890, y + 18)])
    s += texto(100, y + 14, f'C{i+1}', 40, NAVY, 'middle')

# Referencias de color
s += cable([(60, 566), (120, 566)], CAST) + texto(132, 578, 'Fase (la misma)', 32)
s += cable([(440, 566), (500, 566)], CEL) + texto(512, 578, 'Neutro', 32, CEL_TXT)
s += cable_pe([(720, 566), (780, 566)]) + texto(792, 578, 'PE', 32, VERDE)

# Condiciones (hasta 3 de uso general)
s += texto(60, 650, 'Hasta 3 de uso general, si se cumple todo:', 36)
items = ['Misma fase y mismo tablero',
         'Suma de termomagnéticas: hasta 36 A',
         'Hasta 15 bocas en total',
         'Cada circuito completo: fase, N y PE']
for i, t in enumerate(items):
    y = 715 + 62 * i
    s += (f'<circle cx="86" cy="{y-12}" r="22" fill="{VERDE_OK}"/>'
          f'<polyline points="74,{y-12} 83,{y-2} 100,{y-24}" fill="none" stroke="#FFF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
    s += texto(130, y, t, 36)

s += mensaje(['Las 4 condiciones juntas,', 'o cada uno en su caño.'], y=945)
s += texto(60, 1160, 'Corriente admisible del cable:', 32, NAVY) + texto(60, 1202, '× 0,80 con 2 circuitos · × 0,70 con 3', 32, NAVY)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'x.png'
guardar(s, salida)
