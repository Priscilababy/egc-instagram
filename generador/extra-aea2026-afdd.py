# -*- coding: utf-8 -*-
"""Placa extra 4/4 · Detector de arco (AFDD): cuándo es obligatorio en vivienda (fichas 05, 07 y 51). Estilo serie especial."""
import sys
from serie2026 import *

s = fondo(4, 4, 'DETECTOR DE ARCO', '¿CUÁNDO VA SÍ O SÍ?')

# Qué hace
s += tarjeta(60, 385, 960, 210)
s += f'<circle cx="160" cy="490" r="70" fill="{AMA}" opacity="0.45" filter="url(#brillo)"/>'
s += f'<rect x="100" y="430" width="120" height="120" rx="30" fill="{NAVY_D}" stroke="{AMA}" stroke-width="3"/>'
s += rayo(160, 490, 1.05)
s += t(260, 460, 'AFDD', 44, AMA)
s += t(260, 510, 'Detecta arcos que la térmica', 34, BLANCO, negrita=False, max_w=730)
s += t(260, 555, 'y el diferencial no ven', 34, BLANCO, negrita=False, max_w=730)

# Condición
def chip_cond(x, y, w, titulo, sub, color):
    r = tarjeta(x, y, w, 170, borde=color)
    r += t(x + w / 2, y + 78, titulo, 42, color, 'middle', max_w=w - 30)
    r += t(x + w / 2, y + 128, sub, 32, TXT2, 'middle', negrita=False, max_w=w - 30)
    return r

s += chip_cond(60, 625, 420, 'MADERA', 'construcción de madera', '#E0A15C')
s += t(540, 725, 'o', 48, BLANCO, 'middle')
s += chip_cond(600, 625, 420, 'TELGOPOR', 'aislación de EPS', CIAN)
s += t(540, 850, '+', 72, AMA, 'middle')
s += chip_cond(260, 870, 560, 'CAÑO AISLANTE', 'canalización de material aislante', BLANCO)

# Resultado
s += f'<rect x="60" y="1068" width="960" height="120" rx="30" fill="url(#ama)" filter="url(#sombra)"/>'
s += t(540, 1128, 'AFDD OBLIGATORIO', 52, NAVY, 'middle', max_w=900)
s += t(540, 1172, 'En el resto de la vivienda: recomendado', 32, NAVY, 'middle', negrita=False, max_w=900)

s += pie()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
