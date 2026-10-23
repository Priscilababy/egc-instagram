# -*- coding: utf-8 -*-
"""2026-10-24 · AIRE · MAL/BIEN: tuerca flare apretada a ojo vs. doble llave y torquímetro."""
import sys
from placa import *

METAL = '#C9CFD6'


def union(cx, cy):
    """Cuerpo de la válvula (izquierda), tuerca flare (centro) y caño abocardado (derecha)."""
    s = f'<rect x="{cx-170}" y="{cy-55}" width="150" height="110" rx="10" fill="{METAL}" stroke="{NAVY}" stroke-width="5"/>'
    s += texto(cx - 95, cy - 75, 'VÁLVULA', 32, NAVY, 'middle')
    s += f'<rect x="{cx-20}" y="{cy-34}" width="45" height="68" fill="{METAL}" stroke="{NAVY}" stroke-width="5"/>'
    s += f'<polygon points="{cx+25},{cy-52} {cx+90},{cy-52} {cx+105},{cy} {cx+90},{cy+52} {cx+25},{cy+52}" fill="#E8B04A" stroke="{NAVY}" stroke-width="5"/>'
    s += f'<rect x="{cx+105}" y="{cy-22}" width="130" height="44" fill="#D98B5B" stroke="{NAVY}" stroke-width="5"/>'
    s += texto(cx + 170, cy - 36, 'caño', 32, GRIS, 'middle')
    return s


def llave(x, y, largo, ang, color=NAVY):
    """Llave: cabeza en (x, y) y mango hacia el ángulo dado."""
    return (f'<g transform="rotate({ang} {x} {y})">'
            f'<rect x="{x}" y="{y-14}" width="{largo}" height="28" rx="12" fill="{color}"/>'
            f'<circle cx="{x}" cy="{y}" r="26" fill="{color}"/></g>')


def panel(Y, mal):
    color = ROJO if mal else VERDE_OK
    fondo = '#FFF5F5' if mal else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="390" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 18, 'MAL · A OJO, UNA LLAVE' if mal else 'BIEN · DOBLE LLAVE + TORQUE', color)
    cx, cy = 360, Y + 215
    s += union(cx, cy)
    if mal:
        s += llave(cx + 57, cy, 200, 40)           # una sola llave sobre la tuerca
        s += texto(800, Y + 350, 'sin torque', 36, ROJO, 'middle')
        s += texto(800, Y + 150, '¿cuánto aprieto?', 34, ROJO, 'middle')
    else:
        s += llave(cx - 95, cy, 180, 130)          # contrallave sosteniendo el cuerpo de la válvula
        s += llave(cx + 57, cy, 200, 40, VERDE_OK)  # llave dinamométrica sobre la tuerca
        s += texto(800, Y + 150, 'torquímetro', 36, VERDE_OK, 'middle')
        s += texto(800, Y + 350, 'N·m del manual', 36, VERDE_OK, 'middle')
    return s


s = encabezado('TUERCA FLARE DEL SPLIT', 'DOBLE LLAVE Y TORQUE', linea2_amarilla=True)
s += panel(215, True)
s += panel(620, False)
s += mensaje(['Una llave sostiene la válvula,', 'otra aprieta al torque del manual'], y=1030, tam=38)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'tuerca-flare.png'
guardar(s, salida)
