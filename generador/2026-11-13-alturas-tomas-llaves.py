# -*- coding: utf-8 -*-
"""Posteo 2026-11-13 · Alturas y ubicación de tomas y llaves (fichas 08 y 50, AEA 770 edición 2026)."""
import sys
from placa import *

s = encabezado('ALTURAS DE TOMAS', 'Y LLAVES · EDICIÓN 2026')
PISO = 1100          # escala 600 px/m
def y(m): return PISO - m * 600

# Pared y franja de altura de llaves (0,90 a 1,30 m)
s += f'<rect x="60" y="230" width="640" height="{PISO-230}" fill="#F6F8FA" stroke="#DDE2E8" stroke-width="3"/>'
s += f'<rect x="120" y="{y(1.30)}" width="480" height="{y(0.90)-y(1.30)}" fill="#FFF6D6"/>'
# Puerta (marco)
s += f'<rect x="600" y="230" width="100" height="{PISO-230}" fill="#DDE2E8" stroke="{NAVY}" stroke-width="4"/>'
s += f'<text x="650" y="760" font-size="34" font-weight="bold" fill="{NAVY}" text-anchor="middle" transform="rotate(-90 650 760)">PUERTA</text>'
# Piso
s += f'<line x1="50" y1="{PISO}" x2="710" y2="{PISO}" stroke="{NAVY}" stroke-width="12"/>'
s += texto(380, PISO + 50, 'PISO TERMINADO', 32, GRIS, 'middle')

# Regla vertical
s += f'<line x1="100" y1="{PISO}" x2="100" y2="{y(1.30)}" stroke="{NAVY}" stroke-width="5"/>'
for m in (0.20, 0.90, 1.10, 1.30):
    s += f'<line x1="85" y1="{y(m)}" x2="115" y2="{y(m)}" stroke="{NAVY}" stroke-width="5"/>'
s += texto(130, y(1.30) + 45, '1,30 m', 34)
s += texto(130, y(1.10) + 12, '1,10 m', 40)
s += texto(130, y(1.10) + 52, 'recomendada', 32, NAVY, 'start', False)
s += texto(130, y(0.90) - 12, '0,90 m', 34)
s += texto(130, y(0.20) + 12, '20 cm o más', 34)

# Llave a 1,10 m y hasta 25 cm del marco
s += texto(440, y(1.10) - 50, 'LLAVE', 34, NAVY, 'middle')
s += f'<rect x="410" y="{y(1.10)-35}" width="60" height="70" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<line x1="440" y1="{y(1.10)-18}" x2="440" y2="{y(1.10)+18}" stroke="{NAVY}" stroke-width="6"/>'
s += f'<line x1="470" y1="{y(1.10)}" x2="600" y2="{y(1.10)}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="10 8"/>'
s += texto(535, y(1.10) + 50, 'hasta', 32, NAVY, 'middle', False)
s += texto(535, y(1.10) + 88, '25 cm', 32, NAVY, 'middle')

# Zona hasta 0,90 m: tomas con pantalla
s += texto(130, 680, 'Hasta 0,90 m:', 34)
s += texto(130, 722, 'tomas con pantalla', 34)
s += texto(130, 764, '2 x 10 A + T', 34, NAVY, 'start', False)
# Toma sobre zócalo (borde inferior a 20 cm)
s += texto(470, y(0.20) - 85, 'TOMA', 34, NAVY, 'middle')
s += f'<rect x="435" y="{y(0.20)-60}" width="70" height="60" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<circle cx="458" cy="{y(0.20)-32}" r="6" fill="{NAVY}"/><circle cx="482" cy="{y(0.20)-32}" r="6" fill="{NAVY}"/>'
s += f'<line x1="470" y1="{y(0.20)}" x2="470" y2="{PISO}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="10 8"/>'

# Sobre mesada
s += caja(730, 230, 290, 370, 'SOBRE MESADA', 34)
s += f'<rect x="900" y="370" width="64" height="60" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<circle cx="921" cy="400" r="6" fill="{NAVY}"/><circle cx="943" cy="400" r="6" fill="{NAVY}"/>'
s += f'<rect x="750" y="520" width="250" height="30" fill="#C9CFD7" stroke="{NAVY}" stroke-width="4"/>'
s += f'<line x1="880" y1="430" x2="880" y2="520" stroke="{NAVY}" stroke-width="4"/>'
s += f'<line x1="866" y1="430" x2="894" y2="430" stroke="{NAVY}" stroke-width="4"/>'
s += texto(760, 465, '15 cm', 34) + texto(760, 505, 'o más', 34)
s += texto(875, 588, 'MESADA', 32, GRIS, 'middle')

# Pasillo
s += caja(730, 630, 290, 250, 'PASILLO +3 m', 34)
for i, t in enumerate(['Llave de', 'combinación', 'en cada punta']):
    s += texto(750, 750 + 44 * i, t, 34)

s += mensaje(['Rige la', 'edición 2026', 'desde 1/11/26'], x=730, y=910, ancho=290, tam=34)
s += firma()

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
