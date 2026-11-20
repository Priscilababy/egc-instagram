# -*- coding: utf-8 -*-
"""Portada del blog: monofásico o trifásico, cuándo conviene pasar."""
import sys
from placa import *

s = encabezado('MONOFÁSICO O TRIFÁSICO', 'CUÁNDO CONVIENE PASAR')


def fila(y, titulo, linea2):
    r = f'<rect x="60" y="{y}" width="960" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    return r + texto(90, y + 44, titulo, 38) + texto(90, y + 84, linea2, 34, GRIS)


s += texto(60, 275, 'Red de 220/380 V, 50 Hz:', 40)
s += fila(310, 'Monofásico: 1 fase + neutro', '220 V entre fase y neutro')
s += fila(430, 'Trifásico: 3 fases + neutro', '380 V entre fases')
s += fila(550, 'Circuitos IUG, TUG y TUE', 'siempre monofásicos (fase + N)')
s += texto(60, 730, 'Cabecera: bipolar o tetrapolar, 63 A máx.', 38)
s += mensaje(['Carga total de más de', '7 kVA o 32 A: se recomienda', 'pedir suministro trifásico'], y=790, tam=40)
s += texto(60, 1060, '- En trifásico: desequilibrio máx. 30 %', 34)
s += texto(60, 1105, '- Diferencial 30 mA en todos los circuitos', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
