# -*- coding: utf-8 -*-
"""Posteo 2026-10-05 · Reloj programador (timer) para iluminación. Formato CONEXIÓN.
Reloj: L (fase), N (neutro, alimenta su electrónica) y SALIDA (contacto que conmuta la fase). Neutro directo a la
luminaria y PE a su masa. Retorno punteado en gris (color no reservado).""",
import sys
from placa import *

s = encabezado('RELOJ PROGRAMADOR', 'PARA ILUMINACIÓN')
s += tablero()

# Fase: al borne L del reloj.
s += cable([(440, 363), (440, 420), (350, 420), (350, 503)], CAST)
# Neutro: directo a la luminaria y derivación al borne N del reloj.
s += cable([(700, 363), (700, 800), (740, 800), (740, 863)], CEL)
s += cable([(700, 470), (510, 470), (510, 503)], CEL)
s += f'<circle cx="700" cy="470" r="13" fill="{CEL_TXT}"/>'
# PE directo a la masa de la luminaria.
s += cable_pe([(920, 363), (920, 863)])
# Retorno a la luminaria: sale del borne SALIDA del reloj (gris punteado).
s += cable([(430, 806), (430, 850), (560, 850), (560, 863)], RET, punteado=True)

# Reloj programador (timer): L, N y SALIDA (contacto que conmuta la fase)
s += caja(280, 520, 320, 270, 'RELOJ')
s += (f'<circle cx="440" cy="670" r="58" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="440" y1="670" x2="440" y2="627" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
      f'<line x1="440" y1="670" x2="472" y2="690" stroke="{AMARILLO}" stroke-width="6" stroke-linecap="round"/>'
      f'<circle cx="440" cy="670" r="6" fill="{NAVY}"/>'
      f'<line x1="440" y1="728" x2="440" y2="790" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="350" y1="592" x2="350" y2="630" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="510" y1="592" x2="510" y2="630" stroke="{NAVY}" stroke-width="5"/>')
s += borne(350, 520, CAST) + borne(510, 520, CEL) + borne(430, 790, RET)
s += (texto(325, 500, 'L', 36, CAST, 'end') + texto(535, 500, 'N', 36, CEL_TXT)
      + texto(452, 830, 'SALIDA', 32, RET))

# Bornera de la luminaria
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(560, 880, RET) + borne(740, 880, CEL) + borne(920, 880, VERDE)
s += (texto(560, 950, 'L', 32, RET, 'middle') + texto(740, 950, 'N', 32, CEL_TXT, 'middle')
      + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Luminaria encendida
s += (f'<line x1="740" y1="990" x2="740" y2="1030" stroke="#5B6573" stroke-width="10"/>'
      f'<path d="M660,1030 L820,1030 L780,1110 L700,1110 Z" fill="{GRIS}" stroke="#5B6573" stroke-width="4"/>'
      f'<ellipse cx="740" cy="1115" rx="50" ry="16" fill="#FDF3C4" stroke="{NAVY}" stroke-width="4"/>'
      f'<g stroke="{AMARILLO}" stroke-width="8" stroke-linecap="round">'
      f'<line x1="680" y1="1150" x2="665" y2="1170"/><line x1="800" y1="1150" x2="815" y2="1170"/>'
      f'<line x1="710" y1="1165" x2="700" y2="1190"/><line x1="770" y1="1165" x2="780" y2="1190"/>'
      f'<line x1="740" y1="1175" x2="740" y2="1200"/></g>')

s += mensaje(['Sin neutro,', 'el reloj no anda.'], y=1020)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-05-reloj-programador.png'
guardar(s, salida)
