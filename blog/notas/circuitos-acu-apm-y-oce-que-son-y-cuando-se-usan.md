Los circuitos **ACU, APM y OCE** son circuitos de **uso específico**: alimentan cargas que no encajan en los circuitos de uso general (IUG, TUG) ni en el de uso especial (TUE). El **ACU** alimenta una sola carga sin ninguna derivación, el **APM** alimenta pequeños motores monofásicos y el **OCE** cubre cualquier otra carga específica. En una vivienda, la AEA 90364-7-770 remite a la AEA 90364-7-771 para definirlos.

## De dónde salen estos circuitos

La AEA 90364-7-770 (viviendas unifamiliares hasta 63 A) define en su Tabla 770.6.I los circuitos de uso general y especial: IUG, TUG y TUE. Para "cualquier otro tipo" de circuito, la 770 no da reglas propias: remite a la **AEA 90364-7-771**, que es la reglamentación para viviendas, oficinas y locales unitarios.

La 771 (edición 2006) agrupa esos circuitos como de **uso específico** en su cláusula 771.7.6 y los resume en la Tabla 771.7.I. Ahí aparecen, entre otros:

- **APM:** alimentación de pequeños motores.
- **ACU:** alimentación de carga única.
- **MBTF:** alimentación en 220 V de fuentes de muy baja tensión funcional (porteros, alarmas, cámaras).
- **ATE:** alimentación de tensión estabilizada o UPS.
- **ITE:** iluminación trifásica, solo para oficinas y locales.
- **OCE:** otros circuitos específicos.

En esta nota nos concentramos en los tres que más aparecen en una casa: ACU, APM y OCE.

Dos reglas valen para todos los de uso específico:

- A diferencia de los de uso general y especial, que siempre son **monofásicos**, los de uso específico pueden ser **monofásicos o trifásicos** (771.7.6).
- Son **adicionales**: no cuentan para el mínimo de circuitos que pide el grado de electrificación (771.7.6 c). Si la vivienda es de grado medio y lleva tres circuitos, un ACU para la bomba se suma a esos tres; no reemplaza a ninguno.

## ACU: alimentación de carga única

El ACU alimenta **una sola carga**, monofásica o trifásica, **sin ninguna derivación**. Un cable que sale del tablero y llega a un solo equipo. Si en el camino se agrega una toma o se cuelga otro aparato, deja de ser ACU.

- **Sección mínima:** 2,5 mm².
- **Bocas:** una sola, la del equipo.
- **Protección máxima:** no tiene un valor fijo en la tabla; **la fija el proyectista** según el equipo.

La norma da como ejemplos de uso específico las **unidades condensadoras de climatización central** y las **bombas elevadoras de agua** (771.7.6 c). En obra domiciliaria, el caso más común es el aire acondicionado: un split alimentado por una línea propia, sin otros aparatos, que es justamente lo que piden los fabricantes en sus manuales.

Que la protección "la fije el proyectista" no quiere decir que valga cualquiera. Se elige por la corriente del equipo y por lo que admite el cable, como en cualquier otro circuito.

## APM: alimentación de pequeños motores

El APM está pensado para **pequeños motores monofásicos**: ventilación, portones, cortinas.

- **Bocas máximas:** 15, con un máximo de 10 A por boca.
- **Protección máxima de la tabla:** 25 A.
- **Sección mínima:** 2,5 mm².

Acá hay que tener cuidado con el número de la tabla. La protección máxima es un techo, no una recomendación: la termomagnética también tiene que cumplir **IB ≤ In ≤ Iz**, es decir, no superar la corriente que admite el cable. Un 2,5 mm² en caño admite **21 A** (ficha de secciones de la 770), así que con 2,5 mm² la térmica no puede ser de 25 A. Para usar 25 A hace falta una sección mayor, verificada con la tabla de corrientes admisibles.

Además, que sea un circuito de motores no resuelve la protección del motor. La AEA 90364-7-770 pide para los motores de instalación fija (770.13.3):

- Un dispositivo de maniobra que arranque y pare el motor abriendo **fase y neutro** si es monofásico.
- Una protección **dedicada** contra sobrecarga. La termomagnética y el fusible no sirven como protección de sobrecarga de motor.
- Protección contra cortocircuito y fuga a tierra, propia o compartida.

## OCE: otros circuitos específicos

El OCE es la categoría para **cualquier otra carga específica** que no entre en las anteriores.

- **Bocas:** sin límite en la tabla.
- **Protección máxima:** la fija el proyectista.
- **Sección mínima:** 2,5 mm².

"Sin límite" y "la fija el proyectista" no son una carta blanca. El circuito se calcula igual que cualquier otro: corriente de la carga, sección por corriente admisible, caída de tensión y termomagnética que proteja al cable.

## Lo que comparten los tres: diferencial, caño propio y caída de tensión

**Diferencial de 30 mA.** La 771 exige diferencial de 30 mA en ACU, APM y OCE, igual que en los circuitos de uso general (771.18.3.5). La única excepción es un **ACU** donde se **demuestre** que el diferencial perturba el equipo, como el arranque estrella-triángulo de motores medianos y grandes, con una protección alternativa contra contactos directos e indirectos. Un split domiciliario común no entra en esa excepción. Y desde la AEA 90364-7-770 edición 2026, el diferencial tipo AC no es apto en viviendas: para uso general, **tipo A**; para equipos con inverter monofásico, **tipo F**.

**Caño independiente.** Los circuitos de uso específico van siempre en **canalización independiente**: no comparten caño con los de uso general ni con los de uso especial. Todos los conductores del circuito, incluido el PE, van en la misma canalización.

**Caída de tensión.** Para TUE, uso específico y fuerza motriz, el límite es **5 %** según la AEA 90364-7-770 edición 2026.

**Demanda.** Los circuitos de uso específico se suman aparte a la demanda del grado de electrificación (771.9.2). Si la carga total supera **7 kVA o 32 A** en monofásico, la reglamentación **recomienda** pedir suministro trifásico.

## Errores comunes en obra

- Llamar "ACU" a un circuito que tiene una toma de más en el camino. Con una derivación deja de ser carga única.
- Poner la térmica máxima de la tabla (25 A en APM) con un cable de 2,5 mm², que admite 21 A en caño.
- Confiar en la termomagnética como protección de sobrecarga de un motor. La norma pide protección de sobrecarga dedicada.
- Sacar el diferencial del circuito del aire "porque salta". Un split domiciliario no está en la excepción de la 771.
- Pasar el circuito de la bomba o del aire por el mismo caño que los tomas de uso general.

## Preguntas frecuentes

**¿Un aire acondicionado va siempre en un ACU?** No necesariamente. La norma decide por la corriente del equipo: un TUE admite cargas de hasta 20 A con toma de 20 A. Pero los fabricantes piden línea exclusiva, sin otros aparatos, así que en la práctica lo que cumple con la norma y con el manual es un circuito exclusivo por equipo: un TUE de una sola boca o un ACU.

**¿El ACU cuenta para el mínimo de circuitos de la vivienda?** No. Los circuitos de uso específico son adicionales: no se cuentan para el mínimo que pide el grado de electrificación (771.7.6 c).

**¿Un circuito de uso específico puede ser trifásico?** Sí. Los de uso general y especial son siempre monofásicos, pero los de uso específico pueden ser monofásicos o trifásicos (771.7.6).

## Cómo te ayuda EGC

En EGC cargás cada circuito con su potencia y su recorrido, y la app verifica la sección, la termomagnética y la caída de tensión según la AEA. Probala con la [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/).

## Fuentes

- AEA 90364-7-771 (edición 2006): 771.7.6, Tabla 771.7.I, 771.9.2 y 771.18.3.5.
- AEA 90364-7-770 (edición 2017): Tabla 770.6.I, 770.13.3 y 770.8.3.3.
- AEA 90364-7-770 (edición 2026): cambios en diferenciales, canalizaciones y caída de tensión.
- Fichas de la base de conocimiento técnico de EGC.
