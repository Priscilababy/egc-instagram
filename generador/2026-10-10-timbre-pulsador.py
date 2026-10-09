# -*- coding: utf-8 -*-
"""Timbre con pulsador: 220 V al transformador de seguridad, secundario MBTS en serie pulsador-timbre."""
import sys
from placa import *

s = encabezado('TIMBRE CON PULSADOR')
s += tablero()

# Primario 220 V: fase y neutro al transformador (sin PE: el secundario MBTS no se pone a tierra)
s += cable([(440, 363), (440, 480)], CAST)
s += cable([(700, 363), (700, 480)], CEL)

# Transformador de seguridad
s += f'<rect x="340" y="480" width="440" height="165" rx="20" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += texto(560, 526, 'TRANSFORMADOR', 36, NAVY, 'middle')
s += texto(560, 566, 'DE SEGURIDAD', 36, NAVY, 'middle')
s += texto(560, 606, '220 V  ›  hasta 24 V', 32, GRIS, 'middle')
s += borne(440, 480, CAST) + borne(700, 480, CEL)
s += borne(500, 645, RET) + borne(640, 645, RET)

# Pulsador (izquierda) y timbre (derecha)
s += caja(60, 740, 340, 160, 'PULSADOR', 36)
s += f'<circle cx="230" cy="838" r="30" fill="#FFF" stroke="{NAVY}" stroke-width="6"/><circle cx="230" cy="838" r="14" fill="{AMARILLO}"/>'
s += caja(680, 740, 340, 160, 'TIMBRE', 36)
s += f'<path d="M810,860 a40,40 0 0 1 80,0 z" fill="{AMARILLO}" stroke="{NAVY}" stroke-width="5"/><circle cx="850" cy="872" r="7" fill="{NAVY}"/>'
s += borne(230, 740, RET) + borne(230, 900, RET2) + borne(850, 740, RET) + borne(850, 900, RET2)

# Secundario MBTS en serie: transformador -> pulsador -> timbre -> transformador
s += cable([(500, 645), (500, 700), (230, 700), (230, 740)], RET, punteado=True)
s += cable([(230, 900), (230, 945), (850, 945), (850, 900)], RET2, punteado=True)
s += cable([(850, 740), (850, 685), (640, 685), (640, 645)], RET, punteado=True)
s += texto(540, 995, 'Baja tensión (MBTS): sin PE', 34, GRIS, 'middle')

s += mensaje(['Timbre: transformador de', 'seguridad y pulsador en serie.'], y=1030)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'timbre.png'
guardar(s, salida)
