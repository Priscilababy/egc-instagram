# -*- coding: utf-8 -*-
"""Posteo 2026-11-06 · Código de colores y retorno de una llave. Formato CONEXIÓN."""
import sys
from placa import *

s = encabezado('COLORES DE CABLES', 'Y EL RETORNO DE LA LLAVE')
s += tablero()

# Fase a la llave, neutro y PE directo a la bornera del portalámparas
s += cable([(440, 363), (440, 450), (260, 450), (260, 520)], CAST)
s += cable([(700, 363), (700, 800), (780, 800), (780, 863)], CEL)
s += cable_pe([(920, 363), (920, 863)])
# Retorno de la llave al portalámparas (punteado, color no reservado)
s += cable([(260, 790), (260, 850), (545, 850), (545, 863)], RET, punteado=True)

# Llave de un punto
s += caja(60, 520, 400, 270, 'LLAVE DE 1 PUNTO')
s += (f'<line x1="260" y1="592" x2="260" y2="630" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="260" y1="630" x2="260" y2="662" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="260" y1="662" x2="260" y2="734" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
      f'<circle cx="260" cy="662" r="10" fill="{NAVY}"/>'
      f'<circle cx="260" cy="744" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="260" y1="754" x2="260" y2="790" stroke="{NAVY}" stroke-width="5"/>')
s += borne(260, 520, CAST) + borne(260, 790, RET)

# Bornera del portalámparas
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(545, 880, RET) + borne(780, 880, CEL) + borne(920, 880, VERDE)
s += (texto(545, 950, 'RET', 32, RET, 'middle') + texto(780, 950, 'N', 32, CEL_TXT, 'middle')
      + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Referencias de color
def fila(y, color, nombre, detalle, pe=False, punteado=False):
    if pe:
        r = (f'<rect x="485" y="{y}" width="40" height="30" rx="6" fill="{AMAR_PE}"/>'
             f'<rect x="485" y="{y}" width="20" height="30" rx="6" fill="{VERDE}"/>')
    else:
        r = f'<rect x="485" y="{y}" width="40" height="30" rx="6" fill="{color}"/>'
    return r + texto(541, y + 28, nombre, 32, NAVY) + texto(722, y + 28, detalle, 32, GRIS, negrita=False)

s += fila(1030, CAST, 'FASE', 'castaño, negro, rojo')
s += fila(1080, CEL, 'NEUTRO', 'celeste')
s += fila(1130, None, 'PE', 'verde-amarillo', pe=True)
s += fila(1180, RET, 'RETORNO', 'no reservado')

s += mensaje(['Retorno: color', 'no reservado.'])
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-06-colores-cables.png'
guardar(s, salida)
