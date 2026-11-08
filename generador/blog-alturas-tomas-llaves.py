# -*- coding: utf-8 -*-
"""Portada del blog: alturas de tomas y llaves (fichas 08 y 50, edición 2026)."""
import sys
from placa import *

s = encabezado('ALTURAS DE TOMAS', 'Y LLAVES · EDICIÓN 2026')
# Pared, piso y marco de puerta
s += f'<rect x="60" y="240" width="600" height="860" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
s += f'<rect x="500" y="240" width="160" height="860" fill="#DDE2E8" stroke="{NAVY}" stroke-width="4"/>'
s += texto(580, 330, 'PUERTA', 32, GRIS, 'middle')
s += f'<line x1="40" y1="1100" x2="680" y2="1100" stroke="{NAVY}" stroke-width="12"/>'
# Llave a 1,10 m (330 px sobre... escala 700 px/m)
s += f'<rect x="300" y="295" width="50" height="70" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<line x1="325" y1="315" x2="325" y2="345" stroke="{NAVY}" stroke-width="6"/>'
s += texto(325, 420, 'LLAVE', 34, NAVY, 'middle')
s += f'<line x1="350" y1="470" x2="500" y2="470" stroke="{NAVY}" stroke-width="5"/>'
s += texto(425, 515, '≤ 25 cm', 34, NAVY, 'middle')
# Toma a 20 cm
s += f'<rect x="150" y="900" width="70" height="60" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<circle cx="172" cy="930" r="6" fill="{NAVY}"/><circle cx="198" cy="930" r="6" fill="{NAVY}"/>'
s += texto(250, 1055, '20 cm o más', 34)
s += texto(250, 940, 'TOMA', 34)
# Regla vertical
s += f'<line x1="110" y1="1100" x2="110" y2="330" stroke="{NAVY}" stroke-width="5"/>'
for y in (1100, 960, 330):
    s += f'<line x1="95" y1="{y}" x2="125" y2="{y}" stroke="{NAVY}" stroke-width="5"/>'
s += texto(135, 650, '1,10 m', 38)
s += texto(135, 690, '(recomendada)', 32, NAVY, 'start', False)
# Mesada
s += caja(690, 240, 330, 400, 'SOBRE MESADA', 34)
s += f'<rect x="720" y="560" width="270" height="30" fill="#C9CFD7" stroke="{NAVY}" stroke-width="4"/>'
s += f'<rect x="840" y="395" width="70" height="60" rx="8" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<line x1="770" y1="455" x2="770" y2="560" stroke="{NAVY}" stroke-width="5"/>'
s += texto(790, 505, '15 cm', 34) + texto(790, 545, 'o más', 34)
# Pantalla
s += caja(690, 680, 330, 250, 'HASTA 0,90 m', 34)
for i, t in enumerate(['Toma con', 'pantalla', '2 x 10 A + T']):
    s += texto(715, 800 + 48 * i, t, 36)
s += mensaje(['Edición 2026:', 'desde el', '1/11/2026'], x=690, y=960, tam=36)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'prueba.png'
guardar(s, salida)
