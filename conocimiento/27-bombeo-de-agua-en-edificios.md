# 27 · Bombeo de agua en edificios y bombas centrífugas

Fuente: Farina, "Sistema de agua en los inmuebles de propiedad horizontal" (publicado en Ingeniería Eléctrica, octubre 2019) = (AGUA); nota de un fabricante de bombas sobre cómo purgar una bomba centrífuga (2022) = (PURGA). Son **SECUNDARIA**.
**Mandan** las fichas 05 (motores) y 10 (flotantes en MBTS).

## Esquema típico de un edificio (AGUA)
- Cisterna con válvula de flotante mecánica en la entrada → **dos bombas centrífugas** (una de reserva) → caño de subida con **válvula de retención** cerca de las bombas → tanque elevado.
- **Alternancia**: las bombas se turnan para gastarse parejo. La conmutación puede ser manual o automática (por ejemplo, por horas de marcha).
- **Flotante de cisterna**: impide que la bomba arranque o la para si falta agua (que **no trabaje en seco**).
- **Flotante del tanque elevado**: para la bomba al llegar al nivel máximo.
- Cada flotante se conecta en una caja cercana y de ahí van los cables de control al tablero, en cañería. **Cajas de paso y de bornes estancas.**
- Tablero de bombas cerca de ellas, con maniobra, protección, automatismo y **selector manual / automático** (para fallas, puesta en marcha y mantenimiento).
- Ese tablero se alimenta desde el tablero general, en el circuito de **servicios generales** (junto con ascensores e iluminación de espacios comunes).
- Opcional: alarma si una bomba se para en marcha.
- Si el edificio tiene grupo electrógeno, las bombas se consideran carga de emergencia.

## Puesta a tierra de la cañería (AGUA)
- El teflón de las roscas **aísla**: la cañería de acero puede quedar sin continuidad.
- Si no se comprueba la continuidad midiendo, poner **puentes conductores** entre caños, codos y válvulas.
- La cañería va a la barra de PE del tablero de bombas, y esa barra a la puesta a tierra general.
- Coincide con las fichas 06 y 12 (continuidad de las masas).

## Lo que el artículo **no** dice y la norma sí
- **Tensión de control de los flotantes**: el artículo dice "hasta 48 V". **No usar.** La 770 exige **MBTS** para los circuitos de flotante dentro de cisterna y tanque → ficha 10.
- El artículo no menciona diferencial ni detección de falta de fase. Para motores, la 770 pide maniobra que corte todas las fases, detección de falta de fase, protección de sobrecarga dedicada y protección contra fuga a tierra → ficha 05.

## Purgar (cebar) una bomba centrífuga (PURGA) — orden corregido
Señales de que le falta cebado: no aspira, rinde poco, hace ruido y vibra. La causa típica es una **entrada de aire** (un agujero chico o una unión mal sellada en la succión).

1. Desconectar la bomba.
2. Verificar que la válvula de pie esté bien sumergida (ni afuera ni al ras del agua).
3. Revisar que la cañería de succión y sus uniones no tomen aire (incluido el o-ring de la tuerca de unión).
4. Sacar el tapón de purga y revisar su o-ring.
5. Llenar de agua despacio hasta que salga sin aire; si hace falta, girar el eje a mano para liberar burbujas y volver a completar.
6. Colocar el tapón y **todas las tapas y protecciones** antes de energizar.
7. Conectar, encender y verificar el sentido de giro **según el manual de la bomba**.
8. Abrir una canilla para comprobar.

- La nota original manda encender **antes** de colocar la tapa trasera (cubreventilador): es un riesgo mecánico, por eso se reordenó. **Nunca** hacer funcionar la bomba en seco.

## No usar
- Marca, modelos y potencias de la bomba de la nota comercial.
- La tendencia a bombeo solar (es mención general, sin datos).
