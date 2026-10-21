# -*- coding: utf-8 -*-
"""Portada del blog: colores de los cables según la AEA."""
import sys
from placa import *

s = encabezado('COLORES DE CABLES', 'SEGÚN LA AEA')

def fila(y, color, nombre, detalle):
    r = f'<rect x="60" y="{y}" width="200" height="40" rx="10" fill="{color}" stroke="{NAVY}" stroke-width="4"/>'
    return r + texto(290, y + 34, nombre, 36) + texto(640, y + 34, detalle, 34, GRIS)

s += fila(250, '#8B5A2B', 'FASE', 'castaño, negro o rojo')
s += fila(330, '#7EC8E3', 'NEUTRO', 'celeste')
s += (f'<rect x="60" y="410" width="100" height="40" rx="10" fill="#2E9E4F" stroke="{NAVY}" stroke-width="4"/>'
      f'<rect x="160" y="410" width="100" height="40" rx="10" fill="#F2C200" stroke="{NAVY}" stroke-width="4"/>'
      + texto(290, 444, 'PE', 36) + texto(640, 444, 'verde-amarillo', 34, GRIS))
s += (f'<rect x="60" y="490" width="200" height="40" rx="10" fill="#FFF" stroke="{GRIS}" stroke-width="4" stroke-dasharray="10 8"/>'
      + texto(290, 524, 'RETORNO', 36) + texto(640, 524, 'color no reservado', 34, GRIS))
s += texto(60, 620, 'Sin castaño, negro ni rojo,', 36) + texto(60, 666, 'ni celeste, ni verde-amarillo', 36)
s += mensaje(['Retorno: blanco, gris o violeta.', 'Nunca de fase, neutro ni PE.'], y=760, tam=40)
s += texto(60, 1060, '- Identificar los cables en cajas compartidas', 34)
s += texto(60, 1105, '- Confirmar el código con la AEA 90364-7-770', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
