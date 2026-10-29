# 33 · Tierra lejana: radio equivalente de jabalinas (Tabla 771.3.II)

Fuente: Editores SRL, "Protocolo de medición de puesta a tierra. Guía interpretación de la Resolución SRT 900/2015" (editores-srl.com.ar). Reproduce la Tabla 771.3.II y la expresión del radio equivalente de la AEA 90364-7-771.
Tipo de fuente: **SECUNDARIA** que cita la norma. La ficha 06 (AEA 770) **manda** en vivienda.
Redacción propia. Tabla y fórmula verificadas a la vista en las imágenes de la guía.

## Concepto (guía, sección "Toma de tierra lejana o independiente")
- En esquema TT, la toma de protección (Ra) debe ser **tierra lejana** respecto de la toma de servicio (Rb).
- Tierra lejana (VEI 195-02-02): su potencial no cambia en forma apreciable por las corrientes de otros electrodos.
- Distancia mínima, medida en cualquier dirección: **más de 10 veces el radio equivalente (Re)** de la jabalina más larga.
- Re indica la zona de influencia del electrodo. Depende de su forma y medidas.
- Si hay varios electrodos de protección, se unen entre sí y a la barra principal de tierra.

## Radio equivalente de una jabalina cilíndrica
Re ≈ l / ln(l / d)
- Re: radio equivalente (m). l: longitud de la jabalina (m). d: diámetro (m).
- Es una expresión aproximada.

## Tabla 771.3.II · Jabalinas IRAM 2309 y 2310

| Designación | Diámetro exterior (mm) | Longitud (m) | 10·Re (m) |
|---|---|---|---|
| 1/2" | 12,6 | 1,5 | 3,2 |
| 1/2" | 12,6 | 2,0 | 4,0 |
| 1/2" | 12,6 | 3,0 | 5,4 |
| 1/2" | 12,6 | 4,5 | 7,6 |
| 1/2" | 12,6 | 6,0 | 9,8 |
| 5/8" | 14,6 | 1,5 | 3,2 |
| 5/8" | 14,6 | 2,0 | 4,0 |
| 5/8" | 14,6 | 3,0 | 5,6 |
| 5/8" | 14,6 | 4,5 | 7,8 |
| 5/8" | 14,6 | 6,0 | 10,0 |
| 3/4" | 16,2 | 1,5 | 3,4 |
| 3/4" | 16,2 | 2,0 | 4,2 |
| 3/4" | 16,2 | 3,0 | 5,8 |
| 3/4" | 16,2 | 4,5 | 8,0 |
| 3/4" | 16,2 | 6,0 | 10,2 |

- Verificación 1: los 15 valores coinciden con una copia escaneada de la Tabla 771.3.II de la norma original.
- Verificación 2: la fórmula reproduce los 15 valores con diferencia ≤ 0,1 m.
- Coincide con los ejemplos de la Tabla 770.3.I de la ficha 06 (1,5 m → 3,2 a 3,4 m; 3 m → 5,4 a 5,8 m).

## No usar
- Una versión que circula con longitud **4,0 m**: la tabla correcta usa **4,5 m**.
- La fórmula Re = l / ln(4·l / d): no reproduce la tabla.
- La afirmación "si la distancia es menor a 10·Re, el esquema pasa de TT a TN-S": no figura en la fuente. No afirmarla.

## Otros datos de la guía (SRT 900/2015)
- La medición de PAT y continuidad de masas tiene validez de **12 meses** (Art. 2°).
- Lazo de falla en TT, ejemplo de la guía: Rb = 1 Ω, Ra = 10 Ω → Id = 220 / 11 = 20 A, tensión de contacto ≈ 200 V. Una termomagnética no dispara con esa corriente. Por eso en TT la única protección válida contra contactos indirectos es el diferencial.
- Ensayos del diferencial (IEC 61008, instrumento IEC 61557-6): 0,5·IΔn no dispara; 1·IΔn ≤ 300 ms; 2·IΔn ≤ 150 ms; 5·IΔn ≤ 40 ms.
- Continuidad de masas: instrumento IEC 61557-4, ≥ 200 mA, tensión en vacío de 4 a 24 V.

## Uso en el simulador de EGC
- Etapa tierra lejana: el usuario elige diámetro y largo de la jabalina y mueve la distancia a la toma de servicio.
- El simulador marca en verde la distancia mayor a 10·Re y en rojo la menor.
- Mostrar la Tabla 771.3.II y la fórmula como dato.
