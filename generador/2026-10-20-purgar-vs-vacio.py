# -*- coding: utf-8 -*-
"""2026-10-20 · AIRE · MAL/BIEN: "purgar" con el gas del equipo vs. vacío con bomba y vacuómetro."""
import sys
from placa import *


def caja_t(x, y, w, h, l1, l2=None, color=NAVY):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#FFF" stroke="{color}" stroke-width="5"/>'
    if l2:
        s += texto(x + w / 2, y + h / 2 - 8, l1, 34, color, 'middle') + texto(x + w / 2, y + h / 2 + 34, l2, 34, color, 'middle')
    else:
        s += texto(x + w / 2, y + h / 2 + 12, l1, 36, color, 'middle')
    return s


def linea(pts, color=NAVY, w=8):
    d = ' '.join(f'{x},{y}' for x, y in pts)
    return f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'


def panel(Y, etiqueta, color, mal):
    fondo = '#FFF5F5' if mal else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="400" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    if mal:
        s += caja_t(100, Y + 150, 300, 110, 'UNIDAD', 'EXTERIOR')
        s += caja_t(680, Y + 150, 300, 110, 'UNIDAD', 'INTERIOR')
        s += linea([(400, Y + 205), (680, Y + 205)], GRIS, 10)
        s += texto(540, Y + 160, 'su propio gas', 34, ROJO, 'middle')
        s += (f'<circle cx="540" cy="{Y + 280}" r="40" fill="{ROJO}"/>'
              f'<path d="M524,{Y + 264} L556,{Y + 296} M556,{Y + 264} L524,{Y + 296}" stroke="#FFF" stroke-width="10" stroke-linecap="round"/>')
        s += texto(540, Y + 360, 'No hay vacío: no mide nada', 36, ROJO, 'middle')
    else:
        s += caja_t(70, Y + 150, 270, 110, 'BOMBA DE', 'VACÍO')
        s += caja_t(400, Y + 150, 250, 110, 'MANIFOLD', None)
        s += caja_t(710, Y + 150, 270, 110, 'UNIDAD', 'EXTERIOR')
        s += linea([(340, Y + 205), (400, Y + 205)], NAVY, 10) + linea([(650, Y + 205), (710, Y + 205)], NAVY, 10)
        s += linea([(525, Y + 150), (525, Y + 100)], NAVY, 10)
        s += caja_t(370, Y + 30, 310, 70, 'VACUÓMETRO', None, VERDE_OK)
        s += (f'<circle cx="540" cy="{Y + 305}" r="40" fill="{VERDE_OK}"/>'
              f'<path d="M522,{Y + 305} L536,{Y + 321} M536,{Y + 321} L562,{Y + 288}" fill="none" stroke="#FFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>')
        s += texto(540, Y + 380, '15 min mínimo + prueba de retención', 34, VERDE_OK, 'middle')
    return s


s = encabezado('"PURGAR" CON EL GAS', 'O HACER VACÍO', linea2_amarilla=False)
s += panel(225, 'MAL', ROJO, True)
s += panel(635, 'BIEN', VERDE_OK, False)
s += mensaje(['El vacío se hace con bomba.', 'Nunca con el gas del equipo.'], y=1048, tam=36)
s += firma()

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'purgar.png')
