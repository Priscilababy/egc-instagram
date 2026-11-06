# 39 · Croquis, plano y cómputo de materiales desde el plano

Fuente: *Manual del Instalador Electricista · Categoría III*, 2.ª edición, Fundación Relevando Peligros (Córdoba, 2020). Fuente **SECUNDARIA** (manual de capacitación). Páginas citadas: las impresas.
El manual se apoya en la AEA 90364-7-771 (2006) y en la "Guía de 10 kW" de la AEA. En viviendas dentro del alcance de la 770, **mandan las fichas 01 a 12**. Ver la lista de diferencias en `00-fuentes.md`, Lote 7.

## Escalas (1.28, págs. 49-51)
- Escala = medida dibujada / medida real. 1:1 es tamaño real.
- Numerador mayor que denominador: ampliación. Menor: reducción.
- En construcción se usan también escalas intermedias: 1:25, 1:30, 1:40.
- Ejemplo del manual: planta de 60 × 30 m en hoja A3 → escala 1:200 → 30 × 15 cm.
- Las superficies se reducen con el **cuadrado** de la escala.

## Croquis de la instalación (1.31, págs. 59-60)
- El instalador dibuja una vista en planta del local, por ejemplo en hoja A4.
- Se presenta junto con el certificado de instalación apta (Córdoba, ver ficha 13).
- Líneas rectas, como en la Guía de 10 kW de la AEA. Se marcan **puertas y ventanas**.
- No hace falta escala real. Sí hay que mantener la **proporción** entre largos y anchos.
- Se ponen **cotas con las medidas reales**.
- Paredes en trazo grueso y oscuro. Cotas en trazo fino y claro.
- Se puede copiar de un plano de arquitectura o catastral. Si no hay plano, se miden los ambientes en el lugar.
- **Rótulo** abajo a la derecha: titular, dirección, electricista responsable y su número de habilitación.
- Leyenda obligatoria en el rótulo: **"croquis sin escala"**.
- Bocas y cañerías sobre el croquis: según la Guía de 10 kW de la AEA (no está en esta biblioteca).

## Símbolos de referencia del croquis (tabla 6, pág. 52)
Descripción en palabras. Origen: Guía de 10 kW de la AEA, reproducida en el manual. **No** es la norma IRAM de planos (no está en esta biblioteca).
- Boca IUG de centro: círculo con una cruz adentro.
- Boca IUG de pared: el mismo círculo con cruz, con un trazo corto hacia la pared.
- Boca TUG: semicírculo chico sobre una línea.
- Boca TUE: semicírculo con trazo distinto.
- Interruptor de 1 efecto, de 2 efectos y de combinación: trazos con forma de gancho, uno, dos o cruzado.
- Ventilador de techo: hélice de dos aspas.
- Montante: círculo chico con trazo.
- Para dibujarlos en la app, copiar la forma de la Guía de 10 kW de la AEA, no de esta ficha.

## Símbolos de unifilar que agrega el manual (tablas 8 a 10, págs. 53-54)
Complementan la ficha 38 (IRAM 2010 Parte III).
- Interruptor, seccionador e interruptor-seccionador, con y sin fusibles, con su referencia del Vocabulario Electrotécnico Internacional (VEI 441-14-xx).
- Interruptor automático (VEI 441-14-20).
- **Pequeño interruptor termomagnético (PIA)**: dos dibujos admitidos.
- **Interruptor diferencial**: dos dibujos, según cumpla o no la función de seccionamiento.
- Contactor con relé térmico y contactos auxiliares.
- Marcas de conductores sobre la línea (IEC 60617-11): fase (trazo oblicuo), neutro (trazo con punto), PE (trazo con raya), PEN (punto y raya).
- **Ojo:** la tabla 13 muestra un "termomagnético unipolar o monofásico". En vivienda monofásica la 770 **prohíbe** termomagnéticas unipolares (ficha 05).

## Unifilar (1.30, pág. 58)
- Representa la instalación de mayor a menor potencia: del ingreso de energía a los circuitos finales.
- Parte del medidor. Sigue con las protecciones automáticas y diferenciales de cada circuito.
- Indica el calibre de cada protección y la sección de cada conductor.
- Termina en las cargas: tomas, lámparas, motores, alarmas.

## Método de cómputo desde el plano (TP 1, págs. 324-336)
Método del manual para sacar la lista de materiales de un plano de planta. Sirve para el planificador de EGC.
1. Ubicar en planta: medidor, tablero, bocas de luz, tomas, llaves y número de circuito de cada boca.
2. Trazar las cañerías desde el tablero: a la boca de techo de cada ambiente y de ahí a llaves y tomas.
3. Medir cada tramo **horizontal** sobre el plano.
4. Sumar las **subidas y bajadas** a cada caja.
5. Largo de caño = tramo horizontal + subidas + bajadas.
6. Largo de cable = largo del tramo × cantidad de conductores que pasan por ese tramo.
7. Contar cajas por tipo, curvas, conectores o boquillas, llaves y tomas.
8. Armar la tabla resumen: cantidad, precio unitario y monto.

Alturas de cálculo que usa el manual para las subidas (pág. 334). Son **valores para computar**, no reglas de montaje:
- Salida alta: 2,20 m.
- Llaves y tomas a media altura: 1,10 m.
- Tomas bajas: 0,30 m.
- Tablero: 1,10 m.
- Para tomas, la regla de montaje es la de la 770: borde inferior de la caja entre 0,20 y 0,30 m sobre el piso (ficha 08).

Ejemplo del manual, dormitorio 1 (pág. 335): 6,5 m de caño de 15 mm y 10,1 m de caño de 13 mm. Cables: se multiplica cada tramo por sus conductores.

## Cajas: volumen útil (tablas 41 a 43, pág. 299)

| Caja | Volumen (cm³) | Volumen utilizable (cm³) |
|---|---|---|
| Rectangular 5 × 10 | 240 | 120 |
| Cuadrada 10 × 10 | 400 | 200 |
| Octogonal grande | 250 | 120 |
| Octogonal chica | 155 | 75 |

| Sección del conductor (mm²) | 1,5 | 2,5 | 4 | 6 | 10 |
|---|---|---|---|---|---|
| Volumen por conductor (cm³) | 6 | 8,5 | 12 | 20 | 25 |

- Volumen típico de dispositivos: interruptor 1P de 6 a 25 cm³; toma 2P+T 10 A de 18 a 38 cm³; toma 2P+T 20 A de 34 a 40 cm³.
- Uso: sumar conductores y dispositivos de la caja y comparar con el volumen utilizable.

## Cañerías (pág. 297-299)
- Los conductores no deben ocupar más del **35 %** de la sección libre del caño (tabla 40).
- Diámetro mínimo según el manual: 13 mm en circuitos; 15 mm en líneas seccionales y principales.
- Curvas: no menores a 90°; radio mínimo de 3 veces el diámetro exterior; no más de 3 curvas entre cajas.
- Una caja de paso cada 12 m en tramos rectos.
- Sin empalmes dentro del caño.
- Para las reglas de la 770 sobre caños y cajas, usar la ficha 07.

## Uso en EGC
- Planificador: rótulo con "croquis sin escala", cotas reales, puertas y ventanas.
- Cómputo automático: largo de caño y de cable por tramo, más subidas y bajadas.
- Control de llenado de cajas con las tablas de volumen.
- Lista de materiales con cantidades, lista para tomar los precios de EGC.
