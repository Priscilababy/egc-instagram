# -*- coding: utf-8 -*-
"""Contactor con pulsadores de marcha y parada: circuito de mando con enclavamiento (contacto 13-14)."""
import sys
from placa import *

s = encabezado('CONTACTOR: MARCHA', 'Y PARADA')
s += tablero()

# Fase (castaño) a PARADA; neutro (celeste) al borne A2 de la bobina
s += cable([(440, 363), (440, 400), (210, 400), (210, 430)], CAST)
s += cable([(700, 363), (700, 395), (890, 395), (890, 420)], CEL)

# Mando: viajeros punteados en color no reservado
s += cable([(210, 580), (210, 625), (590, 625), (590, 670)], RET, punteado=True)
s += cable([(210, 625), (210, 670)], RET, punteado=True)
s += cable([(210, 820), (210, 865), (890, 865), (890, 620)], RET2, punteado=True)
s += cable([(590, 820), (590, 865)], RET2, punteado=True)

# PARADA (NC)
s += caja(60, 430, 300, 150, 'PARADA', 36)
s += texto(210, 548, 'NC (cerrado)', 32, NAVY, 'middle')
s += borne(210, 430, CAST) + borne(210, 580, RET)

# MARCHA (NA)
s += caja(60, 670, 300, 150, 'MARCHA', 36)
s += texto(210, 788, 'NA (abierto)', 32, NAVY, 'middle')
s += borne(210, 670, RET) + borne(210, 820, RET2)

# Contacto auxiliar 13-14 (NA) del propio contactor, en paralelo con MARCHA
s += caja(430, 670, 320, 150, 'CONTACTO AUX.', 32)
s += texto(590, 788, '13 – 14 (NA)', 32, NAVY, 'middle')
s += borne(590, 670, RET) + borne(590, 820, RET2)

# Bobina
s += caja(760, 420, 260, 200, 'BOBINA', 36)
s += texto(890, 535, 'A2', 34, NAVY, 'middle')
s += texto(890, 598, 'A1', 34, NAVY, 'middle')
s += borne(890, 420, CEL) + borne(890, 620, RET2)

s += mensaje(['Marcha en paralelo con el 13-14,', 'parada NC en serie con la bobina.'], y=930)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'contactor.png'
guardar(s, salida)
