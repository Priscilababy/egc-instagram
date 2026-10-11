# -*- coding: utf-8 -*-
"""Selectividad: diferencial selectivo (S) de 300 mA aguas arriba y 30 mA aguas abajo (2026-10-12)."""
import sys
from placa import *

FX, NX = 190, 510        # fase y neutro de entrada
FB, NB = 190, 960        # barra de fase (izq.) y neutro (der.)
s = encabezado('SELECTIVIDAD', 'DE DIFERENCIALES')

def aparato(y, h, t1, t2):
    r = f'<rect x="100" y="{y}" width="500" height="{h}" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    r += texto(350, y + 42, t1, 34, ancla='middle') + texto(350, y + 82, t2, 34, NAVY, 'middle')
    return r + borne(FX, y, CAST) + borne(NX, y, CEL) + borne(FX, y + h, CAST) + borne(NX, y + h, CEL)

# Cables de punta a punta (fase y neutro pasan por todos los aparatos)
for a, b in ((222, 250), (350, 385), (485, 560)):
    s += cable([(FX, a), (FX, b)], CAST) + cable([(NX, a), (NX, b)], CEL)

s += aparato(250, 100, 'CABECERA', 'bipolar')
s += texto(630, 295, 'TABLERO PRINCIPAL', 34, GRIS)
s += aparato(385, 100, 'DIFERENCIAL S', 'bipolar 300 mA')
s += texto(630, 428, 'Aguas arriba:', 34) + texto(630, 472, 'selectivo (S)', 34)
s += texto(630, 530, 'TABLERO SECCIONAL', 34, GRIS)
s += aparato(560, 100, 'DIFERENCIAL', 'bipolar 30 mA')
s += texto(630, 608, 'Aguas abajo:', 34) + texto(630, 652, 'no retardado', 34)

# Barras y circuitos
tops = [740, 870]
s += cable([(FB, 660), (FB, tops[1] - 28), (340, tops[1] - 28)], CAST)
s += cable([(NX, 660), (NX, tops[0] - 28), (NB, tops[0] - 28), (NB, tops[1] - 28), (820, tops[1] - 28)], CEL)
for y0, t in zip(tops, ('Termomagnética bipolar', 'Termomagnética bipolar')):
    s += cable([(340, y0 - 28), (340, y0)], CAST) + cable([(820, y0 - 28), (820, y0)], CEL)
    if y0 != tops[1]:
        s += cable([(FB, y0 - 28), (340, y0 - 28)], CAST)
    if y0 != tops[1]:
        s += f'<circle cx="{FB}" cy="{y0-28}" r="10" fill="{CAST}"/><circle cx="{NB}" cy="{y0-28}" r="10" fill="{CEL}"/>'
    s += f'<rect x="300" y="{y0}" width="560" height="65" rx="12" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    s += texto(580, y0 + 44, t, 34, ancla='middle')
    s += cable([(420, y0 + 65), (420, y0 + 100)], CAST) + cable([(740, y0 + 65), (740, y0 + 100)], CEL)
    s += borne(340, y0, CAST) + borne(820, y0, CEL)
s += texto(150, tops[1] - 40, 'F', 40, CAST, 'middle') + texto(1005, tops[1] - 40, 'N', 40, CEL_TXT, 'middle')

s += mensaje(['Dos diferenciales en serie:', 'dispara primero el de 30 mA.'], y=1055, tam=34)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'selectividad.png'
guardar(s, salida)
