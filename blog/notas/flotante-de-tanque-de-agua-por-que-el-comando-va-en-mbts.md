El circuito de comando de un flotante eléctrico que trabaja dentro de un tanque de agua, sea la cisterna o el tanque elevado, tiene que ir en **MBTS**: muy baja tensión sin puesta a tierra, de hasta 24 V y alimentada por una fuente de seguridad. Un flotante dentro del tanque conectado directamente a 220 V **no cumple** la reglamentación AEA 90364-7-770. La bomba sí funciona en 220 V, pero con sus propias exigencias de maniobra y protección.

## Qué dice la reglamentación sobre los flotantes

La AEA 90364-7-770 trata en un mismo punto los circuitos de comando que trabajan en ambientes mojados: interruptores a flotante, señalizaciones y alarmas. Para todos ellos pide alimentación en **MBTS**, y aclara que eso incluye a los **tanques cisterna y elevado**.

La MBTS bien hecha protege a la vez contra contactos directos e indirectos. Por eso es la exigencia para los circuitos de comando que trabajan en el agua o junto a ella.

La norma no dibuja un esquema de conexión del flotante con la bomba. Lo que exige es la condición del circuito de comando: que sea MBTS. Cómo se resuelve el mando de la bomba desde ese circuito depende del equipo que uses, y hay que verificarlo en el manual del fabricante.

## Qué tiene que cumplir un circuito para ser MBTS

No alcanza con que la tensión sea baja. La reglamentación pide que se cumplan **todas** estas condiciones a la vez:

- **Tensión nominal de hasta 24 V** en locales secos, húmedos y mojados. Donde el cuerpo puede quedar sumergido, el límite baja a **12 V**.
- **Fuente de seguridad:** un transformador de seguridad según IEC 61558-2-6 o una fuente según IEC 61558-2-16, con salida de 24 V o menos y separación de protección entre primario y secundario. **Nunca un autotransformador.**
- **El secundario no se conecta a tierra:** ni sus partes activas a tierra, ni al PE, ni a partes activas de otros circuitos.
- **Las masas de los equipos MBTS tampoco van a tierra:** no se conectan a tierra, ni al PE, ni a otras masas, ni a masas extrañas. La norma admite una excepción cuando un equipo tiene que quedar unido a una masa extraña, siempre que se asegure que la tensión no supera 24 V.
- **Fichas y tomas propias:** si se usan, según IEC 60309, que no encastren con las de otras tensiones y **sin contacto de tierra**.

Si falla cualquiera de estas condiciones, el circuito ya no es MBTS: pasa a ser **MBTF** (muy baja tensión funcional), que se protege como un circuito común y no sirve para el comando de un flotante dentro del tanque.

## MBTS y MBTF no son lo mismo

Es fácil confundirlas porque usan la misma tensión. La diferencia está en para qué se usan y en cómo se tratan las masas:

- **MBTS:** se usa por seguridad. El secundario y las masas quedan aislados de tierra. Es la que pide la norma para los flotantes en tanques.
- **MBTF:** se usa por funcionamiento, por ejemplo en porteros o alarmas. Se protege como un circuito común: las masas van al **PE del primario**, que tiene que tener corte automático por diferencial, y el PE acompaña al circuito.

Por eso, una fuente cualquiera de 12 o 24 V que encontraste en el depósito no convierte el circuito en MBTS. Tiene que ser una fuente de seguridad de las normas citadas, y el secundario tiene que quedar sin conexión a tierra.

## Cómo se arma la instalación en obra

En un sistema típico de bombeo, el flotante de la cisterna impide que la bomba arranque, o la para, si falta agua, para que no trabaje en seco. El flotante del tanque elevado la para cuando el agua llega al nivel máximo. Con eso en mente, la instalación queda así:

- **Cada flotante** se conecta en una caja cercana al tanque, y desde ahí los cables de comando van al tablero en cañería. Las cajas de paso y de bornes, **estancas**.
- **Caños separados:** los circuitos de 220 V, los de MBTS o MBTF y los de señales débiles van en canalizaciones independientes. El cable del flotante no comparte caño con la alimentación de la bomba.
- **El circuito de la bomba** lleva su protección en el tablero, con diferencial de 30 mA como todo circuito terminal, y las masas de la bomba conectadas al PE.

## La bomba también tiene sus reglas

El flotante es solo una parte. La bomba es un motor de instalación fija, y la reglamentación le pide:

- **Un dispositivo de maniobra que arranque y pare el motor abriendo fase y neutro** si es monofásico, o todas las fases a la vez si es trifásico.
- **Protección dedicada contra sobrecarga.** La termomagnética y el fusible **no sirven** como protección de sobrecarga de un motor. La norma no nombra un aparato en particular, así que el dispositivo se elige según el motor y lo que indique su fabricante.
- **Protección contra cortocircuito y fuga a tierra**, que puede ser propia o compartida.

Un error frecuente es pensar que, como la bomba tiene una termomagnética en el tablero, ya está protegida. Contra cortocircuito puede ser; contra sobrecarga, no.

## Errores comunes en obra

- Conectar el flotante dentro del tanque directamente a 220 V, en serie con la bomba.
- Alimentar el comando con un autotransformador o con una fuente que no es de seguridad, y llamarlo "baja tensión".
- Poner a tierra el secundario o las masas del circuito de MBTS "por las dudas": con eso el circuito deja de ser MBTS.
- Usar más de 24 V para el comando del flotante. Por encima de ese valor ya no es MBTS.
- Pasar el cable del flotante por el mismo caño que la alimentación de la bomba.
- Confiar en la termomagnética como única protección del motor.

## Preguntas frecuentes

**¿Puedo usar un flotante eléctrico de 220 V dentro del tanque si el circuito tiene diferencial?** No. La reglamentación pide que el circuito de comando de un flotante en tanques cisterna y elevado sea MBTS. El diferencial de 30 mA es obligatorio en el circuito de la bomba, pero no reemplaza esa exigencia.

**¿Sirve cualquier fuente de 12 o 24 V?** No. Tiene que ser un transformador de seguridad según IEC 61558-2-6 o una fuente según IEC 61558-2-16, con separación de protección entre primario y secundario. Un autotransformador nunca sirve, y el secundario no se pone a tierra.

**¿El cable del flotante puede ir junto con los de la bomba?** No. Los circuitos de 220 V y los de muy baja tensión van en caños separados.

## Cómo te ayuda EGC

Con [EGC](https://egc.globalepika.net.ar/) armás el presupuesto de la instalación de bombeo con todos sus ítems: fuente de seguridad, cajas estancas, cañerías separadas y la protección de la bomba. Así no se te escapa nada al cotizar.

## Fuentes

- AEA 90364-7-770, edición 2017, 770.7.1 h: circuitos de comando en ambientes mojados, incluidos tanques cisterna y elevado, en MBTS.
- AEA 90364-7-770, edición 2017, 770.14.1: condiciones de la MBTS y de la MBTF.
- AEA 90364-7-770, edición 2017, 770.10.3.8.2 h: separación de sistemas en canalizaciones.
- AEA 90364-7-770, edición 2017, 770.13.3: motores de instalación fija.
- AEA 90364-7-770, edición 2017, 770.14.2.3: diferencial de 30 mA en circuitos terminales.
- Fichas de la base de conocimiento técnico de EGC.
