La vivienda tiene que tener su propia toma de tierra, independiente de la de la distribuidora y dentro del inmueble, con una resistencia de **40 Ω como máximo**. De esa toma sale un cable de puesta a tierra de **4 mm² como mínimo** hasta la barra de tierra del tablero principal, y desde esa barra recorre toda la instalación el conductor de protección (PE), verde-amarillo, de **2,5 mm² como mínimo**. Así lo pide la AEA 90364-7-770 para el esquema TT, que es el que se usa en viviendas.

## Qué es el esquema TT y qué pide la toma de tierra

En el esquema TT la vivienda tiene su **propia toma de tierra de protección**, eléctricamente independiente de la tierra de servicio de la distribuidora. Esa toma queda dentro de los límites del inmueble y se une a todas las masas mediante el conductor PE (AEA 90364-7-770, 770.3.2).

El valor que manda es la resistencia de esa toma: **40 Ω como máximo**, de forma permanente. Se puede lograr con una jabalina o con varios electrodos, siempre que estén todos interconectados con un conductor desnudo enterrado.

Un detalle que genera confusión: la puesta a tierra suplementaria que algunas distribuidoras piden unir al neutro en la entrada es un refuerzo de la tierra de servicio. **No** es la tierra de protección de la vivienda.

## La separación entre tierras

La toma de protección tiene que estar a más de **10 veces el radio equivalente** del electrodo más largo, medido desde la toma de servicio más cercana. La tabla 770.3.I da esa distancia para jabalinas IRAM 2309 y 2310: va de unos 3,2 m para una jabalina de 1,5 m hasta unos 10 m para una de 6 m, según diámetro y largo. Por ejemplo, una jabalina de 1,5 m pide entre 3,2 y 3,4 m, y una de 3 m, entre 5,4 y 5,8 m.

## Los electrodos y las uniones enterradas

Los electrodos pueden ser jabalinas, cintas, placas o cables, siempre según normas IRAM. Las jabalinas son la IRAM 2309 (acero-cobre) y la IRAM 2310 (acero cincado).

Las uniones enterradas se hacen con soldadura cuproaluminotérmica. Si las piezas son de igual sección, también se admite compresión oval o hexagonal, o conexión por compresión en frío según IRAM 2349.

## La cámara de inspección

La unión entre el electrodo y el cable de puesta a tierra se hace dentro de una **cámara de inspección**, con tapa removible a nivel del piso terminado. Se recomienda ubicarla en un lugar no transitado y despejado, para poder inspeccionarla y medir.

Dentro de la cámara, la conexión se hace sobre una **barra de cobre con puentes removibles**, para poder desconectar y medir la toma. Con una sola jabalina IRAM 2309 se puede conectar el cable con el tomacable de bronce o latón (IRAM 2343).

## El cable de puesta a tierra: 4 mm² mínimo

Es el cable que va de la toma de tierra a la barra principal de tierra o barra equipotencial principal. Reglas que conviene tener a mano:

- Sección mínima **4 mm²**.
- Se recomienda que entre por el **tablero principal**, porque ayuda contra sobretensiones. Si no se puede, por la caja o tablero más cercano a la toma.
- Va **independiente** del conductor PE, aunque compartan canalización, y llega a la barra equipotencial principal.

La sección del PE y la del cable de puesta a tierra siguen la tabla 770.14.I. Si la fase es de hasta 16 mm², son iguales a la fase. Entre 16 y 35 mm², 16 mm². Por encima de 35 mm², la mitad de la fase. En todos los casos respetando los mínimos: 2,5 mm² para el PE y 4 mm² para el cable de puesta a tierra.

## El conductor PE dentro de la vivienda

El PE es de cobre aislado, color verde-amarillo, y recorre **toda** la instalación desde la barra principal de tierra, incluidas las cajas y bocas que no tienen tomacorriente (770.14.4.5). Nunca va con menos de **2,5 mm²**. Va en la misma canalización que los demás cables de su circuito.

Las cajas, gabinetes y caños metálicos se conectan con **derivaciones** verde-amarillo tomadas del PE sin cortarlo. **No se permite conectar las masas en serie**, la llamada "guirnalda": si se saca un aparato, no puede quedar sin tierra el siguiente. Las canalizaciones metálicas no reemplazan al PE, aunque igual tienen que quedar puestas a tierra.

La derivación al borne de tierra de tableros, cajas, canalizaciones, equipos y tomacorrientes es de cobre aislado verde-amarillo de 2,5 mm² como mínimo (770.14.4.6). En el tablero tiene que haber una barra, placa o bornera de PE identificada, con bornes suficientes para todos los circuitos.

## Cómo se mide

Se mide preferentemente con **telurímetro**, con la toma **desconectada** de todo lo que tiene vinculado, por eso existen los puentes removibles de la cámara (770.14.4.1 y 770.19.5.3). Como método alternativo de referencia, la norma describe inyectar corriente entre la toma y un electrodo auxiliar lejano, y medir la tensión con un segundo electrodo auxiliar ubicado a aproximadamente el 62 % de esa distancia. La resistencia es V / I. Se repite corriendo el auxiliar 1 m más lejos y 1 m más cerca, y si las tres lecturas coinciden, se promedian. En TT también se puede medir la impedancia de lazo en lugar de la resistencia de puesta a tierra.

## Errores comunes en obra

- Medir la jabalina con la barra del tablero conectada, en lugar de con la toma desconectada.
- Unir el cable de la jabalina sin cámara de inspección, de modo que después no se puede medir.
- Hacer el PE en "guirnalda", pasando de una caja a otra cortando el conductor en cada una.
- Cortar el PE en cajas y bocas sin tomacorriente, o no llevarlo a ellas.
- Confundir la puesta a tierra suplementaria unida al neutro con la tierra de protección, o usar el caño metálico como si fuera el PE.

## Preguntas frecuentes

**¿Alcanza con una jabalina?** Depende del valor que mida. La exigencia es que la resistencia de la toma de tierra de protección sea de 40 Ω como máximo. Se pueden usar varios electrodos interconectados si con uno solo no se llega, y el resultado real se verifica con la medición.

**¿El cable de la jabalina es el mismo que el PE?** No. El cable de puesta a tierra, de 4 mm² mínimo, va de la toma a la barra principal de tierra. El PE, de 2,5 mm² mínimo, sale de esa barra y recorre la instalación. Son conductores independientes, aunque compartan canalización.

**¿Con puesta a tierra ya no hace falta el diferencial?** Hace falta igual. En TT el diferencial es la protección aceptada contra contactos indirectos por corte automático, y todos los circuitos terminales llevan diferencial de 30 mA como máximo (770.14.3.2 y 770.14.2.3).

## Cómo te ayuda EGC

Una puesta a tierra bien hecha termina con una medición y un papel que la respalde. El [protocolo SRT 900/15 en EGC](https://egc.globalepika.net.ar/protocolo-puesta-a-tierra-srt-900-15/) te ayuda a documentar el valor medido y entregarlo al cliente.

## Fuentes

- AEA 90364-7-770, 770.3.2 y Tabla 770.3.I: esquema TT, 40 Ω, separación entre tierras.
- AEA 90364-7-770, 770.14.4.1: toma de tierra y medición con la toma desconectada.
- AEA 90364-7-770, 770.14.4.3 y 770.14.4.4: cámara de inspección y cable de puesta a tierra.
- AEA 90364-7-770, Tabla 770.14.I: sección del PE y del cable de puesta a tierra.
- AEA 90364-7-770, 770.14.4.5 y 770.14.4.6: conductor PE y conexión de las masas.
- AEA 90364-7-770, 770.19.5.3: medición.
- AEA 90364-7-770, 770.14.3.2 y 770.14.2.3: diferencial en TT.
- Fichas de la base de conocimiento técnico de EGC.
