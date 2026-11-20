# -*- coding: utf-8 -*-
"""Placa extra · AEA 770 edición 2026: fechas clave y cambios principales (fichas 49, 50 y 51)."""
import sys
from placa import *

s = encabezado('AEA 770 · EDICIÓN 2026', 'DOS FECHAS CLAVE')

# Línea de tiempo
def fecha(x, color, fondo, d, t1, t2):
    r = f'<rect x="{x}" y="240" width="450" height="270" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    r += texto(x + 225, 330, d, 64, color, 'middle')
    r += texto(x + 225, 400, t1, 40, NAVY, 'middle')
    r += texto(x + 225, 450, t2, 40, NAVY, 'middle')
    return r

s += fecha(60, '#2A8FD0', '#EEF7FD', '1/11/2026', 'VIGENTE', 'la nueva edición')
s += fecha(570, VERDE_OK, '#F3FBF5', '1/3/2027', 'APLICACIÓN', 'OBLIGATORIA')
s += f'<path d="M515,375 L555,375" stroke="{NAVY}" stroke-width="8"/><path d="M548,360 L566,375 L548,390 z" fill="{NAVY}"/>'

# Cambios principales
s += texto(60, 590, 'LO QUE CAMBIA EN OBRA', 44, NAVY)
s += f'<rect x="60" y="606" width="540" height="6" fill="{AMARILLO}"/>'
filas = [
    ('Puesta a tierra (TT):', 'hasta 100 Ω (antes 40 Ω)'),
    ('Diferencial tipo AC:', 'no apto. Mínimo tipo A'),
    ('Obra nueva: un circuito', 'de uso general por caño'),
    ('Alturas de tomas y llaves:', 'tomas a 20 cm o más; llaves 0,90 a 1,30 m'),
]
for i, (a, b) in enumerate(filas):
    Y = 650 + 120 * i
    s += f'<circle cx="100" cy="{Y+40}" r="34" fill="{NAVY}"/>'
    s += texto(100, Y + 54, str(i + 1), 40, '#FFF', 'middle')
    s += texto(160, Y + 30, a, 40, NAVY)
    s += texto(160, Y + 78, b, 40, '#2A3A4D', 'start', False)

s += f'<rect x="60" y="1135" width="960" height="80" rx="18" fill="#FFF6D6" stroke="{AMARILLO}" stroke-width="4"/>'
s += texto(540, 1190, 'Obra nueva: proyectala ya con la 2026', 40, NAVY, 'middle')
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
