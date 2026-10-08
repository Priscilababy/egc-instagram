# -*- coding: utf-8 -*-
"""Placa MAL / BIEN: carcasa metálica sin conductor de protección vs. con PE (2026-10-09)."""
import sys
from placa import *


def panel(Y, etiqueta, color, con_pe):
    fondo = '#F3FBF5' if con_pe else '#FFF5F5'
    s = f'<rect x="50" y="{Y}" width="980" height="470" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
    s += chip(80, Y + 22, etiqueta, color)
    s += caja(340, Y + 90, 400, 300, 'ARTEFACTO')
    s += texto(560, Y + 340, 'carcasa metálica', 34, ancla='middle')
    s += texto(560, Y + 288, 'falla: la fase toca', 32, ROJO, 'middle')
    # fase y neutro hasta sus bornes
    s += texto(90, Y + 200, 'fase', 34, CAST)
    s += cable([(90, Y + 215), (390, Y + 215)], CAST) + borne(390, Y + 215, CAST)
    s += texto(90, Y + 330, 'neutro', 34, CEL_TXT)
    s += cable([(90, Y + 345), (390, Y + 345)], CEL) + borne(390, Y + 345, CEL)
    # falla: la fase toca la carcasa (pared derecha)
    s += (f'<polyline points="390,{Y+215} 560,{Y+215} 600,{Y+245} 650,{Y+190} 740,{Y+215}" fill="none" '
          f'stroke="{ROJO}" stroke-width="8" stroke-dasharray="14 10" stroke-linejoin="round"/>')
    if con_pe:
        s += cable_pe([(740, Y + 300), (885, Y + 300), (885, Y + 395)])
        s += borne(740, Y + 300, VERDE)
        for i, w in enumerate((90, 60, 30)):
            s += f'<line x1="{885-w/2}" y1="{Y+395+i*17}" x2="{885+w/2}" y2="{Y+395+i*17}" stroke="{VERDE}" stroke-width="8" stroke-linecap="round"/>'
        s += texto(885, Y + 160, 'PE a tierra', 34, VERDE_OK, 'middle')
        s += texto(885, Y + 205, 'corta el', 34, VERDE_OK, 'middle')
        s += texto(885, Y + 250, 'diferencial', 34, VERDE_OK, 'middle')
    else:
        s += texto(885, Y + 160, 'SIN PE', 40, ROJO, 'middle')
        s += texto(885, Y + 235, '220 V', 60, ROJO, 'middle')
        s += texto(885, Y + 285, 'en la carcasa', 34, ROJO, 'middle')
    return s


s = encabezado('CARCASA METÁLICA', 'CON FALLA DE AISLACIÓN', linea2_amarilla=True)
s += panel(240, 'SIN CABLE PE', ROJO, False)
s += panel(740, 'CON PE A TIERRA', VERDE_OK, True)
s += firma()

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-10-09-carcasa-sin-pe.png'
guardar(s, salida)
