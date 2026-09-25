# -*- coding: utf-8 -*-
"""Posteo 2026-09-26 · La llave corta la fase, nunca el neutro. Formato MAL/BIEN.
Con la llave en el neutro, al "apagar" la luz el portalámparas sigue con la fase puesta:
riesgo de golpe al cambiar la lámpara pensando que está sin tensión."""
import sys
from placa import *


def panel(Y, etiqueta, color, error):
    fondo = '#FFF5F5' if error else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)

    YF, YN = Y + 190, Y + 330
    LAMP_X, LAMP_W = 720, 290
    SW_X, SW_W, SW_H = 400, 200, 100

    s += borne(140, YF, CAST) + texto(100, YF + 12, 'F', 36, CAST, 'end')
    s += borne(140, YN, CEL) + texto(100, YN + 12, 'N', 36, CEL_TXT, 'end')

    fase_cortada = not error  # BIEN: la llave va en la fase. MAL: va en el neutro.
    y_llave = YF if fase_cortada else YN
    y_directo = YN if fase_cortada else YF
    color_directo = CEL if y_directo == YN else CAST
    color_llave = CAST if fase_cortada else CEL

    s += cable([(140, y_directo), (LAMP_X, y_directo)], color_directo)
    s += cable([(140, y_llave), (SW_X, y_llave)], color_llave)
    s += cable([(SW_X + SW_W, y_llave), (LAMP_X, y_llave)], color_llave)

    s += (f'<rect x="{SW_X}" y="{y_llave - SW_H / 2}" width="{SW_W}" height="{SW_H}" rx="16" '
          f'fill="#FFF" stroke="{NAVY}" stroke-width="5"/>')
    s += texto(SW_X + SW_W / 2, y_llave - SW_H / 2 - 20, 'LLAVE APAGADA', 32, NAVY, 'middle')
    s += (f'<circle cx="{SW_X + 24}" cy="{y_llave}" r="11" fill="{NAVY}"/>'
          f'<circle cx="{SW_X + SW_W - 24}" cy="{y_llave}" r="11" fill="{NAVY}"/>'
          f'<line x1="{SW_X + 24}" y1="{y_llave}" x2="{SW_X + SW_W - 60}" y2="{y_llave - 32}" '
          f'stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>')

    # Portalámparas: borne de arriba = fase, borne de abajo = neutro.
    s += (f'<rect x="{LAMP_X}" y="{Y + 110}" width="{LAMP_W}" height="260" rx="18" '
          f'fill="#FFF" stroke="{NAVY}" stroke-width="5"/>')
    s += texto(LAMP_X + LAMP_W / 2, Y + 95, 'PORTALÁMPARAS', 32, NAVY, 'middle')
    s += borne(LAMP_X + 50, YF, CAST) + borne(LAMP_X + 50, YN, CEL)

    bx, by = LAMP_X + 190, (YF + YN) / 2
    s += f'<circle cx="{bx}" cy="{by - 20}" r="55" fill="#FDF3C4" stroke="{NAVY}" stroke-width="4"/>'
    s += f'<rect x="{bx - 24}" y="{by + 30}" width="48" height="42" rx="5" fill="{GRIS}" stroke="{NAVY}" stroke-width="3"/>'
    for i in range(3):
        yy = by + 40 + i * 11
        s += f'<line x1="{bx - 24}" y1="{yy}" x2="{bx + 24}" y2="{yy}" stroke="{NAVY}" stroke-width="2"/>'

    if error:
        s += texto(LAMP_X + LAMP_W / 2, Y + 410, 'SIGUE CON FASE', 34, ROJO, 'middle')
    else:
        s += texto(LAMP_X + LAMP_W / 2, Y + 410, 'SIN TENSIÓN', 34, VERDE_OK, 'middle')
    return s


s = encabezado('LA LLAVE CORTA LA FASE', 'NUNCA EL NEUTRO')
s += panel(240, 'LLAVE EN EL NEUTRO', ROJO, True)
s += panel(740, 'LLAVE EN LA FASE', VERDE_OK, False)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-09-26-llave-corta-fase.png'
guardar(s, salida)
