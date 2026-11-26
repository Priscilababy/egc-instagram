# -*- coding: utf-8 -*-
"""Posteo 2026-11-27 · Medición de resistencia de aislación. Formato CONEXIÓN.
Fuentes: conocimiento/70 (AEA 90364-6 ed. 2025, 613.3 y Tabla 613.I: 500 V CC, >= 1 MΩ;
desconectar aparatos y DPS) y conocimiento/12 (AEA 90364-7-770 ed. 2017, 770.19.5.2:
sin alimentación, llaves y protecciones cerradas). Esquema simplificado de un circuito monofásico."""
import sys
from placa import *

s = encabezado('RESISTENCIA DE AISLACIÓN', 'CÓMO SE MIDE')

def panel(x, titulo, puente):
    w = 480
    p = f'<rect x="{x}" y="215" width="{w}" height="500" rx="18" fill="#F6F8FA" stroke="#DDE2E8" stroke-width="3"/>'
    p += texto(x + w / 2, 268, titulo, 36, NAVY, 'middle')
    xs = [x + 120, x + 240, x + 360]
    cols = [(CAST, 'L', CAST), (CEL, 'N', CEL_TXT), (None, 'PE', VERDE)]
    for cx, (col, et, ct) in zip(xs, cols):
        p += texto(cx, 330, et, 40, ct, 'middle')
        if col:
            p += cable([(cx, 350), (cx, 490)], col)
        else:
            p += cable_pe([(cx, 350), (cx, 490)])
        p += f'<circle cx="{cx}" cy="496" r="12" fill="#B87333" stroke="{NAVY}" stroke-width="3"/>'
    if puente:
        # puente entre L y N
        p += f'<line x1="{xs[0]}" y1="496" x2="{xs[1]}" y2="496" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
        p += texto((xs[0] + xs[1]) / 2, 540, 'puente', 32, NAVY, 'middle', negrita=False)
        puntas = [xs[1], xs[2]]
    else:
        puntas = [xs[0], xs[1]]
    # megóhmetro
    p += f'<rect x="{x+60}" y="580" width="{w-120}" height="115" rx="16" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    p += texto(x + w / 2, 628, 'MEGÓHMETRO', 34, NAVY, 'middle')
    p += texto(x + w / 2, 676, '500 V CC', 36, VERDE_OK, 'middle')
    for px in puntas:
        p += f'<line x1="{px}" y1="508" x2="{px}" y2="580" stroke="{NAVY}" stroke-width="6"/>'
        p += f'<circle cx="{px}" cy="508" r="7" fill="{NAVY}"/>'
    return p

s += panel(50, '1 · L contra N', False)
s += panel(550, '2 · L+N contra PE', True)

s += texto(60, 785, 'Antes de medir:', 38)
for i, l in enumerate(['- Sin tensión y sin aparatos conectados.',
                       '- Llaves y termomagnéticas cerradas.',
                       '- DPS desconectados.']):
    s += texto(60, 840 + 52 * i, l, 36, NAVY, negrita=False)

s += mensaje(['Circuito de 220 V:', 'mínimo 1 MΩ.'], y=1000, tam=40)
s += firma('AEA 90364-6 · Tabla 613.I')

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-27-resistencia-aislacion.png'
guardar(s, salida)
