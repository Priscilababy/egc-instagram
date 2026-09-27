# 14 · AEA 90364-7-771: oficinas, locales y circuitos de uso específico

Fuente: AEA 90364-7-771, edición marzo de 2006 (en adelante "la 771"). Páginas: las **impresas** en el encabezado ("Página N"). El ejemplar es de uso exclusivo: no subirlo al repo.

## Cuándo se usa la 771 y cuándo la 770
- La 771 cubre **vivienda, oficina y local individuales** ("unitarios"), sin tope de corriente, desde los bornes de entrada del tablero principal (771.1, pág. 7; 771.4.1, pág. 17).
- Es **anterior** a la 770 (2017) y no la menciona. El texto no dice si la AEA la reemplazó en parte.
- Criterio de esta biblioteca:
  - **Vivienda dentro del alcance de la 770** (hasta 63 A y 10 kA): manda la **770**. La 771 se usa solo donde la 770 remite: circuitos de uso específico (ACU, APM, etc.) → ficha 01.
  - **Oficinas, locales y viviendas fuera del alcance de la 770:** manda la 771.
- En un post sobre viviendas, no citar la 771 para algo que la 770 ya regula distinto.

## Tipos de circuito (771.7.6, págs. 21-25; Tabla 771.7.I, pág. 25)

| Sigla | Qué alimenta | Bocas máx. | Protección máx. | Sección mín. |
|---|---|---|---|---|
| IUG | Iluminación y cargas ≤ 10 A | 15 | 16 A | 1,5 mm² |
| TUG | Tomas 2P+T 10 A (cargas ≤ 10 A) | 15 | 20 A | 2,5 mm² |
| IUE | Solo luminarias; obligatorio para iluminación a la intemperie | 12 | 32 A | 2,5 mm² |
| TUE | Cargas **hasta 20 A** con toma 2P+T 20 A IRAM 2071; obligatorio para tomas a la intemperie | 12 | 32 A | 2,5 mm² |
| APM | Pequeños motores monofásicos (ventilación, portones, cortinas) | 15, ≤ 10 A por boca | 25 A | 2,5 mm² |
| **ACU** | **Una sola carga**, mono o trifásica, **sin ninguna derivación** | — | la fija el proyectista | 2,5 mm² |
| MBTF | Alimentación en 220 V de fuentes MBTF (porteros, alarmas, CCTV) | 15, ≤ 10 A por boca | 20 A | 1,5 mm² |
| ATE | Tensión estabilizada / UPS (tomas rojas o con logo) | 15 | proyectista | 2,5 mm² |
| ITE | Iluminación trifásica (solo oficinas y locales con personal BA4/BA5) | 12 por fase | proyectista | 2,5 mm² |
| OCE | Cualquier otra carga específica | sin límite | proyectista | 2,5 mm² |

- Los de uso general y especial son siempre **monofásicos**. Los de uso específico pueden ser mono o trifásicos (771.7.6).
- Los circuitos de uso específico son **adicionales**: no cuentan para el mínimo de circuitos del grado (771.7.6 c, pág. 23).
- Ejemplos de uso específico que da la norma: fuentes de MBT, **unidades condensadoras de climatización central**, bombas elevadoras de agua (771.7.6 c, pág. 23).
- La protección máxima de la tabla no reemplaza la regla IB ≤ In ≤ Iz: un 2,5 mm² en caño admite 21 A (ficha 04), así que no lleva térmica de 32 A.

## Grados de electrificación en viviendas (Tabla 771.8.I, pág. 27; Tabla 771.8.II, pág. 28)
- Mínimo ≤ 60 m² y ≤ 3,7 kVA · medio hasta 130 m² y ≤ 7 kVA · elevado hasta 200 m² y ≤ 11 kVA · superior más de 200 m² o más de 11 kVA.
- Superficie = cubierta + 50 % de la semicubierta (771.8.1.5, pág. 26).
- Circuitos mínimos: mínimo 2 · medio 3 · elevado 5 (**2 IUG + 2 TUG + 1 TUE**) · superior 6 (se suma uno de libre elección).
- En grado elevado o superior, living o dormitorio de **más de 36 m²** llevan una boca TUE. Si es para un equipo de aire acondicionado, la boca **puede quedar fuera del ambiente**, en las paredes exteriores a él, según lo que necesite la carga (771.8.2.3.3, pág. 29).

## Oficinas y locales (771.8.3.2, págs. 31-34)
- Grados: mínimo ≤ 30 m² · medio hasta 75 m² · elevado hasta 150 m² · superior más de 150 m² (Tabla 771.8.IV, pág. 32).
- Salón general: 1 IUG y 1 TUG cada 9 m² (Tabla 771.8.VI, pág. 34).
- Oficinas o locales en edificios proyectados como vivienda: se usan las tablas de vivienda (771.8.3.1, pág. 31).

## Demanda (771.9, págs. 45-46)
- Valores mínimos por circuito (Tabla 771.9.I, pág. 45): TUG 2200 VA · TUE 3300 VA · IUG en vivienda 66 % de (bocas × 150 VA).
- Simultaneidad por grado (Tabla 771.9.II): 1 · 0,9 · 0,8 · 0,7.
- Los circuitos de uso específico se suman aparte (771.9.2).
- En edificios de oficinas o locales la simultaneidad puede ser **cercana a 1** por el aire acondicionado (771.9.4.2, pág. 46).
- Más de 7 kVA o 32 A en monofásico: **recomendable** pedir trifásico (771.9.3.3, pág. 46).

## Diferencias con la 770 que conviene conocer
| Tema | 770 (ficha) | 771 |
|---|---|---|
| Alimentación de llaves y retornos | 1 mm² (ficha 04) | 1,5 mm² (Tabla 771.13.I, pág. 89) |
| Bocas máximas del TUE | 15 | 12 (Tabla 771.7.I) |
| Caída de tensión en seccionales | 1 % recomendado | 1 % **máximo** (771.13 b, pág. 89) |
| Altura de tomas sobre zócalo | 0,20-0,30 m | ≥ 0,15 m (771.8.6.2, pág. 44) |
| Reserva de cable en cajas | 0,1 m | 150 mm (771.12.3.13.1, pág. 81) |
| Fusibles | — | prohibidos en viviendas y oficinas (771.20.5.2, pág. 160) |
| Un cable por borne | obligatorio | recomendado (771.20.4, pág. 149) |

## Datos que la 770 no trae
- **Cable al sol:** factor de corrección adicional **0,85** (771.16.2.3.2, pág. 101).
- **Temperatura distinta de 40 °C** (PVC, Tabla 771.16.II.a, pág. 95): 30 °C × 1,15 · 35 °C × 1,08 · 45 °C × 0,91 · 50 °C × 0,82.
- No se puede calcular un cable con menos temperatura porque el local tenga aire acondicionado: el equipo puede fallar (771.16.2.1.5, nota 1, pág. 93).
- **Cables IRAM 2178 / 62266** en caño (método B2, Tabla 771.16.III, pág. 96): 1,5 → 14 A · 2,5 → 20 A · 4 → 26 A · 6 → 33 A · 10 → 45 A.
- **Fórmula rápida de caída de tensión** (771.19.7 c, pág. 142): ΔU = GDC × I × L / S, con L en metros y S en mm². GDC cobre, cos φ 0,8: **0,040** monofásico · **0,035** trifásico.
- **Llaves junto a puertas** (771.8.6.1, pág. 44): centro de la caja entre 0,9 y 1,3 m (recomendado 1,10 m), a ≤ 0,15 m del marco, del lado del cerradero.
- **Motores de menos de 0,75 kW:** la protección de sobrecarga dedicada no es exigible, solo recomendable (771.17.3.1, pág. 116).
- **Equipotencialización principal:** incluye los conductos de aire acondicionado y calefacción (771.18.5.8.1 f, pág. 130).
- **Periodicidad de inspección:** 5 años como máximo (771.23.4.3, pág. 164). Igual criterio que la 770.

## Diferencial en la 771 (771.18.3.5, pág. 123)
- 30 mA obligatorio en IUG, IUE, TUG, TUE, MBTF, ATE, APM, **ACU**, ITE y OCE.
- Única excepción: un **ACU** donde se demuestre que el diferencial perturba el equipo (ejemplo de la norma: arranque estrella-triángulo de motores medianos y grandes), con protección alternativa contra contactos directos e indirectos. Criterio EGC (no de la norma): un split domiciliario no entra en esa excepción.
- La opción de diferencial de hasta 300 mA para ACU es solo para locales con personal BA4/BA5; **excluye viviendas y oficinas** (771.18.4.3 b.2, pág. 126).
