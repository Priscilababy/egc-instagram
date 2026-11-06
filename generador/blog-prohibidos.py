# -*- coding: utf-8 -*-
"""Portada del blog: cables, caños y cajas prohibidos."""
import sys
from placa import *

s = encabezado('LO QUE NO SE PERMITE', 'EN INSTALACIÓN FIJA', linea2_amarilla=True)


def fila(y, titulo, sub):
    r = f'<rect x="60" y="{y}" width="960" height="130" rx="18" fill="#FFF" stroke="{ROJO}" stroke-width="5"/>'
    r += chip(80, y + 35, 'NO', ROJO, 40)
    return r + texto(230, y + 60, titulo, 40) + texto(230, y + 105, sub, 34, GRIS)


s += fila(250, 'Cable de alambre macizo', 'un solo alambre')
s += fila(400, 'Cordón tipo taller', 'solo para aparatos portátiles')
s += fila(550, 'Cable embutido sin caño', 'directo en la pared')
s += fila(700, 'Caño naranja propagante', 'de la llama')
s += mensaje(['Empalmes: solo en cajas,', 'nunca dentro del caño'], y=870, tam=40)
s += firma()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
