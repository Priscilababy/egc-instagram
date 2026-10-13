La sección de un cable no se elige por costumbre ("1,5 para luces y 2,5 para tomas") sino por tres condiciones que se cumplen a la vez: no bajar de la sección mínima de la tabla de la AEA, que el cable aguante la corriente que le va a pasar sin recalentarse y que la caída de tensión quede dentro del límite. En una vivienda, las mínimas son 1,5 mm² para iluminación (IUG) y 2,5 mm² para tomas (TUG y TUE); pero la protección que le pongas tiene que ser compatible con el cable, y esa es la parte que más se olvida.

## Las secciones mínimas de la AEA 90364-7-770

La Tabla 770.11.I fija los valores por debajo de los cuales no se puede bajar, aunque el cálculo dé menos:

- Línea principal: 4 mm².
- Circuitos seccionales: 2,5 mm².
- IUG (iluminación de uso general): 1,5 mm².
- IUG que incluye tomas de uso general: 2,5 mm².
- TUG (tomas de uso general): 2,5 mm².
- TUE (tomas de uso especial): 2,5 mm².
- Uso específico: 2,5 mm² (1,5 mm² si alimenta muy baja tensión funcional).
- Alimentación y retornos de llaves: 1 mm².
- Conductor de protección (PE): 2,5 mm².

Son mínimos, no recomendaciones de diseño: si la corriente o la distancia lo exigen, se sube la sección.

## Qué corriente aguanta cada sección

La Tabla 770.12.I da la corriente admisible de los cables de cobre IRAM NM 247-3 en cañería, con una temperatura ambiente de cálculo de 40 °C. Para un circuito monofásico (dos cables cargados más el PE):

- 1,5 mm²: 15 A.
- 2,5 mm²: 21 A.
- 4 mm²: 28 A.
- 6 mm²: 36 A.
- 10 mm²: 50 A.

Con estos valores se cumple la condición de coordinación de la norma: **IB ≤ In ≤ Iz**. Es decir, la corriente de proyecto del circuito (IB) tiene que ser menor o igual que la corriente nominal de la termomagnética (In), y esta menor o igual que la corriente admisible del cable (Iz).

## La protección máxima de cada tipo de circuito y el cable que la soporta

La Tabla 770.6.I fija la protección máxima de cada circuito terminal. Pero ese máximo solo se puede usar si el cable lo soporta:

- **TUG con 2,5 mm²:** protección máxima de 20 A. El cable admite 21 A, así que la combinación de 2,5 mm² con 20 A cumple.
- **IUG con 1,5 mm²:** la protección máxima del tipo de circuito es 16 A, pero el cable de 1,5 mm² admite 15 A. Una termomagnética de 16 A **no** cumple con ese cable: la protección tiene que ser de 15 A o menos (por ejemplo, 10 A). Si el circuito de iluminación lleva tomas derivadas y por eso el cable es de 2,5 mm², sí se puede llegar a 16 A.
- **TUE:** el máximo del tipo de circuito es 32 A, pero con 2,5 mm² el cable admite 21 A. Para usar 32 A hace falta una sección mayor: con 6 mm² (36 A) la condición se cumple. Con 2,5 mm² la protección no puede pasar de 20 A.

En todos los casos, la termomagnética de un circuito monofásico es bipolar, con los dos polos protegidos.

## Varios circuitos en el mismo caño

Cuando comparten cañería, la corriente admisible baja. La Tabla 770.12.II da un factor de **0,80** para dos circuitos monofásicos y de **0,70** para tres. El PE no cuenta como cable cargado.

Con el ejemplo de 2,5 mm²: 21 A × 0,8 = 16,8 A. Con dos circuitos en el mismo caño, ese cable ya no admite una termomagnética de 20 A. Hay que bajar la protección o subir la sección. Cuándo se permite agrupar circuitos en una cañería es otro tema, que tiene sus propias reglas en la reglamentación.

## La caída de tensión

Desde los bornes de salida del tablero principal hasta cualquier punto de uso, el límite en circuitos terminales de iluminación y tomas es del **3 %**. En circuitos que alimentan solo motores es del 5 % en régimen y del 15 % en el arranque.

La norma da una tabla rápida para monofásico, con cables unipolares en caño y cos φ = 0,8, en V/(A·km): 26 para 1,5 mm², 15 para 2,5 mm², 10 para 4 mm², 6,5 para 6 mm² y 3,8 para 10 mm². Con ella el cálculo es directo. Ejemplo: 10 A por 2,5 mm² a 20 m de distancia da 15 × 10 × 0,020 = 3 V, que son cerca del 1,4 % de 220 V. La distancia es la longitud del recorrido, no los metros de cable ida y vuelta.

## Errores comunes en obra

- Poner una termomagnética de 16 A en un circuito de 1,5 mm² porque "el circuito de iluminación lleva 16 A".
- Usar 2,5 mm² con una termomagnética de 25 o 32 A en un circuito de uso especial.
- Meter varios circuitos en el mismo caño sin aplicar el factor de agrupamiento.
- Calcular la sección solo por corriente y no verificar la caída de tensión en los tramos largos.
- Usar cable de alambre macizo o cordón tipo taller en instalación fija: está prohibido.

## Preguntas frecuentes

**¿Alcanza con respetar la sección mínima de la tabla?** No siempre. La mínima es el piso. Después hay que verificar la corriente admisible, la coordinación con la protección y la caída de tensión; la sección final es la mayor que resulte de esas verificaciones.

**¿Puedo usar 1,5 mm² en un circuito de tomas?** No. Las tomas de uso general y especial llevan 2,5 mm² como mínimo. Y un circuito de iluminación que incluye tomas de uso general también.

**¿La sección de las llaves es la misma que la del circuito?** No. La alimentación y los retornos de las llaves pueden ser de 1 mm² como mínimo, según la Tabla 770.11.I.

## Cómo te ayuda EGC

Verificar corriente, protección y caída de tensión en cada circuito lleva tiempo, y un error se paga en obra. La [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) te ayuda a elegir la sección y a dejar el cálculo documentado para el presupuesto.

## Fuentes

- AEA 90364-7-770, Tabla 770.11.I (secciones mínimas).
- AEA 90364-7-770, Tabla 770.6.I (protección máxima por tipo de circuito).
- AEA 90364-7-770, Tabla 770.12.I (corriente admisible) y Tabla 770.12.II (agrupamiento).
- AEA 90364-7-770, 770.15.2.1 y 770.15.3 (coordinación cable-protección).
- AEA 90364-7-770, 770.15.6 y Tabla 770.15.IV (caída de tensión).
- Fichas de la base de conocimiento técnico de EGC.
