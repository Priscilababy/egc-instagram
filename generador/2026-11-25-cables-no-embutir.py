# -*- coding: utf-8 -*-
"""Posteo 2026-11-25 · MAL / BIEN: qué cable va dentro del caño embutido.
Fuente: conocimiento/07 y 04 (AEA 90364-7-770, 770.10 y 770.10.1)."""
import sys, math
from placa import *

COBRE = '#C77B30'
FUNDA = '#9AA3AD'


def nucleo(cx, cy, r, macizo=False):
    """Núcleo de cobre: macizo = un solo alambre; si no, 7 hebras."""
    if macizo:
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{COBRE}" stroke="#8A5320" stroke-width="3"/>'
    h = r / 3
    s = f'<circle cx="{cx}" cy="{cy}" r="{h}" fill="{COBRE}" stroke="#8A5320" stroke-width="2"/>'
    for i in range(6):
        a = math.pi / 3 * i
        s += (f'<circle cx="{cx + 2*h*math.cos(a):.1f}" cy="{cy + 2*h*math.sin(a):.1f}" r="{h}" '
              f'fill="{COBRE}" stroke="#8A5320" stroke-width="2"/>')
    return s


def conductor(cx, cy, r, color, macizo=False, pe=False):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
    if pe:  # verde-amarillo: medio círculo amarillo
        s += (f'<path d="M{cx-r},{cy} A{r},{r} 0 0 1 {cx+r},{cy} Z" fill="{AMAR_PE}"/>')
    s += nucleo(cx, cy, r * 0.55, macizo)
    return s


def cano(cx, cy, r=130):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#F4F4F4" stroke="#5E6B78" stroke-width="10"/>')


def cruz(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="34" fill="{ROJO}"/>'
            f'<path d="M{cx-14},{cy-14} L{cx+14},{cy+14} M{cx+14},{cy-14} L{cx-14},{cy+14}" stroke="#FFF" '
            f'stroke-width="9" stroke-linecap="round"/>')


def tilde(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="34" fill="{VERDE_OK}"/>'
            f'<path d="M{cx-16},{cy} L{cx-4},{cy+13} L{cx+17},{cy-13}" fill="none" stroke="#FFF" '
            f'stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>')


def panel_mal(Y):
    s = f'<rect x="50" y="{Y}" width="980" height="380" rx="24" fill="#FFF5F5" stroke="{ROJO}" stroke-width="5"/>'
    s += chip(80, Y + 22, 'MAL · EN EL CAÑO', ROJO)
    cx, cy = 225, Y + 230
    s += cano(cx, cy)
    # cordón tipo taller: funda con 3 conductores
    fx, fy = cx - 35, cy - 20
    s += f'<circle cx="{fx}" cy="{fy}" r="78" fill="{FUNDA}" stroke="#6F7883" stroke-width="4"/>'
    for (dx, dy), col, pe in (((-30, -18), CAST, False), ((30, -18), CEL, False), ((0, 34), VERDE, True)):
        s += conductor(fx + dx, fy + dy, 28, col, pe=pe)
    # alambre macizo
    s += conductor(cx + 58, cy + 68, 32, CAST, macizo=True)
    # textos
    s += cruz(450, Y + 140)
    s += texto(500, Y + 154, 'Cordón tipo taller', 42)
    s += texto(500, Y + 200, 'es para aparatos portátiles', 34, GRIS)
    s += cruz(450, Y + 280)
    s += texto(500, Y + 294, 'Alambre macizo', 42)
    s += texto(500, Y + 340, 'un solo alambre', 34, GRIS)
    return s


def panel_bien(Y):
    s = f'<rect x="50" y="{Y}" width="980" height="380" rx="24" fill="#F3FBF5" stroke="{VERDE_OK}" stroke-width="5"/>'
    s += chip(80, Y + 22, 'BIEN · EN EL CAÑO', VERDE_OK)
    cx, cy = 225, Y + 230
    s += cano(cx, cy)
    for (dx, dy), col, pe in (((-52, -35), CAST, False), ((52, -35), CEL, False), ((0, 55), VERDE, True)):
        s += conductor(cx + dx, cy + dy, 44, col, pe=pe)
    s += tilde(450, Y + 140)
    s += texto(500, Y + 154, 'Unipolar IRAM NM 247-3', 42)
    s += texto(500, Y + 200, 'o IRAM 62267, varios alambres', 34, GRIS)
    s += tilde(450, Y + 280)
    s += texto(500, Y + 294, 'Fase, neutro y PE', 42)
    s += texto(500, Y + 340, 'juntos en el mismo caño', 34, GRIS)
    return s


s = encabezado('¿QUÉ CABLE VA', 'DENTRO DEL CAÑO?')
s += panel_mal(222)
s += panel_bien(620)
s += mensaje(['Cordón tipo taller y alambre macizo:', 'prohibidos en instalación fija'], x=60, y=1040, tam=38)
s += firma('AEA 90364-7-770')

salida = sys.argv[1] if len(sys.argv) > 1 else '2026-11-25-cables-no-embutir.png'
guardar(s, salida)
