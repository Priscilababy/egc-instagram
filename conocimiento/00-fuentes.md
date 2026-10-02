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

## Normas citadas que **no** están en esta biblioteca

Si un tema depende de ellas, verificar en fuente oficial antes de afirmar:
- AEA 90364 partes 1 a 6 (reglas generales; por ejemplo, dónde va la llave unipolar y la prueba de polaridad 613.8).
- AEA 90364-7-701 (baños y locales con ducha o bañera: zonas y volúmenes).
- AEA 95150 (acometida, pilar y medición).
- AEA 92305 (protección contra rayos).
- IRAM 2071 (tomacorrientes 2P+T: posición de los bornes).
- IEC 61008 / 61009 (diferenciales), IEC 60898-1 (termomagnéticas).
- AEA 90364-3 (influencias externas, AQ), 90364-4-43 (sobrecorrientes), 90364-4-44 (sobretensiones, 442 y 443), 90364-5 (sección 558 motores, 552), 90364-8 (eficiencia energética), 90364-7-790 (estaciones de servicio). Citadas en el Lote 3.
- IEC 61643-11 (DPS), IEC 60038 (tensiones normalizadas), IEC 60721 (condiciones ambientales), IEC 60034-1 (motores).
- IRAM 2379 (esquemas de conexión a tierra), IRAM 2004 (conductores de cobre desnudo).
- Resolución SRT 900/2015 (texto completo), Ley 19.587 y Decreto 351/79.
