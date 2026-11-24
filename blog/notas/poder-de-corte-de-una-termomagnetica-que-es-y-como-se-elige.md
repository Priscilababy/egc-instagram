El poder de corte de una termomagnética es la corriente de cortocircuito más alta que puede interrumpir sin dañarse ni dejar de funcionar. Se elige mirando la corriente de cortocircuito presunta en el lugar donde se instala: el poder de corte tiene que ser igual o mayor. No tiene nada que ver con el calibre (10 A, 16 A, 20 A): una termomagnética de 10 A y otra de 32 A pueden tener el mismo poder de corte.

## Qué es el poder de corte y por qué importa

La termomagnética protege el cable contra dos cosas distintas. La **sobrecarga** es una corriente un poco mayor que la normal, sostenida en el tiempo: la detecta la parte térmica. El **cortocircuito** es una corriente muy alta que aparece de golpe cuando se tocan fase y neutro, o dos fases: lo detecta la parte magnética y tiene que abrir enseguida.

En un cortocircuito la corriente puede llegar a miles de amperes. Si la termomagnética no está preparada para esa corriente, puede no llegar a cortar o quedar dañada en el intento. Por eso, además del calibre y de la curva, cada termomagnética trae marcado su poder de corte, en amperes o en kA.

La parte general de la reglamentación AEA 90364 (sección 43, protección contra sobrecorrientes) define los conceptos que se usan en este tema: corriente de proyecto, corriente admisible del cable, sobrecarga, cortocircuito, poder de corte, selectividad y protección de respaldo.

## Icn e Ics: los dos valores de la norma IEC 60898-1

La AEA 90364-7-770 pide que las termomagnéticas de la vivienda cumplan **IEC 60898-1** (770.16.5.2). Esa norma de producto maneja dos valores:

- **Icn**: poder de corte asignado. Es el número grande que figura en el frente del aparato.
- **Ics**: poder de corte de servicio. Es la corriente de cortocircuito que la termomagnética puede cortar y seguir funcionando normalmente después.

El Ics sale de multiplicar el Icn por un factor que fija la norma:

- Icn hasta 6.000 A: el Ics es igual al Icn.
- Icn de más de 6.000 A y hasta 10.000 A: el Ics es el 75 % del Icn, con un mínimo de 6.000 A.
- Icn de más de 10.000 A: el Ics es el 50 % del Icn, con un mínimo de 7.500 A.

Ejemplo: una termomagnética de 10 kA de Icn tiene un Ics de 7.500 A. Una de 6 kA tiene 6.000 A de Ics. Cuando una distribuidora o un pliego pide un "poder de corte mínimo", conviene fijarse si habla de Icn o de Ics.

## Cómo se elige en una vivienda

El primer dato es la **corriente de cortocircuito presunta** en el tablero: la corriente que circularía si hubiera un cortocircuito franco en ese punto. No se adivina: sale del cálculo del proyecto o del dato que fije la distribuidora.

Con ese dato:

- La termomagnética tiene que tener un poder de corte igual o mayor que la corriente de cortocircuito presunta en el punto donde se instala.
- La AEA 90364-7-770 se aplica a viviendas con una corriente de cortocircuito presunta en el origen de **10 kA como máximo** (además de la cabecera de 63 A como máximo). Si el cortocircuito presunto supera 10 kA, corresponde la AEA 90364-7-771.
- El proyecto de la instalación incluye el cálculo de cortocircuito (Anexo 770-A), y el tablero se marca con la **corriente de cortocircuito máxima de cálculo**, junto con el fabricante o montador responsable y la tensión.

En monofásico, además, las termomagnéticas son **bipolares con los dos polos protegidos**; las unipolares, las "1P+N" y las de neutro pasante están prohibidas (770.16.5.1). Tienen que poder bloquearse en abierto con candado o precinto y abrir todos los polos a la vez (770.16.5.2).

## El poder de corte en el pilar

En el tablero principal del pilar (TP), la distribuidora fija un poder de corte mínimo para la termomagnética. En las fichas oficiales de Edenor para Tarifa 1, ese valor depende de la ficha que corresponda a la conexión:

- Pilar individual (en el terreno o en la línea municipal): **4.500 A** en monofásico y **6.000 A** en trifásico.
- Agrupados de 6 medidores monofásicos, gabinetes colectivos y conexiones subterráneas: **3.000 A** en monofásico y **4.500 A** en trifásico.

Edenor pide termomagnética según IEC 60947 o IEC 60898, bipolar en monofásico y tetrapolar en trifásico, y un diferencial de 30 mA con calibre igual o mayor que el de la termomagnética. El valor se toma de la ficha elegida, no se deduce solo de si la acometida es aérea o subterránea. En otras distribuidoras, mirá su reglamento.

## El diferencial también tiene un límite

El diferencial no es una protección contra cortocircuitos y su capacidad de ruptura es baja: como mínimo 500 A o 10 veces su corriente nominal, lo que sea mayor (Tabla 770-B.X). Por eso la 770 pide verificar que el diferencial soporte el cortocircuito del lugar. Si no lo soporta, se lo protege con un dispositivo contra cortocircuitos **aguas arriba**, según lo que indique su fabricante. Como excepción, se admite que lo protejan las termomagnéticas de aguas abajo en el mismo tablero, con los valores que dé el fabricante (770.15.2.2.5 y Anexo 770-B.2.4).

Si se cambia un diferencial por otro de distinta marca o características, la verificación se vuelve a hacer.

## Errores comunes en obra

- Elegir la termomagnética solo por el calibre, sin mirar el poder de corte que trae marcado.
- Confundir Icn con Ics: una termomagnética de 10 kA de Icn tiene 7.500 A de Ics, no 10.000 A.
- Poner en el pilar una termomagnética con menos poder de corte que el que pide la ficha de la distribuidora.
- Dar por hecho que el diferencial corta cualquier cortocircuito: su capacidad de ruptura es baja y hay que coordinarlo con la protección de aguas arriba según el fabricante.
- Reemplazar un aparato del tablero por otro "parecido" sin repetir la verificación.

## Preguntas frecuentes

**¿Más poder de corte significa que la termomagnética salta antes?** No. El poder de corte dice cuánta corriente puede interrumpir, no cuándo actúa. Cuándo salta depende del calibre y de la curva.

**¿Qué pasa si pongo una termomagnética con más poder de corte del necesario?** Nada malo: cumple igual. Lo que no se puede es quedarse corto. El poder de corte mínimo lo fija el cortocircuito del lugar o, en el pilar, la ficha de la distribuidora.

**¿Una termomagnética IEC 60947 sirve en el tablero de la vivienda?** La AEA 90364-7-770 pide termomagnéticas IEC 60898-1 en la instalación de la vivienda (770.16.5.2). En el tablero principal del pilar, Edenor acepta IEC 60947 o IEC 60898.

## Cómo te ayuda EGC

Con el [tablero en EGC](https://egc.globalepika.net.ar/tablero-electrico/) y el [esquema unifilar](https://egc.globalepika.net.ar/esquema-unifilar/) dejás anotadas las protecciones de cada circuito y las entregás ordenadas junto con el presupuesto. EGC arma el documento; la firma y la responsabilidad son del profesional interviniente.

## Fuentes

- AEA 90364-7-770, edición 2017: 770.1 y 770.4.2 f (alcance hasta 10 kA de cortocircuito presunto), Anexo 770-A (contenido del proyecto), 770.16.5.1 (termomagnéticas bipolares en monofásico), 770.16.5.2 (IEC 60898-1 y bloqueo en abierto), 770.15.2.2.5, Anexo 770-B.2.4 y Tabla 770-B.X (protección del diferencial), marcado del tablero.
- AEA 90364-4-43, 430.2: definiciones de sobrecorrientes y poder de corte.
- IEC 60898-1: Icn, Ics y factor Ics / Icn.
- Edenor: fichas técnicas de conexión Tarifa 1 (protecciones del tablero principal).
- Revista Ingeniería Eléctrica: artículo técnico sobre protección contra sobrecorrientes.
- Fichas de la base de conocimiento técnico de EGC.
