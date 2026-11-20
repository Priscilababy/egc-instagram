# -*- coding: utf-8 -*-
"""Placa extra 2/4 · Qué tipo de diferencial va en vivienda, edición 2026 (fichas 49, 50 y 51). Estilo serie especial."""
import sys
from serie2026 import *

s = fondo(2, 4, '¿QUÉ DIFERENCIAL', 'VA EN LA CASA?')

filas = [
    ('AC', ROJO, 'NO APTO EN VIVIENDAS', 'La electrónica lo puede', 'dejar sin actuar'),
    ('A', AMA, 'USO GENERAL', 'Alterna y continua', 'pulsante'),
    ('F', CIAN, 'EQUIPOS INVERTER', 'Cargas monofásicas con', 'frecuencias mixtas'),
    ('B', VERDE, 'CONTINUA LISA', 'Cargador de auto o FV,', 'si el fabricante lo pide'),
]
Y0, H, G = 385, 164, 14
for i, (letra, color, tit, l1, l2) in enumerate(filas):
    y = Y0 + i * (H + G)
    malo = letra == 'AC'
    s += tarjeta(60, y, 960, H, borde=color if malo else None)
    # ficha con la letra
    s += f'<circle cx="160" cy="{y + H/2}" r="64" fill="{color}" opacity="0.35" filter="url(#brillo)"/>'
    s += f'<rect x="100" y="{y+22}" width="120" height="120" rx="28" fill="{color}"/>'
    tam = 60 if malo else 84
    s += t(160, y + 82 + tam * 0.36, letra, tam, NAVY if not malo else BLANCO, 'middle')
    if malo:
        s += f'<line x1="112" y1="{y+130}" x2="208" y2="{y+34}" stroke="{BLANCO}" stroke-width="8" stroke-linecap="round"/>'
    s += t(260, y + 58, tit, 40, color if malo else BLANCO, max_w=740)
    s += t(260, y + 104, l1, 34, TXT2, negrita=False, max_w=740)
    s += t(260, y + 144, l2, 34, TXT2, negrita=False, max_w=740)
    if malo:
        s += f'<rect x="830" y="{y+24}" width="165" height="52" rx="26" fill="{ROJO}"/>'
        s += t(912, y + 62, 'FUERA', 32, BLANCO, 'middle')

# Destacado
yd = Y0 + 4 * (H + G) + 4
s += f'<rect x="60" y="{yd}" width="960" height="84" rx="26" fill="url(#ama)" filter="url(#sombra)"/>'
s += t(540, yd + 56, '30 mA en todos los circuitos terminales', 38, NAVY, 'middle', max_w=900)

s += pie()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
