# -*- coding: utf-8 -*-
"""Ejemplo 2 · Formato "MAL / BIEN": neutro compartido entre dos diferenciales (publicado el 2026-09-23).
Usar como plantilla para placas de error común: panel rojo arriba (mal), panel verde abajo (bien)."""
import sys
from placa import *


def panel(Y, etiqueta, color, compartido):
    fondo = '#FFF5F5' if compartido else '#F3FBF5'
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    for x, n in ((100, '1'), (660, '2')):
        s += (f'<rect x="{x}" y="{Y+100}" width="320" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
              + texto(x + 160, Y + 168, f'ID {n} · 30 mA', 46, ancla='middle')
              + f'<rect x="{x}" y="{Y+340}" width="320" height="100" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
              + texto(x + 160, Y + 408, f'CIRCUITO {n}', 46, ancla='middle'))
    for x in (160, 920):  # fases por fuera
        s += cable([(x, Y + 200), (x, Y + 340)], CAST)
    if compartido:
        s += (f'<rect x="425" y="{Y+228}" width="230" height="84" rx="12" fill="#FFF" stroke="{CEL_TXT}" stroke-width="5"/>'
              + texto(540, Y + 284, 'N COMÚN', 36, CEL_TXT, 'middle'))
        for pts in ([(360, Y+200), (360, Y+250), (425, Y+250)], [(700, Y+200), (700, Y+250), (655, Y+250)],
                    [(360, Y+340), (360, Y+290), (425, Y+290)], [(700, Y+340), (700, Y+290), (655, Y+290)]):
            s += cable(pts, CEL)
        s += (f'<circle cx="540" cy="{Y+150}" r="42" fill="{ROJO}"/>'
              f'<path d="M522,{Y+132} L558,{Y+168} M558,{Y+132} L522,{Y+168}" stroke="#FFF" stroke-width="10" stroke-linecap="round"/>')
    else:
        for x in (360, 700):
            s += cable([(x, Y + 200), (x, Y + 340)], CEL)
        s += (f'<circle cx="530" cy="{Y+270}" r="46" fill="{VERDE_OK}"/>'
              f'<path d="M508,{Y+270} L525,{Y+288} L554,{Y+252}" fill="none" stroke="#FFF" stroke-width="11" '
              f'stroke-linecap="round" stroke-linejoin="round"/>')
        s += (f'<line x1="640" y1="{Y+44}" x2="690" y2="{Y+44}" stroke="{CAST}" stroke-width="10"/>'
              + texto(704, Y + 57, 'fase', 34)
              + f'<line x1="810" y1="{Y+44}" x2="860" y2="{Y+44}" stroke="{CEL}" stroke-width="10"/>'
              + texto(874, Y + 57, 'neutro', 34))
    return s


s = encabezado('¿SALTA EL DIFERENCIAL', 'SIN MOTIVO?', linea2_amarilla=False)
s += panel(240, 'BORNERA DE NEUTRO COMÚN', ROJO, True)
s += panel(740, 'CADA NEUTRO AL SUYO', VERDE_OK, False)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else 'ejemplo_neutros.png'
guardar(s, salida)
