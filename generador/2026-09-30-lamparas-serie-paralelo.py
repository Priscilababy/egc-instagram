# -*- coding: utf-8 -*-
"""Posteo 2026-09-30 · Dos lámparas con una misma llave: en serie vs. en paralelo. Formato MAL/BIEN.
Serie: la tensión se reparte (iguales: mitad cada una) y si una se quema se apagan las dos.
Paralelo: cada lámpara recibe la tensión completa y son independientes."""
import sys
from placa import *


def lampara(cx, cy, r=42):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FDF3C4" stroke="{NAVY}" stroke-width="5"/>'
            f'<path d="M{cx-30},{cy-30} L{cx+30},{cy+30} M{cx+30},{cy-30} L{cx-30},{cy+30}" '
            f'stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')


def llave(x, y):
    w, h = 170, 90
    return (f'<rect x="{x}" y="{y-h/2}" width="{w}" height="{h}" rx="16" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
            + texto(x + w / 2, y - h / 2 - 16, 'LLAVE', 34, NAVY, 'middle')
            + f'<circle cx="{x+24}" cy="{y}" r="11" fill="{NAVY}"/><circle cx="{x+w-24}" cy="{y}" r="11" fill="{NAVY}"/>'
            f'<line x1="{x+24}" y1="{y}" x2="{x+w-56}" y2="{y-30}" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>')


def panel(Y, etiqueta, color, serie):
    fondo = '#FFF5F5' if serie else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    s += texto(1000, Y + 60, 'lámparas de 220 V iguales', 32, NAVY, 'end', False)
    YF, YN = Y + 190, Y + 385
    s += borne(140, YF, CAST) + texto(100, YF + 12, 'F', 36, CAST, 'end')
    s += borne(140, YN, CEL) + texto(100, YN + 12, 'N', 36, CEL_TXT, 'end')
    SW = 240
    s += cable([(140, YF), (SW, YF)], CAST)
    s += llave(SW, YF)
    if serie:
        L1, L2 = 600, 830
        s += cable([(SW + 170, YF), (L1, YF)], RET, True)
        s += cable([(L1, YF), (L2, YF)], RET2, True)
        s += cable([(L2, YF), (960, YF), (960, YN)], RET2, True)
        s += cable([(140, YN), (960, YN)], CEL)
        s += lampara(L1, YF) + lampara(L2, YF)
        s += texto(L1, YF + 95, '110 V', 38, ROJO, 'middle') + texto(L2, YF + 95, '110 V', 38, ROJO, 'middle')
        s += texto(540, Y + 448, 'Si una se quema, se apagan las dos', 36, ROJO, 'middle')
    else:
        L1, L2 = 600, 830
        YM = (YF + YN) // 2
        s += cable([(SW + 170, YF), (L2, YF)], RET, True)
        s += cable([(140, YN), (L2, YN)], CEL)
        for x in (L1, L2):
            s += cable([(x, YF), (x, YM - 42)], RET, True)
            s += cable([(x, YM + 42), (x, YN)], CEL)
            s += lampara(x, YM)
            s += texto(x + 56, YM + 14, '220 V', 38, VERDE_OK)
        s += texto(540, Y + 448, 'Cada lámpara va por su cuenta', 36, VERDE_OK, 'middle')
    return s


s = encabezado('¿DOS LÁMPARAS, UNA LLAVE?', 'SERIE VS. PARALELO')
s += panel(240, 'EN SERIE', ROJO, True)
s += panel(740, 'EN PARALELO', VERDE_OK, False)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-09-30-lamparas-serie-paralelo.png'
guardar(s, salida)
