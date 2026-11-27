# -*- coding: utf-8 -*-
# Placa comercial: cobros y saldos. Genera comerciales/posts/2026-12-01-1900-com-cobros-saldos.jpg
from comercial import *

s = cabecera('COBROS Y SALDOS,', 'A LA VISTA.')
s += paso(1, 380, 'Anotás el anticipo', 'Lo que te dieron para arrancar.')
s += paso(2, 545, 'Sumás los pagos parciales', 'A medida que avanza la obra.')
s += paso(3, 710, 'Ves lo que falta cobrar', 'El saldo de cada trabajo.')
s += tilde(890, 'Ningún saldo queda en el olvido.')
s += cta()
s += pie()
salida(s, __file__)
