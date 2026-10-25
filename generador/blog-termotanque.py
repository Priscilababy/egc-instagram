# -*- coding: utf-8 -*-
"""Portada del blog: termotanque eléctrico, circuito y protección."""
import sys
from placa import *

s = encabezado('TERMOTANQUE ELÉCTRICO', 'QUÉ CIRCUITO LLEVA')


def fila(y, titulo, linea2):
    r = f'<rect x="60" y="{y}" width="960" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    return r + texto(90, y + 44, titulo, 38) + texto(90, y + 84, linea2, 34, GRIS)


s += texto(60, 275, 'La corriente de la placa decide:', 40)
s += fila(310, 'Hasta 10 A: toma de 10 A (TUG)', 'protección máx. 20 A')
s += fila(430, 'Más de 10 A y hasta 20 A: TUE', 'toma 2P+T de 20 A')
s += fila(550, 'Un solo equipo, sin derivaciones: ACU', 'sección mínima 2,5 mm²')
s += texto(60, 730, 'Diferencial 30 mA + térmica bipolar', 38)
s += mensaje(['Se verifica IB ≤ In ≤ Iz:', 'la térmica nunca pasa', 'lo que aguanta el cable'], y=790, tam=40)
s += texto(60, 1060, '- 2,5 mm² en caño: Iz 21 A, térmica de hasta 20 A', 34)
s += texto(60, 1105, '- PE al borne de tierra del equipo', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
