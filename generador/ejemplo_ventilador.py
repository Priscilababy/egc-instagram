# -*- coding: utf-8 -*-
"""Ejemplo 1 · Diagrama de conexión: ventilador de techo con luz (publicado el 2026-09-24).
Usar como plantilla para esquemas del tipo "tablero → llave → artefacto"."""
import sys
from placa import *

s = encabezado('VENTILADOR DE TECHO', 'CON LUZ')
s += tablero()

# Fase del IT al común de la llave. Neutro y PE directo a la bornera del ventilador.
s += cable([(440, 363), (440, 450), (260, 450), (260, 503)], CAST)
s += cable([(700, 363), (700, 800), (780, 800), (780, 863)], CEL)
s += cable_pe([(920, 363), (920, 863)])
# Retornos (punteados, color no reservado): punto 1 -> motor (gris), punto 2 -> luz (violeta)
s += cable([(150, 806), (150, 850), (545, 850), (545, 863)], RET, punteado=True)
s += cable([(370, 806), (370, 828), (660, 828), (660, 863)], RET2, punteado=True)

# Llave de 2 puntos
s += caja(60, 520, 400, 270, 'LLAVE DE 2 PUNTOS')
s += (f'<line x1="260" y1="592" x2="260" y2="630" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="150" y1="630" x2="370" y2="630" stroke="{NAVY}" stroke-width="5"/>')
for x in (150, 370):
    s += (f'<line x1="{x}" y1="630" x2="{x}" y2="662" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="662" x2="{x}" y2="734" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
          f'<circle cx="{x}" cy="662" r="10" fill="{NAVY}"/>'
          f'<circle cx="{x}" cy="744" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="754" x2="{x}" y2="790" stroke="{NAVY}" stroke-width="5"/>')
s += texto(106, 718, '1', 44, ancla='middle') + texto(414, 718, '2', 44, ancla='middle')
s += borne(260, 520, CAST) + borne(150, 790, RET) + borne(370, 790, RET2)

# Bornera del ventilador
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(545, 880, RET) + borne(660, 880, RET2) + borne(780, 880, CEL) + borne(920, 880, VERDE)
s += (texto(545, 950, 'MOTOR', 32, RET, 'middle') + texto(660, 950, 'LUZ', 32, RET2, 'middle')
      + texto(780, 950, 'N', 32, CEL_TXT, 'middle') + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Dibujo del ventilador con luz encendida
s += (f'<line x1="760" y1="990" x2="760" y2="1040" stroke="#5B6573" stroke-width="10"/>'
      f'<ellipse cx="600" cy="1070" rx="105" ry="20" fill="#C9CFD7" stroke="#5B6573" stroke-width="4"/>'
      f'<ellipse cx="920" cy="1070" rx="105" ry="20" fill="#C9CFD7" stroke="#5B6573" stroke-width="4"/>'
      f'<ellipse cx="760" cy="1068" rx="78" ry="36" fill="{GRIS}" stroke="#5B6573" stroke-width="4"/>'
      f'<g stroke="{AMARILLO}" stroke-width="8" stroke-linecap="round">'
      f'<line x1="678" y1="1150" x2="660" y2="1162"/><line x1="842" y1="1150" x2="860" y2="1162"/>'
      f'<line x1="710" y1="1192" x2="700" y2="1210"/><line x1="810" y1="1192" x2="820" y2="1210"/>'
      f'<line x1="760" y1="1200" x2="760" y2="1220"/></g>'
      f'<path d="M700,1102 a60,80 0 0 0 120,0 z" fill="#FDF3C4" stroke="{NAVY}" stroke-width="5"/>')

s += mensaje(['Entra 1 fase,', 'salen 2 retornos:', 'motor y luz.'])
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'ejemplo_ventilador.png'
guardar(s, salida)
