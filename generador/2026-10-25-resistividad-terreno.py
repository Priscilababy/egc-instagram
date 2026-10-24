# -*- coding: utf-8 -*-
"""Posteo 2026-10-25 · Resistividad del terreno: la misma jabalina da distinto según el suelo. Formato CONEXIÓN (gráfico).
Fuente: conocimiento/23 (tabla de resistividades PAT1; jabalina 3 m x 5/8" = 19,4 Ω con 50 Ω·m, PAT7;
la resistencia es proporcional a la resistividad: valores derivados, orientativos) y 06 (40 Ω, 770.3.2)."""
import sys
from placa import *

s = encabezado('LA MISMA JABALINA,', 'DISTINTO TERRENO')

X0, ESC = 340, 6          # origen de las barras y px por ohm
K = 19.4 / 50             # Ω por cada Ω·m (jabalina 3 m, 5/8")
suelos = [('Pantanoso', 30), ('Arcilloso', 100), ('Arena húmeda', 200), ('Arena seca', 1000)]
y0, PASO = 350, 120

s += texto(70, 250, 'Jabalina de 3 m, 5/8&quot;: resistencia calculada', 32, NAVY, negrita=False)
for i, (nom, rho) in enumerate(suelos):
    y = y0 + i * PASO
    r = rho * K
    s += texto(70, y + 30, nom, 36)
    s += texto(70, y + 72, f'{rho} Ω·m', 32, NAVY, negrita=False)
    ancho = int(r * ESC)
    if ancho > 600:
        ancho = 640
        s += f'<rect x="{X0}" y="{y}" width="{ancho}" height="80" rx="8" fill="{AMARILLO}" stroke="{NAVY}" stroke-width="4"/>'
        s += f'<rect x="{X0+ancho-70}" y="{y-4}" width="26" height="88" fill="#FFFFFF" transform="skewX(-20)" transform-origin="{X0+ancho-70} {y}"/>'
        s += texto(X0 + 20, y + 54, f'≈ {int(round(r, -1))} Ω', 38)
    else:
        s += f'<rect x="{X0}" y="{y}" width="{ancho}" height="80" rx="8" fill="{AMARILLO}" stroke="{NAVY}" stroke-width="4"/>'
        s += texto(X0 + ancho + 16 if r < 30 else X0 + 40 * ESC + 24, y + 54, f'≈ {int(round(r))} Ω', 38)

xl = X0 + 40 * ESC
s += f'<line x1="{xl}" y1="318" x2="{xl}" y2="{y0 + 4*PASO - 40}" stroke="{ROJO}" stroke-width="5" stroke-dasharray="14 10"/>'
s += texto(xl + 12, 312, 'máx. 40 Ω', 34, ROJO)
s += f'<line x1="{X0}" y1="320" x2="{X0}" y2="{y0 + 4*PASO - 40}" stroke="{NAVY}" stroke-width="5"/>'

s += mensaje(['El terreno decide cuánto da la jabalina.', 'Los ohms reales se miden con telurímetro.'], y=900)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-25-resistividad-terreno.png'
guardar(s, salida)
