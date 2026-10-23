En una vivienda, la AEA 90364-7-770 divide los circuitos terminales en tres tipos: **IUG** (iluminación de uso general), **TUG** (tomacorrientes de uso general) y **TUE** (tomacorrientes de uso especial). La diferencia es qué carga alimentan: el IUG lleva luminarias y cargas de hasta 10 A, el TUG lleva tomas de 10 A, y el TUE lleva tomas para cargas de más de 10 A, como las que se enchufan en una toma de 20 A. Cada tipo tiene su protección máxima, su límite de bocas y su sección mínima de cable.

## Qué es cada circuito

La Tabla 770.6.I de la AEA 90364-7-770 (edición 2017) los define así:

- **IUG:** alimenta luminarias, ventiladores, combinaciones y cargas unitarias de hasta 10 A, conectadas por bornera o por una toma 2P+T de 10 A. Protección máxima: 16 A. Hasta 15 bocas.
- **TUG:** alimenta cargas unitarias de hasta 10 A a través de tomas 2P+T de 10 A. Protección máxima: 20 A. Hasta 15 bocas.
- **TUE:** alimenta cargas unitarias de más de 10 A, con tomas 2P+T de 20 A (hasta 20 A) o tomas IEC 60309 (hasta 16 A). Protección máxima: 32 A. Hasta 15 bocas.
- **Uso específico:** cualquier otro tipo de circuito. La 770 remite a la AEA 90364-7-771.

Todos los circuitos de uso general y especial son **monofásicos**. Y la protección máxima de la tabla se refiere a la termomagnética en **ambos polos**: en monofásico, la protección es bipolar.

## Qué puede alimentar cada uno

La 770 da varios criterios útiles que se olvidan seguido:

- **Una luminaria por boca**, con una o más lámparas, hasta 10 A.
- **Ventiladores de techo y extractores** se pueden colgar del circuito de iluminación. Para calcular la demanda cuentan como **una boca de iluminación**.
- **Fuentes de timbres y porteros** pueden ir en un IUG; cada fuente cuenta como una boca de iluminación.
- **Una boca de tomas** admite 2 tomas en caja rectangular de 5 × 10 cm, o 4 tomas en caja cuadrada de 10 × 10 cm.
- En una boca con toma de 20 A se pueden sumar tomas de 10 A.
- La toma de un **toilette** (baño sin bañera ni ducha) puede ir en el circuito de iluminación.
- Se recomienda que los circuitos de exterior sean independientes. En semicubiertos, los artefactos son IP44 como mínimo; a la intemperie, IP54 como mínimo.

Los baños, cocinas y lavaderos tienen además requisitos propios en la AEA 90364-7-701.

## Sección del cable y protección: la combinación tiene que cerrar

La Tabla 770.11.I fija secciones mínimas: **1,5 mm²** para IUG, **2,5 mm²** para TUG y TUE, y 2,5 mm² para un IUG que incluya tomas de uso general. Pero la protección máxima de la tabla de circuitos es un techo, no una recomendación: la termomagnética también tiene que cumplir IB ≤ In ≤ Iz, es decir, no superar la corriente admisible del cable.

Con la Tabla 770.12.I (cable en cañería, monofásico, 40 °C, un solo circuito en el caño):

- **IUG con 1,5 mm²:** Iz = 15 A. La termomagnética no puede ser de 16 A, aunque la tabla de circuitos admita hasta 16 A. Tiene que ser de 15 A o menos.
- **IUG con 2,5 mm²:** Iz = 21 A. Admite hasta 16 A, el máximo del tipo de circuito.
- **TUG con 2,5 mm²:** Iz = 21 A. Admite 20 A, el máximo del tipo de circuito.
- **TUE con 2,5 mm²:** Iz = 21 A. Admite hasta 20 A. Para llegar a 32 A hace falta más sección: 4 mm² (Iz = 28 A) no alcanza y 6 mm² (Iz = 36 A) sí.

Si hay dos circuitos monofásicos en el mismo caño, la corriente admisible se multiplica por 0,80. Con 2,5 mm² queda en 16,8 A y ya no admite una termomagnética de 20 A.

## Cuántos circuitos y cuántas bocas

El número mínimo de circuitos depende del grado de electrificación, que se define por la superficie (cubierta más el 50 % de la semicubierta):

- **Mínimo** (hasta 60 m²): 2 circuitos, 1 IUG y 1 TUG.
- **Medio** (más de 60 y hasta 130 m²): 3 circuitos.
- **Elevado** (más de 130 y hasta 200 m²): 5 circuitos.
- **Superior** (más de 200 m²): 6 circuitos, con uno de libre elección.

En los grados medio, elevado y superior hay dos variantes de reparto entre IUG y TUG (por ejemplo, 2 IUG y 1 TUG, o 1 IUG y 2 TUG en el grado medio). Una vivienda de menos de 130 m² con un dormitorio de más de 36 m² toma los puntos mínimos del grado elevado.

Los circuitos de uso general tienen demanda mínima por circuito: 2200 VA para el TUG, 2200 VA para un IUG con tomas derivadas y 3300 VA para el TUE. Son mínimos: si las cargas reales son mayores, se usan las reales.

## Errores comunes en obra

- Poner una termomagnética de 16 A en un IUG con cable de 1,5 mm², sin verificar que 16 A supera la corriente admisible.
- Colgar un electrodoméstico fijo de más de 10 A de un TUG en vez de darle un TUE.
- Superar las 15 bocas por circuito.
- Meter dos circuitos en el mismo caño sin aplicar el factor de agrupamiento.
- Olvidar que todos los circuitos terminales llevan diferencial de 30 mA como máximo (770.14.2.3), incluidos los de iluminación.

## Preguntas frecuentes

**¿Un ventilador de techo va en IUG o en TUG?** En el circuito de iluminación. La 770 permite colgar ventiladores de techo y extractores del IUG, y para la demanda cuentan como una boca de iluminación.

**¿Cuándo corresponde un TUE?** Cuando la carga unitaria supera 10 A y se alimenta con una toma 2P+T de 20 A o una toma IEC 60309. La protección máxima del tipo es 32 A, pero la que corresponde a tu circuito sale del cable: con 2,5 mm² es de hasta 20 A.

**¿Qué pasa si el equipo no entra en ninguno de los tres?** Es un circuito de uso específico y se rige por la AEA 90364-7-771. Por ejemplo, un único equipo sin derivaciones (como un aire acondicionado) se considera circuito de uso específico según la 771 (771.7.6).

## Cómo te ayuda EGC

Saber qué circuito corresponde es el primer paso; después hay que verificar que cable y térmica cierren con IB ≤ In ≤ Iz. La [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) te ayuda a dimensionar la sección y la caída de tensión de cada circuito.

## Fuentes

- AEA 90364-7-770 (edición 2017), 770.6.6 y Tabla 770.6.I: tipos de circuitos terminales.
- AEA 90364-7-770, 770.7.1: criterios generales de bocas.
- AEA 90364-7-770, 770.7.3, 770.7.4, Tablas 770.7.I y 770.7.II: grado de electrificación y número de circuitos.
- AEA 90364-7-770, 770.8.1: demanda de potencia.
- AEA 90364-7-770, Tabla 770.11.I: secciones mínimas.
- AEA 90364-7-770, Tabla 770.12.I, Tabla 770.12.II y 770.15.2.1: corriente admisible, agrupamiento y coordinación cable-protección.
- AEA 90364-7-770, 770.14.2.3: diferencial de 30 mA.
- Fichas de la base de conocimiento técnico de EGC.
