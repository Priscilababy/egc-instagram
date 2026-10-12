# -*- coding: utf-8 -*-
"""Posteo 2026-10-13 · MAL / BIEN: 6 cables retorcidos en un empalme vs. bornera normalizada (ficha 07)."""
import sys
from placa import *

ALTO_P = 400


def panel(Y, etiqueta, color, mal):
    fondo = '#FFF5F5' if mal else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="{ALTO_P}" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 20, etiqueta, color)
    filas = (Y + 160, Y + 240, Y + 320)
    cy = Y + 240
    for y in filas:  # seis cables celestes (todos el mismo neutro) que llegan al empalme
        s += cable([(90, y), (400 if not mal else 450, y)], CEL) + cable([(990, y), (680 if not mal else 630, y)], CEL)
    if mal:
        s += (f'<ellipse cx="540" cy="{cy}" rx="110" ry="100" fill="#4A4A4A"/>'
              f'<path d="M470,{cy-70} L600,{cy-90} M450,{cy+60} L630,{cy+30} M470,{cy+90} L600,{cy+75}" stroke="#7A7A7A" stroke-width="8"/>'
              + texto(540, cy + 13, 'CINTA', 36, '#FFF', 'middle'))
        s += texto(540, Y + 378, '6 cables retorcidos', 36, ROJO, 'middle')
    else:
        s += (f'<rect x="400" y="{Y+135}" width="280" height="200" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
              + texto(540, cy + 13, 'BORNERA', 34, NAVY, 'middle'))
        for y in filas:
            s += borne(400, y, NAVY) + borne(680, y, NAVY)
        s += texto(540, Y + 380, 'conexión normalizada', 36, VERDE_OK, 'middle')
    return s


s = encabezado('EMPALME: ¿RETORCIDO', 'O BORNERA?')
s += panel(215, 'MAL · MÁS DE 4 CABLES JUNTOS', ROJO, True)
s += panel(630, 'BIEN · USÁ BORNERA', VERDE_OK, False)
s += mensaje(['Más de 4 cables juntos: bornera.', 'Empalmes nunca dentro del caño.'], y=1048)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-13-empalme-vs-bornera.png'
guardar(s, salida)
