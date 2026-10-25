Un termotanque eléctrico lleva un circuito que sale de su corriente, no de los litros ni de la marca: se toma la potencia de la placa, se la pasa a amperes y con ese número se elige el tipo de circuito, el cable y la termomagnética. Lo más prolijo es darle un circuito exclusivo, sin otros aparatos ni derivaciones, con diferencial de 30 mA, termomagnética bipolar y 2,5 mm² como mínimo, verificando siempre que el cable aguante la térmica (IB ≤ In ≤ Iz).

## Primero la corriente: qué dice la placa

La reglamentación AEA 90364 clasifica los circuitos por la corriente de la carga y por el tipo de toma. Por eso el punto de partida es la potencia de la placa del equipo, que se convierte a corriente dividiendo por la tensión: I = P / 220 V. Dos ejemplos orientativos, solo para entender la cuenta (la placa del modelo que instalás es la que manda):

- Un equipo de 1.500 W consume alrededor de 6,8 A.
- Un equipo de 3.000 W consume alrededor de 13,6 A.

Esa corriente es la corriente de proyecto, la IB de la verificación que se hace más abajo. Antes de dibujar nada, leé la placa y el manual del equipo.

## Qué tipo de circuito corresponde

La AEA 90364-7-770 define los circuitos terminales según la corriente de cada toma:

- **TUG (tomacorrientes de uso general):** tomas 2P+T de 10 A para cargas unitarias de hasta 10 A. Protección máxima de 20 A en ambos polos.
- **TUE (tomacorrientes de uso especial):** tomas 2P+T de 20 A IRAM 2071 para cargas de más de 10 A y hasta 20 A. Protección máxima de 32 A en ambos polos.
- **Circuito de uso específico (ACU):** alimenta **una sola carga, sin ninguna derivación**, por conexión fija o por una toma dedicada. En viviendas, la 770 remite a la AEA 90364-7-771 para estos circuitos (771.7.6). La sección mínima es 2,5 mm² y la protección la fija el proyectista según el equipo.

Con esa lógica, un termotanque de hasta 10 A entra en el rango de una toma de 10 A y uno de más de 10 A y hasta 20 A necesita una toma de 20 A. Pero la norma no obliga a elegir una u otra: lo que importa es que la toma y el circuito soporten la corriente del equipo. Como criterio de EGC, y no como una exigencia de la norma, conviene darle al termotanque su propio circuito: es una carga de potencia importante, y compartirla con tomas de uso general mezcla en el mismo cable a un aparato que consume mucho con otros que se enchufan y desenchufan. Un ACU o un TUE de una sola boca resuelve las dos cosas.

## Las protecciones del circuito

**Diferencial de 30 mA.** Todos los circuitos terminales llevan un diferencial de 30 mA como máximo, sin retardo (AEA 90364-7-770, 770.14.2.3). El del termotanque no es una excepción.

**Termomagnética bipolar.** En monofásico, las protecciones de circuito son bipolares con los dos polos protegidos. Están prohibidas las unipolares, las marcadas 1P+N y las de neutro pasante (770.16.5.1). La termomagnética tiene que cumplir IEC 60898-1 y poder bloquearse en abierto.

**El PE.** El equipo es una masa metálica: el conductor de protección llega hasta el termotanque y se conecta al borne de tierra del equipo. El PE mínimo es 2,5 mm² (Tabla 770.11.I) y las masas se conectan por derivación, nunca en serie.

## Cable y térmica: IB ≤ In ≤ Iz

La sección mínima de un TUE o de un circuito de uso específico es 2,5 mm² (Tabla 770.11.I). Pero es un piso, no un cálculo. Después de elegir la sección se verifica que la corriente del equipo, la termomagnética y el cable cumplan:

- **IB** es la corriente del equipo.
- **In** es el calibre de la termomagnética.
- **Iz** es la corriente admisible del cable.

Para 2,5 mm² en caño, en monofásico, la tabla da Iz = 21 A (Tabla 770.12.I). Por eso la térmica no puede pasar de 20 A. Dos combinaciones que cumplen:

- Equipo de 1.500 W (6,8 A): térmica de 10 A, cable de 2,5 mm². Se verifica 6,8 ≤ 10 ≤ 21.
- Equipo de 3.000 W (13,6 A): térmica de 16 A, cable de 2,5 mm². Se verifica 13,6 ≤ 16 ≤ 21.

Si en el mismo caño van dos circuitos monofásicos, la corriente admisible se multiplica por 0,80: 21 × 0,8 = 16,8 A, y ya no admite una térmica de 20 A. Por eso la forma en que se canaliza también cuenta.

## Caída de tensión

En circuitos terminales de tomas, el límite es 3 % desde el tablero principal (770.15.6). Con la tabla rápida de la 770 (Tabla 770.15.IV), un cable de 2,5 mm² da 15 V/(A·km). Ejemplo: 13,6 A a 15 m del tablero dan 15 × 13,6 × 0,015 = 3,06 V, alrededor del 1,4 % de 220 V. Cumple. Si el termotanque quedara mucho más lejos, hay que recalcular con una sección mayor. La caída se verifica siempre, aunque la casa sea chica.

## Puesta a tierra y cañerías

Un caso de obra que figura en la bibliografía técnica: un termotanque con una falla, unido al PE por la ficha y a un caño metálico que más adelante sigue en plástico. Ese tramo de caño metálico puede quedar electrificado. Por eso las masas extrañas (caños metálicos de agua y gas, estructuras) se unen a la barra equipotencial principal. En un termotanque, antes de dar por buena la instalación, medí la continuidad del PE hasta el equipo y revisá cómo quedó vinculada la cañería metálica.

## Errores comunes en obra

- Enchufar el termotanque a una toma de uso general compartida con otros aparatos.
- Elegir la térmica por la potencia del equipo sin verificar que el cable la aguante.
- Usar una termomagnética unipolar o 1P+N en un circuito monofásico.
- Dejar al termotanque sin PE, o con un PE conectado a un toma de tres espigas cuya espiga de tierra no está conectada a nada.
- Usar un cordón tipo taller como instalación fija: está prohibido (770.10.1).

## Preguntas frecuentes

**¿Un termotanque eléctrico lleva circuito propio?** La norma decide por la corriente del equipo y el tipo de toma. Un circuito exclusivo, ya sea un TUE de una sola boca o un ACU, es el criterio de EGC porque el termotanque es una carga de potencia relevante.

**¿Alcanza con 2,5 mm²?** Es el mínimo. Para muchos equipos domésticos alcanza, siempre que se verifique IB ≤ In ≤ Iz y la caída de tensión. Si la corriente supera lo que admite el cable, se sube la sección.

**¿Lleva diferencial?** Sí. Todos los circuitos terminales llevan un diferencial de 30 mA como máximo.

## Cómo te ayuda EGC

Con la [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) podés verificar la sección, la termomagnética y la caída de tensión del circuito de un termotanque antes de presupuestar. Así le presentás al cliente un trabajo con el cable y la protección ya calculados.

## Fuentes

- AEA 90364-7-770, edición 2017: 770.14.2.3, 770.16.5.1, 770.15.6, 770.10.1, Tabla 770.11.I, Tabla 770.12.I, Tabla 770.15.IV.
- AEA 90364-7-771: 771.7.6.
- Fichas de la base de conocimiento técnico de EGC.
