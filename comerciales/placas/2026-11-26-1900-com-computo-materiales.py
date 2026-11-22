# -*- coding: utf-8 -*-
# Placa comercial: cómputo de materiales. Genera comerciales/posts/2026-11-26-1900-com-computo-materiales.jpg
from comercial import *

s = cabecera('CÓMPUTO DE MATERIALES', 'PARA EL CORRALÓN.')
s += paso(1, 380, 'Armás el cómputo', 'Los materiales del trabajo, en una lista.')
s += paso(2, 545, 'Vas al corralón', 'Con la lista en la mano, sin papelitos.')
s += paso(3, 710, 'Tildás lo comprado', 'Ves de un vistazo qué falta.')
s += tilde(890, 'Nada se queda en el mostrador.')
s += cta()
s += pie()
salida(s, __file__)
