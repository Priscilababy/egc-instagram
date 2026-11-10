# -*- coding: utf-8 -*-
"""Portada del blog: flotante de tanque, comando en MBTS (ficha 10)."""
import sys
from placa import *

s = encabezado('FLOTANTE DE TANQUE', 'COMANDO EN MBTS', linea2_amarilla=True)


def panel(Y, h, etiqueta, color, fondo, lineas):
    t = f'<rect x="50" y="{Y}" width="980" height="{h}" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    t += chip(80, Y + 22, etiqueta, color)
    for i, l in enumerate(lineas):
        t += texto(90, Y + 135 + 56 * i, l, 40)
    return t


s += panel(240, 260, 'MAL', ROJO, '#FFF5F5',
           ['Flotante dentro del tanque', 'conectado a 220 V'])
s += panel(530, 380, 'BIEN', VERDE_OK, '#F3FBF5',
           ['Comando en MBTS: hasta 24 V', 'Fuente de seguridad IEC 61558',
            'Nunca autotransformador', 'Secundario y masas sin tierra'])
s += (f'<circle cx="900" cy="390" r="56" fill="{ROJO}"/>'
      f'<path d="M876,366 L924,414 M924,366 L876,414" stroke="#FFF" stroke-width="13" stroke-linecap="round"/>')
s += (f'<circle cx="900" cy="680" r="56" fill="{VERDE_OK}"/>'
      f'<path d="M873,680 L894,702 L929,658" fill="none" stroke="#FFF" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>')
s += mensaje(['Cables de MBTS y de 220 V', 'en caños separados'], y=950)
s += firma()
guardar(s, sys.argv[1])
