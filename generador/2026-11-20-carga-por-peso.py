# -*- coding: utf-8 -*-
"""Posteo 2026-11-20 · AIRE · MAL / BIEN: cargar refrigerante "a ojo" vs. por peso con balanza (ficha 17 y 20)."""
import sys
from placa import *


def manometro(cx, cy):
    """Manómetro con signo de pregunta (carga 'a ojo')."""
    s = (f'<circle cx="{cx}" cy="{cy}" r="95" fill="#FFF" stroke="{NAVY}" stroke-width="8"/>'
         f'<path d="M{cx-70},{cy+30} A75,75 0 1 1 {cx+70},{cy+30}" fill="none" stroke="{GRIS}" stroke-width="6"/>')
    for ang in range(-200, 21, 30):
        import math
        a = math.radians(ang)
        x1, y1 = cx + 62 * math.cos(a), cy + 62 * math.sin(a)
        x2, y2 = cx + 76 * math.cos(a), cy + 76 * math.sin(a)
        s += f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{NAVY}" stroke-width="5"/>'
    s += (f'<rect x="{cx-14}" y="{cy+95}" width="28" height="40" fill="{NAVY}"/>'
          + texto(cx, cy + 40, '?', 110, ROJO, 'middle'))
    return s


def balanza(cx, base):
    """Garrafa sobre balanza con display."""
    s = (f'<rect x="{cx-110}" y="{base-60}" width="220" height="60" rx="10" fill="{NAVY}"/>'
         f'<rect x="{cx-60}" y="{base-52}" width="120" height="44" rx="6" fill="#DFF5E6"/>'
         + texto(cx, base - 16, 'kg', 34, VERDE_OK, 'middle')
         + f'<rect x="{cx-125}" y="{base-78}" width="250" height="18" rx="6" fill="{GRIS}"/>'
         f'<rect x="{cx-60}" y="{base-228}" width="120" height="150" rx="40" fill="#FFF" stroke="{NAVY}" stroke-width="7"/>'
         f'<rect x="{cx-22}" y="{base-258}" width="44" height="34" rx="6" fill="{NAVY}"/>')
    return s


def panel(Y, etiqueta, color, fondo):
    return (f'<rect x="50" y="{Y}" width="980" height="380" rx="24" fill="{fondo}" stroke="{color}" stroke-width="5"/>'
            + chip(80, Y + 22, etiqueta, color))


s = encabezado('¿CARGÁS EL GAS', 'A OJO?')

# MAL
Y = 230
s += panel(Y, 'MAL · A OJO', ROJO, '#FFF5F5')
s += manometro(200, Y + 200)
s += texto(360, Y + 160, 'Cargo hasta que', 42)
s += texto(360, Y + 212, '"parece" que enfría.', 42)
s += texto(360, Y + 282, 'De más: suben presiones', 36, ROJO)
s += texto(360, Y + 328, 'y corriente.', 36, ROJO)

# BIEN
Y = 630
s += panel(Y, 'BIEN · POR PESO', VERDE_OK, '#F3FBF5')
s += balanza(200, Y + 362)
s += texto(360, Y + 140, 'Carga de la placa', 42)
s += texto(360, Y + 192, '+ gramos por metro', 42)
s += texto(360, Y + 244, 'extra (manual).', 42)
s += texto(360, Y + 314, 'Mezclas: en fase líquida.', 36, VERDE_OK)

s += mensaje(['Primero: sin fugas y con vacío.', 'Después: el gas se pesa.'], y=1030)
s += firma('Manual del fabricante')

salida = sys.argv[1] if len(sys.argv) > 1 else 'carga.png'
guardar(s, salida)
