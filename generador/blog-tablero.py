# -*- coding: utf-8 -*-
"""Portada del blog: tablero eléctrico de vivienda, ubicación, IP y reserva."""
import sys
from placa import *

s = encabezado('TABLERO DE VIVIENDA', 'DÓNDE Y CÓMO ARMARLO')


def fila(y, titulo, linea2):
    r = f'<rect x="60" y="{y}" width="960" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    return r + texto(90, y + 44, titulo, 38) + texto(90, y + 84, linea2, 34, GRIS)


s += texto(60, 275, 'Lo que pide la AEA 90364-7-770:', 40)
s += fila(310, 'Lugar seco y de fácil acceso', 'nunca en baños ni dentro de muebles')
s += fila(430, 'Principal a 2 m del medidor, como máx.', 'gabinete Clase II · intemperie IP54')
s += fila(550, 'Grado de protección IP41 o IP31D', 'palancas entre 0,40 m y 2 m del piso')
s += fila(670, 'Espacio libre de 0,9 m adelante', 'iluminación de 200 lx en el frente')
s += mensaje(['Reserva libre del 20 %', 'para sumar circuitos', 'sin cambiar el gabinete'], y=820, tam=40)
s += texto(60, 1110, '- Un solo cable por borne', 34)
s += texto(60, 1155, '- Barra de PE con borne para cada circuito', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
