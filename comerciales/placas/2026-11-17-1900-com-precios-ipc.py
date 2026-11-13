# -*- coding: utf-8 -*-
# Placa comercial: precios por IPC. Genera comerciales/posts/2026-11-17-1900-com-precios-ipc.jpg
from comercial import *

s = cabecera('PRECIOS AL DÍA', 'CON EL IPC DEL INDEC.')
s += paso(1, 360, 'Elegís los meses', 'EGC toma el índice oficial del INDEC.')
s += paso(2, 505, 'Ves el porcentaje', 'Entre los meses que elegiste.')
s += paso(3, 650, 'Ajusta todos los precios', 'Juntos, en un toque.')
s += tilde(820, 'Si te equivocás, lo deshacés.')
s += tilde(910, 'Te avisa cuando un presupuesto vence.')
s += cta()
s += pie()
salida(s, __file__)
