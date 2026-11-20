# -*- coding: utf-8 -*-
"""Placa extra · Detector de arco (AFDD): cuándo es obligatorio en vivienda (fichas 05, 07 y 51)."""
import sys
from placa import *

s = encabezado('DETECTOR DE ARCO', '¿CUÁNDO ES OBLIGATORIO?')

# Qué hace
s += f'<rect x="60" y="230" width="960" height="190" rx="24" fill="#EEF7FD" stroke="#2A8FD0" stroke-width="5"/>'
s += f'<rect x="85" y="255" width="140" height="140" rx="18" fill="{NAVY}"/>'
s += f'<path d="M168,272 L128,334 L156,334 L140,380 L188,312 L160,312 L176,272 z" fill="{AMARILLO}"/>'
s += texto(255, 300, 'AFDD: detecta arcos', 42)
s += texto(255, 350, 'que la térmica y el diferencial', 36, NAVY, 'start', False)
s += texto(255, 395, 'no ven. Ayuda a prevenir incendios.', 36, NAVY, 'start', False)

# Ecuación: material + caño aislante = obligatorio
def bloque(x, titulo, l1, l2, color, fondo):
    r = f'<rect x="{x}" y="470" width="270" height="300" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    r += texto(x + 135, 545, titulo, 40, color, 'middle')
    r += texto(x + 135, 640, l1, 34, NAVY, 'middle', False)
    r += texto(x + 135, 684, l2, 34, NAVY, 'middle', False)
    return r

s += bloque(60, 'MADERA', 'Construcción', 'de madera', '#8A5A2B', '#FBF4EC')
s += texto(361, 640, 'o', 48, NAVY, 'middle')
s += bloque(392, 'EPS', 'Aislación de', 'telgopor', '#2A8FD0', '#EEF7FD')
s += texto(706, 642, '+', 64, NAVY, 'middle')
s += bloque(750, 'CAÑO', 'De material', 'aislante', NAVY, '#F2F4F7')

# Resultado
s += f'<path d="M540,790 L540,840" stroke="{NAVY}" stroke-width="10"/><path d="M516,830 L540,862 L564,830 z" fill="{NAVY}"/>'
s += f'<rect x="60" y="880" width="960" height="140" rx="24" fill="{VERDE_OK}"/>'
s += texto(540, 970, 'AFDD OBLIGATORIO', 60, '#FFF', 'middle')

s += f'<rect x="60" y="1060" width="960" height="140" rx="18" fill="#FFF6D6" stroke="{AMARILLO}" stroke-width="4"/>'
s += texto(540, 1118, 'En el resto de la vivienda:', 38, NAVY, 'middle', False)
s += texto(540, 1168, 'recomendado', 42, NAVY, 'middle')
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
