# -*- coding: utf-8 -*-
"""MAL / BIEN: cañería de acero con teflón en las roscas (sin continuidad) vs. con puentes a la barra PE."""
import sys
from placa import *

CANO = '#B9C1CC'


def panel(Y, etiqueta, titulo, color, bien):
    fondo = '#F3FBF5' if bien else '#FFF5F5'
    s = f'<rect x="50" y="{Y}" width="980" height="480" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    s += texto(80 + 36 + int(40 * 0.68) * len(etiqueta) + 20, Y + 62, titulo, 38)
    yp = Y + 220
    # tres tramos de caño y dos uniones roscadas
    for x0, x1 in ((90, 390), (430, 690), (730, 990)):
        s += f'<rect x="{x0}" y="{yp-28}" width="{x1-x0}" height="56" rx="8" fill="{CANO}" stroke="{NAVY}" stroke-width="5"/>'
    for xu in (410, 710):
        s += f'<rect x="{xu-20}" y="{yp-38}" width="40" height="76" rx="6" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    # barra PE del tablero de bombas, a la PAT general
    s += (f'<rect x="90" y="{Y+370}" width="560" height="80" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          + texto(370, Y+422, 'BARRA PE · TABLERO BOMBAS', 34, ancla='middle')
          + cable_pe([(650, Y+410), (700, Y+410)])
          + texto(715, Y+422, 'a PAT', 36, VERDE))
    if bien:
        for xa, xb in ((350, 470), (650, 770)):
            s += cable_pe([(xa, yp-28), (xa, yp-85), (xb, yp-85), (xb, yp-28)])
        s += texto(410, yp-100, 'PUENTE', 34, VERDE, 'middle') + texto(710, yp-100, 'PUENTE', 34, VERDE, 'middle')
        s += cable_pe([(200, yp+28), (200, Y+370)])
        s += texto(240, Y+320, 'continuidad', 36, VERDE_OK)
        s += (f'<circle cx="920" cy="{Y+300}" r="42" fill="{VERDE_OK}"/>'
              f'<path d="M900,{Y+300} L914,{Y+316} L942,{Y+282}" fill="none" stroke="#FFF" stroke-width="10" '
              f'stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        s += texto(410, yp+80, 'TEFLÓN', 34, ROJO, 'middle') + texto(710, yp+80, 'TEFLÓN', 34, ROJO, 'middle')
        s += texto(100, Y+350, 'sin continuidad con la barra PE', 34, ROJO)
        s += (f'<circle cx="920" cy="{Y+300}" r="42" fill="{ROJO}"/>'
              f'<path d="M902,{Y+282} L938,{Y+318} M938,{Y+282} L902,{Y+318}" stroke="#FFF" stroke-width="10" stroke-linecap="round"/>')
    return s


s = encabezado('CAÑERÍA DE ACERO', 'DEL TABLERO DE BOMBAS', linea2_amarilla=False)
s += panel(225, 'MAL', 'Teflón en las roscas, sin puentes', ROJO, False)
s += panel(735, 'BIEN', 'Puentes y cable a la barra PE', VERDE_OK, True)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-26-caneria-continuidad.png'
guardar(s, salida)
