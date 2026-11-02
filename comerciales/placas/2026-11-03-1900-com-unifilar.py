# -*- coding: utf-8 -*-
# Placa comercial: tablero y unifilar. Genera comerciales/posts/2026-11-03-1900-com-unifilar.jpg
from comercial import *

s = cabecera('CARGÁS LOS CIRCUITOS.', 'EGC DIBUJA EL UNIFILAR.', etiqueta='NUEVO EN EGC')
s += paso(1, 360, 'Cargás cada circuito', 'Potencia y largo del recorrido.')
s += paso(2, 505, 'EGC verifica cada uno', 'Sección, térmica y caída de tensión (AEA).')
s += paso(3, 650, 'Arma el tablero', 'Diferenciales de 30 mA y línea principal.')
s += paso(4, 795, 'Sale el PDF de 2 hojas', 'Unifilar + cuadro de cargas y materiales.')
s += texto(540, 950, 'Simbología IRAM 2010 e IEC 60617.', 36, GRIS_T, 'middle', negrita=False)
s += cta()
s += pie()
salida(s, __file__)
