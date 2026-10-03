# -*- coding: utf-8 -*-
"""Posteo 2026-10-04 · Sensor de movimiento con llave de anulación. Formato CONEXIÓN.
Sensor: L (fase), N (neutro, alimenta su electrónica) y CARGA (fase conmutada). La llave unipolar de anulación
puentea L con CARGA (en paralelo con el contacto del sensor): cerrada = luz fija; abierta = manda el sensor.
Neutro directo a la luminaria y PE a su masa. Retorno punteado en gris (color no reservado)."""
import sys
from placa import *

s = encabezado('SENSOR DE MOVIMIENTO', 'CON LLAVE DE ANULACIÓN')
s += tablero()

# Fase: al borne L del sensor y, derivada, a la llave de anulación.
s += cable([(440, 363), (440, 420), (350, 420), (350, 503)], CAST)
s += cable([(350, 420), (135, 420), (135, 503)], CAST)
s += f'<circle cx="350" cy="420" r="13" fill="{CAST}"/>'
# Neutro: directo a la luminaria y derivación al borne N del sensor.
s += cable([(700, 363), (700, 800), (740, 800), (740, 863)], CEL)
s += cable([(700, 470), (510, 470), (510, 503)], CEL)
s += f'<circle cx="700" cy="470" r="13" fill="{CEL_TXT}"/>'
# PE directo a la masa de la luminaria.
s += cable_pe([(920, 363), (920, 863)])
# Retorno a la luminaria: sale del borne CARGA del sensor y de la llave (gris punteado).
s += cable([(135, 806), (135, 850), (560, 850), (560, 863)], RET, punteado=True)
s += cable([(430, 806), (430, 850)], RET, punteado=True)
s += f'<circle cx="430" cy="850" r="13" fill="{RET}"/>'

# Llave unipolar de anulación (cerrada = luz fija)
s += caja(40, 520, 190, 270, 'LLAVE')
s += (f'<line x1="135" y1="592" x2="135" y2="630" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="135" cy="640" r="10" fill="{NAVY}"/>'
      f'<line x1="135" y1="640" x2="135" y2="744" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
      f'<circle cx="135" cy="744" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="135" y1="754" x2="135" y2="790" stroke="{NAVY}" stroke-width="5"/>')
s += borne(135, 520, CAST) + borne(135, 790, RET)

# Sensor de movimiento (PIR)
s += caja(280, 520, 320, 270, 'SENSOR')
s += (f'<path d="M370,720 a70,70 0 0 1 140,0 z" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
      f'<circle cx="440" cy="700" r="20" fill="{AMARILLO}"/>'
      f'<path d="M400,690 a50,50 0 0 1 80,0" fill="none" stroke="{AMARILLO}" stroke-width="6" stroke-linecap="round"/>'
      f'<line x1="440" y1="720" x2="440" y2="790" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="350" y1="592" x2="350" y2="630" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="510" y1="592" x2="510" y2="630" stroke="{NAVY}" stroke-width="5"/>')
s += borne(350, 520, CAST) + borne(510, 520, CEL) + borne(430, 790, RET)
s += (texto(325, 500, 'L', 36, CAST, 'end') + texto(535, 500, 'N', 36, CEL_TXT)
      + texto(452, 830, 'CARGA', 32, RET))

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

s += mensaje(['Cerrada: luz fija.', 'Abierta: sensor.'], y=1020)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-04-sensor-movimiento.png'
guardar(s, salida)
