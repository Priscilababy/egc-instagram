La caída de tensión es la diferencia entre la tensión que sale del tablero y la que llega al artefacto, y en los circuitos terminales de iluminación y tomas la AEA 90364-7-770 la limita al **3 %**. Se calcula multiplicando la corriente por la distancia y por el valor en V/(A·km) de la sección elegida. Si el resultado pasa del límite, no se cambia la protección: se sube la sección del cable.

## Qué dice la norma

La caída de tensión se mide **desde los bornes de salida del tablero principal hasta cualquier punto de uso**. Los límites de la reglamentación son:

- Circuitos terminales de iluminación y tomas (uso general o especial): **3 %** como máximo.
- Circuitos que alimentan solo motores: **5 %** en régimen y **15 %** durante el arranque.
- Circuitos seccionales: se recomienda no pasar del **1 %**.

Para el cálculo, las luminarias y las tomas se consideran con su demanda en el extremo más lejano del circuito. En iluminación se toma 2/3 de la carga total ubicada en el extremo.

## Cómo se calcula

La fórmula general es ΔU = k · I · L · (R cos φ + X sen φ), donde:

- k vale 2 en monofásico y √3 en trifásico.
- I es la corriente de proyecto del circuito, en amperes.
- L es la **distancia** hasta el punto de uso, en kilómetros. Es el largo del recorrido, no los metros de cable de ida y vuelta: el factor 2 de k ya cuenta el retorno.
- R y X son la resistencia y la reactancia del cable por kilómetro.
- A falta de datos, se toma cos φ = 0,85. En el arranque de motores, cos φ = 0,30.

Para no usar R y X, la norma trae la Tabla 770.15.IV, con el valor ya resuelto en monofásico, cables unipolares en caño y cos φ = 0,8. Se expresa en V/(A·km):

- 1,5 mm²: 26.
- 2,5 mm²: 15.
- 4 mm²: 10.
- 6 mm²: 6,5.
- 10 mm²: 3,8.
- 16 mm²: 2,4.

Con esa tabla la cuenta queda así: **ΔU (en volts) = valor de la tabla × corriente × distancia en km**. Para pasarla a porcentaje, se divide por la tensión (220 V) y se multiplica por 100.

## Ejemplo 1: un circuito que cumple

Un circuito de tomas con cable de 2,5 mm², una corriente de proyecto de 10 A y 20 m de distancia:

- ΔU = 15 × 10 × 0,020 = 3 V.
- 3 V sobre 220 V es cerca del 1,4 %.
- Está dentro del límite del 3 %.

## Ejemplo 2: un circuito largo que no cumple

Ahora un circuito de uso especial de 2,5 mm² con una corriente de proyecto de 15 A. El 3 % de 220 V son 6,6 V.

- A 25 m: ΔU = 15 × 15 × 0,025 = 5,6 V, cerca del 2,6 %. Cumple.
- A 35 m: ΔU = 15 × 15 × 0,035 = 7,9 V, cerca del 3,6 %. **No cumple.**

Con la misma corriente, la distancia máxima para 2,5 mm² es de unos 29 m (6,6 ÷ (15 × 15) ≈ 0,029 km). A 35 m hay que subir a 4 mm²:

- ΔU = 10 × 15 × 0,035 = 5,25 V, cerca del 2,4 %. Cumple.

El cable de 2,5 mm² cumplía por corriente: la Tabla 770.12.I le da 21 A en cañería, y una termomagnética de hasta 20 A respeta la condición IB ≤ In ≤ Iz. Lo que falló fue la caída de tensión. Por eso la sección final es siempre la mayor que resulte de verificar todas las condiciones.

## Qué hacer cuando no cumple

- **Subir la sección del cable.** Es la solución de fondo: reduce el valor de la tabla y baja la caída.
- **Acortar el recorrido**, si el trazado lo permite.
- **No es solución cambiar la termomagnética.** La protección no corrige la caída de tensión y además tiene que seguir cumpliendo IB ≤ In ≤ Iz con el cable nuevo.

Si cambiás la sección, la protección máxima sigue dependiendo del tipo de circuito y de lo que el cable soporte. El cable más grande no obliga a poner una térmica mayor.

## Errores comunes en obra

- Elegir la sección solo por la corriente admisible y no verificar la caída en los tramos largos.
- Medir la distancia en metros de cable ida y vuelta y volver a multiplicar por 2: el factor k ya lo incluye.
- Mezclar unidades: la distancia va en kilómetros con los valores en V/(A·km).
- Usar el límite del 5 % de los motores en un circuito de tomas, que tiene límite de 3 %.
- Aplicar el 1 % recomendado para seccionales como si fuera el límite de un circuito terminal, o al revés.

## Preguntas frecuentes

**¿La caída de tensión se calcula con la corriente de la termomagnética?** No. Se calcula con la corriente de proyecto del circuito (IB), es decir, la que realmente va a circular según las cargas que alimenta.

**¿El límite del 3 % es el mismo para iluminación que para tomas?** Sí. En circuitos terminales de iluminación y tomas, de uso general o especial, el máximo es 3 %. Cambia solo para circuitos que alimentan únicamente motores.

**¿Qué pasa en el arranque de un motor?** Se admite una caída mayor, hasta el 15 %, y el cálculo se hace con cos φ = 0,30. En régimen, el límite de esos circuitos es 5 %.

## Cómo te ayuda EGC

Verificar la sección, la protección y la caída de tensión de cada circuito a mano lleva tiempo y es fácil equivocarse con las unidades. La [calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/) te ayuda a hacer esas verificaciones en cada circuito.

## Fuentes

- AEA 90364-7-770, 770.15.6: caída de tensión.
- AEA 90364-7-770, Tabla 770.15.IV: caída de tensión en V/(A·km), monofásico.
- AEA 90364-7-770, Tabla 770.12.I: corriente admisible en cañería.
- AEA 90364-7-770, 770.15.2.1 y 770.15.3: coordinación IB ≤ In ≤ Iz.
- Fichas de la base de conocimiento técnico de EGC.
