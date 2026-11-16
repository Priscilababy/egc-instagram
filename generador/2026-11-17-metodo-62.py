# -*- coding: utf-8 -*-
"""Posteo 2026-11-17 · Método del 62 %: las tres lecturas para medir la puesta a tierra.
Fuentes: conocimiento/06 (AEA 770 ed. 2017, medición), 34 (criterio de las 3 lecturas), 49 y 50 (100 Ω ed. 2026)."""
import sys
from placa import *

s = encabezado('MEDIR LA TIERRA:', 'MÉTODO DEL 62 %')

XT, XT1 = 180, 960
XT2 = int(XT + 0.62 * (XT1 - XT))   # 663
SUELO = 640

# Telurímetro
s += caja(300, 225, 520, 190, 'TELURÍMETRO', 40)
s += texto(560, 375, 'R = V / I', 52, NAVY, 'middle')
# bornes del instrumento (abajo)
for x, c in ((360, NAVY), (XT2, RET2), (760, RET)):
    s += borne(x, 415, c)

# Suelo
s += f'<rect x="45" y="{SUELO}" width="990" height="170" fill="#E9DCC8"/>'
s += f'<line x1="45" y1="{SUELO}" x2="1035" y2="{SUELO}" stroke="#7A5C3A" stroke-width="6"/>'

# Puntas: T (jabalina a medir), T2 (tensión), T1 (corriente)
def pica(x, color, alto=150, ancho=14):
    return (f'<rect x="{x-ancho//2}" y="{SUELO-20}" width="{ancho}" height="{alto+20}" fill="{color}"/>'
            f'<polygon points="{x-ancho//2},{SUELO+alto} {x+ancho//2},{SUELO+alto} {x},{SUELO+alto+22}" fill="{color}"/>')

# T2 a -1 m y +1 m (posiciones fantasma)
for dx in (-105, 105):
    s += (f'<rect x="{XT2+dx-6}" y="{SUELO-14}" width="12" height="120" fill="none" '
          f'stroke="{RET2}" stroke-width="4" stroke-dasharray="10 8"/>')
s += texto(XT2 - 112, SUELO - 30, '−1 m', 32, RET2, 'end')
s += texto(XT2 + 112, SUELO - 30, '+1 m', 32, RET2, 'start')

s += pica(XT, '#9A6A3A', 170, 20) + pica(XT2, RET2) + pica(XT1, RET)

# Cables de medición
s += cable([(360, 432), (360, 500), (XT, 500), (XT, SUELO - 20)], NAVY)
s += cable([(XT2, 432), (XT2, SUELO - 20)], RET2)
s += cable([(760, 432), (760, 500), (XT1, 500), (XT1, SUELO - 20)], RET)
s += texto(XT2 + 18, 560, 'V', 40, RET2)
s += texto(915, 560, 'I', 40, RET, 'middle')

# Rótulos de las puntas (bajo tierra)
s += texto(XT + 26, SUELO + 60, 'T', 44, NAVY)
s += texto(XT + 26, SUELO + 100, 'toma', 32, NAVY)
s += texto(XT2 + 18, SUELO + 60, 'T2', 44, RET2)
s += texto(XT1 - 26, SUELO + 60, 'T1', 44, RET, 'end')
s += texto(XT1 - 26, SUELO + 100, 'lejos', 32, RET, 'end')

# Cotas
def cota(x1, x2, y, t, color=NAVY):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="4"/>'
            f'<line x1="{x1}" y1="{y-16}" x2="{x1}" y2="{y+16}" stroke="{color}" stroke-width="4"/>'
            f'<line x1="{x2}" y1="{y-16}" x2="{x2}" y2="{y+16}" stroke="{color}" stroke-width="4"/>'
            + texto((x1 + x2) / 2, y - 14, t, 36, color, 'middle'))
s += cota(XT, XT2, 880, '62 % de D', RET2)
s += cota(XT, XT1, 960, 'D', NAVY)

# Mensaje y valor máximo
s += mensaje(['Toma desconectada.', 'T2 al 62 %, −1 m y +1 m.', 'Si coinciden, promediás.'], y=995, tam=38)
s += (f'<rect x="745" y="995" width="285" height="230" rx="18" fill="{NAVY}"/>'
      + texto(887, 1060, 'MÁXIMO', 36, '#FFF', 'middle')
      + texto(887, 1130, '100 Ω', 64, AMARILLO, 'middle')
      + texto(887, 1190, 'ed. 2026', 34, '#FFF', 'middle'))
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'metodo62.png')
