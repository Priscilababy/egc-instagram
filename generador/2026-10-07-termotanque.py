# -*- coding: utf-8 -*-
"""Placa 2026-10-07 · Circuito dedicado para termotanque eléctrico (CONEXIÓN)."""
import sys
from placa import *

s = encabezado('CIRCUITO PARA', 'TERMOTANQUE ELÉCTRICO')
s += tablero(it_txt='IT 2P')

# Termotanque: bornera arriba y cuerpo del equipo abajo
s += f'<rect x="540" y="600" width="460" height="90" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += f'<rect x="540" y="720" width="460" height="470" rx="60" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'

# Cables: fase castaño, neutro celeste, PE verde-amarillo, todos al termotanque
s += cable([(440, 363), (440, 560), (620, 560), (620, 600)], CAST)
s += cable([(700, 363), (700, 530), (780, 530), (780, 600)], CEL)
s += cable_pe([(920, 363), (920, 600)])
s += borne(620, 600, CAST) + borne(780, 600, CEL) + borne(920, 600, VERDE)
s += (texto(620, 666, 'L', 36, CAST, 'middle') + texto(780, 666, 'N', 36, CEL_TXT, 'middle')
      + texto(920, 666, 'PE', 36, VERDE, 'middle'))

# Interior: resistencia y termostato
s += texto(770, 790, 'TERMOTANQUE', 40, NAVY, 'middle')
zig = 'M600,900 h40 l20,-40 l40,80 l40,-80 l40,80 l40,-80 l40,80 l20,-40 h40'
s += f'<path d="{zig}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>'
s += texto(770, 1000, 'RESISTENCIA', 32, NAVY, 'middle')
s += texto(770, 1120, 'TERMOSTATO', 32, NAVY, 'middle')

# Datos del circuito (izquierda)
s += texto(60, 450, 'Línea exclusiva', 36) + texto(60, 495, 'Cable 2,5 mm² mín.', 36)
s += texto(60, 560, 'Diferencial 30 mA', 36) + texto(60, 605, 'y térmica bipolar', 36)

s += mensaje(['Se elige por la', 'corriente de la placa,', 'no por los litros.'], y=890)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-07-termotanque.png'
guardar(s, salida)
