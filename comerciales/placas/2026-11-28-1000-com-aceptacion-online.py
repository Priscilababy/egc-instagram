# -*- coding: utf-8 -*-
# Placa comercial: aceptación online. Genera comerciales/posts/2026-11-28-1000-com-aceptacion-online.jpg
from comercial import *

s = cabecera('EL CLIENTE ACEPTA', 'DESDE UN LINK.')
s += paso(1, 380, 'Mandás el presupuesto', 'Con el link para aceptarlo.')
s += paso(2, 545, 'El cliente lo acepta', 'Desde ese mismo link.')
s += paso(3, 710, 'Pasa solo a Aceptado', 'No lo cambiás a mano.')
s += tilde(890, 'Sabés qué trabajos están confirmados.')
s += cta()
s += pie()
salida(s, __file__)
