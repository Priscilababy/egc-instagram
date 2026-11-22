# -*- coding: utf-8 -*-
"""Portada del blog: motores, sección del cable y protección de sobrecarga (fichas 05, 25, 04)."""
import sys
from placa import *

s = encabezado('MOTORES: CABLE Y', 'PROTECCIÓN DE SOBRECARGA')


def fila(y, titulo, linea2):
    r = f'<rect x="60" y="{y}" width="960" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    return r + texto(90, y + 44, titulo, 38) + texto(90, y + 84, linea2, 34, GRIS)


s += texto(60, 275, 'Lo que pide un motor de instalación fija:', 38)
s += fila(310, 'Cable: 125 % de la corriente', 'nominal del motor (o del más grande)')
s += fila(430, 'Maniobra: corta fase y neutro', 'o todas las fases a la vez')
s += fila(550, 'Trifásico: detector de', 'falta de fase que corte')
s += fila(670, 'Sobrecarga: protección', 'dedicada al motor')
s += mensaje(['La termomagnética y el fusible', 'no sirven como protección', 'de sobrecarga del motor.'], y=815, tam=40)
s += texto(60, 1115, '- Caída de tensión: 5 % en marcha', 34)
s += texto(60, 1165, '- Diferencial 30 mA en el circuito', 34)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
