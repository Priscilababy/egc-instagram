# -*- coding: utf-8 -*-
"""Prueba de estanqueidad con nitrógeno antes del vacío (ficha 17, BP p. 64-68)."""
import sys
from placa import *

COBRE = '#B87333'
s = encabezado('PRUEBA CON NITRÓGENO', 'ANTES DEL VACÍO')

# Cilindro + regulador
s += f'<rect x="70" y="330" width="140" height="300" rx="45" fill="#C9CFD7" stroke="{NAVY}" stroke-width="5"/>'
s += texto(140, 500, 'N2', 60, NAVY, 'middle')
s += f'<rect x="95" y="268" width="90" height="62" rx="10" fill="{NAVY}"/>'

# Manguera, manómetro, unidad exterior
s += cable([(185, 300), (345, 300)], NAVY)
s += cable([(455, 300), (560, 300), (560, 420), (640, 420)], NAVY)
s += f'<circle cx="400" cy="300" r="55" fill="#FFF" stroke="{NAVY}" stroke-width="6"/>'
s += f'<line x1="400" y1="300" x2="428" y2="262" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
s += f'<circle cx="400" cy="300" r="8" fill="{NAVY}"/>'
s += texto(400, 392, 'MANÓMETRO', 34, NAVY, 'middle')
s += caja(640, 240, 370, 330, 'UNIDAD EXTERIOR')
s += f'<rect x="622" y="400" width="40" height="40" rx="6" fill="{AMARILLO}" stroke="{NAVY}" stroke-width="4"/>'
s += texto(680, 428, 'Válvula', 32)

# Caños de cobre y unidad interior
s += cable([(760, 570), (760, 640)], COBRE) + cable([(890, 570), (890, 640)], COBRE)
s += caja(640, 640, 370, 170, 'UNIDAD INTERIOR')

# Reglas
for i, t in enumerate(['Solo nitrógeno seco', 'Siempre con regulador', 'Nunca oxígeno ni aire', 'Presión: la del manual']):
    s += texto(60, 715 + 54 * i, t, 36)

# Fugas
s += caja(640, 860, 370, 300, 'FUGAS')
for i, t in enumerate(['Agua jabonosa', 'en cada unión:', 'burbujas =', 'hay fuga.']):
    s += texto(670, 982 + 50 * i, t, 36)

s += mensaje(['Presurizá y esperá', '10 min como mínimo:', 'la aguja no baja.'], y=930)
s += firma('Manual del fabricante')

salida = sys.argv[1] if len(sys.argv) > 1 else 'prueba.png'
guardar(s, salida)
