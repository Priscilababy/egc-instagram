# -*- coding: utf-8 -*-
"""Posteo 2026-10-06 · Tira LED: 220 V -> fuente -> 12 V (CONEXIÓN)."""
import sys
from placa import *

s = encabezado('TIRA LED A 12 V', 'FUENTE, LLAVE Y POLARIDAD')
s += tablero()

# Fase -> llave unipolar; neutro y PE directo a la fuente
s += cable([(440, 363), (440, 450), (260, 450), (260, 520)], CAST)
s += cable([(700, 363), (700, 600)], CEL)
s += cable_pe([(920, 363), (920, 600)])
# Retorno de la llave (fase conmutada) -> borne L de la fuente: color no reservado
s += cable([(460, 700), (560, 700)], RET, punteado=True)
# Salida de 12 V: + (gris) y - (violeta), no son colores de fase
s += cable([(700, 900), (700, 1010)], RET, punteado=True)
s += cable([(900, 900), (900, 1010)], RET2, punteado=True)

# Llave unipolar (corta la fase)
s += caja(60, 520, 400, 250, 'LLAVE 1 POLO')
s += (f'<line x1="260" y1="592" x2="260" y2="640" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="260" cy="640" r="10" fill="{NAVY}"/>'
      f'<line x1="260" y1="640" x2="352" y2="684" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
      f'<circle cx="400" cy="700" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="410" y1="700" x2="460" y2="700" stroke="{NAVY}" stroke-width="5"/>')
s += borne(260, 520, CAST) + borne(460, 700, RET)

# Fuente
s += f'<rect x="560" y="600" width="460" height="300" rx="20" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(560, 700, RET) + borne(700, 600, CEL) + borne(920, 600, VERDE)
s += borne(700, 900, RET) + borne(900, 900, RET2)
s += (texto(592, 712, 'L', 40, NAVY)
      + texto(700, 664, 'N', 40, CEL_TXT, 'middle') + texto(920, 664, 'PE', 40, VERDE, 'middle')
      + texto(800, 770, 'FUENTE 12 V', 44, NAVY, 'middle')
      + texto(800, 822, 'separa 220 V de 12 V', 32, NAVY, 'middle')
      + texto(700, 872, '+', 52, NAVY, 'middle') + texto(900, 872, '−', 52, NAVY, 'middle'))

# Tira LED
s += f'<rect x="610" y="1010" width="410" height="76" rx="14" fill="#FDF3C4" stroke="{NAVY}" stroke-width="5"/>'
for x in range(640, 1000, 60):
    if abs(x - 700) > 25 and abs(x - 900) > 25:
        s += f'<rect x="{x}" y="1036" width="28" height="28" rx="6" fill="{AMARILLO}" stroke="{NAVY}" stroke-width="3"/>'
s += borne(700, 1010, RET) + borne(900, 1010, RET2)
s += texto(700, 1062, '+', 48, NAVY, 'middle') + texto(900, 1062, '−', 48, NAVY, 'middle')
s += texto(780, 1150, 'Respetá la polaridad', 38, NAVY, 'middle')

s += mensaje(['La tira va a 12 V,', 'nunca a 220 V.'])
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '../posts/2026-10-06-tira-led.png'
guardar(s, salida)
