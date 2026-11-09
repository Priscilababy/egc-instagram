# -*- coding: utf-8 -*-
"""Posteo 2026-11-10 · Caída de tensión: el largo obliga a subir la sección. Formato CONEXIÓN."""
import sys
from placa import *

s = encabezado('CAÍDA DE TENSIÓN', 'CUANDO EL CABLE ES LARGO')
s += tablero(it_txt='IT 16 A')

# Cables del tablero a la carga (largo), con marca de distancia
s += cable([(440, 363), (440, 560)], CAST)
s += cable([(700, 363), (700, 560)], CEL)
s += cable_pe([(920, 363), (920, 560)])
s += texto(70, 450, 'DISTANCIA', 36, NAVY) + texto(70, 520, '60 m', 56, NAVY)
s += f'<line x1="330" y1="400" x2="330" y2="540" stroke="{NAVY}" stroke-width="5"/>'
s += f'<line x1="315" y1="400" x2="345" y2="400" stroke="{NAVY}" stroke-width="5"/><line x1="315" y1="540" x2="345" y2="540" stroke="{NAVY}" stroke-width="5"/>'

# Carga
s += caja(300, 560, 720, 80, 'CARGA: 10 A · 220 V', 40)
s += borne(440, 560, CAST) + borne(700, 560, CEL) + borne(920, 560, VERDE)

# Comparación
s += f'<rect x="60" y="670" width="960" height="150" rx="18" fill="#FDECEC" stroke="{ROJO}" stroke-width="4"/>'
s += chip(80, 690, 'NO', ROJO)
s += texto(210, 733, 'Cable de 2,5 mm²', 44)
s += texto(80, 790, '9 V de caída = 4,1 %. Pasa el 3 %.', 40, ROJO)
s += f'<rect x="60" y="840" width="960" height="150" rx="18" fill="#E8F6EC" stroke="{VERDE_OK}" stroke-width="4"/>'
s += chip(80, 860, 'SÍ', VERDE_OK)
s += texto(210, 903, 'Cable de 4 mm²', 44)
s += texto(80, 960, '6 V de caída = 2,7 %. Cumple.', 40, VERDE_OK)

s += mensaje(['El largo también', 'decide la sección.'], x=330, y=1020)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-10-caida-de-tension.png'
guardar(s, salida)
