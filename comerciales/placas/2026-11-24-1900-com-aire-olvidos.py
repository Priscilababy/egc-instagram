# -*- coding: utf-8 -*-
# Placa comercial: aire acondicionado, lo que se olvida cobrar. Genera comerciales/posts/2026-11-24-1900-com-aire-olvidos.jpg
from comercial import *

s = cabecera('AIRE ACONDICIONADO:', 'LO QUE SE OLVIDA COBRAR.')
s += paso(1, 360, 'Lista propia de aire', 'Por frigorías, parte eléctrica y service.')
s += paso(2, 505, 'Metro extra de cañería', 'La instalación incluye hasta 3 m.')
s += paso(3, 650, 'Gas adicional y altura', 'Cada uno es un ítem aparte.')
s += paso(4, 795, 'Ménsula, pasamuros, desagote', 'También, cada uno por separado.')
s += texto(540, 950, 'Lo que no figura en el presupuesto, no se cobra.', 36, GRIS_T, 'middle', negrita=False)
s += cta()
s += pie()
salida(s, __file__)
