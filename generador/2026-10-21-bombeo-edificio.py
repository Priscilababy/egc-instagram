# -*- coding: utf-8 -*-
"""2026-10-21 · CONEXIÓN: bombeo en edificio, dos bombas alternadas, flotantes en MBTS y válvula de retención."""
import sys
from placa import *

s = encabezado('BOMBEO EN EDIFICIO', 'DOS BOMBAS Y FLOTANTES')
AGUA = '#CFE8F7'
CANO = '#4A5A6E'

def cano(pts):
    p = ' '.join(f'{x},{y}' for x, y in pts)
    return f'<polyline points="{p}" fill="none" stroke="{CANO}" stroke-width="16" stroke-linejoin="round"/>'

def flotante(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="18" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
            f'<line x1="{x}" y1="{y-18}" x2="{x}" y2="{y-34}" stroke="{NAVY}" stroke-width="5"/>')

# Tanque elevado
s += f'<rect x="600" y="240" width="400" height="160" rx="12" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<rect x="603" y="320" width="394" height="77" fill="{AGUA}"/>'
s += texto(800, 292, 'TANQUE ELEVADO', 34, ancla='middle')
s += flotante(680, 362) + texto(715, 372, 'flotante', 32)

# Cisterna
s += f'<rect x="60" y="780" width="320" height="200" rx="12" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<rect x="63" y="840" width="314" height="137" fill="{AGUA}"/>'
s += texto(240, 822, 'CISTERNA', 34, ancla='middle')
s += flotante(100, 910) + texto(135, 920, 'flotante', 32)

# Cañerías: succión (abajo), descarga (arriba) y subida con retención
s += cano([(380, 870), (720, 870)])
s += cano([(500, 870), (500, 775)]) + cano([(720, 870), (720, 775)])
s += cano([(500, 665), (500, 600), (900, 600), (900, 400)])
s += cano([(720, 665), (720, 600)])
s += (f'<polygon points="900,478 870,520 930,520" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="868" y1="478" x2="932" y2="478" stroke="{NAVY}" stroke-width="6"/>')
s += texto(850, 508, 'RETENCIÓN', 32, ancla='end')

# Bombas
s += f'<rect x="430" y="650" width="370" height="140" rx="16" fill="#F6F8FA" stroke="{GRIS}" stroke-width="4" stroke-dasharray="14 10"/>'
for x, n in ((500, 'B1'), (720, 'B2')):
    s += f'<circle cx="{x}" cy="720" r="55" fill="#FFF" stroke="{NAVY}" stroke-width="6"/>' + texto(x, 734, n, 40, ancla='middle')

# Tablero de bombas
s += caja(60, 250, 400, 270, 'TABLERO DE BOMBAS', 32)
s += texto(260, 380, 'MANUAL / AUTO', 38, ancla='middle') + texto(260, 450, 'ALTERNANCIA', 38, ancla='middle')

# Comando de flotantes en MBTS (punteado, color no reservado)
s += cable([(460, 362), (680, 362)], RET, punteado=True)
s += cable([(100, 520), (100, 892)], RET, punteado=True)
s += texto(480, 345, 'MBTS', 34, RET)
s += texto(118, 640, 'MBTS', 34, RET)
# Fuerza a las bombas
s += cable([(400, 520), (400, 720), (430, 720)], NAVY)
s += texto(415, 580, 'FUERZA', 32)

s += texto(430, 935, '- Una bomba de reserva', 34)
s += texto(430, 980, '- Se alternan: desgaste parejo', 34)
s += texto(430, 1025, '- Nunca en seco: flotante de cisterna', 34)
s += mensaje(['Flotantes: comando en MBTS,', 'nunca a 220 V.'], y=1040)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'bombeo.png')
