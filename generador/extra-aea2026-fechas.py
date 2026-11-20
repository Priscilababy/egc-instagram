# -*- coding: utf-8 -*-
"""Placa extra 1/4 · AEA 770 edición 2026: fechas clave y cambios principales (fichas 49, 50 y 51). Estilo serie especial."""
import sys
from serie2026 import *

s = fondo(1, 4, 'LA NUEVA 770', 'YA TIENE FECHA')

# Línea de tiempo
s += tarjeta(60, 390, 960, 250)
s += f'<defs><linearGradient id="linea" x1="0" x2="1"><stop offset="0" stop-color="{CIAN}"/><stop offset="1" stop-color="{AMA}"/></linearGradient></defs>'
s += f'<rect x="240" y="447" width="600" height="10" rx="5" fill="url(#linea)"/>'
s += f'<circle cx="240" cy="452" r="24" fill="{CIAN}"/><circle cx="240" cy="452" r="10" fill="{NAVY}"/>'
s += f'<circle cx="840" cy="452" r="46" fill="{AMA}" opacity="0.55" filter="url(#brillo)"/>'
s += f'<circle cx="840" cy="452" r="30" fill="url(#ama)"/><circle cx="840" cy="452" r="12" fill="{NAVY}"/>'
s += t(240, 550, '1/11/2026', 62, CIAN, 'middle', max_w=400)
s += t(240, 605, 'VIGENTE', 36, BLANCO, 'middle')
s += t(840, 550, '1/3/2027', 62, AMA, 'middle', max_w=400)
s += t(840, 605, 'OBLIGATORIA', 36, BLANCO, 'middle')

# Cambios en obra
s += t(60, 702, 'LO QUE CAMBIA EN OBRA', 38, TXT2, extra=' letter-spacing="3"')
celdas = [
    (60, 725, '100 Ω', 'Tierra máxima en TT', 'antes: 40 Ω'),
    (555, 725, 'TIPO A', 'Diferencial mínimo', 'el AC no es apto'),
    (60, 965, '1 CIRCUITO', 'de uso general', 'por caño (obra nueva)'),
    (555, 965, '0,90 a 1,30 m', 'altura de las llaves', 'tomas: 20 cm o más'),
]
for x, y, grande, l1, l2 in celdas:
    s += tarjeta(x, y, 465, 220)
    s += f'<rect x="{x}" y="{y+30}" width="8" height="160" rx="4" fill="url(#ama)"/>'
    s += t(x + 40, y + 92, grande, 62, AMA, max_w=410)
    s += t(x + 40, y + 148, l1, 36, BLANCO, max_w=410)
    s += t(x + 40, y + 194, l2, 34, TXT2, negrita=False, max_w=410)

s += pie()
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'prueba.png')
