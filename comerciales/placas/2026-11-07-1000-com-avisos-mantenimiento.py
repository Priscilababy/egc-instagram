# -*- coding: utf-8 -*-
# Placa comercial: avisos de mantenimiento. Genera comerciales/posts/2026-11-07-1000-com-avisos-mantenimiento.jpg
from comercial import *

s = cabecera('TU PRÓXIMO TRABAJO', 'YA LO HICISTE.')
s += paso(1, 360, 'Aire antes del verano', 'Aviso para el mantenimiento.')
s += paso(2, 505, 'Revisión eléctrica anual', 'Aviso para volver a la obra.')
s += paso(3, 650, 'Nada se envía solo', 'Vos controlás cada aviso.')
s += cta()
s += pie()
salida(s, __file__)
