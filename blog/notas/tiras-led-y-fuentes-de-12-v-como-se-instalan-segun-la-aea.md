Una tira LED de 12 V se alimenta siempre desde una fuente que tenga el primario y el secundario **separados**: nunca desde un autotransformador. Del lado de 220 V, la fuente es una carga más de un circuito con su diferencial de 30 mA. Del lado de 12 V, si el cable entre la fuente y la tira mide más de 3 m, ese tramo pasa a ser **parte de la instalación** y tiene que cumplir la reglamentación AEA 90364-7-770: aislación adecuada, sección correcta y protección contra sobrecarga y cortocircuito. Además, el cable de 12 V no comparte caño con el de 220 V.

## Qué fuente usar: primario y secundario separados

La tira trabaja en muy baja tensión, pero eso no quiere decir que cualquier aparato que baje la tensión sirva. La reglamentación pide, para las fuentes de hasta 24 V, un transformador con el primario y el secundario **separados**. Un **autotransformador** no cumple, aunque la tensión de salida sea la misma.

Hay dos formas de encarar el circuito de 12 V, y cambian cómo se tratan las masas:

- **MBTS (muy baja tensión sin puesta a tierra):** la fuente es de seguridad, según IEC 61558-2-6 (transformador) o IEC 61558-2-16 (fuente), con salida de 24 V o menos y separación de protección entre primario y secundario. El secundario y sus partes activas **no** se conectan a tierra, ni al PE, ni a partes activas de otros circuitos. Las masas de los equipos de MBTS **tampoco** van a tierra.
- **MBTF (muy baja tensión funcional):** misma tensión, pero sin cumplir todas las condiciones de la MBTS. Se protege como un circuito común: las masas se conectan al **PE del primario**, que tiene que tener corte automático por diferencial, y el PE acompaña al circuito.

Si falla cualquiera de las condiciones de la MBTS, el circuito es MBTF y se trata como tal. Que la tensión sea baja no alcanza: lo que define la categoría es la fuente y cómo queda conectado el secundario.

## Del lado de 220 V: la fuente es una carga del circuito

La entrada de la fuente se conecta como cualquier otra carga fija:

- La **llave unipolar corta la fase**, nunca el neutro. La fase va a la llave y el retorno de la llave va al borne L de la fuente.
- El **neutro** va directo al borne N de la fuente.
- Si la fuente tiene borne de tierra, se conecta al **PE**.
- Las conexiones se hacen **dentro de cajas**, como pide la 770 para llaves, protecciones y conexiones.

El circuito terminal que la alimenta lleva **diferencial de 30 mA**, como todos los circuitos terminales de la vivienda. Con la edición 2026 de la AEA 770, vigente desde el 1/11/2026, el diferencial tipo AC ya no es apto en viviendas: para uso general se usa **tipo A**.

Los bornes y los colores de los cables propios de cada fuente cambian según el modelo. Antes de conectar, confirmalos en el manual del fabricante.

## Del lado de 12 V: cuándo el cable es parte de la instalación

La AEA 90364-7-770 define hasta dónde llega el "equipo" y desde dónde empieza la "instalación". Los cables que unen una unidad con otra son parte del equipo solo si miden **hasta 3 m** y hay una sola unidad esclava. Si miden más, o si hay varias esclavas, esos cables son **parte de la instalación**. La propia norma da como ejemplo los cables entre la fuente y las lámparas o tiras LED.

Cuando ese tramo es parte de la instalación, tiene que tener:

- **Aislación adecuada.**
- **Sección correcta** para la corriente que lleva.
- **Protección contra sobrecarga y cortocircuito.**

Ojo con un dato: la Tabla 770.11.I fija **1,5 mm²** para los circuitos de uso específico que alimentan MBTF, pero la 770 **no** fija una sección mínima para el cable entre la fuente y la tira. La sección de ese tramo sale de la corriente y del largo, no de un número de tabla.

Hay que tener en cuenta que, para la misma potencia, a 12 V circula mucha más corriente que a 220 V. Si el cable entre la fuente y la tira es largo o fino, la caída de tensión se nota: la tira se ve más tenue en el extremo más alejado.

## Canalizaciones: el 12 V va en su propio caño

La 770 pide canalizaciones **separadas** para cada sistema: 220/380 V por un lado, MBTS o MBTF (hasta 24 V) por otro, y señales débiles y datos por otro. El cable de la tira no comparte caño con la alimentación de 220 V de la fuente.

Si en algún tramo no se puede separar, la norma admite tres alternativas: una cubierta aislante adicional para los cables de menor tensión, una pantalla metálica conectada a tierra, o un cable multipolar aislado para la tensión mayor.

Sobre los cables a la vista, la 770 prohíbe en interiores y semicubiertos los conductores desnudos o los unipolares sin envoltura tendidos en el aire. La única excepción es para circuitos de **hasta 24 V alimentados con fuente MBTS**. Con una fuente que no es de seguridad, esa excepción no aplica.

## Errores comunes en obra

- Alimentar la tira con un autotransformador o con una fuente cualquiera sin verificar que tenga primario y secundario separados.
- Llamar "MBTS" a un circuito con una fuente común y, por eso, dejar las masas sin conexión al PE. Si no cumple todas las condiciones, es MBTF y las masas van al PE del primario.
- Pasar el cable de 12 V por el mismo caño que el de 220 V para ahorrar una cañería.
- Alejar la fuente varios metros de la tira y usar el mismo cable fino que trae la tira, sin protección y sin pensar en la caída de tensión.
- Cortar el neutro con la llave en lugar de la fase.

## Preguntas frecuentes

**¿La tira LED de 12 V lleva diferencial?** El circuito de 220 V que alimenta la fuente es un circuito terminal, y todos los circuitos terminales de la vivienda llevan diferencial de 30 mA. Con la edición 2026, tipo A.

**¿Qué sección tiene que tener el cable entre la fuente y la tira?** La 770 no fija un mínimo para ese tramo. Si mide más de 3 m o alimenta varias tiras, es parte de la instalación y la sección tiene que ser la correcta para la corriente, con protección contra sobrecarga y cortocircuito. A 12 V la corriente es alta, así que conviene tener en cuenta también la caída de tensión.

**¿Puedo pasar el cable de 12 V por el caño de la luz?** No. La 770 pide canalizaciones separadas para 220 V y para MBTS o MBTF. Si en un tramo no se puede separar, hay que usar una de las alternativas que admite la norma: cubierta aislante adicional, pantalla metálica a tierra o multipolar aislado para la tensión mayor.

## Cómo te ayuda EGC

Con la [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) verificás la sección y la caída de tensión del circuito que alimenta la fuente, y lo sumás al presupuesto sin pasar los números a mano.

## Fuentes

- AEA 90364-7-770 (edición 2017), 770.1: cables entre unidades de más de 3 m o con varias esclavas son parte de la instalación; ejemplo de fuentes y tiras LED.
- AEA 90364-7-770 (edición 2017), 770.14.1: MBTS (fuente IEC 61558-2-6 o IEC 61558-2-16, secundario y masas sin conexión a tierra) y MBTF (masas al PE del primario).
- AEA 90364-7-770 (edición 2017), 770.7.1 f y g: fuentes de hasta 24 V con primario y secundario separados, no autotransformador.
- AEA 90364-7-770 (edición 2017), 770.10.3.8.2: canalizaciones separadas para 220/380 V, MBTS o MBTF y señales débiles.
- AEA 90364-7-770 (edición 2017), 770.10.1: desnudos o unipolares sin envoltura en el aire, solo hasta 24 V con fuente MBTS.
- AEA 90364-7-770 (edición 2017), Tabla 770.11.I: 1,5 mm² para circuitos de uso específico que alimentan MBTF.
- AEA 90364-7-770 (edición 2017), 770.14.2.3: diferencial de 30 mA en todos los circuitos terminales.
- AEA 90364-7-770 edición 2026 (resumen oficial AEA): diferencial tipo AC no apto en viviendas.
- Fichas de la base de conocimiento técnico de EGC.
