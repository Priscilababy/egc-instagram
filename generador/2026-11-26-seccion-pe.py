# -*- coding: utf-8 -*-
"""Posteo 2026-11-26 · Sección del conductor PE según la sección de fase. Formato CONEXIÓN.
Fuentes: conocimiento/06 (AEA 90364-7-770 ed. 2017, Tabla 770.14.I, 770.14.4.4 y 770.14.4.5)
y conocimiento/50 (edición 2026: secciones mínimas sin cambios, PE 2,5 mm²).
Cortes de cable esquemáticos, tamaños no a escala real."""
import math
import sys
from placa import *

s = encabezado('SECCIÓN DEL PE', 'SEGÚN LA FASE')

# Tabla 770.14.I
xt, yt, wt = 60, 235, 960
filas = [('Fase hasta 16 mm²', 'igual a la fase'),
         ('Fase de más de 16 a 35 mm²', '16 mm²'),
         ('Fase de más de 35 mm²', 'la mitad')]
alto_cab, alto_fila = 76, 84
s += f'<rect x="{xt}" y="{yt}" width="{wt}" height="{alto_cab + alto_fila * 3}" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="3"/>'
s += f'<path d="M{xt},{yt+alto_cab} v-{alto_cab-14} a14,14 0 0 1 14,-14 h{wt-28} a14,14 0 0 1 14,14 v{alto_cab-14} z" fill="{NAVY}"/>'
s += texto(xt + 24, yt + 52, 'SECCIÓN DE FASE', 36, '#FFF')
s += texto(xt + wt - 24, yt + 52, 'SECCIÓN DEL PE', 36, AMARILLO, 'end')
for i, (a, b) in enumerate(filas):
    y = yt + alto_cab + alto_fila * i
    if i:
        s += f'<line x1="{xt}" y1="{y}" x2="{xt+wt}" y2="{y}" stroke="#DDE2E8" stroke-width="3"/>'
    s += texto(xt + 24, y + 56, a, 38, CAST)
    s += texto(xt + wt - 24, y + 56, b, 38, VERDE_OK, 'end')

# Ejemplos: corte de cable fase (castaño) y PE (verde-amarillo)
ye = 640
s += texto(60, ye, 'Ejemplos (mm²):', 38)
ejemplos = [(1.5, 2.5, '1,5', '2,5'), (4, 4, '4', '4'), (25, 16, '25', '16'), (50, 25, '50', '25')]
COBRE = '#D98E4A'
yc = 790
for i, (sf, spe, tf, tpe) in enumerate(ejemplos):
    cx = 180 + 240 * i
    rf = 7 * math.sqrt(sf) + 10
    rp = 7 * math.sqrt(spe) + 10
    xf, xp = cx - 4 - rf, cx + 4 + rp
    s += f'<circle cx="{xf:.0f}" cy="{yc}" r="{rf:.0f}" fill="{CAST}"/>'
    s += f'<circle cx="{xf:.0f}" cy="{yc}" r="{rf*0.62:.0f}" fill="{COBRE}" stroke="#A8662E" stroke-width="2"/>'
    s += f'<circle cx="{xp:.0f}" cy="{yc}" r="{rp:.0f}" fill="{VERDE}" stroke="{AMAR_PE}" stroke-width="9"/>'
    s += f'<circle cx="{xp:.0f}" cy="{yc}" r="{rp*0.55:.0f}" fill="{COBRE}" stroke="#A8662E" stroke-width="2"/>'
    s += texto(cx, 900, f'fase {tf}', 34, CAST, 'middle')
    s += texto(cx, 944, f'PE {tpe}', 34, VERDE_OK, 'middle')
    if i < 3:
        s += f'<line x1="{cx+120}" y1="700" x2="{cx+120}" y2="960" stroke="#DDE2E8" stroke-width="3"/>'
s += texto(180, 986, '(por mínimo)', 32, GRIS, 'middle', negrita=False)

s += mensaje(['PE nunca menos de 2,5 mm².', 'Cable de PAT: mínimo 4 mm².'], y=1025, tam=40)
s += firma('AEA 90364 · Tabla 770.14.I')

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-26-seccion-pe.png'
guardar(s, salida)
