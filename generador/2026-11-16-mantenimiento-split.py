# -*- coding: utf-8 -*-
"""Mantenimiento preventivo de un split: rutina y qué medir y anotar (ficha 20, BP p. 41-44; MB p. 70)."""
import sys
from placa import *

s = encabezado('MANTENIMIENTO SPLIT', 'QUÉ LIMPIAR Y QUÉ ANOTAR')


def lista(x, y0, items, color, sin_casilla=()):
    out = ''
    for i, t in enumerate(items):
        y = y0 + 64 * i
        if i in sin_casilla:
            out += texto(x + 50, y, t, 34)
            continue
        out += f'<rect x="{x}" y="{y-30}" width="34" height="34" rx="6" fill="#FFF" stroke="{color}" stroke-width="5"/>'
        out += (f'<polyline points="{x+7},{y-13} {x+15},{y-5} {x+28},{y-24}" fill="none" stroke="{color}"'
                f' stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
        out += texto(x + 50, y, t, 34)
    return out


s += caja(45, 215, 485, 600, 'LIMPIAR Y REVISAR')
s += lista(70, 345, ['Filtros', 'Serpentina interior', 'Serpentina exterior', 'Turbina interior',
                     'Bandeja y desagote', 'Ventilador exterior', 'Bornes y tornillos', 'Uniones: fugas'], VERDE_OK)

s += caja(550, 215, 485, 600, 'MEDIR Y ANOTAR')
s += lista(575, 345, ['Tensión', 'Corriente (pinza)', 'Presión de alta', 'Presión de baja',
                      'Temp. de retorno', 'Temp. de impulsión', 'Temp. y humedad', 'interior y exterior'], NAVY, sin_casilla=(7,))

s += mensaje(['Anotá cada medición', 'en la hoja de vida', 'del equipo.'], x=45, y=845, ancho=485)

s += f'<rect x="550" y="845" width="485" height="230" rx="18" fill="#FDECEC" stroke="{ROJO}" stroke-width="4"/>'
for i, t in enumerate(['Exterior: lavar', 'sin mojar las', 'partes eléctricas.']):
    s += texto(578, 910 + 60 * i, t, 38, ROJO)

s += texto(540, 1150, 'Compará con la placa', 36, NAVY, 'middle')
s += texto(540, 1200, 'y con los valores del fabricante.', 36, NAVY, 'middle')
s += firma('Manual del fabricante')

salida = sys.argv[1] if len(sys.argv) > 1 else 'prueba.png'
guardar(s, salida)
