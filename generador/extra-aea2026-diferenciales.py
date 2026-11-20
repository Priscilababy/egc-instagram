# -*- coding: utf-8 -*-
"""Placa extra · Qué tipo de diferencial va en vivienda, edición 2026 (fichas 49, 50 y 51)."""
import sys
from placa import *

s = encabezado('¿QUÉ DIFERENCIAL VA?', 'AEA 770 · EDICIÓN 2026')


def tarjeta(Y, letra, color, fondo, t1, t2, t3, tam=84):
    r = f'<rect x="60" y="{Y}" width="960" height="210" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    r += f'<rect x="85" y="{Y+30}" width="150" height="150" rx="20" fill="{color}"/>'
    r += texto(160, Y + 105 + tam * 0.36, letra, tam, '#FFF', 'middle')
    r += texto(270, Y + 72, t1, 44, NAVY)
    r += texto(270, Y + 126, t2, 38, '#2A3A4D', 'start', False)
    r += texto(270, Y + 176, t3, 38, '#2A3A4D', 'start', False)
    return r


s += tarjeta(225, 'AC', ROJO, '#FFF5F5', 'NO APTO en viviendas', 'Las cargas electrónicas', 'lo pueden dejar sin actuar', tam=64)
# cruz sobre AC
s += f'<line x1="100" y1="390" x2="220" y2="270" stroke="#FFF" stroke-width="9" stroke-linecap="round"/>'
s += tarjeta(455, 'A', VERDE_OK, '#F3FBF5', 'USO GENERAL', 'Detecta alterna y', 'continua pulsante')
s += tarjeta(685, 'F', '#2A8FD0', '#EEF7FD', 'EQUIPOS INVERTER', 'Cargas monofásicas con', 'frecuencias mixtas')
s += tarjeta(915, 'B', NAVY, '#F2F4F7', 'CONTINUA LISA', 'Cargador de auto o FV,', 'si el fabricante lo pide')

s += f'<rect x="60" y="1145" width="960" height="70" rx="18" fill="#FFF6D6" stroke="{AMARILLO}" stroke-width="4"/>'
s += texto(540, 1194, 'Todos de 30 mA en circuitos terminales', 38, NAVY, 'middle')
s += firma('AEA 90364-7-770')

guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
