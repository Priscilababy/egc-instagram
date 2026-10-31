# 35 · Red de BT en TN con neutro múltiplemente a tierra: factor F y tensión de contacto

Fuente: Semerdjian, J. R. "Análisis del factor F de incremento del potencial de tierra en redes de BT con gestión de neutro TN múltiplemente conectado a tierra". AEA, versión 1.0, agosto 2023, 8 págs. https://aea.org.ar/pdfviewer/estudio-factor-f/
Tipo de fuente: **SECUNDARIA** (estudio técnico publicado por la AEA; no es reglamentación). Trata la **red de la distribuidora**, no la instalación de la vivienda. Para la vivienda mandan las fichas 06, 23, 31 y 33.
Redacción propia. No es copia textual del documento.

## De qué trata (págs. 2-3)
- Redes de BT de distribución con gestión de neutro **TN** y neutro conectado a tierra en muchos puntos: electrodo profundo en el centro de transformación (CT) y jabalinas de refuerzo a lo largo del recorrido.
- Busca verificar que, ante una falla a tierra, la tensión de contacto no supere los límites de las normas.
- Referencia: EN 50522:2022 (puesta a tierra en instalaciones de más de 1 kV), Tabla 2.

## Definiciones (págs. 3-4)
- **UE**, incremento del potencial de tierra: UE = IE × ZE. IE = corriente de falla drenada a tierra; ZE = impedancia del sistema de puesta a tierra.
- **UTp**, tensión de contacto admisible: **85 V** para fallas despejadas en **≤ 5 s** (EN 50522, tabla B.4).
- Condición en TN: **UE ≤ F × UTp**.
- **F**: factor por conexiones adicionales del PEN a tierra. La EN 50522 dice: típico 2; hasta 5 según suelo y conexiones; F = 1 si el neutro o PEN de BT solo está conectado a la tierra de AT.
- En TT y en IT con PE no distribuido, la condición de tensión de contacto de esa tabla **no se aplica**. En todos los esquemas: UE ≤ 1.200 V (falla ≤ 5 s) y UE ≤ 250 V (falla > 5 s), como tensión de esfuerzo.

## Valores de F que propone el estudio (págs. 4-5)
| F | Cuándo |
|---|---|
| → ∞ | La red forma parte de un **sistema de puesta a tierra global** (EN 50522, 5.4.2, directriz C1; Anexo N): centro de ciudad o zona densamente construida, edificios con tierras de cimientos interconectadas, muchos electrodos unidos por PEN o vainas, varias subestaciones cercanas. |
| 2 | No se cumple lo anterior. Valor por defecto. |
| 4 | Se aplican las medidas M del Anexo E de la EN 50522. **El estudio no lo recomienda** para BT: medidas pensadas para subestaciones AT/MT. |
| 5 | Red TN con electrodo profundo en el CT y jabalinas de refuerzo a lo largo del neutro. |

## Método de verificación UT ≤ UTp (págs. 5-7)
- Supone que **toda** la corriente de falla vuelve por el neutro, sin factor de reducción (caso más exigente).
- Datos: **Ik1"** (cortocircuito monofásico según AEA-IEC 60909-0; tiene que despejar en ≤ 5 s), **RPAT** (resistencia de puesta a tierra del neutro de la red: electrodo del CT en paralelo con las jabalinas de refuerzo) y **ρS** (resistividad de la superficie de apoyo, Ω·m).
- Fórmula de la tensión de contacto:
  UT = Ik1" × ZTMP / [1 + (ZTMP + RF1 + RF2) / RPAT] ≤ 85 V
- **ZTMP** (cuerpo, mano izquierda–ambos pies) = ZT(UT) × BF / HF = 1.225 Ω × 0,75 / 1 = **918,75 Ω**.
  - ZT(225 V) = 1.225 Ω: valor no superado por el 50 % de la población (AEA 90479-1, tabla 1).
  - BF = 0,75 (AEA 90479-1, figura 3). HF = 1 (AEA 90479-1, tabla 12), caso más desfavorable.
- **RF1** (calzado gastado y húmedo) = **1.000 Ω** (EN 50522, B.4).
- **RF2** (superficie de apoyo) = **1,5 × ρS**.
- Forma final: UT = Ik1" × 918,75 / [1 + (1.918,75 + 1,5·ρS) / RPAT] ≤ 85 V.
- La fórmula de RPAT (ec. 5) combina RCT y las RADi en paralelo. Su forma exacta no se pudo leer bien en el PDF: **no usarla** sin verificar en la fuente.

## Ejemplo de cálculo propio de EGC (no está en la fuente)
Ik1" = 1.000 A, ρS = 100 Ω·m:
| RPAT | UE | UT | Cumple 85 V |
|---|---|---|---|
| 2 Ω | 2.000 V | ≈ 887 V | No |
| 1 Ω | 1.000 V | ≈ 444 V | No |
| 0,5 Ω | 500 V | ≈ 222 V | No |
| ≤ 0,19 Ω | ≤ 190 V | ≤ 85 V | Sí |
- Con ρS = 1.000 Ω·m alcanza RPAT ≤ 0,32 Ω; con 3.000 Ω·m, RPAT ≤ 0,59 Ω.
- UT ≈ 44 % de UE con ρS = 100 Ω·m: el calzado y el piso se llevan el resto. Es la idea detrás de F > 1.
- Marcar siempre como **ejemplo ilustrativo**, no como cálculo de una red real.

## Bibliografía que cita la fuente (pág. 8)
- AEA 90479-1:2020, efectos de la corriente sobre el cuerpo humano. **No está en esta biblioteca.**
- UNE-EN 50522:2022. **No está en esta biblioteca.**

## Uso en contenidos de EGC (deducción a partir de fichas 06 y 33)
- Mensaje para electricistas: el neutro de la red está a tierra en muchos puntos, pero **durante una falla puede subir de potencial**. No es una tierra de protección.
- En la vivienda: esquema **TT**, toma de protección propia e independiente de la tierra de servicio, a más de 10·Re (ficha 33), ≤ 40 Ω (ficha 06, AEA 770 ed. 2017), PE verde-amarillo ≥ 2,5 mm², cable de PAT ≥ 4 mm², diferencial 30 mA.
- **Nunca** puentear PE con neutro en tomas o tableros.
- No afirmar que la AEA "obliga" a usar F = 2 o F = 5: es una propuesta de un estudio técnico, no reglamentación.
- La fuente no da valores de Ik1" ni de RPAT de redes reales argentinas: no inventarlos.

## Publicado con esta ficha
- Nota del blog "El neutro de la calle no es tu tierra" y placa de Instagram EGC-neutro-no-es-tierra.png.
