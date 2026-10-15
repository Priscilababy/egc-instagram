# -*- coding: utf-8 -*-
"""2026-10-16 · AIRE · MAL/BIEN: split con alargue vs. línea exclusiva con diferencial y térmica bipolar."""
import sys
from placa import *


def tres(x1, x2, Y):
    return (cable([(x1, Y + 140), (x2, Y + 140)], CAST) + cable([(x1, Y + 170), (x2, Y + 170)], CEL)
            + cable_pe([(x1, Y + 200), (x2, Y + 200)]))


def bloque(x, Y, w, t, tam=38, h=130):
    return (f'<rect x="{x}" y="{Y+105}" width="{w}" height="{h}" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
            + texto(x + w / 2, Y + 105 + h / 2 + 14, t, tam, ancla='middle'))


def mal(Y):
    s = f'<rect x="50" y="{Y}" width="980" height="390" rx="24" fill="#FFF5F5" stroke="{ROJO}" stroke-width="5"/>'
    s += chip(80, Y + 20, 'MAL · ALARGUE COMPARTIDO', ROJO)
    s += tres(80, 980, Y)
    s += bloque(80, Y, 220, 'TABLERO') + bloque(410, Y, 230, 'ALARGUE') + bloque(760, Y, 220, 'SPLIT')
    for x in (485, 525, 565):
        s += cable([(x, Y + 235), (x, Y + 270)], GRIS)
    s += (f'<rect x="395" y="{Y+265}" width="260" height="105" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          + texto(525, Y + 308, 'OTROS', 36, ancla='middle') + texto(525, Y + 351, 'APARATOS', 36, ancla='middle'))
    s += texto(700, Y + 330, 'El fabricante', 36, ROJO) + texto(700, Y + 372, 'pide sin alargue', 36, ROJO)
    return s


def bien(Y):
    s = f'<rect x="50" y="{Y}" width="980" height="390" rx="24" fill="#F3FBF5" stroke="{VERDE_OK}" stroke-width="5"/>'
    s += chip(80, Y + 20, 'BIEN · LÍNEA EXCLUSIVA', VERDE_OK)
    s += tres(80, 980, Y)
    s += bloque(80, Y, 220, 'ID 30 mA') + bloque(340, Y, 260, 'TÉRMICA 2P') + bloque(760, Y, 220, 'SPLIT')
    s += texto(80, Y + 310, 'Cable de 2,5 mm² como mínimo', 38)
    s += texto(80, Y + 360, 'Un solo equipo, sin derivaciones', 38)
    return s


s = encabezado('SPLIT CON ALARGUE', 'O LÍNEA EXCLUSIVA', linea2_amarilla=True)
s += mal(215)
s += bien(625)
s += mensaje(['Un split, una línea propia:', 'diferencial 30 mA + térmica bipolar'], y=1030, tam=38)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'split.png'
guardar(s, salida)
