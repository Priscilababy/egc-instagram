# -*- coding: utf-8 -*-
"""2026-10-22 · AIRE · MAL/BIEN: pasamuros sin pendiente vs. Ø 65 mm con pendiente hacia afuera."""
import sys
from placa import *

AGUA = '#2A8FD0'


def esquema(Y, mal):
    # pared en el centro; interior a la izquierda, exterior a la derecha
    s = f'<rect x="490" y="{Y+85}" width="90" height="250" fill="#C9CFD6" stroke="{NAVY}" stroke-width="4"/>'
    s += texto(535, Y + 372, 'PARED', 32, GRIS, 'middle')
    s += texto(230, Y + 135, 'INTERIOR', 36, ancla='middle')
    s += texto(850, Y + 135, 'EXTERIOR', 36, ancla='middle')
    # pasamuros (caño que atraviesa la pared); mal: sube hacia afuera, bien: baja hacia afuera
    yi, yo = (Y + 245, Y + 205) if mal else (Y + 205, Y + 245)
    h = 24
    xi, xo = 450, 620
    pts = f'{xi},{yi-h} {xo},{yo-h} {xo},{yo+h} {xi},{yi+h}'
    s += f'<polygon points="{pts}" fill="#FFF" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>'
    if mal:
        # agua que entra por la boca exterior
        s += f'<path d="M760,{Y+200} L650,{Y+205}" stroke="{AGUA}" stroke-width="8" stroke-dasharray="6 8" fill="none"/>'
        s += f'<path d="M650,{Y+205} l22,-14 m-22,14 l22,14" stroke="{AGUA}" stroke-width="8" fill="none"/>'
        s += texto(800, Y + 300, 'el agua entra', 34, ROJO, 'middle')
    else:
        s += f'<path d="M620,{yo+h+4} v60" stroke="{AGUA}" stroke-width="10" stroke-dasharray="6 8" fill="none"/>'
        s += texto(240, Y + 305, 'Ø 65 mm', 34, VERDE_OK, 'middle')
        s += texto(800, Y + 320, 'sale el agua', 34, VERDE_OK, 'middle')
    return s


def panel(Y, mal):
    color = ROJO if mal else VERDE_OK
    fondo = '#FFF5F5' if mal else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="390" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 18, 'MAL · PENDIENTE AL REVÉS' if mal else 'BIEN · BAJA HACIA AFUERA', color)
    return s + esquema(Y, mal)


s = encabezado('PASAMUROS DEL SPLIT', 'PENDIENTE HACIA AFUERA', linea2_amarilla=True)
s += panel(215, True)
s += panel(620, False)
s += mensaje(['Pasamuros Ø 65 mm: la boca de afuera', '5 a 7 mm más baja que la de adentro'], y=1030, tam=38)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'pasamuros.png'
guardar(s, salida)
