# -*- coding: utf-8 -*-
"""Posteo 2026-10-02 · Puesta a tierra: jabalina, cámara de inspección y cable hasta la barra PE. Formato CONEXIÓN.
Fuente: conocimiento/06 (AEA 90364-7-770, 770.3.2, 770.14.4.1, 770.14.4.3, 770.14.4.4)."""
import sys
from placa import *

s = encabezado('PUESTA A TIERRA', 'JABALINA Y CÁMARA')

# Tierra (suelo) debajo del nivel de piso
s += '<path d="M31,600 H1049 V1202 a28,28 0 0 1 -28,28 H59 a28,28 0 0 1 -28,-28 Z" fill="#EFE6DA"/>'
s += f'<line x1="31" y1="600" x2="1049" y2="600" stroke="{NAVY}" stroke-width="5"/>'
s += texto(1025, 585, 'NIVEL DE PISO', 32, GRIS, 'end')

# Tablero principal con barra PE
s += caja(60, 235, 500, 150, 'TABLERO PRINCIPAL')
s += f'<rect x="100" y="322" width="420" height="44" rx="8" fill="{VERDE}"/>'
s += texto(310, 355, 'BARRA PE', 32, '#FFF', 'middle')

# Cable de puesta a tierra (verde-amarillo) hasta la cámara
s += cable_pe([(260, 366), (260, 667)])
s += texto(300, 470, 'Cable de PAT', 40)
s += texto(300, 520, 'mínimo 4 mm²', 40)

# Cámara de inspección, tapa a nivel del piso
s += f'<rect x="190" y="600" width="240" height="180" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += f'<rect x="184" y="590" width="252" height="16" rx="4" fill="{NAVY}"/>'
# barra de cobre con puente removible
s += '<rect x="226" y="656" width="76" height="26" fill="#C77B30"/><rect x="318" y="656" width="76" height="26" fill="#C77B30"/>'
s += f'<rect x="288" y="650" width="44" height="38" rx="6" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
s += borne(260, 669, AMAR_PE)
# del puente a la jabalina
s += cable_pe([(360, 682), (360, 760)])
# jabalina
s += f'<polygon points="352,740 368,740 368,980 360,1010 352,980" fill="#9AA3AF" stroke="#5B6573" stroke-width="4"/>'

# Rótulos
s += f'<line x1="436" y1="640" x2="466" y2="640" stroke="{NAVY}" stroke-width="4"/>'
s += texto(476, 650, 'Cámara de inspección', 36)
s += texto(476, 696, 'con tapa a nivel del piso', 34, NAVY, negrita=False)
s += texto(476, 742, 'y barra con puente removible', 34, NAVY, negrita=False)
s += texto(420, 880, 'Jabalina IRAM 2309 o 2310', 36)
s += texto(420, 930, 'Resistencia: 40 Ω como máximo', 34, NAVY, negrita=False)

s += mensaje(['La cámara permite desconectar', 'la jabalina y medir la tierra.'], y=1040)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-02-puesta-a-tierra.png'
guardar(s, salida)
