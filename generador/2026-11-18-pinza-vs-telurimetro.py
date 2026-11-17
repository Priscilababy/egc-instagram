# -*- coding: utf-8 -*-
"""Posteo 2026-11-18 · MAL/BIEN: medir la tierra de una vivienda TT con pinza vs. con el método del 62 %.
Fuentes: conocimiento/34 (pinza: necesita lazo de retorno), 06 (770.19.5.3, telurímetro y 62 %), 33 (TT, toma independiente)."""
import sys
from placa import *


def pica(x, suelo, color, alto=110, ancho=16):
    return (f'<rect x="{x-ancho//2}" y="{suelo-16}" width="{ancho}" height="{alto+16}" fill="{color}"/>'
            f'<polygon points="{x-ancho//2},{suelo+alto} {x+ancho//2},{suelo+alto} {x},{suelo+alto+20}" fill="{color}"/>')


def suelo(Y, alto=150):
    return (f'<rect x="54" y="{Y}" width="972" height="{alto}" fill="#E9DCC8"/>'
            f'<line x1="54" y1="{Y}" x2="1026" y2="{Y}" stroke="#7A5C3A" stroke-width="6"/>')


s = encabezado('¿MEDÍS LA TIERRA', 'CON PINZA?')

# ───────── PANEL MAL ─────────
Y = 222
s += f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="#FFF5F5" stroke="{ROJO}" stroke-width="5"/>'
s += chip(80, Y + 22, 'MAL', ROJO)
s += texto(210, Y + 63, 'pinza en vivienda TT', 40, ROJO)
SU = Y + 330   # 552
s += suelo(SU, 132)
# barra PE de la vivienda
s += (f'<rect x="90" y="{Y+110}" width="220" height="90" rx="12" fill="#FFF" stroke="{VERDE}" stroke-width="5"/>'
      + texto(200, Y + 170, 'BARRA PE', 36, VERDE, 'middle'))
XJ = 200
s += cable_pe([(XJ, Y + 200), (XJ, SU - 16)])
s += pica(XJ, SU, '#9A6A3A', 100, 20)
s += texto(XJ + 30, SU + 70, '1 sola jabalina', 34, NAVY)
# pinza abrazando el cable de tierra
PY = Y + 262
s += (f'<ellipse cx="{XJ}" cy="{PY}" rx="46" ry="24" fill="none" stroke="{NAVY}" stroke-width="10"/>'
      f'<line x1="{XJ+46}" y1="{PY}" x2="{XJ+110}" y2="{PY}" stroke="{NAVY}" stroke-width="12"/>'
      f'<rect x="{XJ+110}" y="{PY-45}" width="150" height="90" rx="12" fill="{NAVY}"/>'
      + texto(XJ + 185, PY + 13, 'PINZA', 34, '#FFF', 'middle'))
# explicación
s += texto(500, Y + 150, 'No hay lazo cerrado:', 38, NAVY)
s += texto(500, Y + 200, 'la pinza no mide', 38, NAVY)
s += texto(500, Y + 250, 'la toma de tierra.', 38, NAVY)
s += (f'<circle cx="930" cy="{Y+400}" r="46" fill="{ROJO}"/>'
      f'<path d="M910,{Y+380} L950,{Y+420} M950,{Y+380} L910,{Y+420}" stroke="#FFF" stroke-width="11" stroke-linecap="round"/>')

# ───────── PANEL BIEN ─────────
Y = 712
s += f'<rect x="50" y="{Y}" width="980" height="390" rx="24" fill="#F3FBF5" stroke="{VERDE_OK}" stroke-width="5"/>'
s += chip(80, Y + 22, 'BIEN', VERDE_OK)
s += texto(240, Y + 63, 'telurímetro, método 62 %', 40, VERDE_OK)
XT, XT1 = 160, 960
XT2 = int(XT + 0.62 * (XT1 - XT))   # 656
SU = Y + 270   # 982
s += suelo(SU, 112)
s += (f'<rect x="300" y="{Y+100}" width="300" height="90" rx="12" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      + texto(450, Y + 160, 'TELURÍMETRO', 36, NAVY, 'middle'))
s += cable([(330, Y + 190), (330, Y + 225), (XT, Y + 225), (XT, SU - 16)], NAVY)
s += cable([(500, Y + 190), (500, Y + 225), (XT2, Y + 225), (XT2, SU - 16)], RET2)
s += cable([(600, Y + 125), (XT1, Y + 125), (XT1, SU - 16)], RET)
# posiciones -1 m y +1 m
for dx in (-70, 70):
    s += (f'<rect x="{XT2+dx-6}" y="{SU-12}" width="12" height="72" fill="none" '
          f'stroke="{RET2}" stroke-width="4" stroke-dasharray="10 8"/>')
s += pica(XT, SU, '#9A6A3A', 50, 20) + pica(XT2, SU, RET2, 50) + pica(XT1, SU, RET, 50)
s += texto(XT + 24, SU + 50, 'T', 40, NAVY)
s += texto(XT + 24, SU + 98, 'toma', 32, NAVY)
s += texto(XT2 - 84, SU + 45, '−1 m', 32, RET2, 'end')
s += texto(XT2 + 84, SU + 45, '+1 m', 32, RET2)
s += texto(XT2, SU + 102, 'T2 al 62 %', 32, RET2, 'middle')
s += texto(XT1 - 24, SU + 50, 'T1', 40, RET, 'end')
s += texto(XT1 - 24, SU + 98, 'lejos', 32, RET, 'end')

# mensaje clave
s += mensaje(['Vivienda TT: tres lecturas con telurímetro.'], y=1118, ancho=960, tam=38)
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'pinza.png')
