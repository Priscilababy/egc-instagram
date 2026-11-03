# -*- coding: utf-8 -*-
# Placa comercial: presupuesto por WhatsApp. Genera comerciales/posts/2026-11-05-1900-com-presupuesto-whatsapp.jpg
from comercial import *

s = cabecera('PRESUPUESTO EN MINUTOS.', 'LO MANDÁS POR WHATSAPP.')
s += paso(1, 360, 'Armás el presupuesto', 'En la app, desde el celular.')
s += paso(2, 505, 'Sale un PDF', 'Con tu logo y tu matrícula.')
s += paso(3, 650, 'Dice qué incluye el precio', 'Escrito en el mismo PDF.')
s += paso(4, 795, 'Lo mandás por WhatsApp', 'Y seguís con la obra.')
s += cta()
s += pie()
salida(s, __file__)
