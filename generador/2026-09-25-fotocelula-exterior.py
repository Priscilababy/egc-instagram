# -*- coding: utf-8 -*-
"""Posteo 2026-09-25 · Fotocélula para luz exterior. Formato CONEXIÓN (tablero -> fotocélula -> luminaria)."""
import sys
from placa import *

s = encabezado('FOTOCÉLULA PARA', 'LUZ EXTERIOR')
s += tablero()

# Fase del IT al borne L de la fotocélula.
s += cable([(440, 363), (440, 420), (170, 420), (170, 503)], CAST)
# Neutro: directo a la luminaria y derivación al borne N de la fotocélula (alimenta el sensor).
s += cable([(700, 363), (700, 800), (740, 800), (740, 863)], CEL)
s += cable([(700, 470), (350, 470), (350, 503)], CEL)
s += f'<circle cx="700" cy="470" r="13" fill="{CEL_TXT}"/>'
# PE directo a la masa de la luminaria.
s += cable_pe([(920, 363), (920, 863)])
# Salida CARGA de la fotocélula a la luminaria: fase conmutada.
s += cable([(260, 806), (260, 850), (560, 850), (560, 863)], NEG, punteado=True)

# Caja de la fotocélula con sensor de luz
s += caja(60, 520, 400, 270, 'FOTOCÉLULA')
s += (f'<polyline points="170,592 170,690 210,690" fill="none" stroke="{NAVY}" stroke-width="5"/>'
      f'<polyline points="350,592 350,690 310,690" fill="none" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="260" y1="740" x2="260" y2="790" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="260" cy="690" r="50" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="260" cy="690" r="22" fill="{AMARILLO}"/>')
for a, b, c, d in ((282, 690, 302, 690), (276, 706, 290, 720), (260, 712, 260, 732), (244, 706, 230, 720),
                   (238, 690, 218, 690), (244, 674, 230, 660), (260, 668, 260, 648), (276, 674, 290, 660)):
    s += f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="{AMARILLO}" stroke-width="6" stroke-linecap="round"/>'
s += borne(170, 520, CAST) + borne(350, 520, CEL) + borne(260, 790, NEG)
s += (texto(140, 500, 'L', 36, CAST, 'end') + texto(380, 500, 'N', 36, CEL_TXT)
      + texto(235, 840, 'CARGA', 32, NEG, 'end'))

# Bornera de la luminaria exterior
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(560, 880, NEG) + borne(740, 880, CEL) + borne(920, 880, VERDE)
s += (texto(560, 950, 'L', 32, NEG, 'middle') + texto(740, 950, 'N', 32, CEL_TXT, 'middle')
      + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Farol exterior encendido
s += (f'<line x1="740" y1="990" x2="740" y2="1030" stroke="#5B6573" stroke-width="10"/>'
      f'<path d="M660,1030 L820,1030 L780,1110 L700,1110 Z" fill="{GRIS}" stroke="#5B6573" stroke-width="4"/>'
      f'<ellipse cx="740" cy="1115" rx="50" ry="16" fill="#FDF3C4" stroke="{NAVY}" stroke-width="4"/>'
      f'<g stroke="{AMARILLO}" stroke-width="8" stroke-linecap="round">'
      f'<line x1="680" y1="1150" x2="665" y2="1170"/><line x1="800" y1="1150" x2="815" y2="1170"/>'
      f'<line x1="710" y1="1165" x2="700" y2="1190"/><line x1="770" y1="1165" x2="780" y2="1190"/>'
      f'<line x1="740" y1="1175" x2="740" y2="1200"/></g>')

s += mensaje(['Conmuta la fase.', 'Necesita neutro', 'para funcionar.'])
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-09-25-fotocelula-exterior.png'
guardar(s, salida)
