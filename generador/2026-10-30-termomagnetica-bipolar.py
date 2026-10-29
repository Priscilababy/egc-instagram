# -*- coding: utf-8 -*-
"""Portada del blog · Termomagnética bipolar en monofásico (2026-10-30)."""
import sys
from placa import *

s = encabezado('TERMOMAGNÉTICA', 'BIPOLAR EN MONOFÁSICO')

# Entrada y salida: fase (castaño) y neutro (celeste), cada uno por su polo
s += cable([(440, 230), (440, 372)], CAST) + cable([(640, 230), (640, 372)], CEL)
s += cable([(440, 770), (440, 835)], CAST) + cable([(640, 770), (640, 835)], CEL)

s += caja(250, 300, 580, 470, 'TERMOMAGNÉTICA')
for x in (440, 640):
    s += (f'<line x1="{x}" y1="372" x2="{x}" y2="445" stroke="{NAVY}" stroke-width="6"/>'
          f'<circle cx="{x}" cy="455" r="10" fill="{NAVY}"/>'
          f'<line x1="{x}" y1="455" x2="{x}" y2="545" stroke="{NAVY}" stroke-width="8" stroke-linecap="round"/>'
          f'<line x1="{x}" y1="545" x2="{x}" y2="580" stroke="{NAVY}" stroke-width="6"/>'
          f'<rect x="{x-40}" y="580" width="80" height="80" rx="8" fill="#F6F8FA" stroke="{NAVY}" stroke-width="5"/>'
          f'<line x1="{x}" y1="660" x2="{x}" y2="770" stroke="{NAVY}" stroke-width="6"/>')
# Manija común: los dos polos abren y cierran juntos
s += f'<line x1="440" y1="505" x2="640" y2="505" stroke="{AMARILLO}" stroke-width="8" stroke-dasharray="14 10"/>'
s += texto(420, 725, 'FASE', 32, CAST, 'end') + texto(660, 725, 'NEUTRO', 32, CEL_TXT, 'start')

s += chip(60, 850, 'BIEN: 2 polos protegidos', VERDE_OK, 36)
s += chip(60, 925, 'MAL: 1P+N o unipolar', ROJO, 36)

s += mensaje(['Monofásico: bipolar,', 'fase y neutro protegidos.'], y=1010)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'portada.png'
guardar(s, salida)
