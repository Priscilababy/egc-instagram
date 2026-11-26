# -*- coding: utf-8 -*-
"""Portada del blog: mediciones antes de entregar una instalación (fichas 70, 12, 49)."""
import sys
from placa import *


def fila(y, n, titulo, valor):
    s = f'<rect x="80" y="{y}" width="920" height="130" rx="16" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
    s += f'<circle cx="140" cy="{y+65}" r="34" fill="{NAVY}"/>'
    s += texto(140, y + 79, str(n), 40, '#FFF', 'middle')
    s += texto(200, y + 56, titulo, 40)
    s += texto(200, y + 106, valor, 36, VERDE_OK)
    return s


s = encabezado('ANTES DE ENTREGAR', 'LA INSTALACIÓN')
s += fila(230, 1, 'Continuidad del PE', 'En todas las masas')
s += fila(380, 2, 'Aislación (500 V CC)', 'Mínimo 1 MΩ por circuito')
s += fila(530, 3, 'Puesta a tierra (TT)', 'Máximo 100 Ω (770 ed. 2026)')
s += fila(680, 4, 'Diferencial de 30 mA', 'Con instrumento: ≤ 300 ms a IΔn')
s += mensaje(['Primero inspección visual,', 'después las mediciones,', 'y todo queda en el informe.'], x=60, y=870, tam=40)
s += firma('AEA 90364-6 · AEA 90364')

guardar(s, sys.argv[1])
