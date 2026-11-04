La cantidad de jabalinas no la fija una regla: la fija el terreno. La AEA 90364-7-770 pide que la toma de tierra de la vivienda tenga una resistencia de **40 Ω como máximo** y que se verifique midiéndola. Con una jabalina alcanza si el terreno es bueno; si el terreno es seco, arenoso o rocoso, hace falta más largo, más jabalinas en paralelo, o ambas cosas. Y entre el largo y el diámetro, el que más pesa es el largo.

## Qué exige la reglamentación

En el esquema TT, que es el de las viviendas, la toma de tierra de protección tiene una resistencia de **40 Ω como máximo, de forma permanente** (AEA 90364-7-770, 770.3.2). Se mide sobre el conjunto de electrodos, **desconectado** de todo lo que tiene vinculado (770.14.4.1).

La norma admite usar varios electrodos, siempre que estén todos interconectados con un conductor desnudo enterrado. Lo que no hace es decir "una jabalina" o "dos jabalinas": el número sale de lo que dé la medición.

## Qué cambia de un terreno a otro

La propiedad del terreno que importa es la **resistividad**, que se mide en **Ω·m**. Cambia con la humedad (la época del año y las napas), las sales disueltas, la temperatura, el tamaño de los granos y las capas del suelo. Los rellenos son impredecibles.

Como referencia, estos son valores orientativos de resistividad:

- Terreno pantanoso: unos 30 Ω·m.
- Arcilloso, greda o tierra de cultivo: unos 100 Ω·m.
- Arena húmeda: unos 200 Ω·m.
- Grava húmeda: unos 500 Ω·m.
- Arena o grava seca: unos 1.000 Ω·m.
- Rocoso: unos 3.000 Ω·m.

Son valores de referencia, no de proyecto. En obras grandes la resistividad se mide antes de proyectar, con el método Wenner. En una vivienda lo que vale es la **medición final** de la toma con telurímetro y el límite de 40 Ω.

## Cuánto da una jabalina

Una tabla de un artículo técnico, calculada para un terreno de **50 Ω·m**, da estos valores de resistencia para una jabalina de 5/8":

- 1,5 m de largo: 35,2 Ω.
- 3 m de largo: 19,4 Ω.
- 4,5 m de largo: 13,7 Ω.
- 6 m de largo: 10,6 Ω.

Es una tabla conservadora: da valores algo más altos que otros métodos de cálculo. Sirve para entender las proporciones, no para reemplazar la medición ni las tablas del fabricante de la jabalina.

De esa tabla salen dos ideas prácticas:

- **El largo pesa mucho más que el diámetro.** Pasar de 1/2" a 3/4" baja la resistencia alrededor de un 5 %. Pasar de 1,5 m a 3 m la baja alrededor de un 45 %.
- **La resistencia es proporcional a la resistividad.** Con un terreno de 100 Ω·m en vez de 50, los valores de la tabla se duplican. Una jabalina de 1,5 m, que en el ejemplo da 35,2 Ω, daría unos 70 Ω: no llega a los 40 Ω. Por eso en terrenos secos o arenosos una sola jabalina corta puede no alcanzar.

## Qué hacer cuando una jabalina no alcanza

Las opciones son dos:

- **Alargar la jabalina.** Las jabalinas IRAM 2309 (acero revestido de cobre) vienen en tramos acoplables de 1,5 y 3 m, con diámetros comerciales de 1/2", 5/8" y 3/4".
- **Poner varias jabalinas en paralelo**, unidas con conductor desnudo enterrado. La jabalina simple es lo más común en vivienda, pero también se usan varias en paralelo. Una variante es el triángulo, con tres jabalinas unidas por el conductor enterrado.

Las uniones enterradas se hacen con soldadura cuproaluminotérmica; si las piezas son de igual sección, también se admite compresión oval o hexagonal o conexión por compresión en frío según IRAM 2349. Todo conjunto tiene que poder **desarmarse para medir**: por eso la conexión se hace en una cámara de inspección, sobre una barra de cobre con puentes removibles.

Las jabalinas tienen que respetar además la separación con la toma de tierra de servicio de la distribuidora ("tierra lejana"): más de 10 veces el radio equivalente del electrodo más largo.

## Cómo se mide

La norma prefiere el **telurímetro**. El método alternativo de referencia hace circular corriente entre la toma y un electrodo auxiliar lejano, y mide la tensión contra un segundo auxiliar ubicado a aproximadamente el 62 % de esa distancia. La resistencia es R = V / I. Se repite corriendo el segundo auxiliar 1 m más lejos y 1 m más cerca; si las tres lecturas coinciden, se promedian.

## Errores comunes en obra

- Clavar una jabalina corta en un terreno seco y dar por buena la tierra sin medir.
- Medir con la jabalina todavía conectada a la instalación: la norma pide medir la toma desconectada.
- Preocuparse por el diámetro y no por el largo: cambiar de 1/2" a 3/4" mejora poco; duplicar el largo mejora mucho.
- Enterrar las uniones sin cámara de inspección, de modo que después no se puede desconectar para medir.
- Usar caños de agua o canillas como "tierra": su continuidad es incierta y no reemplazan a la toma de tierra.

## Preguntas frecuentes

**¿Una sola jabalina alcanza para una vivienda?** Depende del terreno. Si la medición da 40 Ω o menos, sí. Si da más, hay que alargarla o agregar otras en paralelo.

**¿Por qué la medición manda sobre las tablas?** Porque la resistividad cambia con la humedad, las sales y las capas del suelo. Las tablas son de referencia; el límite de 40 Ω se verifica sobre la toma real.

**¿Sirve poner una jabalina más gruesa?** Ayuda poco. En la tabla de referencia, pasar de 1/2" a 3/4" baja la resistencia alrededor de un 5 %, mientras que duplicar el largo la baja alrededor de un 45 %.

## Cómo te ayuda EGC

Cuando entregás una instalación, la medición de la puesta a tierra queda registrada en el protocolo. EGC te ayuda a armar ese documento: la firma y la responsabilidad son del profesional interviniente. Podés verlo en [protocolo SRT 900/15 en EGC](https://egc.globalepika.net.ar/protocolo-puesta-a-tierra-srt-900-15/).

## Fuentes

- AEA 90364-7-770 (edición 2017), 770.3.2: esquema TT y resistencia de la toma de tierra.
- AEA 90364-7-770, 770.14.4.1 a 770.14.4.3: toma de tierra, uniones y cámara de inspección.
- AEA 90364-7-770, 770.19.5.3: medición de la puesta a tierra.
- Artículos técnicos de la revista Ingeniería Eléctrica sobre sistemas de puesta a tierra (valores orientativos de resistividad y de resistencia de jabalinas).
- Fichas de la base de conocimiento técnico de EGC.
