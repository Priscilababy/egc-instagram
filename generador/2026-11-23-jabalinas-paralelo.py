# -*- coding: utf-8 -*-
"""Posteo 2026-11-23 · Jabalinas en paralelo: separación entre ellas. Formato CONEXIÓN.
Fuente: conocimiento/31 (AEA 90364-7-771, Anexo 771-C, 771-C.2.2 Nota 2, pág. 189; 771-C.2.4)
y 49/50/52 (100 Ω, edición 2026). Dibujo a escala: 3 m = 200 px, 6 m = 400 px."""
import sys
from placa import *

s = encabezado('JABALINAS EN PARALELO', 'SEPARACIÓN MÍNIMA: 2 × L')

COBRE = '#B87333'
XA, XB = 340, 740        # 400 px = 6 m
SUELO = 480
FONDO = SUELO + 200      # 200 px = 3 m

# Barra PE del tablero y cable de puesta a tierra
s += f'<rect x="60" y="225" width="240" height="80" rx="12" fill="#F6F8FA" stroke="{VERDE}" stroke-width="4"/>'
s += texto(180, 278, 'BARRA PE', 38, VERDE, 'middle')
s += cable_pe([(180, 305), (180, 360), (XA, 360), (XA, SUELO-46)])
s += texto(XA + 24, 300, 'cable de PAT', 34, VERDE, negrita=False)
s += texto(XA + 24, 340, 'a la barra PE', 34, VERDE, negrita=False)

# Cota de separación (sobre el suelo)
yc = 418
s += (f'<line x1="{XA+70}" y1="{yc}" x2="{XB-70}" y2="{yc}" stroke="{NAVY}" stroke-width="4"/>'
      f'<path d="M{XA+70},{yc} l18,-10 v20 z M{XB-70},{yc} l-18,-10 v20 z" fill="{NAVY}"/>')
s += texto((XA+XB)/2, yc - 16, '6 m o más', 40, NAVY, 'middle')

# Suelo
s += f'<rect x="45" y="{SUELO}" width="990" height="250" fill="#EFE6D8"/>'
s += f'<line x1="45" y1="{SUELO}" x2="1035" y2="{SUELO}" stroke="#7A6A55" stroke-width="5"/>'

# Conductor desnudo enterrado entre las dos cámaras
s += cable([(XA, SUELO + 30), (XB, SUELO + 30)], COBRE)
s += texto((XA+XB)/2, SUELO + 85, 'cobre desnudo enterrado', 32, '#7A4A1E', 'middle', negrita=False)

for x, rot in ((XA, 'A'), (XB, 'B')):
    # jabalina
    s += f'<rect x="{x-9}" y="{SUELO+20}" width="18" height="{FONDO-SUELO-20}" fill="#8A8F96" stroke="{NAVY}" stroke-width="3"/>'
    s += f'<path d="M{x-9},{FONDO} L{x},{FONDO+22} L{x+9},{FONDO} z" fill="#8A8F96" stroke="{NAVY}" stroke-width="3"/>'
    # cámara de inspección
    s += f'<rect x="{x-55}" y="{SUELO-38}" width="110" height="80" rx="6" fill="none" stroke="{NAVY}" stroke-width="5"/>'
    s += f'<rect x="{x-62}" y="{SUELO-46}" width="124" height="12" fill="{NAVY}"/>'
    s += f'<circle cx="{x}" cy="{SUELO+30}" r="11" fill="{NAVY}"/>'

s += texto(70, SUELO + 110, 'cámara', 34, NAVY, negrita=False)
s += texto(70, SUELO + 150, 'en cada', 34, NAVY, negrita=False)
s += texto(70, SUELO + 190, 'jabalina', 34, NAVY, negrita=False)
s += f'<line x1="{140}" y1="{SUELO+75}" x2="{XA-58}" y2="{SUELO+20}" stroke="{NAVY}" stroke-width="3"/>'

# Cota del largo
xl = XB + 70
s += (f'<line x1="{xl}" y1="{SUELO+20}" x2="{xl}" y2="{FONDO}" stroke="{NAVY}" stroke-width="4"/>'
      f'<path d="M{xl},{SUELO+20} l-10,18 h20 z M{xl},{FONDO} l-10,-18 h20 z" fill="{NAVY}"/>')
s += texto(xl + 22, SUELO + 125, 'L = 3 m', 40, NAVY)

# Tabla: cuánto sube sobre el cálculo teórico
y0 = 778
s += texto(60, y0, 'Cuánto sube la resistencia sobre el cálculo', 34)
s += texto(60, y0 + 40, 'teórico en paralelo (jabalinas de 3 m):', 34)
filas = [('2 jabalinas', '~7 %', '~3 %'), ('4 en cuadrado', '~20 %', '~8 %')]
xt, yt = 60, y0 + 62
s += f'<rect x="{xt}" y="{yt}" width="960" height="170" rx="12" fill="#F6F8FA" stroke="{NAVY}" stroke-width="3"/>'
s += texto(xt + 20, yt + 46, 'Separación', 34, GRIS)
s += texto(xt + 600, yt + 46, 'a 6 m', 36, NAVY, 'middle')
s += texto(xt + 830, yt + 46, 'a 15 m', 36, NAVY, 'middle')
for i, (a, b, c) in enumerate(filas):
    y = yt + 102 + 54 * i
    s += f'<line x1="{xt}" y1="{y-44}" x2="{xt+960}" y2="{y-44}" stroke="#DDE2E8" stroke-width="3"/>'
    s += texto(xt + 20, y, a, 36, NAVY)
    s += texto(xt + 600, y, b, 38, ROJO if b == '~20 %' else NAVY, 'middle')
    s += texto(xt + 830, y, c, 38, VERDE_OK, 'middle')

s += mensaje(['Más juntas, menos rinden.', 'Se mide al final: 100 Ω máx.'], y=1035, tam=40)
s += firma('AEA 90364-7-771 · Anexo C')

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-23-jabalinas-paralelo.png'
guardar(s, salida)
