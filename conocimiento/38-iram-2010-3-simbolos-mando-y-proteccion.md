# 38 · Símbolos de mando y protección para esquemas (IRAM 2010 Parte III)

Fuente: IRAM 2010 Parte III, "Dibujo técnico. Símbolos gráficos electrotécnicos. Aparatos y dispositivos de mando y protección", diciembre 1988 (33 págs., copia escaneada). Páginas citadas: las impresas.
Equivale a IEC 617-7 (1983). La numeración de cada símbolo es la de esa IEC (pág. 3).
Sirve para **esquemas funcionales y unifilares** (tableros, comandos). **No** trae los símbolos para el **plano de planta** (tomas, bocas, llaves sobre el plano): esos van en otra parte de la IRAM 2010, que **no** está en esta biblioteca.
Los dibujos no se copian acá: se describen. Para dibujar, mirar la norma.

## Reglas generales (cap. I, pág. 3)
- Cada símbolo muestra la **función** del contacto o aparato, no su forma física.
- Puede agregarse un círculo chico, lleno o vacío, que marca la articulación del contacto.
- Algunos símbolos viejos (IEC 117-3, 1963) siguen en uso. Están en el Anexo A.

## Marcas que se agregan al contacto (sección 1, pág. 4)

| N° | Marca | Significa |
|---|---|---|
| 07-01-01 | Semicírculo | Función contactor |
| 07-01-02 | Cruz (×) | Función interruptor de potencia automático |
| 07-01-03 | Raya | Función seccionador |
| 07-01-04 | Semicírculo con raya | Función seccionador bajo carga |
| 07-01-05 | Cuadrado lleno | Apertura automática |
| 07-01-06 | Triángulo | Contacto de posición (fin de carrera) |
| 07-01-07 | Triángulo chico | Retorno automático |
| 07-01-08 | Círculo | Retorno no automático |

## Contactos (sección 2, pág. 5)
- **07-02-01 / 07-02-02:** contacto **normalmente abierto (NA)**. También es el símbolo general de **interruptor**.
- **07-02-03:** contacto **normalmente cerrado (NC)**.
- **07-02-04:** contacto de dos posiciones; el NC abre antes de que cierre el otro.
- **07-02-05:** contacto de tres posiciones con posición central abierta.
- **07-02-06 / 07-02-07:** dos posiciones con superposición; el NA cierra antes de que abra el otro.
- **07-02-08 / 07-02-09:** contacto doble, ambos abiertos o ambos cerrados en reposo.

## Mando manual (sección 7, pág. 8)
- **07-07-01:** interruptor manual NA, símbolo general.
- **07-07-02:** **pulsador NA** (vuelve solo).
- **07-07-03:** botón tirador NA (vuelve solo).
- **07-07-04:** interruptor NA con mando rotativo (no vuelve solo).
- Los mandos de "oprimir" o "tirar" ya se entienden con retorno automático. No hace falta dibujar el retorno (pág. 8).

## Aparatos de conexión (sección 13, págs. 14-15)

| N° | Aparato |
|---|---|
| 07-13-01 | Interruptor (se usa 07-02-01 o 07-02-02) |
| 07-13-02 | Contactor |
| 07-13-03 | Contactor con apertura automática |
| 07-13-04 | Ruptor |
| 07-13-05 | **Interruptor de potencia automático** (contacto con cruz) |
| 07-13-06 | **Seccionador** |
| 07-13-07 | Seccionador de dos sentidos con posición central abierta |
| 07-13-08 | Seccionador bajo carga |
| 07-13-09 | Seccionador bajo carga con apertura automática |
| 07-13-10 | Seccionador manual con dispositivo de bloqueo |

## Arrancadores de motor (sección 14, pág. 16)
- **07-14-01:** arrancador, símbolo general (rectángulo con diagonales en la parte de arriba).
- Variantes: por pasos (07-14-02), arrancador-regulador (07-14-03), con parada automática (07-14-04), directo por contactor para dos sentidos de marcha (07-14-05), **estrella-triángulo (07-14-06)**, por autotransformador (07-14-07), por tiristores (07-14-08).

## Bobinas de relé y contactor (sección 15, pág. 17)
- **07-15-01 / 07-15-02:** órgano de mando (bobina), símbolo general: un rectángulo.
- **07-15-07:** relé temporizado al desenergizar.
- **07-15-08:** relé temporizado al energizar.
- **07-15-09:** temporizado en ambos casos.
- **07-15-10:** relé de alta velocidad.

## Relés de medición (secciones 16 y 17, págs. 19-22)
- Magnitudes con símbolo propio: tensión de falla a masa (07-16-02), tensión residual (07-16-03), corriente inversa (07-16-04), **corriente diferencial Id (07-16-05)**, corriente de neutro (07-16-08).
- Relés de ejemplo: falta de tensión U = 0 (07-17-01), tensión mínima U < (07-17-07), corriente máxima temporizada I > (07-17-04), falta de fase en trifásico (07-17-12).
- Esta parte **no** trae un símbolo armado para el "interruptor diferencial" de vivienda ni para la "termomagnética". No inventarlos: usar 07-13-05 y la magnitud Id según la norma, o la parte de la IRAM que corresponda.

## Protección (secciones 21 y 22, págs. 24-25)
- **07-21-01:** **fusible**, símbolo general (rectángulo chico atravesado por la línea).
- 07-21-02: lado del fusible que queda con tensión, con trazo grueso.
- 07-21-03 a 07-21-05: fusible con percutor, con o sin contacto de señal.
- 07-21-06: interruptor tripolar que abre al fundir cualquier fusible con percutor.
- **07-21-07:** interruptor-fusible. **07-21-08:** seccionador-fusible. **07-21-09:** seccionador bajo carga-fusible.
- **07-22-03:** **descargador** (rectángulo con flecha). 07-22-01 y 07-22-02: explosores.

## Otros
- Sensores de proximidad y roce: secciones 19 y 20 (págs. 22-23).
- Anexo A: símbolos anteriores todavía en uso (págs. 26-30).

## Uso en EGC
- Unifilar del planificador: interruptor general, seccionador, fusible y contactor con estos símbolos y su número.
- Posteos de comandos (contactor, pulsadores, arranque estrella-triángulo): usar estos símbolos.
- Antes de dibujar un diferencial o una termomagnética como símbolo único, verificar en la IRAM vigente.
- Vigencia: es la edición 1988. IEC 617 fue reemplazada por IEC 60617. Verificar en iram.org.ar si hay edición nueva antes de citarla como vigente.
