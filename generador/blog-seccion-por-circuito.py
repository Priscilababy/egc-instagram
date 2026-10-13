# -*- coding: utf-8 -*-
"""Portada del blog: sección de cable por circuito (fichas 02 y 04)."""
import sys
from placa import *

s = encabezado('SECCIÓN DE CABLE', 'EN CADA CIRCUITO')
filas = [('IUG', '1,5 mm²', 'térmica ≤ 15 A', '15 A'),
         ('TUG', '2,5 mm²', 'térmica ≤ 20 A', '21 A'),
         ('TUE 32 A', '6 mm²', '', '36 A')]
y = 250
s += texto(60, y + 40, 'CIRCUITO', 32, GRIS) + texto(340, y + 40, 'CABLE', 32, GRIS) + texto(640, y + 40, 'ADMITE', 32, GRIS)
for n, sec, term, iz in filas:
    y += 80
    s += f'<rect x="45" y="{y}" width="990" height="100" rx="16" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
    s += texto(70, y + 66, n, 44)
    s += texto(340, y + 66, sec, 48, CAST)
    s += texto(640, y + 66, iz, 48, VERDE_OK)
    s += texto(1010, y + 114, term, 32, NAVY, 'end', negrita=False) if False else ''
    y += 40
s += texto(60, 820, 'IUG: 1,5 mm² admite 15 A: no va con 16 A.', 34, NAVY)
s += texto(60, 870, 'TUE de 32 A: pide 6 mm², no 2,5.', 34, NAVY)
s += mensaje(['La térmica nunca puede', 'ser mayor que lo que', 'aguanta el cable.'], y=930)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'portada.png')
