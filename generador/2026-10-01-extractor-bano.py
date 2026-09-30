# -*- coding: utf-8 -*-
"""Posteo 2026-10-01 · Extractor de baño que prende junto con la luz. Formato CONEXIÓN.
Una llave unipolar corta la fase; el retorno (gris, punteado) alimenta luz y extractor en paralelo.
Neutro y PE directo a la bornera. Fuente: fichas 08 y 21 (el extractor cuenta como boca de iluminación)."""
import sys
from placa import *

s = encabezado('EXTRACTOR DE BAÑO', 'QUE PRENDE CON LA LUZ')
s += tablero()

# Fase del IT al común de la llave; neutro y PE directo a la bornera
s += cable([(440, 363), (440, 450), (260, 450), (260, 503)], CAST)
s += cable([(700, 363), (700, 800), (780, 800), (780, 863)], CEL)
s += cable_pe([(920, 363), (920, 863)])
# Retorno único (gris punteado) que se deriva a luz y extractor
s += cable([(260, 806), (260, 850), (660, 850), (660, 863)], RET, punteado=True)
s += cable([(545, 850), (545, 863)], RET, punteado=True)
s += f'<circle cx="545" cy="850" r="10" fill="{RET}"/>'

# Llave de 1 punto (corta la fase)
s += caja(60, 520, 400, 270, 'LLAVE DE 1 PUNTO')
s += (f'<line x1="260" y1="592" x2="260" y2="662" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="260" cy="662" r="10" fill="{NAVY}"/>'
      f'<line x1="260" y1="662" x2="318" y2="738" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
      f'<circle cx="260" cy="744" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="260" y1="754" x2="260" y2="790" stroke="{NAVY}" stroke-width="5"/>')
s += borne(260, 520, CAST) + borne(260, 790, RET)

# Bornera
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(545, 880, RET) + borne(660, 880, RET) + borne(780, 880, CEL) + borne(920, 880, VERDE)
s += (texto(545, 950, 'LUZ', 32, RET, 'middle') + texto(660, 950, 'EXTR.', 32, RET, 'middle')
      + texto(780, 950, 'N', 32, CEL_TXT, 'middle') + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Cargas
s += cable([(545, 990), (545, 1040)], RET, punteado=True)
s += (f'<circle cx="545" cy="1085" r="42" fill="#FDF3C4" stroke="{NAVY}" stroke-width="5"/>'
      f'<path d="M515,1055 L575,1115 M575,1055 L515,1115" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')
s += texto(545, 1185, 'LUZ', 32, NAVY, 'middle')
s += cable([(660, 990), (660, 1012), (730, 1012), (730, 1040)], RET, punteado=True)
s += (f'<rect x="680" y="1040" width="100" height="100" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="730" cy="1090" r="36" fill="#FFF" stroke="{NAVY}" stroke-width="4"/>'
      f'<g fill="{GRIS}" stroke="{NAVY}" stroke-width="3">'
      f'<path d="M730,1090 L730,1056 Q752,1066 730,1090 Z"/>'
      f'<path d="M730,1090 L764,1090 Q754,1112 730,1090 Z"/>'
      f'<path d="M730,1090 L730,1124 Q708,1114 730,1090 Z"/>'
      f'<path d="M730,1090 L696,1090 Q706,1068 730,1090 Z"/></g>')
s += texto(730, 1185, 'EXTRACTOR', 32, NAVY, 'middle')

s += texto(1010, 1075, 'N y PE siguen', 32, NAVY, 'end') + texto(1010, 1115, 'a cada equipo', 32, NAVY, 'end')
s += mensaje(['Una llave,', 'dos cargas', 'en paralelo.'])
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-01-extractor-bano.png'
guardar(s, salida)
