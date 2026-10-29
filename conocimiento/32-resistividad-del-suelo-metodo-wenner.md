# 32 · Resistividad del suelo: método Wenner

Fuente: N. Malpica Albert, "Sistemas de puesta a tierra. Caracterización del suelo por dos estratos. Método Schlumberger-Wenner", marzo 2022, rev. feb. 2024, págs. 5-9. Basado en ANSI/IEEE Std 81-2012.
Tipo de fuente: **SECUNDARIA** (apuntes de autor, no norma argentina). Las fichas 06 (AEA 770) y 31 (AEA 771 Anexo C) **mandan** sobre esta ficha.
Redacción propia. No es copia textual del documento.

## Para qué sirve
- Mide la resistividad real del terreno antes de diseñar la puesta a tierra.
- Reemplaza a las tablas orientativas de la ficha 31 cuando se necesita precisión.
- La AEA 771 pide medir la resistividad hasta la profundidad del electrodo cuando no se conocen los estratos (771-C.9.3 → ficha 31).

## Armado (pág. 5)
- 4 electrodos en línea recta, a la **misma separación d** entre cada uno.
- Profundidad de los electrodos **b**: del orden de 30 cm o menos.
- Instrumento: telurímetro de 4 hilos.
- Electrodos 1 y 4 (extremos): inyectan corriente (bornes I1 e I2).
- Electrodos 2 y 3 (centro): miden tensión (bornes P1 y P2).
- El telurímetro muestra R = V / I.
- Las picas que trae el instrumento miden en general 40 cm o menos (pág. 8).

## Fórmula completa (ec. 2-18, pág. 8)
ρa = 4·π·d·R / [1 + 2·d / √(d² + 4·b²) − 2·d / √(4·d² + 4·b²)]
- ρa: resistividad aparente (Ω·m).
- d: separación entre electrodos (m).
- b: profundidad de los electrodos (m).
- R: lectura del telurímetro (Ω).
- Verificado a la vista en el original.

## Fórmula simplificada (ec. 2-19, pág. 9)
- Si d es mucho mayor que b: R ≈ ρa / (2·π·d).
- Despejada: **ρa ≈ 2·π·d·R**.
- Es la forma de uso habitual en obra.

## Cómo leer el resultado (pág. 8)
- Suelo homogéneo: ρa da igual con cualquier separación d.
- Si ρa cambia al variar d, el suelo tiene capas (estratos) distintas. Es el caso normal.
- Más separación d → la medición llega a más profundidad.

## Límite del método (pág. 9)
- Al aumentar d, la lectura R baja.
- Con d muy grande, R queda fuera del rango del instrumento o en el orden de su error.
- En ese caso el autor recomienda el método Schlumberger (separaciones distintas). Fuera de alcance para vivienda.

## Fuera de ámbito (no usar en contenido domiciliario)
- Método Schlumberger, caracterización en dos estratos y algoritmo de máxima pendiente (IEEE 81 Anexo B). Son de subestaciones y obras grandes.

## Uso en el simulador de EGC
- Etapa resistividad: el usuario mueve la separación d y lee R. El simulador calcula ρa con la fórmula simplificada.
- Mostrar la fórmula completa como dato avanzado.
- Comparar el resultado con las Tablas 771-C.VIII y 771-C.IX (ficha 31).
- Recordar siempre: lo que vale es la medición final de la toma, ≤ 40 Ω en vivienda (ficha 06).
