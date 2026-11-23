# -*- coding: utf-8 -*-
"""Posteo 2026-11-24 · Tierra lejana: la toma de protección separada de la tierra de servicio. Formato CONEXIÓN.
Fuentes: conocimiento/06 (AEA 90364-7-770 ed. 2017, 770.3.2, 770.14.4.2, Tabla 770.3.I),
conocimiento/33 (Tabla 771.3.II, jabalinas IRAM 2309/2310) y conocimiento/35 (neutro de la red a tierra en muchos puntos).
Dibujo esquemático, no a escala."""
import sys
from placa import *

s = encabezado('TIERRA LEJANA', 'A MÁS DE 10 × Re')

XS, XP = 230, 830        # toma de servicio / toma de protección
SUELO = 480
FONDO = 650

# Arriba: neutro de la red (izquierda) y barra PE del tablero (derecha)
s += f'<rect x="55" y="222" width="350" height="80" rx="12" fill="#F6F8FA" stroke="{CEL_TXT}" stroke-width="4"/>'
s += texto(230, 274, 'NEUTRO DE LA RED', 32, CEL_TXT, 'middle')
s += cable([(XS, 302), (XS, SUELO + 30)], CEL)
s += f'<rect x="690" y="222" width="280" height="80" rx="12" fill="#F6F8FA" stroke="{VERDE}" stroke-width="4"/>'
s += texto(830, 275, 'BARRA PE', 38, VERDE, 'middle')
s += cable_pe([(XP, 302), (XP, SUELO - 46)])
s += texto(XP - 24, 350, 'cable de PAT', 32, VERDE, 'end', negrita=False)

# Cota de separación
yc = 430
s += (f'<line x1="{XS+40}" y1="{yc}" x2="{XP-80}" y2="{yc}" stroke="{NAVY}" stroke-width="4"/>'
      f'<path d="M{XS+40},{yc} l18,-10 v20 z M{XP-80},{yc} l-18,-10 v20 z" fill="{NAVY}"/>')
s += texto((XS + XP - 40) / 2, yc - 18, 'más de 10 × Re', 40, NAVY, 'middle')

# Suelo
s += f'<rect x="45" y="{SUELO}" width="990" height="250" fill="#EFE6D8"/>'
s += f'<line x1="45" y1="{SUELO}" x2="1035" y2="{SUELO}" stroke="#7A6A55" stroke-width="5"/>'

for x in (XS, XP):
    s += f'<rect x="{x-9}" y="{SUELO+20}" width="18" height="{FONDO-SUELO-20}" fill="#8A8F96" stroke="{NAVY}" stroke-width="3"/>'
    s += f'<path d="M{x-9},{FONDO} L{x},{FONDO+22} L{x+9},{FONDO} z" fill="#8A8F96" stroke="{NAVY}" stroke-width="3"/>'
    s += f'<circle cx="{x}" cy="{SUELO+30}" r="11" fill="{NAVY}"/>'
# cámara de inspección solo en la toma de protección
s += f'<rect x="{XP-55}" y="{SUELO-38}" width="110" height="80" rx="6" fill="none" stroke="{NAVY}" stroke-width="5"/>'
s += f'<rect x="{XP-62}" y="{SUELO-46}" width="124" height="12" fill="{NAVY}"/>'

s += texto((XS + XP) / 2, SUELO + 90, 'sin ninguna unión', 34, NAVY, 'middle', negrita=False)
s += texto((XS + XP) / 2, SUELO + 132, 'entre las dos tomas', 34, NAVY, 'middle', negrita=False)
s += texto(XS, SUELO + 225, 'TOMA DE SERVICIO', 32, CEL_TXT, 'middle')
s += texto(XP, SUELO + 225, 'TOMA DE PROTECCIÓN', 32, VERDE, 'middle')

# Tabla 10 × Re (Tabla 771.3.II / 770.3.I, jabalinas IRAM 2309 y 2310, de 1/2" a 3/4")
y0 = 770
s += texto(60, y0, 'Según largo y diámetro (1/2" a 3/4"):', 34)
filas = [('Jabalina de 1,5 m', 'más de 3,2 a 3,4 m'),
         ('Jabalina de 3 m', 'más de 5,4 a 5,8 m'),
         ('Jabalina de 6 m', 'más de 9,8 a 10,2 m')]
xt, yt = 60, y0 + 22
s += f'<rect x="{xt}" y="{yt}" width="960" height="186" rx="12" fill="#F6F8FA" stroke="{NAVY}" stroke-width="3"/>'
for i, (a, b) in enumerate(filas):
    y = yt + 48 + 58 * i
    if i:
        s += f'<line x1="{xt}" y1="{y-40}" x2="{xt+960}" y2="{y-40}" stroke="#DDE2E8" stroke-width="3"/>'
    s += texto(xt + 24, y, a, 36, NAVY)
    s += texto(xt + 936, y, b, 36, VERDE_OK, 'end')

s += mensaje(['La tierra de la casa es propia,', 'independiente y lejana.'], y=1020, tam=40)
s += firma('AEA 90364 · Tabla 771.3.II')

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-24-tierra-lejana.png'
guardar(s, salida)
