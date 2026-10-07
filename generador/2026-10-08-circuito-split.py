# -*- coding: utf-8 -*-
"""Placa 2026-10-08 · Circuito especial para aire acondicionado split (CONEXIÓN)."""
import sys
from placa import *

s = encabezado('CIRCUITO PARA', 'AIRE ACONDICIONADO SPLIT')
s += tablero(it_txt='IT 2P')

# Bornera de alimentación del equipo y cuerpo del split
s += f'<rect x="540" y="600" width="460" height="90" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += f'<rect x="540" y="720" width="460" height="470" rx="40" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'

# Cables: fase castaño, neutro celeste, PE verde-amarillo
s += cable([(440, 363), (440, 560), (620, 560), (620, 600)], CAST)
s += cable([(700, 363), (700, 530), (780, 530), (780, 600)], CEL)
s += cable_pe([(920, 363), (920, 600)])
s += borne(620, 600, CAST) + borne(780, 600, CEL) + borne(920, 600, VERDE)
s += (texto(620, 666, 'L', 36, CAST, 'middle') + texto(780, 666, 'N', 36, CEL_TXT, 'middle')
      + texto(920, 666, 'PE', 36, VERDE, 'middle'))

# Unidad interior (arriba): cuerpo y rejilla de salida de aire
s += texto(770, 770, 'SPLIT', 40, NAVY, 'middle')
s += f'<rect x="580" y="795" width="380" height="90" rx="22" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += f'<line x1="610" y1="860" x2="930" y2="860" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
s += texto(770, 940, 'INTERIOR', 32, NAVY, 'middle')

# Unidad exterior (abajo): ventilador
s += f'<line x1="770" y1="955" x2="770" y2="985" stroke="{NAVY}" stroke-width="6"/>'
s += f'<rect x="600" y="985" width="340" height="125" rx="18" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += f'<circle cx="770" cy="1047" r="45" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
for ang in (0, 120, 240):
    s += (f'<ellipse cx="770" cy="1026" rx="12" ry="21" fill="{NAVY}" transform="rotate({ang} 770 1047)"/>')
s += texto(770, 1160, 'EXTERIOR', 32, NAVY, 'middle')

# Datos del circuito (izquierda)
s += texto(60, 450, 'Un solo equipo,', 36) + texto(60, 495, 'sin derivaciones', 36)
s += texto(60, 560, 'Diferencial 30 mA', 36) + texto(60, 605, 'y térmica bipolar', 36)
s += texto(60, 670, 'Cable 2,5 mm² mín.', 36)

s += mensaje(['Se elige por la', 'corriente, no por', 'las frigorías.'], y=890, ancho=450)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-08-circuito-split.png'
guardar(s, salida)
