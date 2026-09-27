# -*- coding: utf-8 -*-
"""Posteo 2026-09-28 · Bomba de agua con automático de tanque (flotante eléctrico). Formato
CONEXIÓN. El comando del flotante va en MBTS (transformador de seguridad, <=24 V), nunca en
220 V dentro del tanque (conocimiento/README.md, aviso; conocimiento/10, 770.7.1 h). El motor
se maniobra con un contactor bipolar que corta fase y neutro (conocimiento/05, 770.13.3)."""
import sys
from placa import *

s = encabezado('BOMBA DE AGUA', 'CON FLOTANTE')
s += tablero()

# Fase y neutro del tablero bajan derecho: entran al bloque MBTS y siguen al contactor.
s += cable([(440, 363), (440, 490)], CAST)
s += cable([(440, 490), (440, 520)], CAST)
s += cable([(700, 363), (700, 490)], CEL)
s += cable([(700, 490), (700, 520)], CEL)
# PE directo a la masa del motor (las masas del circuito MBTS no se conectan a tierra).
s += cable_pe([(920, 363), (920, 863)])

# Bloque del transformador de seguridad + flotante (MBTS, <=24 V). La fase y el neutro
# solo pasan por acá para alimentar el primario del transformador (220 V); no se cortan.
s += (f'<rect x="380" y="380" width="440" height="110" rx="16" fill="#F6F8FA" stroke="{NAVY}" stroke-width="4"/>'
      + texto(600, 430, 'TRANSF. + FLOTANTE', 32, NAVY, 'middle')
      + texto(600, 468, '24 V MBTS (TANQUE)', 32, GRIS, 'middle'))
# Salida del transformador: circuito de comando a 24 V (color no reservado, punteado).
s += cable([(570, 490), (570, 520)], RET, punteado=True)
s += borne(570, 520, RET)

# Caja del contactor: bobina a 24 V (A1/A2) y contactos que cortan fase y neutro a la vez.
s += caja(380, 520, 440, 270, 'CONTACTOR')
s += texto(410, 575, 'L', 36, CAST, 'end') + texto(730, 575, 'N', 36, CEL, 'start')
for x in (440, 700):
    s += (f'<line x1="{x}" y1="520" x2="{x}" y2="630" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="630" x2="{x}" y2="662" stroke="{NAVY}" stroke-width="5"/>'
          f'<circle cx="{x}" cy="662" r="10" fill="{NAVY}"/>'
          f'<line x1="{x}" y1="662" x2="{x}" y2="734" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
          f'<circle cx="{x}" cy="744" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="754" x2="{x}" y2="790" stroke="{NAVY}" stroke-width="5"/>')
# Bobina del contactor, alimentada por el circuito de 24 V del flotante.
# (el tramo bajo el encabezado no se dibuja: el propio encabezado navy lo cubre;
# retoma como línea visible recién debajo, para no cortar el título "CONTACTOR")
s += (f'<line x1="570" y1="592" x2="570" y2="650" stroke="{RET}" stroke-width="6" stroke-dasharray="16 12"/>'
      f'<rect x="505" y="650" width="130" height="80" rx="12" fill="#FFF" stroke="{RET}" stroke-width="5"/>'
      + texto(570, 685, 'BOBINA', 32, RET, 'middle') + texto(570, 720, '24 V', 32, RET, 'middle'))
s += borne(440, 520, CAST) + borne(700, 520, CEL)
s += borne(440, 790, CAST) + borne(700, 790, CEL)

# Salida del contactor (fase y neutro ya conmutados) a la bornera del motor.
s += cable([(440, 790), (440, 830), (560, 830), (560, 863)], CAST)
s += cable([(700, 790), (700, 830), (740, 830), (740, 863)], CEL)

# Bornera del motor de la bomba
s += f'<rect x="480" y="880" width="540" height="110" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(560, 880, CAST) + borne(740, 880, CEL) + borne(920, 880, VERDE)
s += (texto(560, 950, 'L', 32, CAST, 'middle') + texto(740, 950, 'N', 32, CEL_TXT, 'middle')
      + texto(920, 950, 'PE', 32, VERDE, 'middle'))

# Dibujo simplificado de la bomba (motor + cuerpo de bomba)
s += (f'<line x1="740" y1="990" x2="740" y2="1025" stroke="#5B6573" stroke-width="10"/>'
      f'<rect x="655" y="1025" width="170" height="110" rx="16" fill="{GRIS}" stroke="#5B6573" stroke-width="4"/>'
      f'<circle cx="825" cy="1080" r="34" fill="#C9CFD7" stroke="#5B6573" stroke-width="4"/>'
      f'<line x1="859" y1="1080" x2="910" y2="1080" stroke="#5B6573" stroke-width="10" stroke-linecap="round"/>')
s += texto(740, 1098, 'M', 56, '#FFF', 'middle')

s += mensaje(['El flotante va', 'a 24 V (MBTS),', 'nunca a 220 V.'], tam=32)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-09-28-bomba-flotante.png'
guardar(s, salida)
