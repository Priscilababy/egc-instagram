# Base de conocimiento técnico · EGC

Fichas con lo que dice la normativa argentina sobre instalaciones eléctricas domiciliarias, y con las reglas de instalación y mantenimiento de aire acondicionado split, **en palabras propias** y con la referencia exacta de dónde sale cada dato (documento, cláusula o tabla, página impresa).
Las armó Claude leyendo los documentos que juntó Fran. Los documentos originales **no** están en este repositorio: las normas AEA e IRAM tienen derechos de autor y este repo es público.

## Orden de fuentes (obligatorio para la rutina)

1. **Esta carpeta.** Si el dato está en una ficha, se usa tal cual, con su referencia.
2. **Web oficial o confiable** (AEA, IRAM, IEC, ENRE, entes provinciales, universidades, fabricantes reconocidos) para lo que no esté acá. Si la web contradice una ficha, gana la ficha: anotá la diferencia en el resumen de la corrida para que Fran la revise.
3. **Lo que no se pudo verificar no se afirma.** Tampoco se "completa" con memoria o sentido común.

## Cómo citar en los posteos

- Si la ficha trae cláusula o tabla (por ejemplo "770.14.2.3" o "Tabla 770.11.I"), se puede citar así: `AEA 90364-7-770, 770.14.2.3`.
- Si la ficha dice **"sin número verificado"**, se escribe solo `reglamentación AEA 90364`.
- Nunca inventar un número de artículo, tabla o página.

## Fichas

| Ficha | Qué tiene |
|---|---|
| [00-fuentes.md](00-fuentes.md) | Qué documentos se leyeron, cuáles sirven y cuáles **no** (y por qué) |
| [01-alcance-y-conceptos.md](01-alcance-y-conceptos.md) | Alcance de la 770, esquema TT, tensiones, líneas y circuitos, qué es una "boca" |
| [02-circuitos-y-grado-de-electrificacion.md](02-circuitos-y-grado-de-electrificacion.md) | IUG / TUG / TUE, grados de electrificación, circuitos y puntos mínimos, demanda |
| [03-colores-e-identificacion.md](03-colores-e-identificacion.md) | Código de colores, **retornos**, cables prohibidos por color |
| [04-secciones-intensidad-y-caida-de-tension.md](04-secciones-intensidad-y-caida-de-tension.md) | Secciones mínimas, corriente admisible, agrupamiento, IB ≤ In ≤ Iz, caída de tensión |
| [05-protecciones.md](05-protecciones.md) | Diferencial 30 mA, termomagnéticas bipolares, cabecera, selectividad, motores, DPS |
| [06-puesta-a-tierra.md](06-puesta-a-tierra.md) | 40 Ω, jabalina, cámara de inspección, cable de PAT, conductor PE, masas |
| [07-canalizaciones-cajas-y-uniones.md](07-canalizaciones-cajas-y-uniones.md) | Cables y caños prohibidos, curvas, cajas, agrupamiento, **empalmes**, medidas de caños |
| [08-tomacorrientes-llaves-y-bocas.md](08-tomacorrientes-llaves-y-bocas.md) | Alturas, tomas con pantalla, bocas mixtas, pasillos, escaleras, IP |
| [09-tableros.md](09-tableros.md) | Ubicación, IP, reserva 20 %, un cable por borne, barra PE, marcado |
| [10-muy-baja-tension-y-casos-especiales.md](10-muy-baja-tension-y-casos-especiales.md) | MBTS / MBTF, flotantes de tanque, timbres, LED, cercas eléctricas, piscinas |
| [11-subterraneas.md](11-subterraneas.md) | Cables enterrados dentro del terreno (770) y diferencia con la vía pública (95101) |
| [12-inspeccion-y-mediciones.md](12-inspeccion-y-mediciones.md) | Inspecciones, mediciones, aislación, periodicidad, mantenimiento |
| [13-habilitacion-cordoba.md](13-habilitacion-cordoba.md) | Ley 10281 de Córdoba y registro de instaladores (ERSeP) |
| [14-aea-771-oficinas-locales-y-circuitos-especificos.md](14-aea-771-oficinas-locales-y-circuitos-especificos.md) | AEA 771: cuándo se usa, circuitos ACU / APM / OCE, grados, demanda, diferencias con la 770 |
| [15-aire-acondicionado-conceptos-y-dimensionamiento.md](15-aire-acondicionado-conceptos-y-dimensionamiento.md) | Ciclo de refrigeración, frigorías / BTU / kW, eficiencia, qué se puede decir sobre dimensionar |
| [16-aire-acondicionado-ubicacion-soportes-y-desagote.md](16-aire-acondicionado-ubicacion-soportes-y-desagote.md) | Distancias de las unidades, ménsulas, pasamuros Ø 65, desagote de condensado |
| [17-aire-acondicionado-canerias-vacio-y-carga.md](17-aire-acondicionado-canerias-vacio-y-carga.md) | Diámetros y largos, abocardado, torque, nitrógeno, vacío, carga, recuperación, prueba final |
| [18-aire-acondicionado-conexion-electrica.md](18-aire-acondicionado-conexion-electrica.md) | Qué circuito lleva un split, protecciones, sección, cable de interconexión, tierra, intemperie |
| [19-refrigerantes-y-normativa-ambiental.md](19-refrigerantes-y-normativa-ambiental.md) | Res. 1640/2012 (R-22), Montreal y Kigali, R-410A / R-32 / R-290, aceites, seguridad |
| [20-aire-acondicionado-mantenimiento-y-diagnostico.md](20-aire-acondicionado-mantenimiento-y-diagnostico.md) | Rutina de mantenimiento, qué medir, diagnóstico por síntomas, garantía |
| [21-extraccion-y-ventilacion-domiciliaria.md](21-extraccion-y-ventilacion-domiciliaria.md) | Extractores de baño y cocina: renovaciones de aire e instalación (fuente de confiabilidad baja) |
| [22-presupuesto-aire-acondicionado.md](22-presupuesto-aire-acondicionado.md) | Ítems para presupuestar instalación, parte eléctrica y mantenimiento de splits (base para la app) |
| [23-puesta-a-tierra-terreno-electrodos-y-calculo.md](23-puesta-a-tierra-terreno-electrodos-y-calculo.md) | Resistividad del terreno, cuánto da una jabalina, configuraciones, equipotencialización, casos de obra sin PE |
| [24-sobretensiones-categorias-y-dps.md](24-sobretensiones-categorias-y-dps.md) | Origen de las sobretensiones, nivel ceráunico, categorías I a IV, DPS y varistores |
| [25-motores-alimentacion-proteccion-y-mantenimiento.md](25-motores-alimentacion-proteccion-y-mantenimiento.md) | Cable al 125 %, seccionador con candado, arranque, altura, sobrecalentamiento, mantenimiento |
| [26-tableros-poder-de-corte-indicacion-y-borneras.md](26-tableros-poder-de-corte-indicacion-y-borneras.md) | Icn / Ics de termomagnéticas, luces piloto e instrumentos, borneras, temperatura del tablero |
| [27-bombeo-de-agua-en-edificios.md](27-bombeo-de-agua-en-edificios.md) | Cisterna, dos bombas con alternancia, flotantes, tablero de bombas, tierra de la cañería, purgado |
| [28-eficiencia-energetica-y-factor-de-potencia.md](28-eficiencia-energetica-y-factor-de-potencia.md) | AEA 90364-8 (zonificación, clases EIEC) y conceptos de corrección del factor de potencia |
| [29-protocolo-srt-900-incumbencias-y-seguridad-de-productos.md](29-protocolo-srt-900-incumbencias-y-seguridad-de-productos.md) | Res. SRT 900/15: qué hace el electricista y qué el de Higiene y Seguridad; productos inseguros |
| [30-ambitos-especiales-cercas-y-estaciones-de-servicio.md](30-ambitos-especiales-cercas-y-estaciones-de-servicio.md) | Cercas electrificadas (barrera, distancias) y estaciones de servicio (Sección 790) |
| [37-aea-701-banos-cocinas-y-lavaderos.md](37-aea-701-banos-cocinas-y-lavaderos.md) | AEA 701: zonas 0 a 3 en baños, cocinas y lavaderos, IP por zona, qué va en cada zona, equipotencial, termotanques |
| [38-iram-2010-3-simbolos-mando-y-proteccion.md](38-iram-2010-3-simbolos-mando-y-proteccion.md) | IRAM 2010-III: símbolos de contactos, interruptor, seccionador, contactor, pulsador, bobinas, fusibles y descargadores para esquemas y unifilares |
| [39-croquis-plano-y-computo-de-materiales.md](39-croquis-plano-y-computo-de-materiales.md) | Croquis sin escala con cotas y rótulo, símbolos del croquis, unifilar, cómputo de caños, cables y cajas desde el plano, volumen de cajas |
| [40-efectos-de-la-corriente-en-el-cuerpo.md](40-efectos-de-la-corriente-en-el-cuerpo.md) | Umbrales de percepción, no soltar y fibrilación, recorrido, contacto directo e indirecto, tensiones de seguridad |
| [41-lamparas-residuos-ip-ik-y-clase-termica.md](41-lamparas-residuos-ip-ik-y-clase-termica.md) | Tipos de lámparas, mercurio y qué hacer si se rompe un tubo, IP e IK, clase térmica de aislantes |
| [42-presupuesto-puesta-en-servicio-e-inspeccion.md](42-presupuesto-puesta-en-servicio-e-inspeccion.md) | Conceptos de presupuesto y mano de obra, cronograma, pruebas de puesta en servicio, frecuencia de inspección, Res. ERSeP 11/2018 |
| [43-iram-2010-simbolos-de-instalacion-en-planta.md](43-iram-2010-simbolos-de-instalacion-en-planta.md) | IRAM 2010 Sección IV: símbolos del plano de planta (bocas, llaves, tomas, tableros, medidor, cañerías, montantes, timbre) |
| [44-iram-dibujo-tecnico-formatos-rotulo-lineas-escalas.md](44-iram-dibujo-tecnico-formatos-rotulo-lineas-escalas.md) | IRAM 4502 a 4513: formatos A, márgenes, plegado, rótulo, tipos de línea, letras, escalas y acotación |
| [45-codigo-edificacion-caba-locales-puertas-banos.md](45-codigo-edificacion-caba-locales-puertas-banos.md) | Código de Edificación CABA: clases de locales, alturas, superficies y lados mínimos, pasillos, puertas, baños, ventilación, medidores |
| [46-codigo-edificacion-cordoba-locales-puertas-banos.md](46-codigo-edificacion-cordoba-locales-puertas-banos.md) | Código de Edificación de Córdoba: grupos de locales, alturas, dimensiones mínimas, ventilación, baños, puertas, muros, instalación eléctrica y medidores. Tabla de diferencias con CABA |
| [47-rt-caba-muros-no-ceramicos-hcca.md](47-rt-caba-muros-no-ceramicos-hcca.md) | Reglamento Técnico CABA, muros no cerámicos: espesores mínimos de HCCA (12,5 / 10 / 7,5 cm) y cómo embutir caños en HCCA |
| [48-rt-caba-muros-ceramicos-divisorios-canaletas.md](48-rt-caba-muros-ceramicos-divisorios-canaletas.md) | Reglamento Técnico CABA, muros cerámicos: medianeras 0,30 / 0,45 m, muro privativo 0,15 m, canaletas de 5 cm, nichos de medidores |
| [49-aea-770-edicion-2026-cambios.md](49-aea-770-edicion-2026-cambios.md) | AEA 770 edición 2026 (resumen oficial AEA): tipo AC no apto, PAT máx. 100 Ω en TT con diferencial ≤ 300 mA, movilidad eléctrica, FV, THD, IEC 61439 |

## Avisos sobre temas de `temas.md`

- **AEA 770 edición 2026 (ficha 49):** las fichas 01 a 12 son de la edición 2017. Puesta a tierra: la 2026 fija **100 Ω** máx. (con diferencial ≤ 300 mA); la 2017 fijaba 40 Ω. Diferencial tipo AC: **no apto** en la 2026. **Vigente desde el 1/11/2026**: en posteos y notas nuevas usar 100 Ω y diferencial tipo A (AC no apto). Los valores de la 2017 solo como antecedente.

Antes de armar estos temas, leé la ficha indicada. Algunos cambian por completo lo que se puede dibujar.

- **La llave corta la fase, nunca el neutro:** la regla es correcta, pero no está escrita en la 770 (está en la parte general de la AEA 90364, fuera de esta biblioteca). Citar solo "reglamentación AEA 90364". Retornos en color no reservado → ficha 03.
- **Bomba de agua con automático de tanque (flotante eléctrico):** el circuito de comando del flotante dentro de tanques va en **MBTS** (muy baja tensión sin puesta a tierra), no en 220 V → ficha 10. El motor además necesita maniobra que corte fase y neutro y protección de sobrecarga propia → ficha 05. Un esquema con flotante a 220 V dentro del tanque es **incorrecto**.
- **Empalme retorcido con cinta vs. borne:** la AEA **admite** el empalme retorcido intercalando hebras en ciertos casos → ficha 07. El "MAL" no puede ser "retorcer"; tiene que ser algo que la norma prohíbe (más de 4 cables retorcidos, empalme dentro del caño, sin aislación equivalente, secciones mayores a 4 mm² retorcidas).
- **Tablero monofásico de vivienda:** termomagnéticas **bipolares con los dos polos protegidos**; no se permiten 1P+N ni "neutro pasante" → fichas 05 y 09.
- **Motor monofásico con capacitor / contactor:** requisitos de 770.13.3 → ficha 05.
- **Tira LED / fuente 12 V:** fuente con transformador de devanados separados (nunca autotransformador); cables fuente-LED de más de 3 m son parte de la instalación; canalización separada de la de 220 V → fichas 01, 07 y 10.
- **Aire acondicionado split (circuito):** la norma decide por la **corriente** del equipo y el tipo de toma, no por las frigorías: toma 10 A solo hasta 10 A; toma 20 A en TUE hasta 20 A; un solo equipo sin derivaciones = ACU. Los 4 fabricantes piden **línea exclusiva**. Diferencial de 30 mA **obligatorio** también ahí (ningún manual lo menciona, la norma sí) → fichas 14 y 18. No afirmar "a partir de X frigorías va circuito propio": esa regla no existe en la AEA.
- **Termotanque eléctrico:** misma lógica que el split: el circuito sale de su corriente (TUG hasta 10 A, TUE hasta 20 A, ACU si es un solo equipo sin derivaciones). Verificar la placa y el manual del equipo → fichas 02, 14 y 18.
- **Temas de aire acondicionado en general:** el público también son instaladores de aire. Manda el **manual del fabricante** del modelo; las fichas 16 y 17 dan lo que se repite entre marcas y el **rango** cuando no coinciden. **Nunca nombrar marcas** en los posteos.
- **Vacío:** los manuales piden bomba de vacío 15 min mínimo hasta −76 cmHg; la buena práctica agrega vacuómetro (500 / 250 micrones) y prueba de retención. "Purgar con el gas del equipo" es **MAL** → ficha 17.
- **Nitrógeno:** solo nitrógeno seco con regulador; **nunca oxígeno ni aire comprimido** → ficha 17.
- **R-22:** la Res. 1640/2012 prohíbe fabricar, importar y vender equipos **nuevos** con R-22. **No** dice nada de recargar o reparar equipos existentes: no afirmar que "está prohibido recargar R-22" → ficha 19.
- **R-32:** es **A2L** (ligeramente inflamable) → ficha 19.
- **Frecuencia de limpieza de filtros:** las fuentes no coinciden; decir "según el uso y lo que indique el manual" → ficha 20.
- **Frigorías por m²:** no hay una regla oficial en esta biblioteca; no publicar una cifra como norma → ficha 15.
- **Ordenanza de Rosario 3419/83:** dice retorno negro, fase roja y tierra desnuda. Sigue publicada, pero técnicamente la AEA vigente la supera: **no usar** como fuente técnica → ficha 00.
- **Extractor de baño:** puede ir en el circuito de iluminación (cuenta como boca de iluminación) → ficha 08. Caudal orientativo → ficha 21. Las zonas del baño están en la AEA 90364-7-701, que **no** está en esta biblioteca.
- **Tomacorriente con descarga a tierra:** la posición de cada borne es de IRAM 2071, que **no** está en esta biblioteca. Verificar antes de dibujar.
- **Selectividad, DPS, protector de tensión:** fichas 05 y 06.
- **Timbre / portero:** MBTF o MBTS cambian si las masas van a tierra → ficha 10.

## Avisos sobre el Lote 3 (fichas 23 a 30)

Las fichas 23 a 30 salen de **artículos de revista** (fuente SECUNDARIA). Si chocan con las fichas 01 a 22, ganan las fichas 01 a 22.

- **Flotantes de tanque a 48 V:** un artículo lo dice; **no usar**. La 770 pide **MBTS** → ficha 10.
- **Cable de puesta a tierra de 2,5 mm²:** un artículo lo admite; en vivienda el mínimo es **4 mm²** → ficha 06.
- **Monofásico "hasta 14 kW":** no usar. La 770 recomienda trifásico por encima de 7 kVA o 32 A → ficha 02.
- **Tabla de categorías de sobretensión (I a IV):** para la red argentina usar la fila 230/400 V (6 / 4 / 2,5 / 1,5 kV) y verificarla antes de publicar → ficha 24.
- **DPS:** ninguna fuente de la biblioteca trae clases, Up ni ubicación. No completar con memoria → fichas 05 y 24.
- **Motores:** no inferir que alcanza con la termomagnética; la sobrecarga necesita protección **dedicada** → fichas 05 y 25.
- **Protocolo SRT 900/15:** no afirmar que hacen falta dos firmas ni quién puede firmar en cada provincia → ficha 29.
- **Prueba mensual del diferencial:** es recomendación del **fabricante**, no de la AEA → ficha 23.
- **Cláusulas 771, 558, 443:** las citan los artículos pero no están verificadas en esta biblioteca; citar "reglamentación AEA 90364".
- **Purgado de bomba:** usar el orden corregido de la ficha 27 (todas las tapas puestas antes de encender, nunca en seco).
- **Baños, cocinas y lavaderos (701):** usar la ficha 37 (edición 2012). Tomas y llaves de 220 V solo en **zona 3**. Termotanque con **conexión fija**, nunca con ficha. **No afirmar** que hay zona 2 alrededor de la pileta de cocina o de lavar: las figuras B.6 y B.7 solo dibujan zonas 0 y 1. No usar medidas de la edición 2002 (zona 3 de 2,40 m, lavatorio con 60 cm de alto).
- **Símbolos:** plano de planta (bocas, llaves, tomas, tableros) → ficha 43 (IRAM 2010 Sección IV). Esquemas y unifilares → ficha 38 (IRAM 2010 Parte III). En vivienda, toma siempre con tierra (A 2920). No inventar un símbolo único de diferencial o de termomagnética.
- **Planos:** formato, rótulo, líneas, escalas y cotas → ficha 44 (normas IRAM de dibujo técnico).
- **Manual de Córdoba (fichas 39 a 42):** es fuente SECUNDARIA basada en la 771. Antes de usar un número de esas fichas, revisar la lista "No usar del manual" en `00-fuentes.md` (Lote 7). Si una ficha 01 a 12 dice otra cosa, gana la ficha 01 a 12.
- **Temas vigentes, no viejos:** no hacer posteos ni notas sobre tecnología en desuso (tubos y lámparas fluorescentes, incandescentes, halógenas, balastos, cables y prácticas reemplazadas). Si una ficha trae algo viejo, usarlo solo como contexto. Antes de elegir un tema, preguntarse si un electricista lo instala hoy.
- **Arquitectura (ficha 45):** valores del Código de Edificación de **CABA**. Fuera de CABA, citarlos como "en CABA". Espesores de muros: ver fichas 47 y 48.
- **Arquitectura (ficha 46):** valores del Código de Edificación de la **ciudad de Córdoba**. Citarlos como "en Córdoba". No mezclar con los de CABA (ficha 45) sin aclarar de dónde es cada uno.
- **Muros (fichas 47 y 48):** espesores de los Reglamentos Técnicos de **CABA**. Hay valores para medianeras, muros privativos y HCCA. **No** hay valor normativo para tabiques interiores de ladrillo: no afirmarlo.
