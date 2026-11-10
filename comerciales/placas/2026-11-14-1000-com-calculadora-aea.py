# -*- coding: utf-8 -*-
# Placa comercial: calculadora AEA. Genera comerciales/posts/2026-11-14-1000-com-calculadora-aea.jpg
from comercial import *

s = cabecera('CALCULADORA AEA', 'EN EL CELULAR.')
s += paso(1, 360, 'Cargás el circuito', 'Potencia y largo del recorrido.')
s += paso(2, 505, 'Sección y termomagnética', 'La calculadora las verifica.')
s += paso(3, 650, 'Caída de tensión', 'Revisada antes del tablero.')
s += cta()
s += pie()
salida(s, __file__)
