# 10 · Muy baja tensión y casos especiales

Fuente: AEA 90364-7-770, edición 2017.

## MBTS · Muy Baja Tensión Sin puesta a tierra (770.14.1, págs. 41-43)
- Protege a la vez contra contactos directos e indirectos si se cumple **todo** esto:
  - Tensión nominal de hasta **24 V** en locales secos, húmedos y mojados; hasta **12 V** donde el cuerpo puede estar sumergido.
  - Fuente de seguridad: transformador de seguridad **IEC 61558-2-6** o fuente **IEC 61558-2-16**. Salida ≤ 24 V y separación de protección entre primario y secundario. **Nunca autotransformador.**
  - El secundario y sus partes activas **no** se conectan a tierra ni a PE ni a partes activas de otros circuitos.
  - Las masas de los equipos MBTS **no** se conectan a tierra, ni a PE u otras masas, ni a masas extrañas (excepción: si un equipo tiene que quedar unido a una masa extraña, se admite si se asegura que no supera 24 V).
  - Fichas y tomas de MBTS según IEC 60309, que no encastren con otras tensiones y **sin** contacto de tierra.
- Si falla cualquiera de estas condiciones, el circuito **no** es MBTS: es MBTF.
- MBTS de **12 V** obligatoria para luminarias y aparatos sumergidos en piscinas, fuentes y juegos de agua (zonas 0 y 1), con la fuente fuera de las zonas 0, 1 y 2.

## MBTF · Muy Baja Tensión Funcional (770.14.1, nota 4, pág. 42)
- Misma tensión que la MBTS, pero se usa por funcionamiento (porteros, alarmas), no por seguridad.
- Se protege como un circuito común: barreras o aislación para la tensión del primario, y las masas se conectan al **PE del primario**, que tiene que tener corte automático (diferencial).
- El **PE acompaña** al circuito de MBTF.

## Timbres, porteros, alarmas (770.7.1 f y g, pág. 12)
- Sus fuentes pueden colgarse del circuito de iluminación (cada fuente = 1 boca).
- Alimentados en **MBTF**: toda parte metálica **a tierra**, y el PE acompaña al circuito.
- Alimentados en **MBTS** (transformador IEC 61558-2-6 o fuente IEC 61558-2-16 certificados): las masas **no** van a tierra.
- Fuentes de hasta 24 V: transformador con primario y secundario **separados**; **no** autotransformador.

## Flotantes, señalización y comandos en lugares mojados (770.7.1 h, pág. 12)
- Los circuitos de comando (interruptores a **flotante**, señalizaciones, alarmas) en ambientes mojados, **incluidos los tanques cisterna y elevado**, se alimentan en **MBTS**.
- Consecuencia para los posteos: un flotante eléctrico dentro del tanque conectado a 220 V **no cumple**. La 770 no dibuja el esquema; solo exige que ese circuito de comando sea MBTS. Antes de dibujar, verificar un equipo real cuyo circuito de flotante trabaje en MBTS (fuente de seguridad IEC 61558) y cómo maneja a la bomba.
- La bomba (motor) cumple 770.13.3 (ficha 05).

## Separación de sistemas en canalizaciones (770.10.3.8.2 h, pág. 30)
- 220/380 V, MBTS/MBTF, señales débiles y datos van en caños **separados** (ficha 07).

## Tiras y fuentes LED, dimmers, splits (770.1, pág. 5)
- Los cables entre fuente y LEDs (o entre unidades de un equipo) de más de 3 m, o con varias unidades esclavas, son **parte de la instalación**: aislación adecuada, sección correcta y protección contra sobrecarga y cortocircuito.
- La Tabla 770.11.I fija 1,5 mm² para **circuitos de uso específico que alimentan MBTF**. La 770 **no** fija la sección de los cables entre la fuente y la tira LED: no afirmar un mínimo para ese tramo.
- Instalación a la vista de desnudos o sin envoltura en el aire: solo hasta 24 V con fuente MBTS (770.10.1 g).

## Cercas eléctricas (770.7.7, pág. 17)
- Equipos según IEC 60335-2-76, montados según el fabricante, a **2,5 m o más** sobre el piso terminado.
- Circuito **independiente**, siempre con diferencial **≤ 30 mA**.
- Carteles de señalización; la operan personas autorizadas.

## Calefacción radiante embutida (770.7.6, pág. 17)
- Cables o folios radiantes en techos y pisos: Anexo E de AEA 90364-7-771 (no está en esta biblioteca).

## Equipos de ubicación fija en cocina y lavadero (770.7.1 i, pág. 12)
- Heladera, freezer, extractor de humo, lavavajillas, cocina, anafe y horno (también a gas con alimentación eléctrica), lavarropas, secarropas, planchadoras fijas.
