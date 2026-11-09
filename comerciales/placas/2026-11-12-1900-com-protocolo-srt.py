# -*- coding: utf-8 -*-
# Placa comercial: protocolo SRT 900/15. Genera comerciales/posts/2026-11-12-1900-com-protocolo-srt.jpg
from comercial import *

s = cabecera('PROTOCOLO SRT 900/15', 'DESDE EL CELULAR.')
s += paso(1, 360, 'Una tarjeta por toma', 'Cargás cada medición en la obra.')
s += paso(2, 505, 'Sale el PDF de 3 hojas', 'Con el formato del Anexo.')
s += paso(3, 650, 'La firma es tuya', 'Del profesional interviniente.')
s += cta()
s += pie()
salida(s, __file__)
