# -*- coding: utf-8 -*-
"""2026-11-11 · MAL / BIEN: dos cables en un mismo borne de la termomagnética vs. un cable por borne (fichas 07 y 09)."""
import sys
from placa import *


def termo(x0, Y):
    """Termomagnética bipolar: caja con bornes L (castaño) y N (celeste) arriba y abajo."""
    s = (f'<rect x="{x0}" y="{Y+110}" width="300" height="140" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
         + texto(x0 + 150, Y + 172, 'TERMO', 40, ancla='middle')
         + texto(x0 + 150, Y + 214, 'BIPOLAR', 34, ancla='middle'))
    for yy in (Y + 110, Y + 250):
        s += borne(x0 + 70, yy, CAST) + borne(x0 + 230, yy, CEL)
    return s


def circuito(x, Y, w, t):
    return (f'<rect x="{x}" y="{Y+360}" width="{w}" height="80" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
            + texto(x + w / 2, Y + 413, t, 36, ancla='middle'))


def leyenda(Y):
    return (f'<line x1="660" y1="{Y+44}" x2="710" y2="{Y+44}" stroke="{CAST}" stroke-width="10"/>'
            + texto(722, Y + 57, 'fase', 34)
            + f'<line x1="820" y1="{Y+44}" x2="870" y2="{Y+44}" stroke="{CEL}" stroke-width="10"/>'
            + texto(882, Y + 57, 'neutro', 34))


def panel_mal(Y):
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="#FFF5F5" stroke="{ROJO}" stroke-width="5"/>'
    s += chip(80, Y + 22, 'MAL: DOS POR BORNE', ROJO) + leyenda(Y)
    x0 = 390
    s += circuito(250, Y, 580, 'CIRCUITO 1 Y CIRCUITO 2')
    # dos cables entrando al mismo borne inferior de fase y al mismo de neutro
    s += cable([(x0 + 64, Y + 250), (x0 + 64, Y + 290), (310, Y + 320), (310, Y + 360)], CAST)
    s += cable([(x0 + 76, Y + 250), (x0 + 76, Y + 290), (520, Y + 320), (520, Y + 360)], CAST)
    s += cable([(x0 + 224, Y + 250), (x0 + 224, Y + 290), (580, Y + 320), (580, Y + 360)], CEL)
    s += cable([(x0 + 236, Y + 250), (x0 + 236, Y + 290), (770, Y + 320), (770, Y + 360)], CEL)
    s += termo(x0, Y)
    for bx in (x0 + 70, x0 + 230):  # resalta los bornes con dos cables
        s += f'<circle cx="{bx}" cy="{Y+268}" r="34" fill="none" stroke="{ROJO}" stroke-width="6"/>'
    s += texto(370, Y + 205, '2 CABLES', 36, ROJO, 'end') + texto(370, Y + 247, 'EN 1 BORNE', 36, ROJO, 'end')
    s += (f'<circle cx="860" cy="{Y+180}" r="46" fill="{ROJO}"/>'
          f'<path d="M840,{Y+160} L880,{Y+200} M880,{Y+160} L840,{Y+200}" stroke="#FFF" stroke-width="11" stroke-linecap="round"/>')
    return s


def panel_bien(Y):
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="#F3FBF5" stroke="{VERDE_OK}" stroke-width="5"/>'
    s += chip(80, Y + 22, 'BIEN: UNO POR BORNE', VERDE_OK) + leyenda(Y)
    for x0, n, cx in ((130, '1', 100), (650, '2', 620)):
        s += cable([(x0 + 70, Y + 250), (x0 + 70, Y + 360)], CAST)
        s += cable([(x0 + 230, Y + 250), (x0 + 230, Y + 360)], CEL)
        s += termo(x0, Y)
        s += circuito(cx, Y, 360, 'CIRCUITO ' + n)
    s += (f'<circle cx="540" cy="{Y+250}" r="46" fill="{VERDE_OK}"/>'
          f'<path d="M518,{Y+250} L535,{Y+268} L564,{Y+232}" fill="none" stroke="#FFF" stroke-width="11" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')
    return s


s = encabezado('¿DOS CABLES EN', 'EL MISMO BORNE?', linea2_amarilla=True)
s += panel_mal(240)
s += panel_bien(740)
s += firma()
salida = sys.argv[1] if len(sys.argv) > 1 else 'x.png'
guardar(s, salida)
