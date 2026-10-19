# -*- coding: utf-8 -*-
"""Portada del blog: puesta a tierra en una vivienda (jabalina, 40 Ω, cable de 4 mm²)."""
import sys
from placa import *

s = encabezado('PUESTA A TIERRA', 'EN UNA VIVIENDA')

def caja_t(x, y, w, h, l1, l2=None):
    r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
    if l2:
        return r + texto(x + w/2, y + h/2 - 6, l1, 34, ancla='middle') + texto(x + w/2, y + h/2 + 36, l2, 34, ancla='middle')
    return r + texto(x + w/2, y + h/2 + 12, l1, 36, ancla='middle')

# tablero (arriba) con barra PE
s += caja_t(60, 260, 420, 130, 'TABLERO', 'BARRA PE')
# cámara de inspección
s += caja_t(60, 560, 420, 130, 'CÁMARA DE', 'INSPECCIÓN')
# cable de puesta a tierra: tablero -> cámara
s += cable_pe([(270, 390), (270, 560)])
s += texto(300, 485, 'Cable de PAT', 34) + texto(300, 527, '4 mm² mín.', 34)
# jabalina
s += cable_pe([(270, 690), (270, 740)])
s += f'<rect x="250" y="740" width="40" height="230" rx="8" fill="{GRIS}" stroke="{NAVY}" stroke-width="5"/>'
s += texto(320, 880, 'JABALINA', 34)
s += f'<line x1="60" y1="715" x2="480" y2="715" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 10"/>'
s += texto(500, 725, 'nivel del piso', 32)
# PE hacia las cajas
s += cable_pe([(480, 325), (700, 325)])
s += caja_t(700, 260, 320, 130, 'CAJAS Y', 'TOMAS')
s += texto(590, 300, 'PE', 34, VERDE, 'middle')
s += texto(860, 440, 'PE 2,5 mm² mín.', 34, ancla='middle')
s += mensaje(['Toma de tierra:', '40 Ω como máximo.'], x=560, y=790, tam=38)
s += texto(60, 1060, '- Medir con la toma desconectada', 34)
s += texto(60, 1105, '- PE a todas las cajas, sin guirnalda', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
