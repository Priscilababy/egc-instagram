# -*- coding: utf-8 -*-
"""Tablero monofásico de vivienda: cabecera, diferencial, termomagnéticas bipolares y barra PE (2026-09-29)."""
import sys
from placa import *

FX, NX = 190, 510        # fase y neutro de entrada
FB, NB = 190, 960        # barra de fase (izq.) y neutro (der.)
s = encabezado('TABLERO MONOFÁSICO', 'DE VIVIENDA')

# Entrada y tramo cabecera -> diferencial (cables debajo de los aparatos)
s += cable([(FX, 222), (FX, 370)], CAST) + cable([(NX, 222), (NX, 370)], CEL)

def aparato(y, h, t1, t2):
    r = f'<rect x="100" y="{y}" width="500" height="{h}" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    r += texto(350, y + 42, t1, 34, ancla='middle') + texto(350, y + 82, t2, 34, NAVY, 'middle')
    return r + borne(FX, y, CAST) + borne(NX, y, CEL) + borne(FX, y + h, CAST) + borne(NX, y + h, CEL)

s += aparato(225, 95, 'CABECERA', 'bipolar')
s += texto(630, 268, 'Corta fase y neutro', 34) + texto(630, 312, '63 A como máximo', 34)
s += cable([(FX, 320), (FX, 370)], CAST) + cable([(NX, 320), (NX, 370)], CEL)
s += aparato(370, 95, 'DIFERENCIAL', 'bipolar 30 mA')
s += texto(630, 413, 'Fase y neutro pasan', 34) + texto(630, 457, 'por el diferencial', 34)

# Barras: fase a la izquierda, neutro a la derecha (sin cruces)
tops = [545, 680, 815]
s += cable([(FB, 465), (FB, tops[2] - 28), (340, tops[2] - 28)], CAST)
s += cable([(NX, 465), (NX, 485), (NB, 485), (NB, tops[2] - 28), (820, tops[2] - 28)], CEL)
datos = [('IUG · hasta 16 A', '1,5 mm² mín.'), ('TUG · hasta 20 A', '2,5 mm² mín.'), ('TUE · hasta 32 A', '2,5 mm² mín.')]
for y0, (t, sec) in zip(tops, datos):
    s += cable([(FB, y0 - 28), (340, y0 - 28), (340, y0)], CAST)
    s += cable([(NB, y0 - 28), (820, y0 - 28), (820, y0)], CEL)
    if y0 != tops[2]:
        s += f'<circle cx="{FB}" cy="{y0-28}" r="10" fill="{CAST}"/><circle cx="{NB}" cy="{y0-28}" r="10" fill="{CEL}"/>'
    s += f'<rect x="300" y="{y0}" width="560" height="65" rx="12" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    s += texto(580, y0 + 44, t, 34, ancla='middle')
    s += cable([(420, y0 + 65), (420, y0 + 100)], CAST) + cable([(740, y0 + 65), (740, y0 + 100)], CEL)
    s += texto(580, y0 + 98, sec, 32, GRIS, 'middle')
    s += borne(340, y0, CAST) + borne(820, y0, CEL)
s += texto(150, tops[1] - 10, 'F', 40, CAST, 'middle') + texto(1005, tops[1] - 10, 'N', 40, CEL_TXT, 'middle')

# Barra PE y toma de tierra
s += f'<rect x="300" y="955" width="560" height="50" rx="10" fill="{AMAR_PE}" stroke="{VERDE}" stroke-width="5"/>'
s += texto(580, 991, 'BARRA PE', 34, VERDE, 'middle')
for x in (380, 580, 780):
    s += cable_pe([(x, 1005), (x, 1030)])
s += cable_pe([(860, 980), (NB, 980), (NB, 1010)])
s += (f'<g stroke="{VERDE}" stroke-width="6"><line x1="925" y1="1010" x2="995" y2="1010"/>'
      f'<line x1="938" y1="1024" x2="982" y2="1024"/><line x1="951" y1="1038" x2="969" y2="1038"/></g>')

s += mensaje(['Bipolar de punta a punta:', 'el neutro pasa por todo.'], y=1055, tam=34)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'tablero.png'
guardar(s, salida)
