# -*- coding: utf-8 -*-
"""Motor monofásico con capacitor: maniobra bipolar (fase y neutro) y capacitor en serie con el auxiliar."""
import sys
from placa import *

s = encabezado('MOTOR MONOFÁSICO', 'CON CAPACITOR')
s += tablero(it_txt='IT 2P')

# Fase y neutro entran a la maniobra bipolar; PE directo a la carcasa del motor
s += cable([(440, 363), (440, 410)], CAST)
s += cable([(700, 363), (700, 410)], CEL)
s += cable_pe([(920, 363), (920, 720)])
s += cable([(440, 650), (440, 720)], CAST)
s += cable([(700, 650), (700, 720)], CEL)

# Maniobra bipolar: abre fase y neutro a la vez
s += caja(380, 410, 400, 240, 'MANIOBRA BIPOLAR', 34)
for x in (440, 700):
    s += (f'<line x1="{x}" y1="482" x2="{x}" y2="525" stroke="{NAVY}" stroke-width="5"/>'
          f'<circle cx="{x}" cy="525" r="10" fill="{NAVY}"/>'
          f'<line x1="{x}" y1="525" x2="{x}" y2="570" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
          f'<circle cx="{x}" cy="580" r="10" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="590" x2="{x}" y2="650" stroke="{NAVY}" stroke-width="5"/>')
s += borne(440, 410, CAST) + borne(700, 410, CEL) + borne(440, 650, CAST) + borne(700, 650, CEL)

# Capacitor entre el borne del principal (donde entra la fase) y el borne del auxiliar
s += cable([(170, 720), (170, 700), (238, 700)], RET, punteado=True)
s += cable([(262, 700), (440, 700)], RET, punteado=True)
s += (f'<line x1="238" y1="672" x2="238" y2="728" stroke="{NAVY}" stroke-width="6"/>'
      f'<line x1="262" y1="672" x2="262" y2="728" stroke="{NAVY}" stroke-width="6"/>'
      f'<circle cx="440" cy="700" r="9" fill="{CAST}"/>')
s += texto(250, 652, 'CAPACITOR', 32, NAVY, 'middle')

# Bornera del motor
s += f'<rect x="60" y="720" width="960" height="240" rx="14" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
s += borne(170, 720, RET) + borne(440, 720, CAST) + borne(700, 720, CEL) + borne(920, 720, VERDE)
s += (texto(170, 795, 'AUXILIAR', 32, RET, 'middle') + texto(440, 795, 'PRINCIPAL', 32, CAST, 'middle')
      + texto(700, 795, 'COMÚN', 32, CEL_TXT, 'middle') + texto(920, 795, 'PE', 32, VERDE, 'middle'))
s += texto(540, 880, 'MOTOR MONOFÁSICO', 44, NAVY, 'middle')
s += texto(540, 935, 'Bornes y capacitor: los define la placa', 32, NAVY, 'middle', negrita=False)

s += mensaje(['Maniobra: corta fase y neutro.', 'Capacitor en serie con el auxiliar.'], y=990)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'motor-capacitor.png'
guardar(s, salida)
