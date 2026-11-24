# -*- coding: utf-8 -*-
"""Portada del blog: poder de corte de una termomagnética (fichas 26, 01, 05, 09, 65)."""
import sys
from placa import *


def fila(y, icn, ics, nota):
    s = f'<rect x="80" y="{y}" width="920" height="120" rx="16" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
    s += texto(120, y + 76, icn, 46)
    s += f'<path d="M420,{y+60} h90 m-24,-20 l24,20 l-24,20" fill="none" stroke="{AMARILLO}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
    s += texto(550, y + 76, ics, 46, VERDE_OK)
    s += texto(990, y + 76, nota, 32, GRIS, 'end', negrita=False)
    return s


s = encabezado('PODER DE CORTE', 'DE UNA TERMOMAGNÉTICA')
s += texto(80, 290, 'Icn (en el frente)', 40)
s += texto(550, 290, 'Ics (de servicio)', 40, VERDE_OK)
s += fila(330, '4.500 A', '4.500 A', '× 1')
s += fila(480, '6.000 A', '6.000 A', '× 1')
s += fila(630, '10.000 A', '7.500 A', '× 0,75')
s += texto(80, 830, 'Factor Ics / Icn según IEC 60898-1', 36, GRIS)
s += mensaje(['Poder de corte ≥ cortocircuito', 'presunto donde se instala', 'Vivienda (770): hasta 10 kA'], x=60, y=900, tam=40)
s += firma('IEC 60898-1 · AEA 90364')

guardar(s, sys.argv[1])
