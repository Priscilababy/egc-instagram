# -*- coding: utf-8 -*-
"""Posteo 2026-09-25 · Fotocélula para luz exterior. Formato CONEXIÓN (tablero -> fotocélula -> luminaria)."""
import sys
from placa import *

s = encabezado('FOTOCÉLULA PARA', 'LUZ EXTERIOR')
s += tablero()

# Fase del IT a la entrada (L) de la fotocélula. Neutro y PE van directo a la bornera de la luminaria.
s += cable([(440, 363), (440, 450), (260, 450), (260, 503)], CAST)
s += cable([(700, 363), (700, 800), (740, 800), (740, 863)], CEL)
s += cable_pe([(920, 363), (920, 863)])
# Salida conmutada (C) de la fotocélula hacia la luminaria: solo corta la fase.
s += cable([(260, 806), (260, 850), (560, 850), (560, 863)], NEG, punteado=True)

# Caja de la fotocélula con sensor de luz
s += caja(60, 520, 400, 270, 'FOTOCÉLULA')
s += f'<line x1="260" y1="592" x2="260" y2="600" stroke="{NAVY}" stroke-width="5"/>'
s += f'<circle cx="260" cy="655" r="55" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<circle cx="260" cy="655" r="26" fill="{AMARILLO}"/>'
for dx, dy, ex, ey in (
    (286, 655, 308, 655), (278, 674, 294, 690), (260, 681, 260, 703), (242, 674, 226, 690),
    (234, 655, 212, 655), (242, 636, 226, 620), (260, 629, 260, 607), (278, 636, 294, 620),
):
    s += f'<line x1="{dx}" y1="{dy}" x2="{ex}" y2="{ey}" stroke="{AMARILLO}" stroke-width="6" stroke-linecap="round"/>'
s += f'<line x1="260" y1="710" x2="260" y2="790" stroke="{NAVY}" stroke-width="5"/>'
s += borne(260, 520, CAST) + borne(260, 790, NEG)

# Bornera de la luminaria exterior
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(560, 880, NEG) + borne(740, 880, CEL) + borne(920, 880, VERDE)
s += (texto(560, 950, 'L', 32, NEG, 'middle') + texto(740, 950, 'N', 32, CEL_TXT, 'middle')
      + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Dibujo del farol exterior encendido
s += (f'<line x1="740" y1="990" x2="740" y2="1030" stroke="#5B6573" stroke-width="10"/>'
      f'<path d="M660,1030 L820,1030 L780,1110 L700,1110 Z" fill="{GRIS}" stroke="#5B6573" stroke-width="4"/>'
      f'<ellipse cx="740" cy="1115" rx="50" ry="16" fill="#FDF3C4" stroke="{NAVY}" stroke-width="4"/>'
      f'<g stroke="{AMARILLO}" stroke-width="8" stroke-linecap="round">'
      f'<line x1="680" y1="1150" x2="665" y2="1170"/><line x1="800" y1="1150" x2="815" y2="1170"/>'
      f'<line x1="710" y1="1165" x2="700" y2="1190"/><line x1="770" y1="1165" x2="780" y2="1190"/>'
      f'<line x1="740" y1="1175" x2="740" y2="1200"/></g>')

s += mensaje(['Corta solo la fase,', 'el neutro va directo', 'a la luminaria.'])
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-09-25-fotocelula-exterior.png'
guardar(s, salida)
