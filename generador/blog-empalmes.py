# -*- coding: utf-8 -*-
"""Portada del blog: empalmes (retorcer vs bornera)."""
import sys
from placa import *

s = encabezado('EMPALMES', 'RETORCER O BORNERA', linea2_amarilla=True)

def panel(Y, etiqueta, color, n, bornera):
    t = f'<rect x="50" y="{Y}" width="980" height="300" rx="24" fill="#F3FBF5" stroke="{color}" stroke-width="5"/>'
    t += chip(80, Y + 18, etiqueta, color, 34)
    cy = Y + 190
    if not bornera:
        for i in range(n):
            y = cy - 60 + i * 40
            t += cable([(110, y), (430, cy)], GRIS)
        t += f'<circle cx="440" cy="{cy}" r="34" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
        t += texto(560, cy + 14, 'unión en caja', 36)
    else:
        t += f'<rect x="400" y="{cy-70}" width="160" height="140" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
        for i in range(n):
            y = cy - 80 + i * 40
            t += cable([(110, y), (400, cy - 56 + i * 28)], GRIS)
        t += texto(600, cy + 14, 'bornera', 36)
    return t

s += panel(240, 'HASTA 4 CABLES · MENOS DE 4 mm²', VERDE_OK, 4, False)
s += panel(570, 'MÁS DE 4 CABLES', VERDE_OK, 5, True)
s += mensaje(['Nunca empalmes', 'dentro del caño'], y=900)
s += firma()
guardar(s, sys.argv[1])
