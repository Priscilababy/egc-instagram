# -*- coding: utf-8 -*-
"""CONEXIÓN: equipotencialización · masas ajenas (agua, gas, estructuras) a la barra equipotencial principal."""
import sys
from placa import *

COBRE = '#B87333'

s = encabezado('EQUIPOTENCIALIZACIÓN', 'TODO A LA MISMA BARRA', linea2_amarilla=True)

# Arriba: toma de tierra y tablero, ambos a la barra
s += caja(60, 250, 320, 190, 'JABALINA')
s += texto(220, 362, 'cable de PAT', 32, ancla='middle') + texto(220, 408, '4 mm² mínimo', 32, ancla='middle')
s += caja(700, 250, 320, 190, 'TABLERO')
s += texto(860, 362, 'conductor PE', 32, ancla='middle') + texto(860, 408, 'a las masas', 32, ancla='middle')
s += cable_pe([(220, 440), (220, 530)]) + cable_pe([(860, 440), (860, 530)])

# Barra equipotencial principal
s += f'<rect x="100" y="530" width="880" height="90" rx="14" fill="{COBRE}" stroke="{NAVY}" stroke-width="5"/>'
s += texto(540, 590, 'BARRA EQUIPOTENCIAL PRINCIPAL', 36, '#FFF', 'middle')

# Abajo: masas extrañas
for x in (210, 540, 870):
    s += cable_pe([(x, 620), (x, 700)])
for x, tit, cuerpo in ((60, 'CAÑO DE AGUA', 'metálico'), (390, 'CAÑO DE GAS', 'metálico'), (720, 'ESTRUCTURA', 'metálica')):
    s += caja(x, 700, 300, 150, tit)
    s += texto(x + 150, 822, cuerpo, 32, ancla='middle')

s += mensaje(['Lo metálico que no es', 'de la instalación también', 'va a la barra.'], y=910)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '../posts/2026-10-28-equipotencializacion.png'
guardar(s, salida)
