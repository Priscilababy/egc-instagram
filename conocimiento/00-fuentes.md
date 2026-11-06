# 00 · Fuentes leídas

Estado: **PRIMARIA** = texto oficial, se puede usar. **SECUNDARIA** = apunte o nota; usar solo si coincide con una primaria. **NO USAR** = de otro país, desactualizada o con errores.

## Lote 1 (recibido el 2026-09-24)

| Documento | Estado | Notas |
|---|---|---|
| AEA 90364-7-770, edición 2017 (viviendas unifamiliares hasta 63 A) | **PRIMARIA** | Leída completa (91 págs.). Es la base de las fichas 01 a 12. Las páginas citadas son las **impresas** en el encabezado ("Página N"). El ejemplar es de uso exclusivo: no subirlo al repo. |
| Resolución ERSeP 164/2020 (Córdoba) | **PRIMARIA** | Solo sirve para el marco de habilitación en Córdoba (ficha 13). Contiene nombres y DNI de personas: **no copiar nada de ese listado**. |
| Nota EGC "AEA 95101 edición 2015 · instalaciones subterráneas" (docx) | SECUNDARIA | Nota propia de EGC; dice haberse verificado contra el ejemplar impreso de la AEA 95101 ed. 2015, salvo el capítulo de alcance. Es para **vía pública** (redes de distribución), no para el interior de una vivienda. |
| "Guía técnica de aplicación de la norma AEA 95101" (PDF, 8 págs.) | **NO USAR** | Sin autor. Mezcla valores de la edición 2007 ya reemplazados (franjas 0,4–1,2 m, caños 1,5d / 2,5d / 3d, neutro 5 Ω cada 200 m). Contradice a la nota EGC anterior. |
| "Intensidad admisible en cables y conductores" (docx) | **NO USAR** como fuente | Apunte de una charla. Tiene errores frente a la AEA 770: dice que el PE es igual a la fase hasta 35 mm² (la Tabla 770.14.I dice igual hasta 16 mm², 16 mm² entre 16 y 35, S/2 arriba de 35); dice que un 2,5 mm² "va con 16 A y no con 20 A" (la 770 admite 20 A en TUG con 2,5 mm², porque 21 A ≥ 20 A); ubica la cinta de advertencia a 20 cm del cable (la 770 la pone a 0,2 m de la superficie); cita "IRAM 2183 / 2473" para el unipolar (hoy es IRAM NM 247-3). Lo que sí coincide con la 770: 40 °C de referencia, 25 °C en suelo, factores 0,80 y 0,70 por agrupamiento, regla de 3 circuitos / 36 A / 15 bocas. |
| "Electricidad domiciliaria" (PDF, 57 págs., contecpe.com.pe) | **NO USAR** | Es de **Perú**. Colores distintos a los argentinos (fase roja/negra/azul, neutro blanco, tierra verde), calibres AWG y alambre macizo. Todo eso es incorrecto en Argentina. |
| "La instalación eléctrica de la vivienda" (PDF, 16 págs.) | **NO USAR** | Es de **España** (REBT: ICP, circuitos C1–C12, 230 V, neutro azul). No aplica en Argentina. |
| "Cálculo de alimentadores en media tensión" (PDF escaneado) | Fuera de ámbito | Media tensión; no es tema de instalaciones domiciliarias. No se procesó (es imagen, sin texto). |

## Lote 2 · aire acondicionado y reglamentación complementaria (recibido el 2026-09-27)

Códigos usados en las fichas 14 a 22 entre paréntesis.

| Documento | Estado | Notas |
|---|---|---|
| (771) AEA 90364-7-771, edición marzo 2006 (viviendas, oficinas y locales unitarios) | **PRIMARIA** | Leída completa (258 págs. impresas). Base de la ficha 14 y de la parte normativa de la 18. Páginas citadas: las **impresas**. Es anterior a la 770: en viviendas dentro del alcance de la 770, manda la 770. Uso exclusivo: no subir el PDF al repo. |
| (R1640) Resolución SAyDS 1640/2012, texto actualizado | **PRIMARIA** | Prohibición de equipos domésticos nuevos con R-22. Arts. 10 a 12 derogados por Res. 15/2024 (Min. Interior). Ficha 19. |
| (F1) Manual de instalación de split pared, frío solo y frío-calor, 09 a 22 mil BTU/h (marca Midea) | SECUNDARIA (fabricante) | Muy completo: distancias, tabla de cañerías, torques, vacío, checklist. Erratas: vacío "−105 Pa" (es ≈ −10⁵ Pa), tabla de torque con N·cm y N·m mezclados, tierra "menor a 4" sin unidad. |
| (F2) Manual de instalación y usuario de multisplit inverter (marca Midea, importa Carrier) | SECUNDARIA (fabricante) | Repite casi todo F1; agrega multisplit y mantenimiento de usuario. Se contradice en la frecuencia del filtro (2 semanas / 3 meses) y en tablas de sección de cable. |
| (F3) Manual de instalación de split frío solo 18 y 22 mil BTU/h, R-22, enero 2006 (marca Carrier) | SECUNDARIA (fabricante, **equipo de R-22, histórico**) | Torques de 1/2" y 5/8" muy superiores a los demás. Largo máximo 15 m en el texto y 20-25 m en su tabla. Fusible máximo 16 A con un modelo de 18 A. |
| (F4) Manual de instalación de multisplit de 2 interiores, agosto 2009 (marca Surrey) | SECUNDARIA (fabricante) | Largo máximo 10 m. Equivalencia de torque en kgf·cm que no cierra; separación trasera de la exterior de solo 4,5 cm en una figura. |
| (BP) "Buenas prácticas en los procesos de instalación y mantenimiento de sistemas de refrigeración y aire acondicionado", Barletta (ONU Ambiente) y Acevedo (ONUDI), MPCEIP Ecuador, 2021 | SECUNDARIA (**confiabilidad alta**) | Documento del programa del Protocolo de Montreal. Base de vacío, nitrógeno, recuperación, refrigerantes y diagnóstico. **No** copiar sus conversiones de unidades (tiene errores en pág. 35 y 74). Sus valores de sobrecalentamiento y subenfriamiento son de refrigeración con válvula termostática, no de split. Cita normas de EE. UU. (DOT, EPA) como referencia, no como norma argentina. |
| (MB) "Manual básico de sistemas de aire acondicionado y extracción mecánica de uso común en arquitectura", Colocho, Daza y Guzmán, Univ. Dr. José Matías Delgado, El Salvador, 2011 | SECUNDARIA (**confiabilidad baja**) | Trabajo de seminario de arquitectura. Sirve para conceptos, ubicación y extracción. **Errores:** dice que la condensadora produce el agua, que R-410A y R-407C "no tienen retirada", fechas europeas del R-22. Tensiones de 110-480 V a 60 Hz: **no aplican** en Argentina. Su fórmula de carga térmica es solo orientativa. |
| (P1) Pliego DGCyE Prov. de Buenos Aires, Región 10, "Instalación de equipos split inverter", General Rodríguez, 2022 (Expte. 4050-236643) | SECUNDARIA | Útil por la **estructura de ítems** de sus 9 cómputos. No usar sus valores eléctricos como regla: erratas ("Dec. 351/96", "IEC 898") y admite retorcer cables de más de 4 mm² (la 770 no). |
| (P2) PETP UNL "Instalaciones eléctricas para aires acondicionados · Aulas", Santa Fe, 2025 | SECUNDARIA | Preinstalación de splits: toma 20 A, condensado PVC Ø 40, caño camisa Ø 60. **NO USAR su tabla de sección de PE** (queda por debajo de la 770). Erratas de normas ("IRAM 62667", "7500 V"). |
| (P3) Anexo VI "Distribución de energía eléctrica", Tribunal Electoral de Santa Fe (sin fecha) | SECUNDARIA | Línea de AA exclusiva y protección por equipo, rotulado, garantía de 12 meses. **No pone diferencial** en la línea de AA: no replicar (la norma lo exige). |
| Anexo VII "Manual de normas y procedimientos de instalación" (redes informáticas en escuelas, DGCyE) | Fuera de ámbito | Cita la "AEA 90365", que no existe. Pide tomas Schuko. Nada de aire acondicionado. |
| Ordenanza 3419/83 de Rosario (reglamento de instalaciones eléctricas interiores) | **NO USAR** (técnicamente) | Texto de 1983, incompleto (remite a un reglamento que no transcribe). Sigue publicado en rosario.gob.ar; no se encontró norma que lo derogue. Superado por la AEA: retorno **negro**, fase roja, neutro azul, tierra con cable desnudo, 15 A para 2,5 mm². Solo sirve como dato histórico. |
| Nota web "Tratamiento de aire: Norma IRAM 80400" (2022) | Fuera de ámbito | Calidad de aire en establecimientos de **salud**, no domicilios. |

## Lote 3 · artículos de la revista Ingeniería Eléctrica (recibido el 2026-10-02)

38 artículos convertidos de PDF a texto. Todos son **SECUNDARIA**: sirven si no contradicen a las fichas 01 a 22. Base de las fichas 23 a 30. De ninguno se copió texto: solo datos en palabras propias. **No** se copiaron correos, sitios personales, marcas ni promociones que traen los artículos.

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| Farina, "Sistema de puesta a tierra", partes 1, 2, 4, 5, 6 y 7 (2022-2023) | SECUNDARIA | 23 | Buena base de resistividad, electrodos y cálculo. Errores: unidad "Ω/m" (es Ω·m), fórmulas de cortocircuito mal transcriptas (parte 6), 30 °C de referencia (la 770 usa 40 °C), conductor de PAT de 2,5 mm² (la 770 pide 4 mm²). Todas sus cláusulas son de la **771**. |
| Farina, "Sistema de puesta a tierra", parte 3 (2022) | Fuera de ámbito | 23 | Neutro de transformadores y generadores (media tensión). Solo se rescata la mención de IRAM 2379. |
| Miravalles, "Tierras extrañas" (2021) | SECUNDARIA (opinión y práctica) | 23 | **No usar** su prueba del PE anulando el diferencial (riesgosa, no normalizada). |
| Miravalles, "Calefacción eléctrica y falta de puesta a tierra" (2022) | SECUNDARIA (opinión y práctica) | 23 | "Adaptadores prohibidos" sin cláusula: no afirmar. |
| Farina, "Protección contra las sobretensiones", parte 1 (2024) | SECUNDARIA | 26 | El título no coincide: trata de **sobrecorrientes** (Icn / Ics). |
| Farina, "Protección contra las sobretensiones", partes 2, 3 y 4 (2024-2025) | SECUNDARIA | 24 | Parte 3: umbrales AQ invertidos (gana ficha 05). Parte 4: fila "220-240 V con punto medio" no aplica en Argentina; verificar la Tabla 44.3 antes de publicar. |
| Santos y otros, "Los varistores de óxido metálico" (2026) | SECUNDARIA (confiabilidad alta en lo conceptual) | 24 | Autores vinculados a un fabricante. Trae un correo personal: no copiar. |
| Farina, "Accidentes eléctricos" (2026) | Opinión | — | Sin datos técnicos. |
| Nota institucional sobre productos eléctricos inseguros (2026) | SECUNDARIA (baja) | 29 | Porcentaje de incendios sin fuente: no usar. QR obligatorio: verificar. |
| Nota sobre un laboratorio de ensayos eléctricos (2026) | Fuera de ámbito | — | Comercial y de media tensión. |
| Farina, "Alimentación de los motores eléctricos trifásicos según la reglamentación de la AEA" (2024) | SECUNDARIA (alta, con reservas) | 25 | Sección 558 no verificada. Dice que la protección de cortocircuito "no se menciona": en vivienda sí la exige la 770. |
| Farina, "Tableros, canalización y motores eléctricos" (2026) | SECUNDARIA | 25 | General. |
| Notas de un fabricante de motores: mono o trifásico (2021), motor de baja tensión (2025), ola de calor (2025), altura (2025), mantenimiento (2026), sobrecalentamiento (2026) | SECUNDARIA (fabricante) | 25 | **No usar** "monofásico hasta 14 kW" ni "el monofásico ahorra consumo". Valores de altura: orientativos del fabricante. |
| Nota de un fabricante de bombas, "Bomba centrífuga: paso a paso para purgarla" (2022) | SECUNDARIA (fabricante) | 27 | Manda encender antes de poner la tapa: se reordenó en la ficha. |
| Berizzo, "Motor de inducción asincrónico" (2021) | SECUNDARIA | 25 | Solo conceptos de 50 Hz y V/Hz. Tolerancia de frecuencia 5-10 %: no usar. Alta frecuencia: fuera de ámbito. |
| Berizzo (traducción de Miller), "Ondas de torque en motores eléctricos" (2025) | Fuera de ámbito | — | Teoría avanzada; traducción de un tercero. |
| Farina, "Medición e indicación en tableros eléctricos" (2023) | SECUNDARIA | 26 | Usa "BA4" para no idóneos: error (ver ficha 09). |
| Farina, "Borneras" (2023) | SECUNDARIA (baja) | 26 | Pocos datos concretos. |
| Nota de un fabricante sobre control de temperatura y humedad en tableros (2026) | SECUNDARIA (catálogo) | 26 | Sin valores recomendados. |
| Farina, "Sistema de agua en los inmuebles de propiedad horizontal" (octubre 2019) | SECUNDARIA | 27 | **No usar** "control hasta 48 V": la 770 pide MBTS (ficha 10). No menciona diferencial ni falta de fase. |
| Piumetto, "Algunas cuestiones técnicas acerca de la eficiencia energética" (2024) | SECUNDARIA | 28 | Redactado por la revista a partir de una charla. |
| Nota de un fabricante, "Corrección del factor de potencia: algunos conceptos clave" (2026) | SECUNDARIA (baja-media) | 28 | Sin números. "Mayor consumo de energía" es impreciso. |
| Mendivil, "El electricista matriculado y el profesional de Higiene y Seguridad" (2026) | SECUNDARIA | 29 | Firma conjunta = interpretación del autor. Validez de 12 meses: verificar. Estadística local y promoción de evento: no usar. |
| Farina, "Protección de inmuebles", partes 1 y 2 (2022-2023) | SECUNDARIA | 30 | Transcribe la 771B.9 (escribe "90365": error). |
| Farina, "Mantenimiento e inspección en estaciones de servicio" (2022) | SECUNDARIA (ámbito especial) | 30 | Sección 790. Sin plazos numéricos. |

## Lote 4 · estudios técnicos de la AEA (recibido el 2026-10-31)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| Semerdjian, "Análisis del factor F de incremento del potencial de tierra en redes de BT con gestión de neutro TN múltiplemente conectado a tierra", AEA, v1.0, agosto 2023 (8 págs.), https://aea.org.ar/pdfviewer/estudio-factor-f/ | SECUNDARIA | 35 | Estudio técnico publicado por la AEA, no reglamentación. Trata la **red de la distribuidora** (TN), no la vivienda (TT): para la vivienda mandan las fichas 06, 23, 31 y 33. Se apoya en EN 50522:2022 y AEA 90479-1:2020, que **no** están en esta biblioteca. La fórmula de RPAT (ec. 5) no se pudo leer bien: no usarla. "Todos los derechos reservados": no subir el PDF ni copiar texto. |
| Texto técnico "Evaluación de las incertidumbres de medición" (mediciones directas), con aval de la AEA, recibido el 2026-10-31 (autor no indicado) | SECUNDARIA de confianza | 36 | Resume CIPM INC-1 (1980), GUM (IRAM 35050) y EA-4/02 (IRAM 35051), que **no** están en esta biblioteca. Factores k de la distribución triangular (2,33 / 2,42) no coinciden con la GUM (≈ 1,90 / 2,20): no usarlos sin verificar. Las mediciones indirectas no se recibieron. |

## Lote 5 · baños, cocinas y lavaderos (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| AEA 90364-7-701, **edición 2012**, completa (40 págs.: texto, Anexo A unifilares, Anexo B figuras, Anexo C calefacción por cables y folios) | **PRIMARIA** | 37 | **Base de la ficha 37.** Texto oficial leído desde una copia publicada en Scribd (documento 769406911). Páginas citadas: las impresas. Cotas de las figuras B.6 a B.9 leídas de los dibujos. Verificar vigencia, adendas y corrigendas en aea.org.ar. Uso exclusivo: no subir el PDF al repo. |
| AEA 90364-7-701, edición 2011 (16 págs. de texto, sin anexos) | Reemplazada | — | Primera copia leída (Scribd 400193616). La edición 2012 la reemplaza. Diferencias: en 2011 el caño de zonas 0 y 1 era "rígido"; en 2012 se pide embutido y aislante, con referencia a 521.8 y 521.9. Los pisos calefactores pasaron de 701.771-E a 701.55.7.7 y Anexo C. |
| Tolocka, "Instalaciones eléctricas en baños según la reglamentación AEA", profetolocka.com.ar, 21-10-2024 | SECUNDARIA | 37 | Resume la 701 edición 2012 y coincide con ella. Su Fig. 3 reproduce las figuras B.7 y B.8. Ya no hace falta: la ficha 37 usa el texto completo. |
| Galizia, "Clasificación de áreas en las instalaciones eléctricas", COPAIPA (Salta), febrero 2011 | SECUNDARIA (**histórica**) | 37 | Autor: secretario del CE-10 de la AEA. Describe la **701 edición 2002** y adelanta el borrador de 2011, que coincide con la ficha 37. **No usar** sus figuras 701.A a 701.D de 2002: zona 2 hasta 2,25 m (hoy hasta el cielorraso), zona 3 de 2,40 m (hoy todo el resto del local), lavatorio con H = 60 cm sobre el borde (hoy 0,40 m; el radio de 0,40 m y los 0,15 m siguen igual). Sirve para piscinas (702), saunas (703) y áreas con riesgo de explosión (771), fuera del alcance del planificador. |

## Lote 6 · símbolos gráficos IRAM (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| IRAM 2010 Parte III, "Símbolos gráficos electrotécnicos. Aparatos y dispositivos de mando y protección", diciembre 1988 (33 págs., escaneada sin texto) | **PRIMARIA** (con reservas de vigencia) | 38 | Equivale a IEC 617-7 (1983), hoy reemplazada por IEC 60617. Sirve para esquemas y unifilares, **no** para el plano de planta. No trae símbolo propio de diferencial ni de termomagnética. Verificar edición vigente en iram.org.ar. Derechos de IRAM: no subir el PDF ni copiar los dibujos. |

## Lote 7 · manual de capacitación de Córdoba (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| *Manual del Instalador Electricista · Categoría III*, 2.ª edición, Fundación Relevando Peligros, Córdoba, 2020 (408 págs.) | SECUNDARIA | 39, 40, 41, 42 | Manual de capacitación para la Ley 10.281 de Córdoba. Se apoya en la AEA 90364-7-771 (2006) y en la Guía de 10 kW de la AEA. Útil para croquis, cómputo desde el plano, efectos de la corriente, lámparas, presupuesto e inspección. Los módulos I y II (matemática y electrotecnia básica) no se procesaron como fichas. |

**No usar del manual** (contradice la 770 o normas vigentes; en vivienda manda la 770):
- Tiempos de disparo del diferencial 0,2 s / 0,1 s / 0,04 s con 10 × IΔn (pág. 137). Vale IEC 61008-1: 300 ms / 150 ms / 40 ms con 5 × IΔn.
- Hasta 3 circuitos en un caño con carga total de **20 A** (págs. 285 y 298). La 770 admite termomagnéticas que sumen hasta **36 A** (ficha 07).
- Retornos y alimentación de llaves de **1,5 mm²** (pág. 309). La 770 pide **1 mm²** como mínimo (ficha 04).
- Termomagnética de **15 A** con cable de 1,5 mm² en el ejemplo (pág. 333). En la 770 el IUG lleva hasta **16 A** (ficha 02).
- Circuitos IUE y TUE con 12 bocas y tabla de puntos mínimos por ambiente (págs. 280-287): son de la **771**. En vivienda dentro de la 770, usar la ficha 02.
- Zonas del baño de la **edición 2002** de la 701 (pág. 311: zona 2 hasta 2,25 m, zona 3 de 2,40 m). Usar la ficha 37 (edición 2012).
- Símbolo de "termomagnético unipolar o monofásico" (tabla 13, pág. 57): en vivienda monofásica la 770 prohíbe termomagnéticas unipolares (ficha 05).
- Caída de tensión 3 % / 5 % y aislación de 1000 Ω/V (págs. 322-323 y 349): usar las fichas 04 y 12.

## Lote 8 · símbolos de planta y dibujo técnico (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| IRAM 2010, Sección IV, "Símbolos gráficos electrotécnicos para instalaciones de alumbrado, calefacción y fuerza motriz", Apéndice II de un libro técnico (4 págs., escaneadas, sin datos del libro) | **PRIMARIA** (reproducción; vigencia a verificar) | 43 | **Simbología para el plano de planta**: bocas, llaves, tomas, tableros, medidor, cañerías y montantes. Desciende de la IRAM 2010 de 1941. Tiene un toma sin tierra (A 2919) que en vivienda no corresponde: usar A 2920. |
| IRAM, *Manual de normas de aplicación para dibujo técnico*, edición XXVII (146 págs., escaneado) | **PRIMARIA** | 44 | Se procesaron IRAM 4502 (líneas), 4503 (letras), 4504 (formatos), 4505 (escalas), 4508 (rótulo) y 4513 (acotación). Las normas de dibujo mecánico (roscas, engranajes, perfiles, terminado superficial) no aplican. Derechos de IRAM: no subir el PDF. |
| Resolución ENRE 207/95: Reglamentación AEA para la ejecución de instalaciones eléctricas en inmuebles (1995) | **NO USAR** | — | Reglamentación vieja, reemplazada por la AEA 90364 (770, 771, 701). Solo dato histórico. |
| Anexo VII "Manual de normas y procedimientos de instalación" (redes informáticas en escuelas) | Fuera de ámbito | — | Ya registrado en el Lote 2. Recibido otra vez. |

## Lote 9 · código de edificación (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| Código de Edificación de la Ciudad de Buenos Aires, texto ordenado Ley 6.100 y Ley 6.438 (BOCBA 17/08/2021), 492 págs. | **PRIMARIA** (solo CABA) | 45 | Se procesaron: clases de locales, alturas, superficies y lados mínimos de vivienda, cocina, circulaciones, unir y dividir locales, puertas, baños, iluminación y ventilación, medidores, instalaciones eléctricas y muros. **No** trae espesores de tabiques ni muros comunes: los remite a los Reglamentos Técnicos, que no están en esta biblioteca. Fuera de CABA, usar solo como referencia. |

## Lote 10 · código de edificación de Córdoba (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| Código de Edificación de la Ciudad de Córdoba, compilado, Ord. 9387/95 y modificatorias (hasta Ord. 13238/22), reglamentado por Dec. 463/96. Dirección de Obras Privadas y Uso del Suelo. 124 págs. | **PRIMARIA** (solo ciudad de Córdoba) | 46 | Se procesaron: grupos de locales, dimensiones mínimas de vivienda, alturas, iluminación y ventilación, baños, subdivisión, puertas y pasillos, muros, instalación eléctrica y medidores. **No** fija espesores de muros ni tabiques, ni ancho de puertas y pasillos internos de la vivienda. La instalación eléctrica la remite a EPEC y a la AEA 90364-7-771 ed. 2006 "o las que la reemplacen". Fuera de la ciudad de Córdoba, usar solo como referencia. |

## Lote 11 · Reglamentos Técnicos de muros, CABA (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| Reglamento Técnico RT 020105-01 "Muros cerámicos", versión 2 (dic. 2022). Anexo 17, Res. MJGGC-SSGU 205/22. 7 págs. | **PRIMARIA** (solo CABA) | 48 | Fija medianeras de 0,30 y 0,45 m, muro privativo de 0,15 m, canaletas (5 cm en medianera de 0,30 y en muro privativo) y nichos de medidores a 5 cm del eje. **No** fija tabiques interiores de ladrillo. |
| Reglamento Técnico RT-041300-020105-02 "Muros no cerámicos", versión 2 (dic. 2022). Anexo 18, Res. MJGGC-SSGU 205/22. 6 págs. | **PRIMARIA** (solo CABA) | 47 | Espesores mínimos de HCCA: 12,5 cm exterior y entre unidades; 7,5 cm tabique interior y sanitario; 10 cm caja de escalera. Procedimiento para embutir caños en HCCA. Hormigón y piedra: sin espesores fijos. |

## Lote 12 · AEA 770 edición 2026 (recibido el 2026-11-06)

| Documento | Estado | Ficha | Notas |
|---|---|---|---|
| @aeaconectada (cuenta oficial de la AEA), Instagram, 26/10/2026: "Lo que debés saber de la nueva edición de AEA 90364-7-770", carrusel de 5 placas | **OFICIAL, resumen** | 49 | Tipo AC no apto; PAT máx. 100 Ω en TT con diferencial ≤ 300 mA (antes 40 Ω); movilidad eléctrica, FV, calefacción por cables, SAI/UPS, THD, simultaneidad, IEC 61439. No trae texto ni fecha de vigencia. Falta el texto completo de la edición 2026. |
| Electroclima, carrusel "AEA 90364-7-770 · Nueva edición (noviembre 2026)", Instagram, placas 2 a 9 de 10 | **SECUNDARIA** (divulgación) | 50 | Comparación 2017 vs 2026 por tema. Columna 2017 coincide con las fichas 02, 04, 06 y 07. Placas generadas con IA: confirmar cada valor 2026 con el texto de la norma. Excepción de 200 Ω y cambio de TUG en dormitorio > 12 m²: verificar. |

## Normas citadas que **no** están en esta biblioteca

Si un tema depende de ellas, verificar en fuente oficial antes de afirmar:
- AEA 90364 partes 1 a 6 (reglas generales; por ejemplo, dónde va la llave unipolar y la prueba de polaridad 613.8).
- AEA 90364-7-701: **ya incorporada** completa en la ficha 37 (edición 2012, Lote 5).
- AEA 95150 (acometida, pilar y medición).
- AEA 92305 (protección contra rayos).
- IRAM 2071 (tomacorrientes 2P+T: posición de los bornes).
- IEC 61008 / 61009 (diferenciales), IEC 60898-1 (termomagnéticas).
- AEA 90364-3 (influencias externas, AQ), 90364-4-43 (sobrecorrientes), 90364-4-44 (sobretensiones, 442 y 443), 90364-5 (sección 558 motores, 552), 90364-8 (eficiencia energética), 90364-7-790 (estaciones de servicio). Citadas en el Lote 3.
- IEC 61643-11 (DPS), IEC 60038 (tensiones normalizadas), IEC 60721 (condiciones ambientales), IEC 60034-1 (motores).
- IRAM 2379 (esquemas de conexión a tierra), IRAM 2004 (conductores de cobre desnudo).
- Resolución SRT 900/2015 (texto completo), Ley 19.587 y Decreto 351/79.
