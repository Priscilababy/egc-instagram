# -*- coding: utf-8 -*-
"""Portada del blog · ¿Qué circuito y qué protección lleva un aire acondicionado split?"""
import sys
from placa import *


def bloque(x, Y, w, t, tam=38, h=130):
    return (f'<rect x="{x}" y="{Y}" width="{w}" height="{h}" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
            + texto(x + w / 2, Y + h / 2 + 14, t, tam, ancla='middle'))


Y = 330
s = encabezado('CIRCUITO DEL SPLIT', 'Y SUS PROTECCIONES', linea2_amarilla=True)
s += chip(60, 235, 'UN EQUIPO · UNA LÍNEA', VERDE_OK)
y1, y2, y3 = Y + 40, Y + 75, Y + 110
for yy, col in ((y1, CAST), (y2, CEL)):
    s += cable([(60, yy), (1020, yy)], col)
s += cable_pe([(60, y3), (1020, y3)])
s += bloque(60, Y, 240, 'ID 30 mA') + bloque(350, Y, 320, 'TÉRMICA 2P') + bloque(780, Y, 240, 'SPLIT')
s += texto(60, Y + 230, 'Cable de 2,5 mm² como mínimo', 40)
s += texto(60, Y + 290, 'Sin otros aparatos ni derivaciones', 40)
s += texto(60, Y + 350, 'IB ≤ In ≤ Iz', 40)
s += texto(60, Y + 410, 'La norma decide por la corriente,', 40)
s += texto(60, Y + 460, 'no por las frigorías', 40)
s += mensaje(['Circuito exclusivo, ID 30 mA', 'y térmica bipolar por equipo'], y=940, tam=38)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'blog-circuito-split.png'
guardar(s, salida)
