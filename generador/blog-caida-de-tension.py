# -*- coding: utf-8 -*-
"""Portada del blog · Caída de tensión: límite 3 % y cálculo con la tabla V/(A·km)."""
import sys
from placa import *

s = encabezado('CAÍDA DE TENSIÓN', 'LÍMITE: 3 %')
# esquema: tablero -> cable -> punto de uso
s += (f'<rect x="60" y="250" width="260" height="170" rx="16" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      + texto(190, 320, 'TABLERO', 44, ancla='middle') + texto(190, 380, '220 V', 44, CEL_TXT, 'middle')
      + f'<rect x="760" y="250" width="260" height="170" rx="16" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      + texto(890, 320, 'TOMA', 44, ancla='middle') + texto(890, 380, 'máx. 3 %', 40, ROJO, 'middle'))
s += cable([(320, 300), (760, 300)], CAST) + cable([(320, 340), (760, 340)], CEL) + cable_pe([(320, 380), (760, 380)])
s += (f'<line x1="330" y1="470" x2="750" y2="470" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="330" y1="450" x2="330" y2="490" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="750" y1="450" x2="750" y2="490" stroke="{NAVY}" stroke-width="5"/>'
      + texto(540, 535, 'L = distancia', 44, ancla='middle'))
# fórmula
s += (f'<rect x="60" y="580" width="960" height="130" rx="18" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
      + texto(540, 665, 'ΔU = tabla × I × L (km)', 54, ancla='middle'))
# tabla V/(A·km)
s += texto(60, 775, 'Tabla V/(A·km), monofásico:', 40)
filas = [('1,5 mm²', '26'), ('2,5 mm²', '15'), ('4 mm²', '10'), ('6 mm²', '6,5')]
for i, (a, b) in enumerate(filas):
    x = 60 + i * 245
    s += (f'<rect x="{x}" y="805" width="225" height="130" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="4"/>'
          + texto(x + 112, 855, a, 36, ancla='middle') + texto(x + 112, 910, b, 48, CEL_TXT, 'middle'))
s += mensaje(['Si pasa del 3 %, se sube', 'la sección del cable'], y=990, tam=42)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
