# -*- coding: utf-8 -*-
"""2026-10-17 · AIRE · CONEXIÓN: cable entre unidad interior y exterior (bucle de goteo, PE a las dos unidades)."""
import sys
from placa import *

NAR = '#E67E22'  # tercer conductor: naranja (color no reservado)

s = encabezado('CABLE ENTRE UNIDAD', 'INTERIOR Y EXTERIOR')

s += caja(60, 250, 340, 340, 'INTERIOR') + caja(760, 250, 260, 340, 'EXTERIOR')
filas = [(400, '1', RET, 530, 630, 630), (440, '2', RET2, 495, 665, 660), (480, '3', NAR, 460, 700, 690)]
for y, n, col, xi, xd, fondo in filas:
    s += texto(330, y + 12, n, 36, col, 'end')
    s += texto(830, y + 12, n, 36, col)
    s += borne(380, y, col) + borne(780, y, col)
    s += cable([(380, y), (xi, y), (xi, fondo), (xd, fondo), (xd, y), (780, y)], col, punteado=True)
y, xi, xd, fondo = 520, 425, 735, 720
s += texto(330, y + 12, 'PE', 36, VERDE, 'end') + texto(830, y + 12, 'PE', 36, VERDE)
s += borne(380, y, VERDE) + borne(780, y, VERDE)
s += cable_pe([(380, y), (xi, y), (xi, fondo), (xd, fondo), (xd, y), (780, y)])

s += texto(580, 790, 'BUCLE DE GOTEO', 38, ancla='middle')
s += texto(60, 870, '- Cable de 1,5 mm² como mínimo', 36)
s += texto(60, 920, '- Hilos que no se usan: aislados', 36)
s += texto(60, 970, '- El PE llega a las dos unidades', 36)
s += mensaje(['Bornes: confirmalos en', 'el manual del modelo.'], y=1020, tam=38)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'cable.png'
guardar(s, salida)
