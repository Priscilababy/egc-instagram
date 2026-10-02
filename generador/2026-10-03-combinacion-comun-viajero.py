# -*- coding: utf-8 -*-
"""Posteo 2026-10-03 · Llave de combinación con común y viajero cambiados. Formato MAL/BIEN.
MAL: la fase entra a un borne viajero y el común de la llave 1 se usa como viajero.
Con las dos llaves en cualquier posición la luz solo enciende en 1 de las 4 combinaciones."""
import sys
from placa import *

SW1_X, SW2_X = 140, 480      # esquinas izquierdas de las llaves
T1 = (180, 260, 340)          # bornes de la llave 1 (de izquierda a derecha)
T2 = (520, 600, 680)          # bornes de la llave 2 (espejo de la llave 1)


def llave(Y, x, titulo, rotulos, rojos=()):
    s = (f'<rect x="{x}" y="{Y+110}" width="240" height="140" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
         + texto(x + 120, Y + 155, titulo, 34, NAVY, 'middle'))
    for i, r in enumerate(rotulos):
        s += texto(x + 40 + 80 * i, Y + 225, r, 40, ROJO if r in rojos else NAVY, 'middle')
    return s


def panel(Y, etiqueta, color, error):
    fondo = '#FFF5F5' if error else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    y2, y1, y3, y4 = Y + 288, Y + 322, Y + 356, Y + 396

    # Llaves: en el MAL el común real de la llave 1 está en el medio y la fase entró al borne de la izquierda.
    rot1 = ('1', 'C', '2') if error else ('C', '1', '2')
    s += llave(Y, SW1_X, 'LLAVE 1', rot1, rojos=('1', 'C') if error else ())
    s += llave(Y, SW2_X, 'LLAVE 2', ('2', '1', 'C'))
    for x in T1 + T2:
        s += borne(x, Y + 250, NAVY)

    # Viajeros (color no reservado, punteados)
    s += cable([(T1[1], Y + 250), (T1[1], y1), (T2[1], y1), (T2[1], Y + 250)], RET, True)
    s += cable([(T1[2], Y + 250), (T1[2], y2), (T2[0], y2), (T2[0], Y + 250)], RET2, True)

    # Fase al borne de la izquierda de la llave 1; retorno del común de la llave 2 a la lámpara
    s += borne(110, y3, CAST) + texto(86, y3 + 13, 'F', 36, CAST, 'end')
    s += cable([(110, y3), (T1[0], y3), (T1[0], Y + 250)], CAST)
    s += cable([(T2[2], Y + 250), (T2[2], y3), (815, y3)], RET, True)
    # Neutro directo a la lámpara
    s += borne(110, y4, CEL) + texto(86, y4 + 13, 'N', 36, CEL_TXT, 'end')
    s += cable([(110, y4), (815, y4)], CEL)

    # Lámpara
    s += texto(900, Y + 112, 'LÁMPARA', 34, NAVY, 'middle')
    s += f'<rect x="790" y="{Y+125}" width="220" height="292" rx="18" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    s += borne(815, y3, RET) + borne(815, y4, CEL)
    bx, by = 920, Y + 215
    s += f'<circle cx="{bx}" cy="{by}" r="48" fill="#FDF3C4" stroke="{NAVY}" stroke-width="4"/>'
    s += f'<rect x="{bx-22}" y="{by+50}" width="44" height="38" rx="5" fill="{GRIS}" stroke="{NAVY}" stroke-width="3"/>'

    if error:
        s += texto(540, Y + 456, 'SOLO ENCIENDE EN 1 DE 4 POSICIONES', 34, ROJO, 'middle')
    else:
        s += texto(540, Y + 456, 'SE PRENDE Y SE APAGA DESDE LAS DOS', 34, VERDE_OK, 'middle')
        s += (f'<line x1="660" y1="{Y+44}" x2="700" y2="{Y+44}" stroke="{CAST}" stroke-width="10"/>'
              + texto(712, Y + 57, 'fase', 34)
              + f'<line x1="810" y1="{Y+44}" x2="850" y2="{Y+44}" stroke="{CEL}" stroke-width="10"/>'
              + texto(862, Y + 57, 'neutro', 34))
    return s


s = encabezado('LLAVE DE COMBINACIÓN', 'EL COMÚN VA A LA FASE')
s += panel(240, 'FASE EN UN VIAJERO', ROJO, True)
s += panel(740, 'FASE AL COMÚN', VERDE_OK, False)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-03-combinacion-comun-viajero.png'
guardar(s, salida)
