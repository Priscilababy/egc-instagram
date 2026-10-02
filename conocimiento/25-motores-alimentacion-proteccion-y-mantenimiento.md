# 25 · Motores: alimentación, protección y mantenimiento

Fuente: artículos técnicos de la revista Ingeniería Eléctrica (Lote 3, ver ficha 00). Son **SECUNDARIA**. Para motores en vivienda **manda la ficha 05** (770.13.3: maniobra que corte fase y neutro o todas las fases, detección de falta de fase en trifásicos, protección de sobrecarga **dedicada**, protección contra cortocircuito y fuga a tierra).
La sección 558 de la AEA 90364-5 que citan **no está en esta biblioteca**: citar "reglamentación AEA 90364".

Códigos de fuente: (MOT-AEA) = Farina, "Alimentación de los motores eléctricos trifásicos según la reglamentación de la AEA" (2024); (MOT-TAB) = Farina, "Tableros, canalización y motores eléctricos" (2026); (FAB-ALT), (FAB-CAL), (FAB-MAN), (FAB-SOB) = notas de un fabricante de motores sobre altura (2025), ola de calor (2025), mantenimiento (2026) y sobrecalentamiento (2026); (BER) = Berizzo, motor de inducción (2021).

## Lo que **no** hay en estas fuentes
- No nombran guardamotor, relé térmico, curvas ni valores de ajuste.
- No tratan arranque estrella-triángulo, arrancador suave ni variador como método de arranque.
- No dan temperaturas por clase de aislación ni valores mínimos de megóhmetro para bobinados. (Los 0,5 MΩ de la ficha 12 son para circuitos, **no** para motores.)

## Cable de alimentación (MOT-AEA)
- **Un motor**: el cable tiene que admitir al menos el **125 % de la corriente nominal** del motor.
- **Varios motores**: 125 % de la nominal del más grande **más** la suma de las nominales de los demás. Si un enclavamiento impide que arranquen juntos, se cuentan solo los que pueden arrancar a la vez.
- **Motores y otras cargas**: 125 % del motor más grande más las nominales del resto; sobre el total se puede aplicar un factor de simultaneidad bien justificado.
- Caída de tensión: 5 % en régimen y 15 % en el arranque → ya está en ficha 04.

## Seccionamiento y bloqueo (MOT-AEA)
- En el tablero, cada motor lleva un **seccionador que se pueda bloquear con candado en abierto**.
- Si el arranque es automático o el motor no se ve desde el tablero, va **otro seccionador cerca del motor**, también bloqueable. Sirve para trabajar con seguridad.
- Coherente con la ficha 05 (termomagnéticas bloqueables en abierto).

## Protecciones (MOT-AEA, FAB-SOB)
- Proteger cable, motor y aparato de maniobra contra sobrecargas en marcha y en el arranque. El dispositivo se elige según el motor y su servicio; consultar al fabricante.
- **Falta de tensión**: dispositivo que corte. Al volver la tensión, el motor puede no arrancar solo o reconectarse automáticamente: se elige según el riesgo de un arranque imprevisto para quien opera.
- Circuito de fuerza y circuito de control llevan cada uno su protección contra cortocircuito.
- **Aviso:** el artículo dice que la protección contra cortocircuito "no está mencionada" en la sección 558. En vivienda **sí** se exige por la 770 → ficha 05. Tampoco inferir que alcanza con la termomagnética: la sobrecarga del motor necesita protección **dedicada**.
- **Falta de fase**: sube la corriente en las fases que quedan y el motor se calienta. **Desequilibrio de tensión** entre fases: desequilibra las corrientes y calienta. Medir tensión entre fases y corriente por fase con el motor andando (FAB-SOB).

## Arranque y red pública (MOT-AEA)
- Con alimentación de la red pública de baja tensión, la corriente de arranque (motor o grupo, sumada a la carga ya conectada) **no debería superar el 40 % de la corriente máxima simultánea contratada**. Esa corriente se calcula con la potencia contratada en kW y cos φ 0,85.
- Con subestación propia o generador, el proyectista estudia cuánto motor admite en arranque directo.
- Dato del artículo, no verificado en la norma: citar "reglamentación AEA 90364".

## Mono o trifásico
- El instalador **no** elige si el motor es mono o trifásico: lo define el equipo. Sí tiene que conocer el **ciclo de trabajo** (duración y forma), porque de ahí salen cables y protecciones (MOT-TAB).
- En vivienda, la 770 **recomienda** pasar a trifásico por encima de **7 kVA o 32 A** → ficha 02. **No usar** la cifra de "hasta 14 kW en monofásico" de una nota comercial, ni la idea de que el monofásico "ahorra consumo".

## Tablero y canalización (MOT-TAB)
- Canalizaciones del tablero al motor y a sensores o pulsadores, elegidas según el ambiente (temperatura, humedad, gases, roedores, intemperie).
- Tablero accesible, seco, lejos de agua, gas y cloacas, con iluminación normal y de emergencia (coincide con ficha 09).
- Según el autor, lo que pide la reglamentación es un mínimo; la técnica de protección de motores de la bibliografía, IRAM e IEC lo completa.

## Altura y temperatura (FAB-ALT, FAB-CAL)
- El motor estándar está pensado para **1.000 m sobre el nivel del mar y 40 °C** de ambiente (IEC 60034-1). Más arriba, el aire enfría menos.
- Valores orientativos **de un fabricante** (no de la norma): a 2.000 m bajar la potencia útil 8 a 10 %; a 3.000 m, 15 a 20 %. Equivale a elegir un motor 10 a 20 % más grande.
- Regla práctica clásica (orientativa): la vida del bobinado se reduce **a la mitad por cada 10 °C** de más.
- Sobretensión y subtensión de la red calientan el motor (la subtensión lo obliga a tomar más corriente).

## Sobrecalentamiento: qué revisar (FAB-SOB)
| Causa | Qué revisar |
|---|---|
| Sobrecarga | Corriente de trabajo, carga accionada, potencia del motor |
| Ventilación | Ventilador, carcasa, entradas de aire, polvo, espacio libre |
| Desequilibrio de tensión | Tensión entre fases y corriente por fase |
| Falta de fase | Alimentación, bornes, protecciones, maniobra |
| Arranques frecuentes | Cantidad y duración de ciclos frente al régimen |
| Rodamientos | Lubricación, juego, ruido, vibración |
| Alineación y correas | Alineación, tensión de correas, poleas, acople |
| Ambiente | Temperatura del local, ventilación, polvo |
- Tocar la carcasa **no** es medir: puede estar muy caliente y ser normal. Comparar con la placa y los datos del fabricante.
- Si calienta sin que haya cambiado la carga, revisar la instalación eléctrica. Cambiar el motor sin corregir la causa mecánica repite la falla.

## Mantenimiento: frecuencias orientativas (FAB-MAN)
| Tarea | Frecuencia |
|---|---|
| Inspección visual, limpieza de ventilación, corriente de trabajo | Diaria o semanal |
| Control de temperatura | Diario/semanal en adelante |
| Vibraciones | Mensual |
| Reapriete de conexiones | Trimestral |
| Lubricación de rodamientos | Trimestral a anual, según horas y fabricante |
| Alineación motor-carga | Trimestral y anual |
| Aislación con megóhmetro, termografía | Semestral y anual |
- Es orientativo y no reemplaza al manual. Estrategias: correctivo, preventivo (por tiempo) y predictivo (por mediciones); conviene combinar las dos últimas.

## Datos útiles de teoría (BER)
- En Argentina la red es de **50 Hz**. Un motor de 4 polos gira a unas **1.450 rpm** (sincronismo 1.500).
- Potencia (kW) = par (N·m) × rpm / 9.550.
- Con variador, en cargas de par constante se mantiene la relación tensión/frecuencia (380 V / 50 Hz = 7,6 V/Hz). El variador genera armónicos e interferencias y necesita filtros.
- **No usar**: la "tolerancia de frecuencia de 5 a 10 %", los motores de 400 a 1.000 Hz y el artículo de ondas de torque (traducción de un tercero, fuera de ámbito).

## No usar
- Marcas, modelos y enlaces de fabricantes; correos y sitios de autores.
