# 34 · Medición de puesta a tierra: método de la pinza

Fuente: EPM (Empresas Públicas de Medellín), Norma Técnica RA6-014 "Mediciones para el sistema de puesta a tierra", sept. 2019, págs. 18-20 y 28-29.
Tipo de fuente: **SECUNDARIA** (norma de una distribuidora de Colombia, no norma argentina). Las fichas 06 (AEA 770) y 12 **mandan**: en vivienda el método de referencia es el telurímetro con el método del 62 %.
Redacción propia. No es copia textual del documento.

## Qué es (pág. 18)
- Mide la resistencia de puesta a tierra sin clavar electrodos auxiliares.
- Se abraza con la pinza la bajada o el cable del electrodo.
- Se usa donde no hay lugar para el método del 62 %: ciudades densas, cámaras subterráneas.

## Cómo funciona (págs. 19-20)
- La pinza induce una tensión E en el lazo y mide la corriente I que circula.
- Los instrumentos trabajan en general a 1,6 kHz y filtran corrientes parásitas.
- Lectura: E / I = Rx + (resistencia de todas las otras tomas en paralelo).
- Rx es la toma medida.
- Si hay muchas otras tomas unidas por el neutro o un cable de guarda, su paralelo es casi cero. Entonces la lectura ≈ Rx.

## Condición clave
- **El método necesita un camino de retorno:** otras tomas de tierra unidas al electrodo medido por un conductor.
- Sin camino de retorno, la pinza no mide la resistencia de la toma.
- La fuente indica que el método **en general no se recomienda**, y menos en sistemas aislados o sin ruta de retorno (pág. 29).

## Límites (pág. 20)
- Supone que las otras tomas tienen valores parecidos y que el conductor que las une tiene resistencia despreciable.
- En redes reales eso no siempre se cumple: corrosión, largo de la red, defectos de montaje.
- Resultado posible: lecturas con error.

## Aplicación en Argentina, vivienda en esquema TT (deducción a partir de fichas 06 y 33)
- La toma de protección (Ra) es **independiente** de la tierra de servicio (Rb) y está a más de 10·Re (ficha 33).
- Una vivienda con una sola jabalina no tiene camino de retorno por tierra propio.
- Por eso, en una vivienda TT típica, la pinza **no reemplaza** al telurímetro.
- Marcar este punto como deducción: la fuente no trata el esquema TT argentino.

## Otro dato de la fuente: método de la pendiente (pág. 28)
- Alternativa al 62 % en áreas restringidas.
- Electrodo de corriente C a una distancia ≥ 6 veces la mayor dimensión de la toma.
- Lecturas con el electrodo de potencial a 0,2·C, 0,4·C y 0,6·C.
- Se calcula µ = (R3 − R2) / (R2 − R1) y se busca un factor k en una tabla de la fuente.
- Tabla de k: no incorporada. No usar el método sin esa tabla.

## Criterio de las tres lecturas en el método del 62 % (pág. 28)
- La fuente acepta hasta **10 %** de diferencia entre R1, R2 y R0.
- Si la diferencia es mayor, alejar el electrodo de corriente y repetir.
- La AEA 770 pide que las tres lecturas "coincidan" (ficha 06). En EGC usar el criterio de la AEA y mencionar el 10 % solo como referencia de otra norma.

## Uso en el simulador de EGC
- Etapa pinza: mostrar cómo funciona con varias tomas unidas (lectura ≈ Rx).
- Mostrar que con una sola jabalina TT y sin retorno la lectura no sirve.
- Mensaje final: en vivienda, medir con telurímetro (ficha 06).
