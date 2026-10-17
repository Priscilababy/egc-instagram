Un split lleva un circuito exclusivo, sin otros aparatos ni derivaciones, con un diferencial de 30 mA, una termomagnética bipolar y un cable de 2,5 mm² como mínimo. El circuito no se decide por las frigorías: se decide por la corriente que marca la placa del equipo y por el tipo de toma o conexión. Después se verifica que la termomagnética proteja al cable (IB ≤ In ≤ Iz) y que la caída de tensión no pase del límite.

## Qué dice la norma sobre el circuito

Ni la AEA 90364-7-770 ni la 90364-7-771 fijan una regla del tipo "a partir de tantas frigorías va circuito propio". Esa regla no existe, y conviene no repetirla en obra ni en un presupuesto. Lo que sí hacen las normas es clasificar los circuitos según la corriente de la carga y el tipo de toma:

- **Toma de 10 A (TUG):** solo para cargas de hasta 10 A por toma.
- **Toma de 20 A en circuito TUE (uso especial):** para cargas de más de 10 A y hasta 20 A, con toma 2P+T de 20 A IRAM 2071. Es un circuito de uso especial que puede tener varias bocas.
- **Circuito ACU (uso específico):** alimenta **un solo equipo, sin ninguna derivación**, por conexión fija o por una toma dedicada. En viviendas, la 770 remite a la 771 para este tipo de circuito.

En la práctica, la forma que cumple con la norma y también con los fabricantes es **un circuito exclusivo por equipo**: un TUE de una sola boca o un ACU. Los cuatro manuales de fabricantes que revisamos piden línea exclusiva, sin otros aparatos, y sin alargues. Aunque la norma permitiera compartir un TUE, manda el manual: instalar fuera de lo que pide el fabricante puede hacer perder la garantía.

## Las protecciones del circuito

**Diferencial de 30 mA.** Todos los circuitos terminales llevan diferencial de 30 mA como máximo, sin retardo (AEA 90364-7-770, 770.14.2.3). El circuito del aire no es una excepción. Ningún manual de fabricante lo menciona, pero la norma lo exige. La 771 admite una única excepción para un ACU donde se demuestre que el diferencial perturba el equipo, con una protección alternativa; no es el caso de un split domiciliario común.

**Termomagnética bipolar.** En monofásico, las protecciones de circuito son bipolares con los dos polos protegidos. Están prohibidas las unipolares, las marcadas 1P+N y las de "neutro pasante" (770.16.5.1).

**Corte omnipolar.** Los cuatro manuales piden un interruptor que corte todos los polos, y tres de ellos piden además una separación de contactos de al menos 3 mm. Hay que verificar ese dato en el interruptor que se elige: no es algo que se pueda dar por hecho.

## Cable y sección

La sección mínima para TUE y para circuitos de uso específico es **2,5 mm²** (Tabla 770.11.I). Pero ese es un piso, no un cálculo: la sección se elige con la corriente de la placa, y después se verifica la condición **IB ≤ In ≤ Iz**:

- IB es la corriente que consume el equipo.
- In es el calibre de la termomagnética.
- Iz es la corriente admisible del cable en las condiciones de instalación.

Para un cable de 2,5 mm² en caño, monofásico, la corriente admisible es de 21 A (Tabla 770.12.I). Por lo tanto la termomagnética no puede pasar de 20 A. Un ejemplo que cumple: un equipo de 15 A en placa, termomagnética de 16 A, cable de 2,5 mm². Se verifica así: 15 ≤ 16 ≤ 21.

Algunos manuales piden una protección de "1,5 veces la capacidad máxima de la unidad". Esa cuenta no reemplaza la verificación anterior: si el resultado supera lo que admite el cable, no se sube la térmica, se sube la sección del cable. Los fabricantes dan además una guía por corriente (hasta 16 A, 2,5 mm²; de 16 a 25 A, 4 mm²; de 25 a 40 A, 6 mm²), que igual hay que contrastar con la verificación de la norma y con la caída de tensión.

## Caída de tensión

Para circuitos terminales de tomas, el límite es **3 %** desde el tablero principal (770.15.6). La norma admite 5 % solo en circuitos que alimentan únicamente motores; para un split, calcular con 3 % es el criterio más seguro. Con la tabla rápida de la 770 (Tabla 770.15.IV), un cable de 2,5 mm² da 15 V/(A·km). Ejemplo: 15 A a 20 m de distancia dan 15 × 15 × 0,020 = 4,5 V, alrededor del 2 % de 220 V. Cumple. Si la distancia fuera mucho mayor, hay que recalcular con una sección más grande.

## Caño, conexión y tierra

- **Caño propio.** Un circuito de uso específico no comparte caño con circuitos de uso general o especial (771.12.3.13.2 d).
- **Conexión fija.** El caño puede llegar hasta la caja de conexión del equipo.
- **Nada de cordones tipo taller.** Están prohibidos como instalación fija (770.10.1).
- **Puesta a tierra.** Es obligatoria en los cuatro manuales y en la norma: el PE llega a las dos unidades. En un aparato de conexión fija, el PE va dentro del mismo cable multipolar o en la misma canalización. Uno de los manuales pide una resistencia de tierra menor a 4 Ω, más exigente que los 40 Ω de la norma: conviene anotar la medición en la entrega.
- **Intemperie.** Las cajas con dispositivos a la intemperie llevan IP44 si no reciben chorros de agua e IP55 si los reciben (770.6.5, nota 2). Si la toma tiene que quedar enchufada a la intemperie, se usan tomas IEC 60309.

## El cable entre la unidad interior y la exterior

Si ese cable mide más de 3 m, o hay varias unidades esclavas, pasa a ser parte de la instalación: aislación, sección y protección según la 770. Los manuales piden al menos 1,5 mm² para la interconexión. La cantidad de hilos y la función de cada borne dependen del modelo, así que los bornes se confirman en el manual del equipo. Algunos equipos se alimentan por la unidad interior y otros por la exterior, y eso también lo dice el manual.

## Errores comunes en obra

- Conectar el split a una toma de un circuito compartido con otros aparatos, o a un alargue.
- Elegir la termomagnética por las frigorías o por la cuenta del fabricante, sin verificar que el cable la soporte.
- Dejar el circuito del aire sin diferencial de 30 mA porque "el manual no lo pide".
- Usar una termomagnética unipolar o 1P+N en un circuito monofásico.
- Instalar sobre una instalación existente que no es segura sin avisarle al cliente. Si la instalación no es segura, se frena y se le explica: es el momento de presupuestar el circuito nuevo.

## Preguntas frecuentes

**¿A partir de cuántas frigorías hace falta un circuito propio?** No hay un número. La norma decide por la corriente del equipo y el tipo de toma, y los fabricantes piden línea exclusiva en todos los casos. Lo seguro es un circuito exclusivo por equipo.

**¿Alcanza con un cable de 2,5 mm²?** Es el mínimo. Si el equipo consume hasta 16 A suele alcanzar, siempre que se verifique IB ≤ In ≤ Iz y la caída de tensión. Con corrientes mayores, se sube la sección del cable.

**¿El split lleva diferencial?** Sí. Todos los circuitos terminales llevan diferencial de 30 mA como máximo (770.14.2.3), y el del aire acondicionado también.

## Cómo te ayuda EGC

Con la [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) podés verificar la sección, la termomagnética y la caída de tensión del circuito del split antes de presupuestarlo. Así llevás al cliente un presupuesto con el cable y la protección ya calculados.

## Fuentes

- AEA 90364-7-770, edición 2017: 770.14.2.3, 770.16.5.1, 770.15.6, 770.10.1, 770.6.5, Tabla 770.11.I, Tabla 770.12.I, Tabla 770.15.IV.
- AEA 90364-7-771: 771.7.6, 771.12.3.13.2 d, 771.18.3.5.
- Manuales de instalación de cuatro fabricantes de equipos split (sin nombrar marcas).
- Fichas de la base de conocimiento técnico de EGC.
