# -*- coding: utf-8 -*-
"""2026-11-05 · MAL / BIEN: térmica vs. agrupamiento de 2 circuitos en un caño (fichas 04 y 07)."""
import sys
from placa import *


def panel(Y, etiqueta, color, ok):
    fondo = '#F3FBF5' if ok else '#FFF5F5'
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    t = '16 A' if ok else '20 A'
    for x in (150, 630):
        s += (f'<rect x="{x}" y="{Y+95}" width="250" height="80" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
              + texto(x + 125, Y + 150, 'TERMO ' + t, 38, ancla='middle'))
        s += cable([(x + 75, Y + 175), (x + 75, Y + 240)], CAST)
        s += cable([(x + 175, Y + 175), (x + 175, Y + 240)], CEL)
    s += (f'<rect x="100" y="{Y+240}" width="880" height="80" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          + texto(540, Y + 293, 'MISMO CAÑO · 2 CIRCUITOS · 2,5 mm²', 36, ancla='middle'))
    s += texto(540, Y + 375, '21 A × 0,80 = 16,8 A', 44, ancla='middle')
    if ok:
        s += texto(540, Y + 430, '16 A ≤ 16,8 A  ·  CUMPLE', 44, VERDE_OK, 'middle')
    else:
        s += texto(540, Y + 430, '20 A > 16,8 A  ·  NO CUMPLE', 44, ROJO, 'middle')
    return s


s = encabezado('2,5 mm² COMPARTIENDO CAÑO', '¿SIGUE VALIENDO 20 A?', linea2_amarilla=True)
s += panel(240, 'MAL: LA TÉRMICA SE PASA', ROJO, False)
s += panel(740, 'BIEN: BAJAR A 16 A', VERDE_OK, True)
s += firma()
salida = sys.argv[1] if len(sys.argv) > 1 else 'x.png'
guardar(s, salida)
