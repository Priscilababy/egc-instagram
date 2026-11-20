# -*- coding: utf-8 -*-
"""Placa extra · MAL/BIEN: caño corrugado liviano embutido en mampostería (fichas 07 y 51)."""
import sys
from placa import *

s = encabezado('CAÑO CORRUGADO', '¿EL LIVIANO EN LA PARED?', linea2_amarilla=True)


def ladrillos(x, y, w, h):
    """Muro de ladrillos simple."""
    r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#E9B8A0" stroke="#B5765A" stroke-width="4"/>'
    fila = 0
    for yy in range(y, y + h, 44):
        r += f'<line x1="{x}" y1="{yy}" x2="{x+w}" y2="{yy}" stroke="#C98A6E" stroke-width="3"/>'
        off = 0 if fila % 2 == 0 else 50
        for xx in range(x + off, x + w, 100):
            r += f'<line x1="{xx}" y1="{yy}" x2="{xx}" y2="{min(yy+44, y+h)}" stroke="#C98A6E" stroke-width="3"/>'
        fila += 1
    return r


def cano(x, y, largo, color, aplastado=False):
    """Caño corrugado horizontal con anillos."""
    alto = 26 if aplastado else 50
    yy = y + (12 if aplastado else 0)
    r = f'<rect x="{x}" y="{yy}" width="{largo}" height="{alto}" rx="{alto/2}" fill="{color}" stroke="{NAVY}" stroke-width="4"/>'
    for xx in range(x + 20, x + largo - 10, 22):
        r += f'<line x1="{xx}" y1="{yy+4}" x2="{xx}" y2="{yy+alto-4}" stroke="{NAVY}" stroke-width="3" opacity="0.45"/>'
    return r


def panel(Y, etiqueta, color, fondo, malo):
    r = f'<rect x="50" y="{Y}" width="980" height="465" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    r += chip(80, Y + 22, etiqueta, color)
    r += ladrillos(80, Y + 110, 420, 260)
    if malo:
        r += cano(110, Y + 210, 360, '#FFFFFF', aplastado=True)
        r += texto(290, Y + 420, 'Liviano · código 23', 38, ROJO, 'middle')
        r += texto(540, Y + 160, 'En mampostería', 40)
        r += texto(540, Y + 210, 'no va.', 40)
        r += texto(540, Y + 280, 'Resiste poca', 38, NAVY, 'start', False)
        r += texto(540, Y + 326, 'compresión.', 38, NAVY, 'start', False)
        r += texto(540, Y + 396, 'Solo construcción', 38, NAVY, 'start', False)
        r += texto(540, Y + 440, 'en seco.', 38, NAVY, 'start', False)
    else:
        r += cano(110, Y + 210, 360, '#DCE6EF')
        r += texto(290, Y + 420, 'Código 33 o 44', 38, VERDE_OK, 'middle')
        r += texto(540, Y + 160, 'Semipesado o pesado', 40)
        r += texto(540, Y + 210, 'en mampostería.', 40)
        r += texto(540, Y + 280, 'Caño certificado', 38, NAVY, 'start', False)
        r += texto(540, Y + 326, 'IRAM 62386.', 38, NAVY, 'start', False)
        r += texto(540, Y + 396, 'Leé el código impreso,', 38, NAVY, 'start', False)
        r += texto(540, Y + 440, 'no el color.', 38, NAVY, 'start', False)
    return r


s += panel(230, 'MAL', ROJO, '#FFF5F5', True)
s += panel(745, 'BIEN', VERDE_OK, '#F3FBF5', False)
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
