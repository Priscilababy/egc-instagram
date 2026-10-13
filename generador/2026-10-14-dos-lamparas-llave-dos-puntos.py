# -*- coding: utf-8 -*-
"""Posteo 2026-10-14 · CONEXIÓN: dos lámparas, cada una con su pulsador de una llave de 2 puntos."""
import sys
from placa import *

s = encabezado('DOS LÁMPARAS', 'LLAVE DE 2 PUNTOS')
s += tablero()

# Fase del IT al común de la llave
s += cable([(440, 363), (440, 450), (260, 450), (260, 503)], CAST)

# Neutro: tronco hasta las dos lámparas (derivación en caja, punto en (880,875))
s += cable([(700, 363), (700, 800), (880, 800), (880, 985), (780, 985)], CEL)
s += cable([(880, 875), (780, 875)], CEL)
s += f'<circle cx="880" cy="875" r="12" fill="{CEL}"/>'

# Retornos punteados, color no reservado: punto 2 -> lámpara 2 (violeta), punto 1 -> lámpara 1 (gris)
s += cable([(370, 806), (370, 875), (520, 875)], RET2, punteado=True)
s += cable([(150, 806), (150, 985), (520, 985)], RET, punteado=True)

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

# Lámparas
for y, nombre, col in ((830, 'LÁMPARA 2', RET2), (940, 'LÁMPARA 1', RET)):
    cy = y + 45
    s += f'<rect x="520" y="{y}" width="260" height="90" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
    s += texto(650, cy + 12, nombre, 34, ancla='middle')
    s += borne(520, cy, col) + borne(780, cy, CEL)
    s += texto(548, cy - 24, 'L', 32, col) if False else ''

s += mensaje(['Cada pulsador enciende', 'su propia lámpara.'], y=1048)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'ejemplo.png'
guardar(s, salida)
