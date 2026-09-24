# 06 · Puesta a tierra y conductor de protección

Fuente: AEA 90364-7-770, edición 2017.

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
