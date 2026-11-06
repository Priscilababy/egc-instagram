# -*- coding: utf-8 -*-
# Placa comercial: EGC actualizada a la AEA 90364-7-770 edición 2026.
from comercial import *

s = cabecera('EGC YA CALCULA CON', 'LA NUEVA AEA 770.', etiqueta='EDICIÓN 2026')
s += paso(1, 360, 'Simultaneidad nueva', 'Con 10 o más circuitos, factor 0,5.')
s += paso(2, 505, 'Circuito IUE al día', 'Hasta 15 bocas y 32 A.')
s += paso(3, 650, 'Un circuito por caño', 'Obra nueva: uno por caño. Reformas: 40 A.')
s += paso(4, 795, 'Puesta a tierra 100 Ω', 'En el simulador gratuito de EGC.')
s += texto(540, 950, 'AEA 90364-7-770, edición 2026.', 36, GRIS_T, 'middle', negrita=False)
s += cta()
s += pie()
salida(s, __file__)
