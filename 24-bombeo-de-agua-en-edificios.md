# 24 · Sistema de agua en edificios de propiedad horizontal (bombeo)

Fuente: FAH (Farina, "Sistema de agua en los inmuebles de propiedad horizontal", Suplemento Instaladores, Ingeniería Eléctrica 347, octubre 2019). SECUNDARIA. Detalle en ficha 00.
La AEA 770 manda sobre esta ficha: flotantes en MBTS (ficha 10) y requisitos de motores (ficha 05).

## Componentes (FAH, figura 1)
- **Cisterna:** tanque subterráneo o a nivel. Recibe agua de la red pública.
- **Válvula a flotante mecánica** en la entrada de la cisterna: corta el ingreso al llegar al nivel fijado.
- **Filtro** en el fondo de la cisterna, conectado a la aspiración de las bombas.
- **Dos bombas centrífugas**, en general con motor asincrónico **trifásico**. Llevan el agua al tanque elevado.
- **Tanque elevado** en la parte más alta. Alimenta a cada unidad.
- **Válvula de retención** en el caño de subida, cerca de las bombas. Evita que el agua vuelva hacia la cisterna al parar la bomba.
- **Tablero de fuerza motriz y control**, cerca de las bombas.

## Funcionamiento (FAH)
- Normal: **automático**. Manual: para fallas, puesta en marcha o mantenimiento (conmutador manual).
- Funciona **una bomba por vez**; la otra es reserva.
- El control **alterna** las bombas para que se gasten parejo. La alternancia puede ser manual o automática por reloj (horas de funcionamiento).
- **Flotante de la cisterna (inferior):** con nivel bajo, para la bomba o impide que arranque. Evita que trabaje en seco y se dañe.
- **Flotante del tanque elevado (superior):** con nivel máximo, para la bomba. Evita el derrame.
- Cada flotante es un cuerpo flotante con un interruptor auxiliar dentro del circuito de control.
- Cada flotante llega a una **caja de conexiones estanca** cercana; de ahí salen los cables de control al tablero, en su canalización.
- Opcional: **alarma** sonora y luminosa (o solo sonora) si la bomba en marcha se detiene por falla.

## Alimentación (FAH)
- El tablero de bombas se alimenta desde el tablero general, en el circuito de **servicios generales** (junto con ascensores y luz de espacios comunes).
- Con grupo electrógeno de emergencia, el bombeo se considera una carga más a respaldar.
- Cables, relé de protección y aparatos de maniobra se eligen por la potencia de los motores y las distancias.

## Tensión del circuito de control · atención
- FAH dice: tensión auxiliar de control **no mayor a 48 V, 50 Hz**.
- La AEA 770 pide **MBTS** para los comandos a flotante dentro de tanques cisterna y elevado (770.7.1 h). MBTS = hasta **24 V**, con fuente de seguridad (ficha 10).
- **En posteos usar la 770: MBTS hasta 24 V.** No publicar "48 V".

## Puesta a tierra de la cañería (FAH)
- Las cañerías de **acero** tienen que tener continuidad eléctrica.
- El teflón de las roscas aísla. Si la continuidad no se verifica con medición, se ponen **puentes** de conductor entre caños, codos, válvulas, etc.
- La cañería se conecta a la **barra de PE del tablero de bombas**. Esa barra va a la PAT general del edificio.
- El agua de red sí conduce (solo el agua químicamente pura no conduce).

## Sensores de nivel (FAH)
- Usar marcas con trayectoria, con repuesto fácil de conseguir.
- Una falla deja al edificio sin agua y el cambio tarda (tanques elevados o subterráneos).
- Componentes eléctricos según normas IRAM.

## Tendencia (FAH)
- Bombeo con paneles fotovoltaicos: la energía se "guarda" como agua en los tanques en lugar de baterías.

## Lo que no está en esta biblioteca
- La 771 nombra las bombas elevadoras de agua como ejemplo de circuito de uso específico (771.7.6 c, ficha 14). Otros requisitos de servicios generales de edificios no están en esta biblioteca.
- Esquema de control con contactores, relés de alternancia y guardamotor: verificar en fuente oficial o de fabricante antes de dibujar.
- Requisitos de la motobomba (770.13.3): ficha 05.
