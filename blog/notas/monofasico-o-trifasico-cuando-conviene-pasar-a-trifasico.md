En una vivienda, la reglamentación de la AEA **recomienda** pedir suministro trifásico cuando la carga total calculada supera **7 kVA o 32 A** en monofásico. No es una obligación automática: la potencia a contratar la acuerdan el usuario y la distribuidora. Lo que sí es obligatorio es calcular bien la demanda, porque de ese número sale la decisión.

## Qué cambia entre monofásico y trifásico

En Argentina la red de baja tensión es de **220/380 V, 50 Hz**: 220 V entre una fase y el neutro, y 380 V entre dos fases (AEA 90364-7-770, 770.4.2).

- **Suministro monofásico:** llegan una fase y el neutro. Toda la vivienda se alimenta de esa única fase.
- **Suministro trifásico:** llegan tres fases (R, S y T) y el neutro. La carga se reparte entre las tres.

Un detalle que mucha gente no sabe: aunque la vivienda tenga suministro trifásico, los circuitos de **uso general y especial** (IUG, TUG, TUE) siguen siendo **monofásicos** (Tabla 770.6.I). Cada uno toma una fase y el neutro. Lo que cambia es que ahora hay tres fases para repartirlos. Los circuitos de **uso específico** (por ejemplo, un motor trifásico) sí pueden ser trifásicos.

Los colores también acompañan: fases R castaño, S negro y T rojo; neutro celeste; conductor de protección verde-amarillo (Tabla 770.10.XIII). Si un circuito monofásico sale de una instalación trifásica, su fase lleva el color de la fase de la que sale.

## Cuándo se recomienda pasar a trifásico

La AEA 90364-7-770 (edición 2017, 770.8.3.3) dice que, si la carga total supera **7 kVA o 32 A** en monofásico, se recomienda pedir suministro trifásico. Las dos cifras son casi la misma: 7.000 VA divididos 220 V dan unos 31,8 A.

La palabra clave es **recomienda**. La potencia a contratar la acuerdan el usuario y la distribuidora (770.7.3.1 y 770.8.3.2), y cada distribuidora tiene sus propias condiciones para dar un suministro trifásico. Lo que no cambia es que la instalación se dimensiona para la carga calculada, se contrate lo que se contrate.

Tampoco hay que confundir esta cifra con otros números que circulan. En notas comerciales aparece, por ejemplo, que "hasta 14 kW se puede en monofásico". Ese número no sale de la reglamentación de viviendas: el umbral que da la 770 es el de 7 kVA o 32 A.

## Cómo se calcula la carga total

La decisión sale de la **demanda de potencia máxima simultánea** (DPMS). En la edición 2017, el cálculo es:

- La demanda mínima de cada circuito según su tipo: IUG sin tomas derivadas, 2/3 de las bocas por 60 VA; IUG con tomas derivadas y TUG, 2200 VA por circuito; TUE, 3300 VA por circuito.
- Esos valores son **mínimos**: si las cargas reales son mayores, se usan las reales.
- Se puede aplicar un coeficiente de simultaneidad según la cantidad de circuitos.
- A la demanda del grado de electrificación se le suma la demanda de los circuitos de **uso específico** (770.8.3.1).

La **edición 2026** de la AEA 90364-7-770, vigente desde el 1/11/2026, cambia algunos puntos de este cálculo:

- La simultaneidad se elige por los circuitos **efectivamente instalados**: 2 circuitos → 1; de 3 a 5 → 0,7; de 6 a 9 → 0,6; 10 o más → 0,5.
- La demanda de la IUE pasa a **120 VA por boca por 2/3**.
- A la demanda se suman las cargas específicas (aire, calefacción, cocción) y los circuitos de **carga de vehículos eléctricos**, que se rigen por la AEA 90364-7-722.

Esto último pesa en la decisión. Una casa con varios equipos de aire, cocción eléctrica y un cargador de auto llega rápido a la zona donde el trifásico empieza a tener sentido.

## Si la vivienda es trifásica: repartir bien las cargas

Pasar a trifásico no sirve de mucho si todo queda colgado de una sola fase. La 770 pide repartir las cargas para que las fases queden **equilibradas**, y **recomienda** un desequilibrio máximo del **30 %** entre ellas (770.8.3.4).

En la práctica, eso significa:

- Anotar la demanda de cada circuito antes de asignarlo a una fase.
- Separar los consumos grandes (aires, termotanque, horno) en fases distintas.
- Dejar escrito en el tablero qué circuito va en qué fase.

Para la caída de tensión, el cálculo trifásico usa √3 en lugar de 2 en la fórmula, y la edición 2026 agrega criterios para circuitos trifásicos desequilibrados.

## Protecciones en una instalación trifásica

Las reglas de protección se adaptan a la cantidad de polos:

- **Cabecera del tablero principal:** en monofásico, termomagnética **bipolar** con los dos polos protegidos; en trifásico, **tetrapolar** con todos los polos protegidos. En los dos casos, **63 A como máximo** para el alcance de la 770 (770.16.5.3). Por encima de 63 A corresponde la AEA 90364-7-771.
- Las cabeceras de todos los tableros **seccionan el neutro**.
- Los circuitos monofásicos que salen de un tablero trifásico siguen llevando termomagnética **bipolar** con los dos polos protegidos. Quedan prohibidas las unipolares, las "1P+N" y las de "neutro pasante" (770.16.5.1).
- Si el neutro de un circuito trifásico tiene menos sección que las fases, necesita protección de sobreintensidad propia.
- **Diferencial de 30 mA** en todos los circuitos terminales. Desde la edición 2026, en obra nueva el tipo AC no es apto: como mínimo **tipo A**.

## Motores trifásicos

Un motor trifásico es una de las razones más comunes para pedir trifásico, pero conviene ordenar las cosas. El instalador **no** elige si el motor es mono o trifásico: eso lo define el equipo. Lo que sí tiene que hacer es protegerlo como pide la 770 (770.13.3):

- Un dispositivo de maniobra que abra **todas las fases a la vez**.
- Un dispositivo que detecte la **falta de una fase** y corte. Con una fase menos, la corriente sube en las otras dos y el motor se calienta.
- Protección **dedicada** contra sobrecarga. La termomagnética y el fusible no sirven como protección de sobrecarga del motor.
- Protección contra cortocircuito y fuga a tierra, propia o compartida.

## Errores comunes en obra

- Pedir trifásico y colgar todos los circuitos de la misma fase. Las cargas se reparten, con un desequilibrio máximo recomendado del 30 %.
- Calcular la demanda solo con los mínimos de la tabla cuando las cargas reales son mayores (aires, horno, cargador de auto).
- Usar termomagnéticas unipolares en los circuitos monofásicos de un tablero trifásico. Siguen siendo bipolares con los dos polos protegidos.
- Creer que el monofásico "ahorra" consumo. El consumo depende de los equipos, no de la cantidad de fases.
- Dejar un motor trifásico sin detección de falta de fase.

## Preguntas frecuentes

**¿Es obligatorio pasar a trifásico si la carga supera los 7 kVA?** No. La reglamentación lo **recomienda** cuando la carga total supera 7 kVA o 32 A en monofásico. La potencia a contratar la acuerdan el usuario y la distribuidora, y la instalación se dimensiona igual para la carga calculada.

**¿En una casa trifásica los tomacorrientes son de 380 V?** No. Los circuitos de uso general y especial son monofásicos: cada uno toma una fase y el neutro, con 220 V. Los 380 V aparecen solo entre fases, en circuitos de uso específico como un motor trifásico.

**¿Qué protección lleva la cabecera de un tablero trifásico de vivienda?** Una termomagnética **tetrapolar** con todos los polos protegidos, de 63 A como máximo dentro del alcance de la AEA 90364-7-770. La cabecera secciona también el neutro.

## Cómo te ayuda EGC

En EGC cargás los circuitos de la vivienda con su potencia y la app calcula la demanda, la sección del cable, la termomagnética y la caída de tensión según la AEA. Así ves con números si la carga total queda cerca del umbral de 7 kVA. Probala con la [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/).

## Fuentes

- AEA 90364-7-770 (edición 2017): 770.4.2, Tabla 770.6.I, 770.7.3.1, 770.8.1, 770.8.3.1 a 770.8.3.4, Tabla 770.10.XIII, 770.13.3, 770.16.5.1 y 770.16.5.3.
- AEA 90364-7-770 (edición 2026): cambios en simultaneidad, demanda de IUE, carga de vehículos eléctricos, caída de tensión y diferenciales.
- AEA 90364-7-722: carga de vehículos eléctricos.
- Fichas de la base de conocimiento técnico de EGC.
