# 31 · AEA 771 Anexo C: electrodos, resistividad y cálculo de puesta a tierra

Fuente: AEA 90364-7-771, edición 2006, Anexo 771-C (Reglamentario), págs. 187-199.
Relación con otras fichas: en **vivienda manda la ficha 06** (AEA 90364-7-770, 2017). Esta ficha aporta datos de cálculo y materiales. Reemplaza a la ficha 23 en resistividades y fórmula de la jabalina, porque es fuente **primaria**.
Redacción propia. No es copia textual de la norma.

## Objetivos de la puesta a tierra (771-C.1.1, pág. 187)
- Une las masas con uno o más electrodos enterrados, sin fusible ni protección intermedia.
- Su resistencia debe cumplir las condiciones de protección de la instalación.
- Funciones: derivar a tierra corrientes de falla, de rayos y de contacto con tensiones mayores.
- Ayuda a que actúen fusibles, termomagnéticas y diferenciales ante una falla a tierra.
- Limita diferencias de tensión entre masas y tierra.
- Si coexisten tierra de protección y tierra funcional, la de protección tiene prioridad (771-C.2.1.1).

## Electrodos admitidos y medidas mínimas (771-C.2.2.1, pág. 188)
Tipos: jabalinas o tubos; pletinas, cintas o cables; placas; electrodos en cimientos.
La resistencia se verifica **por medición** al terminar la obra.

Acero galvanizado en caliente (cinc ≥ 70 µm):
- Jabalina redonda IRAM 2310: diámetro ≥ 12,6 mm. Mínimo **JL16 × 1500 mm**.
- Fleje o pletina: 100 mm², 3 mm de espesor. Solo enterrado, no hincado.
- Barra redonda: diámetro ≥ 10 mm. Solo enterrada, no hincada.
- Caño pesado: diámetro ≥ 25 mm, espesor ≥ 2 mm.
- Jabalina perfil L IRAM 2316 (JPNL 50 × 1500) y perfil X IRAM 2317 (JPNC 50 × 1500).

Cobre:
- Cable: **35 mm²**, alambre ≥ 1,8 mm, IRAM 2004.
- Fleje o pletina: 50 mm², 2 mm de espesor.
- Barra redonda: 35 mm² (6,7 mm de diámetro).
- Caño: diámetro ≥ 20 mm, espesor 2 mm, IRAM 2568.

Acero-cobre:
- Jabalina redonda IRAM 2309: diámetro ≥ 12,6 mm (124 mm²). Mínimo **JL14 × 1500 mm**.
- Cable: 35 mm², IRAM 2467.
- Barra redonda: 50 mm² (8 mm de diámetro), IRAM 2466.

En obra nueva se admite un conductor desnudo en el fondo de la zanja de cimientos, recorriendo el perímetro (pág. 189).

## Condiciones de diseño (771-C.2.2.2 a 771-C.2.2.4, pág. 189)
- Elegir tipo y profundidad considerando sequía y congelamiento del suelo.
- Cuidar la corrosión electrolítica al mezclar metales distintos.
- Prever el aumento de resistencia por corrosión. Medir en forma periódica (771.23.5.2).
- Caños de agua, gas, calefacción y vainas de cables **no** son electrodos. Igual se unen a la BEP (Nota 1).

## Jabalinas en paralelo (Nota 2, pág. 189)
- Separación recomendada: **≥ 2 veces el largo** de la jabalina más larga.
- El conjunto da **más** resistencia que el cálculo teórico en paralelo. La diferencia crece con la cantidad de jabalinas.
- Aumento esperado sobre el valor teórico, jabalinas de 3 m:

| Configuración | Separación | Aumento |
|---|---|---|
| 2 jabalinas | 6 m (2 × L) | ~7 % |
| 2 jabalinas | 15 m (5 × L) | ~3 % |
| 4 jabalinas en cuadrado | 6 m | ~20 % |
| 4 jabalinas en cuadrado | 15 m | ~8 % |

- Unir las jabalinas con conductor desnudo enterrado baja la resistencia total.
- Las uniones entre electrodo, cable de PAT e interconexiones van en cámara de inspección.

## Conductor de puesta a tierra enterrado (Tabla 771-C.I, pág. 189)
| | Con protección mecánica | Sin protección mecánica |
|---|---|---|
| Con protección contra corrosión | 2,5 mm² Cu · 10 mm² Fe | 16 mm² Cu · 16 mm² Fe |
| Sin protección contra corrosión | 25 mm² Cu · 50 mm² Fe | 25 mm² Cu · 50 mm² Fe |

- **En vivienda no usar el 2,5 mm²:** la ficha 06 fija cable de PAT mínimo 4 mm².

## Unión cable-electrodo (771-C.2.3.2, pág. 190)
- Admitidas: soldadura exotérmica (cuproaluminotérmica), conector a presión, morsa u otro conector mecánico.
- La morsa no debe dañar electrodo ni conductor.
- **Prohibida** la soldadura con estaño.

## Barras y medición (771-C.2.4, pág. 190)
- **BEP**: recibe cables de PAT, PE, equipotenciales principales y tierra funcional.
- **Barra principal de tierra**: la del tablero general. Puede coincidir con la BEP. De ella salen todos los PE.
- Cada conductor se desconecta en forma individual y solo con herramienta.
- Se mide cada electrodo por separado y el sistema completo.
- Cada toma lleva cámara de inspección con **barra de medición de cobre ≥ 30 × 3 × 100 mm**, con al menos 5 perforaciones.

## Resistividad del terreno (771-C.9.1, págs. 196)
Tabla 771-C.VIII, valores en Ω·m:

| Tipo de suelo | Más probable | Lluvias > 500 mm/año | Lluvias < 500 mm/año | Agua subterránea salina |
|---|---|---|---|---|
| Aluvial y arcillas livianas | 5 | según napa | según napa | 1 a 5 |
| Arcillas (no aluvial) | 10 | 5 a 20 | 10 a 100 | 3 a 10 |
| Greda | 20 | 10 a 20 | 50 a 300 | 3 a 10 |
| Tierra calcárea porosa | 50 | 30 a 100 | 50 a 300 | 3 a 10 |
| Arenisca porosa | 100 | 30 a 300 | > 1000 | 10 a 30 |
| Cuarzo y caliza compacta | 300 | 100 a 1000 | > 1000 | 30 a 100 |
| Pizarras arcillosas y esquistos | 1000 | 300 a 3000 | > 1000 | 30 a 100 |
| Granito | 1000 | 300 a 3000 | > 1000 | 30 a 100 |
| Pizarras rajadizas, rocas ígneas | 2000 | > 1000 | > 1000 | 30 a 100 |

Tabla 771-C.IX, valores en Ω·m:

| Tipo de suelo | Resistividad |
|---|---|
| Pantanoso | 1 a 30 |
| Limo | 20 a 100 |
| Humus | 10 a 150 |
| Turba húmeda | 5 a 100 |

Son valores **orientativos**. Lo que vale es la medición final (≤ 40 Ω en vivienda → ficha 06).

## Factores que cambian la resistividad (771-C.9.2 a 771-C.9.6, págs. 196-198)
- **Humedad y sales:** más humedad y más sales → menos resistividad.
- Preferir suelo arcilloso a arenoso: retiene más agua.
- Alejar los electrodos de árboles y plantas.
- Exceso de agua corriente (cauces) lava las sales y sube la resistividad.
- **Mejoradores:** sal en canaleta alrededor del electrodo (repetir cada ~2 años); gel (cada ~6 años); electrolito de sulfato cálcico estabilizado (10 a 15 años).
- **Estratos:** si no se conoce el suelo, medir la resistividad hasta la profundidad del electrodo. No extrapolar la medición superficial.
- **Compactación:** compactar alrededor del electrodo con tierra fina y agua lenta.
- **Temperatura:** a menor temperatura, más resistividad. Bajo 0 °C sube muy rápido. En zonas con heladas, enterrar más profundo.
- **Estacionalidad:** medir en la época más desfavorable: frío y sequía.
- **Corriente de falla alta:** calienta el suelo, evapora agua y sube la resistencia.

## Resistencia de una jabalina vertical (771-C.10.1, pág. 198)
R = ρ / (2·π·L) × [ln(8·L / d) − 1]
- L: largo enterrado (m). d: diámetro (m). ρ: resistividad (Ω·m).
- **Verificado a la vista en el original:** el "−1" va fuera del logaritmo.

Simplificaciones de la norma:

| Relación L/d | Resistencia aproximada | Ejemplo |
|---|---|---|
| 25 a 100 | R ≈ 0,75 · ρ / L | 16 o 19 mm × 1500 mm |
| 100 a 600 | R ≈ ρ / L | 16 o 19 mm × 2000 mm |
| 600 a 3000 | R ≈ 1,2 · ρ / L | — |

- Corrige la ficha 23: el autor escribió ln(8L/d − 1). Eso explica la diferencia de 13 a 15 % que marcaba la ficha.

## Conductor desnudo horizontal (771-C.10.2, págs. 198-199)
- Parámetros: largo L, profundidad h y diámetro d.
- Fórmula completa, forma correcta: R = ρ / (2·π·L) × [ln(4·L/d) + ln(L/h) − 2 + 2·h/L − h²/L² + h⁴/(2·L⁴) + …]
- **Errata en el original:** la norma imprime h²/L y h⁴/(2·L), sin exponente en el denominador. Así escritos tienen unidad de metro y no se pueden sumar al resto. La forma correcta (L² y L⁴) coincide con la fórmula de Dwight pasada a largo L, profundidad h y diámetro d.
- Comprobación: cable de 35 mm², L = 45 m, h = 0,8 m → R ≈ 0,043·ρ. La simplificación da 0,044·ρ. Coinciden.
- Los dos últimos términos pesan menos de 0,1 % en casos de obra.
- Verificado a la vista en el original (captura de la pág. 198).
- Simplificación: **R ≈ 2 · ρ / L** para cable de 35 mm² y L ≈ 45 m, 50 mm² y L ≈ 50 m, o 70 mm² y L ≈ 70 m.

## Placa circular vertical (771-C.10.3, pág. 199)
R = ρ / (2·D) × [1/2 + (1/4π)·(D/h) + (7/384)·(D/h)³ + (99/81920)·(D/h)⁵ + …]
- D: diámetro de la placa. h: profundidad del centro de la placa.

## Uso en el simulador de EGC
- Etapa resistividad: usar Tablas 771-C.VIII y 771-C.IX.
- Etapa jabalina: usar la fórmula 771-C.10.1 y mostrar las simplificaciones.
- Etapa paralelo: usar separación ≥ 2·L y los aumentos de la Nota 2.
- Mostrar siempre el límite de vivienda: **≤ 40 Ω** (ficha 06).
