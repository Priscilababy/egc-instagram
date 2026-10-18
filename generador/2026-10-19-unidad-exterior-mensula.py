# -*- coding: utf-8 -*-
"""2026-10-19 · AIRE · CONEXIÓN: unidad exterior en ménsula, espacios libres y caja estanca para la alimentación."""
import sys
from placa import *

s = encabezado('UNIDAD EXTERIOR', 'EN MÉNSULA')
RAYA = '#D5DAE0'

def flecha(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="5"/>'
            f'<circle cx="{x1}" cy="{y1}" r="8" fill="{NAVY}"/><circle cx="{x2}" cy="{y2}" r="8" fill="{NAVY}"/>')

ux, uy, uw, uh = 400, 480, 300, 180
# obstáculos (arriba, izquierda y derecha)
s += f'<rect x="60" y="235" width="960" height="30" fill="{RAYA}" stroke="{NAVY}" stroke-width="4"/>'
s += f'<rect x="130" y="265" width="30" height="400" fill="{RAYA}" stroke="{NAVY}" stroke-width="4"/>'
s += f'<rect x="780" y="265" width="30" height="400" fill="{RAYA}" stroke="{NAVY}" stroke-width="4"/>'
# unidad
s += f'<rect x="{ux}" y="{uy}" width="{uw}" height="{uh}" rx="16" fill="#F6F8FA" stroke="{NAVY}" stroke-width="6"/>'
cx0, cy0 = ux + 150, uy + 90
s += f'<circle cx="{cx0}" cy="{cy0}" r="65" fill="none" stroke="{NAVY}" stroke-width="5"/>'
s += (f'<line x1="{cx0}" y1="{cy0}" x2="{cx0}" y2="{cy0-60}" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="{cx0}" y1="{cy0}" x2="{cx0+52}" y2="{cy0+30}" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="{cx0}" y1="{cy0}" x2="{cx0-52}" y2="{cy0+30}" stroke="{NAVY}" stroke-width="5"/>')
# ménsulas
for x in (ux + 40, ux + uw - 40):
    s += f'<polygon points="{x-20},{uy+uh} {x+20},{uy+uh} {x-20},{uy+uh+80}" fill="{GRIS}" stroke="{NAVY}" stroke-width="4"/>'
s += texto(ux - 10, uy + uh + 60, 'MÉNSULA', 34, ancla='end')

# espacios libres
s += flecha(550, 265, 550, uy) + texto(580, 390, '60 cm', 36)
s += flecha(ux, 570, 160, 570) + texto(280, 545, '60 cm', 36, ancla='middle')
s += flecha(ux + uw, 570, 780, 570) + texto(830, 580, '10 a 30 cm', 34)

# caja estanca con la alimentación (cae por debajo de la unidad, entre ménsulas)
s += f'<rect x="400" y="770" width="300" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += texto(550, 818, 'CAJA ESTANCA', 34, ancla='middle') + texto(550, 862, 'IP44 / IP55', 34, ancla='middle')
s += cable([(490, 770), (490, uy + uh)], CAST)
s += cable([(550, 770), (550, uy + uh)], CEL)
s += cable_pe([(610, 770), (610, uy + uh)])

s += texto(60, 935, '- Pared sólida: aguanta 4 veces el peso', 34)
s += texto(60, 978, '- Nunca apoyada en el piso ni en un recinto', 34)
s += texto(60, 1021, '- Delante: 60 a 200 cm según el modelo', 34)
s += mensaje(['Distancias y bulones:', 'manual del modelo.'], y=1040, tam=36)
s += firma()

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'ext.png')
