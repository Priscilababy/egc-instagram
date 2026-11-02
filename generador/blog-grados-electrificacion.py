# -*- coding: utf-8 -*-
"""Portada del blog: grados de electrificación."""
import sys
from placa import *

s = encabezado('GRADOS DE', 'ELECTRIFICACIÓN')


def fila(y, grado, sup, circ):
    r = f'<rect x="60" y="{y}" width="260" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    r += texto(190, y + 66, grado, 42, NAVY, 'middle')
    return r + texto(350, y + 44, sup, 36) + texto(350, y + 86, circ, 34, GRIS)


s += fila(250, 'MÍNIMO', 'hasta 60 m²', 'mínimo 2 circuitos')
s += fila(370, 'MEDIO', '60 a 130 m²', 'mínimo 3 circuitos')
s += fila(490, 'ELEVADO', '130 a 200 m²', 'mínimo 5 circuitos')
s += fila(610, 'SUPERIOR', 'más de 200 m²', 'mínimo 6 circuitos')
s += texto(60, 790, 'Superficie = cubierta + 50 % de semicubierta', 34)
s += mensaje(['Los metros definen el grado,', 'el grado define los circuitos.'], y=840, tam=40)
s += texto(60, 1110, '- Los puntos mínimos son mínimos: se puede poner más', 34)
s += texto(60, 1160, '- Calculá la superficie con el plano', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
