# -*- coding: utf-8 -*-
"""Posteo 2026-11-19 · Resistividad del suelo: método Wenner con 4 picas en línea.
Fuentes: conocimiento/32 (Wenner, armado y fórmula simplificada ec. 2-19), 31 (771-C.9: medir hasta la
profundidad del electrodo), 49 y 50 (100 Ω ed. 2026)."""
import sys
from placa import *

s = encabezado('RESISTIVIDAD DEL SUELO:', 'MÉTODO WENNER')

SUELO = 640
PX = (150, 410, 670, 930)          # picas 1, 2, 3, 4 (misma separación d)
BX = (330, 470, 610, 750)          # bornes del telurímetro I1, P1, P2, I2
COL = (RET, RET2, RET2, RET)       # corriente gris, tensión violeta

# Telurímetro
s += caja(250, 228, 580, 204, 'TELURÍMETRO 4 HILOS', 38)
s += texto(540, 350, 'R = V / I', 50, NAVY, 'middle')
for x, t, c in zip(BX, ('I1', 'P1', 'P2', 'I2'), COL):
    s += texto(x, 405, t, 32, c, 'middle')
    s += borne(x, 432, c)

# Suelo
s += f'<rect x="45" y="{SUELO}" width="990" height="190" fill="#E9DCC8"/>'
s += f'<line x1="45" y1="{SUELO}" x2="1035" y2="{SUELO}" stroke="#7A5C3A" stroke-width="6"/>'

def pica(x, color, alto=70, ancho=16):
    return (f'<rect x="{x-ancho//2}" y="{SUELO-24}" width="{ancho}" height="{alto+24}" fill="{color}"/>'
            f'<polygon points="{x-ancho//2},{SUELO+alto} {x+ancho//2},{SUELO+alto} {x},{SUELO+alto+18}" fill="{color}"/>')

# Cables (sin cruces): I1->1, P1->2, P2->3, I2->4
s += cable([(BX[0], 449), (BX[0], 480), (PX[0], 480), (PX[0], SUELO - 24)], RET)
s += cable([(BX[1], 449), (BX[1], 530), (PX[1], 530), (PX[1], SUELO - 24)], RET2)
s += cable([(BX[2], 449), (BX[2], 530), (PX[2], 530), (PX[2], SUELO - 24)], RET2)
s += cable([(BX[3], 449), (BX[3], 480), (PX[3], 480), (PX[3], SUELO - 24)], RET)
for i, x in enumerate(PX):
    s += pica(x, COL[i])
s += texto(PX[0] + 22, 605, '1', 40, RET, 'start') + texto(PX[3] - 22, 605, '4', 40, RET, 'end')
s += texto(PX[1] - 22, 605, '2', 40, RET2, 'end') + texto(PX[2] + 22, 605, '3', 40, RET2, 'start')
s += texto(PX[0] + 30, 520, 'I', 40, RET) + texto(PX[3] - 30, 520, 'I', 40, RET, 'end')
s += texto(540, 585, 'V', 40, RET2, 'middle')

# Cota de profundidad b (pica 4)
xb = PX[3] + 50
s += (f'<line x1="{xb}" y1="{SUELO}" x2="{xb}" y2="{SUELO+88}" stroke="{NAVY}" stroke-width="4"/>'
      f'<line x1="{xb-14}" y1="{SUELO}" x2="{xb+14}" y2="{SUELO}" stroke="{NAVY}" stroke-width="4"/>'
      f'<line x1="{xb-14}" y1="{SUELO+88}" x2="{xb+14}" y2="{SUELO+88}" stroke="{NAVY}" stroke-width="4"/>')
s += texto(xb + 22, SUELO + 58, 'b', 40, NAVY)

# Cotas d
def cota(x1, x2, y, t):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{NAVY}" stroke-width="4"/>'
            f'<line x1="{x1}" y1="{y-16}" x2="{x1}" y2="{y+16}" stroke="{NAVY}" stroke-width="4"/>'
            f'<line x1="{x2}" y1="{y-16}" x2="{x2}" y2="{y+16}" stroke="{NAVY}" stroke-width="4"/>'
            + texto((x1 + x2) / 2, y - 14, t, 40, NAVY, 'middle'))
for a, b in zip(PX, PX[1:]):
    s += cota(a, b, 790, 'd')

s += texto(540, 872, 'Misma separación d · b de 30 cm o menos', 34, NAVY, 'middle')

# Fórmula
s += f'<rect x="60" y="900" width="960" height="135" rx="18" fill="{NAVY}"/>'
s += texto(540, 975, 'ρ ≈ 2 · π · d · R', 60, AMARILLO, 'middle')
s += texto(540, 1018, 'válida si d es mucho mayor que b', 32, '#FFF', 'middle')

# Mensaje y ejemplo
s += mensaje(['Más separación d,', 'mide más profundo.'], y=1050, tam=38)
s += (f'<rect x="640" y="1050" width="380" height="170" rx="18" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
      + texto(830, 1110, 'd = 2 m · R = 10 Ω', 34, NAVY, 'middle')
      + texto(830, 1185, 'ρ ≈ 126 Ω·m', 46, NAVY, 'middle'))
s += firma('AEA 90364')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'wenner.png')
