Un motor de instalación fija no se alimenta como un toma más. El cable tiene que admitir **por lo menos el 125 % de la corriente nominal** del motor, y el circuito necesita una **protección de sobrecarga dedicada** al motor: la termomagnética y el fusible no sirven para eso. Además, la maniobra tiene que cortar **fase y neutro** en monofásico, o todas las fases a la vez en trifásico.

## Qué pide la AEA 90364-7-770 para un motor

La reglamentación para viviendas trata a los motores de instalación fija en un punto propio (AEA 90364-7-770, 770.13.3). Lo que pide se resume en cuatro cosas:

- Un **dispositivo de maniobra** que arranque y pare el motor abriendo **fase y neutro** si es monofásico, o **todas las fases a la vez** si es trifásico.
- En motores **trifásicos**, un dispositivo que **detecte la falta de una fase** y corte.
- Una protección **dedicada** contra **sobrecarga**.
- Protección contra **cortocircuito** y contra **fuga a tierra**, que puede ser propia del motor o compartida.

La norma deja claro un punto que en obra se pasa por alto: **los fusibles y las termomagnéticas no sirven como protección de sobrecarga de motores**. La termomagnética protege el cable contra sobrecorrientes y cortocircuitos, pero no está pensada para cuidar el bobinado de un motor que se calienta por trabajar forzado. Por eso la norma pide una protección de sobrecarga **dedicada** al motor. No nombra un aparato puntual: el dispositivo se elige según el motor y su servicio, y conviene consultar al fabricante.

## La sección del cable: la regla del 125 %

Para dimensionar el cable que alimenta motores, la reglamentación de la AEA (según la sección dedicada a motores de la AEA 90364, citada en la bibliografía técnica) usa estas reglas:

- **Un solo motor:** el cable tiene que admitir al menos el **125 % de la corriente nominal** del motor.
- **Varios motores:** el **125 % de la corriente nominal del más grande, más la suma de las nominales de los demás**. Si un enclavamiento impide que arranquen juntos, se cuentan solo los que pueden arrancar a la vez.
- **Motores y otras cargas en el mismo circuito:** el 125 % del motor más grande más las nominales del resto. Sobre el total se puede aplicar un factor de simultaneidad, siempre que esté bien justificado.

Después de ese número vienen las condiciones de siempre. La sección nunca baja del mínimo de la tabla: para un circuito de uso específico, **2,5 mm²** (Tabla 770.11.I). Y la termomagnética se elige con la regla **IB ≤ In ≤ Iz**: corriente de proyecto menor o igual que la nominal de la protección, y esta menor o igual que la corriente admisible del cable (770.15.2.1).

## Un ejemplo de cálculo

Supongamos un circuito monofásico con dos motores: uno de **8 A** de corriente nominal y otro de **5 A**, que pueden arrancar a la vez.

- 125 % del más grande: 8 × 1,25 = **10 A**.
- Más la nominal del otro: 10 + 5 = **15 A**.

El cable tiene que admitir al menos 15 A. Un unipolar de **2,5 mm²** en caño, en monofásico, admite **21 A** a 40 °C de ambiente (Tabla 770.12.I), así que alcanza. Con una corriente de proyecto de 15 A, una termomagnética de 16 A cumple IB ≤ In ≤ Iz (15 ≤ 16 ≤ 21).

Si ese circuito compartiera caño con otro, la corriente admisible del cable baja: con dos circuitos en el mismo caño se multiplica por **0,80** (Tabla 770.12.II), y 21 × 0,8 da 16,8 A. Ojo: desde la edición 2026, los circuitos de uso especial y específico van siempre en **canalización independiente**.

Y esa termomagnética sigue sin ser la protección de sobrecarga de los motores: cada motor necesita la suya, dedicada.

## Caída de tensión: el arranque cuenta

Un motor toma mucha más corriente al arrancar que en marcha. Por eso la caída de tensión tiene límites propios para los circuitos que alimentan solo motores: **5 % en régimen y 15 % en el arranque** (770.15.6). En la edición 2026 se mantiene el 5 % para fuerza motriz, y se acepta más caída en el arranque si los equipos lo admiten.

Para el cálculo en el arranque, a falta de datos, la norma toma **cos φ = 0,30**. En cables largos hasta un motor en el fondo del terreno, esto puede obligar a subir la sección aunque la corriente en marcha no lo pida.

Con alimentación de la red pública, la bibliografía técnica agrega un dato a tener en cuenta: la corriente de arranque del motor (o del grupo), sumada a la carga ya conectada, **no debería superar el 40 % de la corriente máxima simultánea contratada**. Es un dato de artículo técnico, no verificado en el texto de la norma: sirve como criterio para consultar antes de instalar un motor grande.

## Seccionar y bloquear: trabajar seguro

Las fuentes técnicas sobre motores agregan una regla práctica muy útil:

- En el tablero, cada motor lleva un **seccionador que se pueda bloquear con candado en abierto**.
- Si el motor arranca solo (automático) o **no se ve desde el tablero**, va **otro seccionador cerca del motor**, también bloqueable.

Es coherente con lo que pide la 770 para las termomagnéticas: que se puedan **bloquear en abierto** con candado o precinto (770.16.5.2). El objetivo es el mismo: que nadie energice el motor mientras otro está trabajando sobre la bomba, el portón o la máquina.

También hay que pensar qué pasa si **se corta la tensión**. Al volver, el motor puede quedar parado hasta que alguien lo arranque, o reconectarse solo. Se elige según el riesgo que tenga un arranque imprevisto para quien opera el equipo.

## Errores comunes en obra

- Dejar la termomagnética como única protección del motor. Protege el cable, no el bobinado: falta la protección de sobrecarga dedicada.
- Cortar solo la fase con una llave común en un motor monofásico. La maniobra tiene que abrir **fase y neutro**.
- Calcular el cable con la corriente nominal del motor, sin el 125 %.
- No prever la caída de tensión en el arranque en tiradas largas: el motor arranca con dificultad y se calienta.
- No dejar ningún seccionador bloqueable cerca de un motor que arranca solo o que no se ve desde el tablero.

## Preguntas frecuentes

**¿La termomagnética no protege al motor de una sobrecarga?** No como pide la norma. La AEA 90364-7-770 dice que los fusibles y las termomagnéticas no sirven como protección de sobrecarga de motores, y exige una protección dedicada (770.13.3).

**¿Un motor trifásico necesita algo más que uno monofásico?** Sí: un dispositivo que detecte la **falta de una fase** y corte. Con una fase menos, sube la corriente en las otras y el motor se calienta. La maniobra, además, abre todas las fases a la vez.

**¿El circuito de un motor lleva diferencial?** Sí. La protección contra fuga a tierra es parte de lo que pide la norma para motores, y todos los circuitos terminales llevan diferencial de **30 mA** (770.14.2.3). Desde la edición 2026, en obra nueva el tipo AC no es apto: como mínimo **tipo A**.

## Cómo te ayuda EGC

Con la [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) verificás la sección del cable, la corriente admisible y la caída de tensión del circuito antes de presupuestar. Así el cliente recibe un presupuesto con el cable y las protecciones que de verdad corresponden.

## Fuentes

- AEA 90364-7-770, edición 2017: 770.13.3 (motores de instalación fija), Tabla 770.11.I (secciones mínimas), Tabla 770.12.I y Tabla 770.12.II (corriente admisible y agrupamiento), 770.15.2.1 (IB ≤ In ≤ Iz), 770.15.6 (caída de tensión), 770.16.5.2 (bloqueo en abierto), 770.14.2.3 (diferencial de 30 mA).
- AEA 90364-7-770, edición 2026: caída de tensión en fuerza motriz, canalización independiente para uso especial y específico, diferencial tipo AC no apto en obra nueva.
- Revista Ingeniería Eléctrica: artículos técnicos sobre alimentación de motores según la reglamentación de la AEA (regla del 125 %, seccionamiento con candado, arranque y red pública).
- Fichas de la base de conocimiento técnico de EGC.
