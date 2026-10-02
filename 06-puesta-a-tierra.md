# 06 · Puesta a tierra y conductor de protección

Fuente: AEA 90364-7-770, edición 2017. Al final, aportes secundarios del lote 3 (serie de Farina).

## Esquema TT (770.3.2, págs. 6-7)
- La vivienda tiene su **propia toma de tierra de protección**, eléctricamente independiente de la tierra de servicio de la distribuidora, **dentro de los límites del inmueble**, unida a las masas por el conductor PE.
- Resistencia de la toma de tierra de protección: **≤ 40 Ω** (valor máximo permanente). Se mide sobre el conjunto de electrodos, **desconectado** de todo lo que tiene vinculado (770.14.4.1, pág. 45).
- Se pueden usar varios electrodos, todos interconectados con un conductor desnudo enterrado (nota 1).
- La puesta a tierra suplementaria que algunas distribuidoras piden unir al **neutro** en la entrada es un refuerzo de la tierra de servicio y **no** es la tierra de protección (nota 3).
- Si no se puede lograr un TT, remitirse a la Parte 4 de la AEA 90364 (nota 4).

## Separación entre tierras ("tierra lejana") (770.3.2 y 770.14.4.2, págs. 7 y 45)
- La toma de protección tiene que estar a más de **10 veces el radio equivalente** del electrodo más largo, medido desde la toma de servicio más cercana.
- Tabla 770.3.I (pág. 7), jabalinas IRAM 2309 / 2310: esa distancia (10 Re) va de unos **3,2 m** (jabalina de 1,5 m) a unos **10 m** (jabalina de 6 m), según diámetro y largo. Ejemplos: jabalina de 1,5 m → 3,2 a 3,4 m; de 3 m → 5,4 a 5,8 m.

## Toma de tierra (770.14.4.1, pág. 45)
- Electrodos (jabalinas, cintas, placas, cables) según normas IRAM.
- Jabalinas: IRAM 2309 (acero-cobre) e IRAM 2310 (acero cincado).
- Uniones enterradas: soldadura cuproaluminotérmica; si las piezas son de igual sección, también compresión oval o hexagonal o conexión por compresión en frío IRAM 2349.

## Cámara de inspección (770.14.4.3, pág. 45)
- La unión entre electrodo y cable de puesta a tierra se hace dentro de una **cámara de inspección** con tapa removible a nivel del piso terminado. Se **recomienda** ubicarla en un lugar no transitado y despejado, para poder inspeccionar y medir.
- La conexión se hace sobre una **barra de cobre con puentes removibles** para poder desconectar y medir.
- Con una sola jabalina IRAM 2309 se puede conectar el cable con el **tomacable** de bronce o latón (IRAM 2343).

## Cable de puesta a tierra (770.14.4.4, pág. 45)
- Es el cable que va de la toma de tierra a la barra principal de tierra (o barra equipotencial principal).
- Se recomienda que entre por el **tablero principal** (ayuda contra sobretensiones); si no se puede, por la caja o tablero más cercano a la toma.
- Sección mínima **4 mm²**.
- Va **independiente** del conductor PE, aunque compartan canalización, y llega a la barra equipotencial principal.

## Sección del PE y del cable de puesta a tierra (Tabla 770.14.I, pág. 45)
| Sección de fase S | Sección de PE y de cable de PAT |
|---|---|
| S ≤ 16 mm² | igual a S |
| 16 < S ≤ 35 mm² | 16 mm² |
| S > 35 mm² | S / 2 |
- Siempre con los mínimos: PE **2,5 mm²**, cable de PAT **4 mm²**.

## Conductor de protección PE (770.14.4.5, pág. 46)
- Cobre aislado (IRAM NM 247-3, 2178, 62266 o 62267), color verde-amarillo.
- Recorre **toda** la instalación desde la barra principal de tierra, **incluidas las cajas y bocas sin tomacorriente**. Excepción: secundarios de MBTS.
- Nunca menos de **2,5 mm²**.
- Se recomienda no cortarlo en ningún punto, salvo cambios de sección en tableros seccionales y empalmes.
- Cajas, gabinetes y caños metálicos se conectan con **derivaciones** verde-amarillo tomadas del PE sin cortarlo. **No se permite conectar las masas en serie ("guirnalda")** (nota).
- Va en la misma canalización que los demás cables de su circuito (770.10.3.8.2 a, pág. 29).
- Las canalizaciones metálicas **no** reemplazan al PE; igual tienen que quedar puestas a tierra (770.10.3.2, pág. 20).

## Conexión de las masas (770.14.4.6, pág. 46)
- Todas las cajas y canalizaciones metálicas, tableros y equipos tienen borne o barra de tierra identificado (símbolo de tierra, letras PE o verde-amarillo). La marca no se pone sobre tornillos o arandelas que se sacan al conectar.
- Asegurar continuidad eléctrica entre cajas y caños metálicos con piezas que no se aflojen solas.
- La derivación al borne de tierra de tableros, cajas, canalizaciones, equipos **y tomacorrientes** es de cobre aislado verde-amarillo de **2,5 mm²** como mínimo.

## Tableros
- Barra, placa o bornera de PE identificada, con bornes suficientes para todos los circuitos; ahí llegan todos los PE y desde ahí se pone a tierra el tablero (770.16.4, pág. 53).
- En tableros de doble aislación no hace falta poner a tierra riel, cerradura ni bisagras metálicas (pág. 54).

## Medición (770.19.5.3, pág. 60)
- Preferentemente con **telurímetro**.
- Método alternativo de referencia: corriente entre la toma T y un electrodo auxiliar T1 lejano; se mide tensión entre T y un segundo auxiliar T2 ubicado a **~62 %** de la distancia T–T1; R = V / I. Se repite corriendo T2 1 m más lejos y 1 m más cerca; si las tres lecturas coinciden, se promedian.
- En TT se puede medir la impedancia de lazo en lugar de la resistencia de puesta a tierra (nota).
- La toma se mide desconectada de la instalación (770.14.4.1).

---

## Aportes del lote 3 · serie de Farina (SECUNDARIA)

Fuentes: FA1, FA2, FA4, FA5, FA6 y FA7 (detalle en ficha 00). Lo de arriba (AEA 770) manda. Lo de abajo se cita como "según Farina", con el código de la nota.

### Conceptos (FA1)
- "Sistema de puesta a tierra" (SPAT): conjunto de elementos interconectados, no un solo electrodo.
- Dos tipos: de **seguridad** (protege personas y bienes) y **funcional** (operación del sistema eléctrico).
- La "resistencia de puesta a tierra" (Rpat) es en realidad una **impedancia**. Se mide en Ω.
- La **resistividad del terreno** (ρ) es propia del suelo. Se mide en **Ω·m**. Es la resistencia de un cubo de terreno de 1 m de lado.
- La resistividad cambia con la humedad (estaciones, napas), las sales, la temperatura, la granulometría y los estratos.
- El calentamiento del terreno por corrientes de falla elevadas **aumenta** su resistividad.
- Se mide con el método **Wenner** (cuatro electrodos) (FA1 y FA5).
- En obras chicas se reconoce el terreno y se toma un valor de tabla. Los cálculos de PAT siempre son aproximados (FA5).

### Resistividades típicas (FA1 tabla 1; FA5 tabla 1)
Valores medios orientativos. FA5 imprime "Ω/m": la unidad correcta es Ω·m.

| Terreno | ρ (Ω·m) |
|---|---|
| Pantanoso | 30 |
| Arcilloso, de greda, labrantío | 100 |
| Arena húmeda | 200 |
| Grava húmeda | 500 |
| Arena o grava seca | 1.000 |
| Rocoso | 3.000 |

### Tensión de paso y tensión de contacto (FA2)
- Al circular corriente por la PAT, el potencial del suelo sube junto al electrodo y baja con la distancia.
- **Tensión de paso:** entre los dos pies de una persona, separados 0,8 a 1 m.
- **Tensión de contacto:** entre una mano que toca la masa y los pies (unos 1 m en horizontal), o entre las dos manos.
- La 770 fija el objetivo: tensión de contacto ≤ **24 V** (ficha 05, 770.14.3.2).

### Equipotencialización (FA2)
- Es interconectar todas las masas propias y ajenas del edificio y llevarlas a la PAT.
- Masas ajenas que se conectan: cañerías de agua y gas, caños de la instalación eléctrica, estructuras metálicas (escaleras, conductos, rampas).
- Se usa una barra equipotencial principal y, si hace falta, barras secundarias interconectadas.
- Equipos que FA2 conecta **directo a la barra principal:** pararrayos, aire acondicionado central de azotea, antenas satelitales, estructuras decorativas, tendederos, carcasas de reflectores grandes.
- Obras: máquinas, andamios y escaleras metálicas van conectados rígidamente a tierra. FA2 recomienda verificar la continuidad de esas conexiones **cada 2 o 3 días** (recomendación del autor, no de la 770).

### Tipos de electrodo (FA4, confiabilidad media)
- **Jabalina** simple: lo más común; también en paralelo o con conductor enterrado horizontal.
- **Placa** horizontal o vertical (cobre o acero galvanizado): sistemas de datos y pisos técnicos.
- **Triángulo:** 3 jabalinas unidas por conductor enterrado. Baja resistencia y buena dispersión de fallas y rayos.
- **Cruz** y **pata de ganso:** conductores horizontales a 0,5–0,75 m de profundidad. Usadas en pararrayos.
- **Malla:** conductores de cobre enterrados a 0,8–0,9 m, con derivaciones soldadas a columnas y cargas grandes.
- **Perimetral o anillo:** conductor alrededor del edificio con una jabalina en cada esquina.
- **Fundaciones:** hierros de las bases de hormigón armado interconectados por soldadura.
- La resistividad del terreno puede decidir el tipo a usar.

### Materiales (FA5)
- **Jabalina IRAM 2309:** acero revestido de cobre, sección cilíndrica, acoplable. Largos de **1,5 y 3 m**. Diámetros comerciales **12,6 / 14,6 / 16,2 mm** (1/2", 5/8", 3/4").
- **Cable de PAT:** cobre multifilar, PVC verde-amarillo, IRAM NM 247-3. Sección según tabla 771-C.II (misma regla que la Tabla 770.14.I de arriba).
- **Conductor enterrado** (por ejemplo, para unir dos jabalinas): cobre de 7 hilos IRAM 2004, o acero recubierto de cobre (IRAM 2466 y 2467).
- Accesorios: grapa tomacable, caja de inspección, acople, punta y sufridera. Sus resistencias de unión se desprecian en el cálculo.

### Sección mínima del conductor enterrado · NO publicar una cifra
- FA5 dice cobre enterrado de **35 mm²** mínimo.
- FA6 (tabla 1, atribuida a la reglamentación) da otros mínimos para conductor de PAT enterrado:

| | Con protección mecánica | Sin protección mecánica |
|---|---|---|
| Con protección contra corrosión | 2,5 mm² Cu · 10 mm² Fe | 16 mm² Cu · 16 mm² Fe |
| Sin protección contra corrosión | 25 mm² Cu · 50 mm² Fe | 25 mm² Cu · 50 mm² Fe |

- Las dos notas del mismo autor no coinciden y la 770 no da este valor. Verificar en la AEA antes de afirmar.

### Unión cable–jabalina (FA6)
- Con soldadura cuproaluminotérmica, conector a presión u otro elemento diseñado para eso.
- Desmontable para medir. Protegida dentro de cámara o caja.
- Coincide con 770.14.4.1 y 770.14.4.3 (arriba).

### PE de distinto material que la fase (FA6, tabla 2)
- Misma regla de la Tabla 770.14.I, multiplicada por **k1 / k2** si el PE no es del mismo material que la fase.
- k1: del conductor de fase (Tabla 771.19.II; cobre-PVC = 115, aluminio-PVC = 76).
- k2: del PE (tablas 771-C.III a 771-C.VII según cómo está instalado).
- FA6 da como mínimo de PE separado del cable de alimentación: 2,5 mm² Cu con protección mecánica y 4 mm² Cu sin ella. **En viviendas de la 770 el PE va siempre dentro de la canalización del circuito y nunca baja de 2,5 mm²** (arriba).

### Resistencia de una jabalina (FA7, con cita a AEA 90364-7-771, sección 771-C-10)
- Fórmula:  **R = ρ / (2π·L) · [ ln(8·L / d) − 1 ]**
  - R en Ω; ρ resistividad del terreno en Ω·m; L largo enterrado en m; d diámetro en m.
- Variables: ρ la fija el terreno. L y d vienen de IRAM 2309.
- **No usar la tabla 1 de FA7**: sus valores no coinciden con la fórmula (ficha 00).
- Valores calculados con la fórmula (cuenta propia, ρ = 50 Ω·m):

| Largo enterrado | 1/2" (12,6 mm) | 5/8" (14,6 mm) | 3/4" (16,2 mm) |
|---|---|---|---|
| 1,5 m | 31,1 Ω | 30,3 Ω | 29,7 Ω |
| 3 m | 17,4 Ω | 17,0 Ω | 16,7 Ω |
| 4,5 m | 12,3 Ω | 12,0 Ω | 11,9 Ω |
| 6 m | 9,6 Ω | 9,4 Ω | 9,3 Ω |

- Lecturas de la tabla (cuenta propia):
  - R es proporcional a ρ: con ρ = 100 Ω·m, los valores se duplican (1,5 m de 5/8" → 60,6 Ω).
  - Alargar la jabalina baja mucho R. Engrosarla baja poco (de 1/2" a 3/4" a 3 m: −4 %).
  - Son valores teóricos. El valor real se **mide** (770.19.5.3, arriba).
