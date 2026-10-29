En una instalación monofásica de vivienda, las termomagnéticas de los circuitos tienen que ser bipolares y con los dos polos protegidos: uno para la fase y otro para el neutro. La AEA 90364-7-770 prohíbe las unipolares, las bipolares con "neutro no protegido", el "neutro pasante" y las marcadas 1P+N. En trifásico, la regla equivalente es la tetrapolar con todos los polos protegidos.

## Qué dice la norma sobre las protecciones en el tablero

La cláusula 770.16.5 de la AEA 90364-7-770 (edición 2017) ordena los dispositivos que van en un tablero de vivienda. Los puntos que importan para este tema son cuatro:

- Las cabeceras de todos los tableros seccionan el neutro.
- En monofásico, las protecciones de los circuitos son bipolares con los dos polos protegidos. En trifásico, tetrapolares.
- Las termomagnéticas tienen que cumplir IEC 60898-1, poder bloquearse en abierto (con candado o precinto) y abrir y cerrar todos los polos a la vez.
- Cada circuito terminal y cada seccional queda protegido contra contactos directos e indirectos, sobrecargas y cortocircuitos.

Fijate que la regla no habla solo de "poner dos polos". Pide que los dos polos estén protegidos, es decir, que la protección actúe sobre fase y neutro, y que al maniobrar la llave se abran los dos a la vez.

## Qué está prohibido en monofásico

La cláusula 770.16.5.1 es explícita. En una instalación monofásica no se aceptan:

- Termomagnéticas unipolares.
- Bipolares con "neutro no protegido".
- Bipolares con "neutro pasante".
- Las marcadas 1P+N.
- Los combinados termomagnética-diferencial que tengan la protección en un solo polo.

El caso que más confunde es el 1P+N: a simple vista parece una bipolar, pero la norma lo nombra aparte y lo deja afuera. Antes de comprar o de reemplazar una térmica, mirá el marcado del frente y la hoja de datos, y no te guíes por la cantidad de bornes.

## La cabecera del tablero principal

La cabecera del tablero principal es una termomagnética de 63 A como máximo (770.16.5.3). Si la corriente es mayor, el caso pasa a la AEA 90364-7-771. En monofásico es bipolar con los dos polos protegidos; en trifásico, tetrapolar con todos los polos protegidos. Puede llevar un diferencial asociado.

En los tableros seccionales (770.16.5.4), la cabecera es un dispositivo de corte general con aptitud de seccionamiento garantizada. Puede ser:

- Un interruptor-seccionador bipolar o tetrapolar.
- Una termomagnética bipolar con ambos polos protegidos, o tetrapolar.
- Un diferencial IEC 61008 o IEC 61009.

Si la cabecera del seccional no es diferencial, los circuitos que lo necesitan llevan su diferencial propio o agrupado, y cada circuito derivado lleva su termomagnética.

## Cómo queda el tablero armado

Un esquema simple para una vivienda monofásica, de arriba hacia abajo:

- Cabecera: termomagnética bipolar, 63 A como máximo, que secciona el neutro.
- Diferencial de 30 mA, no retardado, en los circuitos terminales.
- Una termomagnética bipolar por cada circuito.
- Barra de neutro y barra de PE identificadas.

Recordá además que todo lo que sale por un diferencial vuelve por ese mismo diferencial: el neutro de cada circuito se conecta aguas abajo del diferencial que lo protege, no a una bornera de neutro común. Y que el diferencial también hay que protegerlo: su corriente nominal tiene que ser mayor o igual que la de la termomagnética en serie aguas arriba, o que la suma de las termomagnéticas que tiene aguas abajo (770.15.2.2.5).

Además, en el tablero va un solo cable por borne, salvo que el borne esté hecho para recibir más de uno (770.16.4).

## Errores comunes en obra

- Colocar una termomagnética unipolar en la fase y dejar el neutro sin maniobra ni protección.
- Usar una marcada 1P+N porque entra más circuitos en el mismo riel.
- Dejar el neutro "pasante" por el tablero, sin pasar por ningún polo.
- Reemplazar un diferencial por otro de distinta marca o características sin volver a verificar la protección del conjunto.
- Armar una barra de neutro común para varios diferenciales, de modo que el neutro de un circuito no vuelva por el diferencial que lo protege.

## Preguntas frecuentes

**¿Una termomagnética de dos bornes es siempre bipolar?** No. Una marcada 1P+N puede tener dos bornes, pero la norma la prohíbe en monofásico. Tiene que ser bipolar con los dos polos protegidos.

**¿Alcanza con que la cabecera sea bipolar?** No. Las cabeceras seccionan el neutro, y además las protecciones de cada circuito son bipolares con los dos polos protegidos. Son dos requisitos distintos.

**¿La termomagnética protege contra una falla a tierra?** En el esquema TT, que es el que rige en vivienda, la protección contra contactos indirectos por corte automático la da el diferencial. La termomagnética no sirve para eso. Cada una cumple su función: la térmica protege de sobrecargas y cortocircuitos; el diferencial de 30 mA, de las fugas a tierra y como protección complementaria contra contactos directos.

## Cómo te ayuda EGC

Cuando armás el tablero de un presupuesto, conviene dejar anotado qué protección lleva cada circuito. Con el [tablero en EGC](https://egc.globalepika.net.ar/tablero-electrico/) y el [esquema unifilar](https://egc.globalepika.net.ar/esquema-unifilar/) lo ves completo antes de comprar los materiales y llegás a la obra con la lista cerrada.

## Fuentes

- AEA 90364-7-770, edición 2017, 770.16.5.1 (dispositivos prohibidos en monofásico).
- AEA 90364-7-770, 770.16.5.2 (requisitos de las termomagnéticas).
- AEA 90364-7-770, 770.16.5.3 (cabecera del tablero principal) y 770.16.5.4 (cabecera de tableros seccionales).
- AEA 90364-7-770, 770.15.2.2.5 (protección del diferencial) y 770.14.3.2 (contactos indirectos en esquema TT).
- AEA 90364-7-770, 770.16.4 (construcción del tablero).
- Fichas de la base de conocimiento técnico de EGC.
