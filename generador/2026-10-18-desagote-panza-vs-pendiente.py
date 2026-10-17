# -*- coding: utf-8 -*-
"""2026-10-18 · AIRE · MAL/BIEN: desagote de condensado con panza vs. pendiente continua hacia afuera."""
import sys
from placa import *

AGUA = '#2A8FD0'


def esquema(Y, mal):
    # pared en el centro; interior a la izquierda (arriba), exterior a la derecha (más abajo)
    s = f'<rect x="500" y="{Y+95}" width="50" height="215" fill="#C9CFD6" stroke="{NAVY}" stroke-width="4"/>'
    s += texto(525, Y + 350, 'PARED', 32, GRIS, 'middle')
    s += (f'<rect x="90" y="{Y+100}" width="270" height="80" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          + texto(225, Y + 154, 'INTERIOR', 38, ancla='middle'))
    if mal:
        pts = f'225,{Y+180} 225,{Y+205} 330,{Y+265} 400,{Y+205} 480,{Y+205} 525,{Y+240} 700,{Y+240} 840,{Y+240}'
        s += f'<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="12" stroke-linejoin="round"/>'
        s += f'<path d="M290,{Y+250} q40,40 80,0 z" fill="{AGUA}"/>'
        s += texto(330, Y + 305, 'agua', 32, AGUA, 'middle')
        s += (f'<path d="M840,{Y+240} v20" stroke="{NAVY}" stroke-width="12"/>'
              f'<rect x="800" y="{Y+265}" width="120" height="75" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
              f'<rect x="806" y="{Y+295}" width="108" height="39" fill="{AGUA}"/>')
        s += texto(860, Y + 372, 'punta en el agua', 32, ROJO, 'middle')
    else:
        pts = f'225,{Y+180} 225,{Y+205} 525,{Y+250} 840,{Y+300}'
        s += f'<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="12" stroke-linejoin="round"/>'
        s += f'<path d="M840,{Y+300} l0,22" stroke="{AGUA}" stroke-width="8" stroke-dasharray="6 8"/>'
        s += texto(870, Y + 355, 'punta libre', 32, VERDE_OK, 'middle')
        s += texto(290, Y + 330, 'siempre bajando', 32, VERDE_OK, 'middle')
    return s


def panel(Y, mal):
    color = ROJO if mal else VERDE_OK
    fondo = '#FFF5F5' if mal else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="390" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 18, 'MAL · CON PANZA' if mal else 'BIEN · PENDIENTE CONTINUA', color)
    return s + esquema(Y, mal)


s = encabezado('DESAGOTE DEL SPLIT', 'CON PANZA O CON PENDIENTE', linea2_amarilla=True)
s += panel(215, True)
s += panel(620, False)
s += mensaje(['Pendiente continua hacia afuera,', 'sin panzas y con la punta libre'], y=1030, tam=38)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'desagote.png'
guardar(s, salida)
