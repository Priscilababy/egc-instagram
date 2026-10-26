# -*- coding: utf-8 -*-
"""Posteo 2026-10-27 · Tensión de paso y tensión de contacto: objetivo 24 V. Formato CONEXIÓN (esquema).
Fuente: conocimiento/23 (PAT2: paso = entre los dos pies, ~0,8 a 1 m; contacto = mano a pies o mano a mano)
y 05 (770.14.3.2: en TT, diferencial; objetivo 24 V; diferencial <= 30 mA y Ra <= 40 Ω)."""
import sys
from placa import *

s = encabezado('TENSIÓN DE PASO', 'Y DE CONTACTO')

def persona(cx, base, brazo_der=None):
    """Figura simple: cabeza, cuerpo, piernas abiertas (pies en cx±70) y brazo opcional hacia (x, y)."""
    p = f'<circle cx="{cx}" cy="{base-250}" r="30" fill="{NAVY}"/>'
    p += f'<line x1="{cx}" y1="{base-218}" x2="{cx}" y2="{base-110}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>'
    p += f'<line x1="{cx}" y1="{base-110}" x2="{cx-70}" y2="{base}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>'
    p += f'<line x1="{cx}" y1="{base-110}" x2="{cx+70}" y2="{base}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>'
    if brazo_der:
        p += f'<line x1="{cx}" y1="{base-190}" x2="{brazo_der[0]}" y2="{brazo_der[1]}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>'
    else:
        p += f'<line x1="{cx}" y1="{base-190}" x2="{cx-50}" y2="{base-110}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>'
        p += f'<line x1="{cx}" y1="{base-190}" x2="{cx+50}" y2="{base-110}" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/>'
    return p

SUELO = 640
# --- Panel izquierdo: PASO ---
s += texto(285, 270, 'PASO', 48, NAVY, 'middle')
s += f'<rect x="60" y="{SUELO}" width="450" height="14" fill="{GRIS}"/>'
s += persona(285, SUELO)
s += f'<line x1="215" y1="{SUELO+50}" x2="355" y2="{SUELO+50}" stroke="{ROJO}" stroke-width="6"/>'
s += f'<line x1="215" y1="{SUELO+36}" x2="215" y2="{SUELO+64}" stroke="{ROJO}" stroke-width="6"/>'
s += f'<line x1="355" y1="{SUELO+36}" x2="355" y2="{SUELO+64}" stroke="{ROJO}" stroke-width="6"/>'
s += texto(285, SUELO+115, 'entre los dos pies', 36, NAVY, 'middle')
s += texto(285, SUELO+160, '(unos 0,8 a 1 m)', 36, NAVY, 'middle', negrita=False)

# --- Panel derecho: CONTACTO ---
s += texto(795, 270, 'CONTACTO', 48, NAVY, 'middle')
s += f'<rect x="570" y="{SUELO}" width="450" height="14" fill="{GRIS}"/>'
# artefacto con carcasa metálica (masa)
s += f'<rect x="850" y="{SUELO-250}" width="130" height="250" rx="12" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += texto(915, SUELO-120, 'MASA', 34, NAVY, 'middle')
s += persona(700, SUELO, brazo_der=(850, SUELO-190))
s += texto(795, SUELO+115, 'mano a pies', 36, NAVY, 'middle')
s += texto(795, SUELO+160, 'o de mano a mano', 36, NAVY, 'middle', negrita=False)

s += mensaje(['En TT el objetivo es que la tensión', 'de contacto no pase de 24 V.', 'Con diferencial 30 mA y toma ≤ 40 Ω.'], y=870)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-27-tension-paso-contacto.png'
guardar(s, salida)
