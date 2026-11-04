# -*- coding: utf-8 -*-
"""Portada del blog: cuánto da cada jabalina (ficha 23, tabla del autor, ρ = 50 Ω·m, 5/8")."""
import sys
from placa import *

s = encabezado('¿CUÁNTAS JABALINAS', 'HACEN FALTA?', linea2_amarilla=True)
s += '<rect x="30" y="300" width="1020" height="560" fill="#E9DCC8"/>'
s += '<rect x="30" y="296" width="1020" height="10" fill="#7B5A2E"/>'
s += texto(60, 270, 'Terreno de 50 Ω·m (referencia)', 36)
for x, L, h, r in ((190, '1,5 m', 135, '35,2 Ω'), (500, '3 m', 270, '19,4 Ω'), (810, '6 m', 540, '10,6 Ω')):
    s += f'<rect x="{x-14}" y="306" width="28" height="{h}" rx="6" fill="#B87333" stroke="{NAVY}" stroke-width="4"/>'
    s += texto(x, 890, L, 44, ancla='middle') + texto(x, 940, r, 44, NAVY, 'middle')
s += mensaje(['El largo pesa mucho más', 'que el diámetro. Límite: 40 Ω,', 'medido con telurímetro.'], y=990)
s += firma()
guardar(s, sys.argv[1])
