# -*- coding: utf-8 -*-
"""Posteo 2026-10-29 · Qué tiene adentro un DPS: varistor y desconectador térmico. Formato CONEXIÓN (esquema).
Fuente: conocimiento/24 (MOV: varistor de óxido de zinc; desconectador térmico en serie; fusible o
termomagnética asociado; fuga de microamperes -> pocos ohms en nanosegundos; se gasta). No se afirma clase, Up ni ubicación."""
import sys
from placa import *

s = encabezado('QUÉ TIENE ADENTRO', 'UN DPS')

def bloque(x, titulo, l1, l2, cap1, cap2, w=270):
    r = f'<rect x="{x}" y="360" width="{w}" height="200" rx="16" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    r += texto(x + w/2, 420, l1, 32, NAVY, 'middle') + texto(x + w/2, 462, l2, 32, NAVY, 'middle')
    r += texto(x + w/2, 610, cap1, 32, NAVY, 'middle', negrita=False)
    r += texto(x + w/2, 650, cap2, 32, NAVY, 'middle', negrita=False)
    return r

# Recuadro punteado: lo que va dentro del DPS
s += f'<rect x="385" y="270" width="650" height="400" rx="20" fill="none" stroke="{GRIS}" stroke-width="5" stroke-dasharray="20 12"/>'
s += texto(712, 322, 'DENTRO DEL DPS', 34, GRIS, 'middle')

s += bloque(45, '', 'FUSIBLE O', 'TÉRMICA', 'asociado', 'al DPS')
s += bloque(400, '', 'DESCONECTADOR', 'TÉRMICO', 'en serie', 'con el varistor', 340)
s += bloque(775, '', 'VARISTOR', '(MOV)', 'disco de', 'óxido de zinc', 245)

# Cables entre bloques y símbolos
s += cable([(30, 515), (45, 515)], NAVY) + cable([(315, 515), (400, 515)], NAVY) + cable([(740, 515), (775, 515)], NAVY)
# símbolos
s += f'<rect x="140" y="497" width="90" height="36" fill="#FFF" stroke="{NAVY}" stroke-width="5"/><line x1="140" y1="515" x2="230" y2="515" stroke="{NAVY}" stroke-width="4"/>'
s += (f'<line x1="515" y1="515" x2="550" y2="515" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="550" y1="515" x2="600" y2="492" stroke="{NAVY}" stroke-width="5"/>'
      f'<line x1="610" y1="515" x2="645" y2="515" stroke="{NAVY}" stroke-width="5"/>')
s += f'<rect x="852" y="497" width="90" height="36" fill="#FFF" stroke="{NAVY}" stroke-width="5"/><line x1="847" y1="545" x2="947" y2="487" stroke="{NAVY}" stroke-width="5"/>'

s += texto(60, 740, 'Tensión normal: fuga de microamperes.', 34, NAVY, negrita=False)
s += texto(60, 790, 'Sobretensión: de megaohms a pocos ohms', 34, NAVY, negrita=False)
s += texto(60, 836, 'en nanosegundos.', 34, NAVY, negrita=False)

s += mensaje(['El varistor se gasta con cada impulso:', 'revisá el DPS después de tormentas.'], y=900)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-29-dps-por-dentro.png'
guardar(s, salida)
