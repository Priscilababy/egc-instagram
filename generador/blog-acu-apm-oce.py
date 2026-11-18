# -*- coding: utf-8 -*-
"""Portada del blog: circuitos ACU, APM y OCE (uso específico, AEA 90364-7-771, Tabla 771.7.I)."""
import sys
from placa import *

s = encabezado('ACU, APM Y OCE', 'CIRCUITOS DE USO ESPECÍFICO')


def fila(y, sigla, que, prot):
    r = f'<rect x="60" y="{y}" width="190" height="90" rx="14" fill="#FFF" stroke="{NAVY}" stroke-width="5"/>'
    r += texto(155, y + 62, sigla, 50, NAVY, 'middle')
    return r + texto(280, y + 40, que, 36) + texto(280, y + 80, prot, 34, GRIS)


s += fila(250, 'ACU', 'Una sola carga, sin derivaciones', 'protección: la fija el proyectista')
s += fila(370, 'APM', 'Pequeños motores monofásicos', '15 bocas · hasta 10 A por boca')
s += fila(490, 'OCE', 'Cualquier otra carga específica', 'bocas sin límite · proyectista')
s += texto(60, 660, 'Sección mínima: 2,5 mm² en los tres', 36)
s += mensaje(['Son adicionales: no cuentan', 'para el mínimo del grado.'], y=710, tam=40)
s += texto(60, 960, '- Diferencial de 30 mA también acá', 34)
s += texto(60, 1010, '- Caño propio, separado del uso general', 34)
s += texto(60, 1060, '- Verificar IB ≤ In ≤ Iz en cada circuito', 34)
s += firma('AEA 90364-7-771')
guardar(s, sys.argv[1] if len(sys.argv) > 1 else 'blog.png')
