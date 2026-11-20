# -*- coding: utf-8 -*-
"""Placa extra 3/4 · Caño corrugado: liviano solo en seco; mampostería semipesado o pesado (fichas 07 y 51). Estilo serie especial."""
import sys
from serie2026 import *

s = fondo(3, 4, 'CAÑO EN LA PARED', 'LEÉ EL CÓDIGO')

# Decodificador del código IRAM 62386
s += tarjeta(60, 385, 960, 270)
for i, x in enumerate((100, 250)):
    s += f'<rect x="{x}" y="420" width="130" height="160" rx="24" fill="url(#ama)"/>'
    s += t(x + 65, 535, '3', 104, NAVY, 'middle')
s += t(165, 625, '1.º', 34, TXT2, 'middle', negrita=False)
s += t(315, 625, '2.º', 34, TXT2, 'middle', negrita=False)
s += t(430, 455, 'IRAM 62386', 40, AMA, max_w=560)
s += t(430, 510, '1.º dígito: COMPRESIÓN', 36, BLANCO, max_w=560)
s += t(430, 560, '2.º dígito: IMPACTO', 36, BLANCO, max_w=560)
s += t(430, 618, '2 liviano · 3 semipesado · 4 pesado', 32, TXT2, negrita=False, max_w=570)


def cano(x, y, largo, grosor, color):
    r = f'<rect x="{x}" y="{y}" width="{largo}" height="{grosor}" rx="{grosor/2}" fill="{color}" stroke="{NAVY}" stroke-width="3"/>'
    for xx in range(x + 16, x + largo - 8, 18):
        r += f'<line x1="{xx}" y1="{y+4}" x2="{xx}" y2="{y+grosor-4}" stroke="{NAVY}" stroke-width="3" opacity="0.35"/>'
    return r


def lado(x, color, codigo, nombre, l1, l2, ok, grosor):
    r = tarjeta(x, 685, 465, 400, borde=color)
    r += t(x + 40, 800, codigo, 92, color, max_w=320)
    # icono
    r += f'<circle cx="{x+400}" cy="760" r="36" fill="{color}"/>'
    if ok:
        r += f'<path d="M{x+382},760 L{x+396},775 L{x+420},745" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    else:
        r += f'<path d="M{x+386},746 L{x+414},774 M{x+414},746 L{x+386},774" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>'
    r += t(x + 40, 860, nombre, 34, BLANCO, max_w=410)
    r += cano(x + 40, 895 + (40 - grosor) / 2, 385, grosor, '#E8EEF5')
    r += t(x + 40, 1000, l1, 34, TXT2, negrita=False, max_w=400)
    r += t(x + 40, 1045, l2, 36, color, max_w=400)
    return r


s += lado(60, ROJO, '23', 'LIVIANO', 'Solo en', 'construcción en seco', False, 22)
s += lado(555, VERDE, '33 · 44', 'SEMIPESADO / PESADO', 'En pared de', 'mampostería', True, 44)

s += f'<rect x="60" y="1102" width="960" height="84" rx="26" fill="url(#ama)" filter="url(#sombra)"/>'
s += t(540, 1158, 'Leé el código impreso, no el color', 38, NAVY, 'middle', max_w=900)

s += pie()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
