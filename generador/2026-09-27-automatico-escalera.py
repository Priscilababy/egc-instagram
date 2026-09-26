# -*- coding: utf-8 -*-
"""Posteo 2026-09-27 · Automático de escalera (pulsadores + temporizador). Formato CONEXIÓN
(tablero -> pulsadores en paralelo -> temporizador -> luminaria). Neutro alimenta la
electrónica del relé y también va directo a la luminaria (conocimiento/README.md, aviso
sobre temporizadores y relojes electrónicos)."""
import sys
from placa import *

s = encabezado('AUTOMÁTICO DE', 'ESCALERA')
s += tablero()

# Fase del IT: a los pulsadores (en paralelo) y al borne L del temporizador.
s += cable([(440, 363), (440, 415), (420, 415), (420, 520)], CAST)
s += cable([(440, 415), (190, 415), (190, 520)], CAST)
# Neutro: directo a la luminaria y derivación al borne N del temporizador (alimenta su electrónica).
s += cable([(700, 363), (700, 800), (740, 800), (740, 863)], CEL)
s += cable([(700, 450), (600, 450), (600, 520)], CEL)
# PE directo a la masa de la luminaria.
s += cable_pe([(920, 363), (920, 863)])
# Orden de los pulsadores al borne del temporizador (color no reservado, punteado).
s += cable([(190, 806), (190, 830), (420, 830), (420, 806)], RET, punteado=True)
# Salida del temporizador (fase conmutada) a la luminaria (color no reservado, punteado).
s += cable([(600, 806), (600, 840), (560, 840), (560, 863)], RET2, punteado=True)

# Caja de pulsadores (2, en paralelo)
s += caja(60, 520, 260, 270, 'PULSADORES', tam=32)
s += (f'<line x1="190" y1="520" x2="190" y2="560" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="130" y1="560" x2="250" y2="560" stroke="{NAVY}" stroke-width="5"/>')
for x in (130, 250):
    s += (f'<line x1="{x}" y1="560" x2="{x}" y2="592" stroke="{NAVY}" stroke-width="5"/>'
          f'<circle cx="{x}" cy="592" r="10" fill="{NAVY}"/>'
          f'<line x1="{x}" y1="592" x2="{x}" y2="656" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
          f'<circle cx="{x}" cy="666" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="676" x2="{x}" y2="700" stroke="{NAVY}" stroke-width="5"/>')
s += (f'<line x1="130" y1="700" x2="250" y2="700" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="190" y1="700" x2="190" y2="790" stroke="{NAVY}" stroke-width="5"/>')
s += texto(130, 760, 'P1', 32, NAVY, 'middle') + texto(250, 760, 'P2', 32, NAVY, 'middle')
s += borne(190, 520, CAST) + borne(190, 790, RET)

# Caja del temporizador (relé de escalera)
s += caja(350, 520, 320, 270, 'TEMPORIZADOR', tam=32)
s += (f'<circle cx="510" cy="655" r="46" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="510" y1="655" x2="510" y2="622" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
      f'<line x1="510" y1="655" x2="535" y2="655" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
      f'<circle cx="510" cy="655" r="5" fill="{NAVY}"/>')
s += (texto(390, 500, 'L', 36, CAST, 'end') + texto(630, 500, 'N', 36, CEL_TXT, 'start'))
s += borne(420, 520, CAST) + borne(600, 520, CEL) + borne(420, 790, RET) + borne(600, 790, RET2)

# Bornera de la luminaria
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(560, 880, RET2) + borne(740, 880, CEL) + borne(920, 880, VERDE)
s += (texto(560, 950, 'L', 32, RET2, 'middle') + texto(740, 950, 'N', 32, CEL_TXT, 'middle')
      + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Farol de luminaria de escalera encendido
s += (f'<line x1="740" y1="990" x2="740" y2="1030" stroke="#5B6573" stroke-width="10"/>'
      f'<path d="M660,1030 L820,1030 L780,1110 L700,1110 Z" fill="{GRIS}" stroke="#5B6573" stroke-width="4"/>'
      f'<ellipse cx="740" cy="1115" rx="50" ry="16" fill="#FDF3C4" stroke="{NAVY}" stroke-width="4"/>'
      f'<g stroke="{AMARILLO}" stroke-width="8" stroke-linecap="round">'
      f'<line x1="680" y1="1150" x2="665" y2="1170"/><line x1="800" y1="1150" x2="815" y2="1170"/>'
      f'<line x1="710" y1="1165" x2="700" y2="1190"/><line x1="770" y1="1165" x2="780" y2="1190"/>'
      f'<line x1="740" y1="1175" x2="740" y2="1200"/></g>')

s += mensaje(['Los pulsadores', 'piden; el relé', 'necesita neutro.'], tam=34)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-09-27-automatico-escalera.png'
guardar(s, salida)
