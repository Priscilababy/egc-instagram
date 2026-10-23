# -*- coding: utf-8 -*-
"""Portada del blog: IUG, TUG y TUE."""
import sys
from placa import *

s = encabezado('IUG, TUG Y TUE', 'QUÉ ES CADA CIRCUITO')


def fila(y, sigla, que, prot):
    r = f'<rect x="60" y="{y}" width="190" height="90" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    r += texto(155, y + 62, sigla, 50, NAVY, 'middle')
    return r + texto(280, y + 40, que, 36) + texto(280, y + 80, prot, 34, GRIS)


s += fila(250, 'IUG', 'Iluminación y cargas hasta 10 A', 'protección máx. 16 A · 15 bocas')
s += fila(370, 'TUG', 'Tomas 2P+T de 10 A', 'protección máx. 20 A · 15 bocas')
s += fila(490, 'TUE', 'Tomas de uso especial (+10 A)', 'protección máx. 32 A · 15 bocas')
s += texto(60, 660, 'Mínimos: IUG 1,5 mm² · TUG y TUE 2,5 mm²', 36)
s += mensaje(['La térmica máxima del circuito', 'nunca supera lo que aguanta el cable'], y=730, tam=40)
s += texto(60, 1000, '- Todos son monofásicos, con diferencial 30 mA', 34)
s += texto(60, 1045, '- Verificar IB ≤ In ≤ Iz en cada circuito', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
