# -*- coding: utf-8 -*-
"""Portada del blog: cables enterrados dentro del terreno (ficha 11, AEA 770 ed. 2017, 770.10.4)."""
import sys
from placa import *

s = encabezado('CABLES ENTERRADOS', 'EN EL TERRENO')

# Corte de zanja
X0, X1 = 330, 750          # paredes de la zanja
SUP = 300                  # superficie
FON = 950                  # fondo (0,7 m)
s += f'<rect x="60" y="{SUP}" width="960" height="{FON-SUP+40}" fill="#E9DCC7"/>'
s += f'<rect x="{X0}" y="{SUP}" width="{X1-X0}" height="{FON-SUP}" fill="#F3EBDD" stroke="#9C8462" stroke-width="5"/>'
s += f'<line x1="60" y1="{SUP}" x2="1020" y2="{SUP}" stroke="{NAVY}" stroke-width="8"/>'
s += texto(80, SUP-20, 'Superficie', 34)

# Cinta a 0,2 m de la superficie (0,2/0,7 * 650 = 186)
yc = SUP + 186
s += f'<rect x="{X0+20}" y="{yc-12}" width="{X1-X0-40}" height="24" fill="{ROJO}"/>'
for x in range(X0+40, X1-30, 60):
    s += f'<rect x="{x}" y="{yc-12}" width="25" height="24" fill="#FFF"/>'
s += texto(X1+25, yc-30, 'Cinta roja', 34) + texto(X1+25, yc+12, 'a 0,2 m de la', 34) + texto(X1+25, yc+54, 'superficie', 34)

# Ladrillos atravesados
yl = FON - 190
for i in range(3):
    x = X0 + 50 + i*115
    s += f'<rect x="{x}" y="{yl}" width="95" height="50" rx="4" fill="#B5533A" stroke="#7A3424" stroke-width="3"/>'
s += texto(X1+25, yl+10, 'Ladrillos', 34) + texto(X1+25, yl+52, 'o loseta', 34)

# Arena y cable
s += f'<rect x="{X0+5}" y="{yl+50}" width="{X1-X0-10}" height="{FON-yl-55}" fill="#F7E7A8"/>'
ycab = FON - 60
s += f'<circle cx="{(X0+X1)//2}" cy="{ycab}" r="34" fill="#2F2F2F"/>'
s += f'<circle cx="{(X0+X1)//2}" cy="{ycab}" r="20" fill="#5A5A5A"/>'
s += texto(X1+25, ycab+5, 'Cable con', 34) + texto(X1+25, ycab+47, 'envoltura', 34)
s += texto(X0+20, FON-100, 'Arena', 32, '#7A5C1E')

# Cota 0,7 m (hasta el cable)
xc = 200
s += f'<line x1="{xc}" y1="{SUP+10}" x2="{xc}" y2="{ycab-10}" stroke="{NAVY}" stroke-width="6"/>'
s += f'<path d="M{xc-16},{SUP+34} L{xc+16},{SUP+34} L{xc},{SUP+8} z" fill="{NAVY}"/>'
s += f'<path d="M{xc-16},{ycab-26} L{xc+16},{ycab-26} L{xc},{ycab} z" fill="{NAVY}"/>'
s += f'<line x1="{xc+20}" y1="{ycab}" x2="{(X0+X1)//2-40}" y2="{ycab}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="10,8"/>'
ym = (SUP+ycab)//2
s += f'<rect x="{xc-110}" y="{ym-70}" width="220" height="140" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="4"/>'
s += texto(xc, ym-5, '0,7 m', 48, NAVY, 'middle')
s += texto(xc, ym+45, 'mínimo', 34, NAVY, 'middle')

s += mensaje(['Unipolar sin envoltura:', 'nunca enterrado, ni en caño'], y=1020, tam=40)
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
