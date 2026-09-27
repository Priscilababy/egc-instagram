# 18 · Aire acondicionado: conexión eléctrica

Fuentes: AEA 90364-7-770 (fichas 01 a 12), AEA 90364-7-771 (ficha 14), manuales F1 a F4, pliegos P1 a P3. Detalle en ficha 00.

## Qué circuito lleva un split
- La norma decide por la **corriente del equipo** y el **tipo de toma**, no por las frigorías. Ni la 770 ni la 771 fijan "a partir de X frigorías, circuito propio" (771: búsqueda sin resultado; ver ficha 14).
- **Toma de 10 A (TUG):** solo cargas de hasta 10 A por toma (770: ficha 02; 771.7.6 a, pág. 22).
- **Toma de 20 A en circuito TUE:** cargas de más de 10 A y hasta 20 A, con toma 2P+T de 20 A IRAM 2071 (770: ficha 02; 771.7.6 b, pág. 23). Es un circuito de uso especial y puede tener varias bocas.
- **Circuito ACU (uso específico):** alimenta **un solo equipo, sin ninguna derivación**, por conexión fija o toma dedicada. Sección mínima 2,5 mm²; la protección la fija el proyectista según el equipo (771.7.6 c2, pág. 24; Tabla 771.13.I, pág. 89). En viviendas la 770 remite a la 771 para estos circuitos (ficha 02).
- La norma da como ejemplo de uso específico a las **unidades condensadoras de climatización central** (771.7.6 c, pág. 23).
- **Lo que piden los fabricantes:** **línea exclusiva** para el equipo, sin otros aparatos (los 4 manuales); sin alargues (F1 p. 3, 13). Aunque la norma permitiera compartir un TUE, el manual manda para no perder la garantía.
- En la práctica, la forma que cumple con la norma **y** con el fabricante es un circuito exclusivo por equipo (TUE de una sola boca o ACU).

## Protecciones
- **Diferencial de 30 mA obligatorio** también en el circuito del aire (770.14.2.3; 771.18.3.5, pág. 123). Ningún manual de fabricante lo menciona, pero la norma lo exige.
  - Única excepción de la 771: un ACU donde se **demuestre** que el diferencial perturba el equipo, con protección alternativa. No aplica a un split común (ficha 14).
- **Termomagnética bipolar** con los dos polos protegidos (770.16.5.1; 771.20.5.1).
- **Coordinación:** corriente del equipo ≤ calibre de la térmica ≤ corriente admisible del cable (IB ≤ In ≤ Iz, ficha 04). Con 2,5 mm² en caño (21 A), la térmica no pasa de 20 A.
- F1 y F2 piden una protección de "1,5 veces la capacidad máxima de la unidad". Esa cuenta no reemplaza la verificación IB ≤ In ≤ Iz: si da más que lo que admite el cable, se sube la sección.
- **Corte omnipolar:** los 4 manuales piden un interruptor que corte **todos los polos**, y 3 de ellos con **separación de contactos de al menos 3 mm** (F1 p. 13; F2; F3). Verificar que el interruptor elegido tenga esa separación de contactos: esta biblioteca no tiene el dato de cada producto.
- **Motores** (regla general): maniobra que corte fase y neutro y protección de sobrecarga propia; la térmica no sirve como protección de sobrecarga del motor (770.13.3; 771.17.3). La norma no dice si la protección interna del equipo alcanza: no afirmarlo.

## Cables y sección
- **Sección mínima 2,5 mm²** para TUE y circuitos de uso específico (Tabla 770.11.I; Tabla 771.13.I).
- La sección se elige con la **corriente de la placa** del equipo. F1 y F2 dan esta guía: hasta 16 A → 2,5 mm²; de 16 a 25 A → 4 mm²; de 25 a 40 A → 6 mm² (F1 p. 14). Igual se verifica IB ≤ In ≤ Iz y la caída de tensión (ficha 04).
- Caída de tensión: 3 % para circuitos terminales desde el tablero principal (ficha 04). La 771 admite 5 % solo en circuitos que alimentan **únicamente motores** (771.13 b); para un split, calcular con 3 % es el criterio seguro (criterio EGC, no de la norma).
- **Caño propio:** un circuito específico no comparte caño con circuitos de uso general o especial (ficha 07; 771.12.3.13.2 d, pág. 82).
- **Conexión fija:** el caño puede llegar hasta la caja de conexión del equipo (ficha 07; 771.12.3.1, pág. 55).
- **Cordón flexible (tipo taller):** prohibido como instalación fija (770.10.1; 771.12.1 l).

## Cable entre la unidad interior y la exterior
- Si mide **más de 3 m**, o hay varias unidades esclavas, ese cable es **parte de la instalación**: aislación, sección y protección según la 770 (770.1; ficha 01).
- Los manuales piden **al menos 1,5 mm²** para la interconexión (F3, F4). La cantidad de hilos depende del modelo: frío solo lleva menos que frío-calor. **Confirmar los bornes en el manual del modelo.**
- Hacer un **bucle de goteo** en el cable que entra a la exterior, para que el agua no corra hacia los bornes (los 4 manuales).
- Aislar los conductores que no se usan (los 4 manuales).
- No mezclar fase y neutro; no cruzar el cable de señal con otros; alejar los cables de caños calientes, del compresor y de partes móviles (F1 p. 14-15).
- Algunos equipos se alimentan por la interior y otros por la exterior: **lo dice el manual**.

## Puesta a tierra
- **Obligatoria** en los 4 manuales y en la norma: el PE llega a las dos unidades (fichas 06; 771.18.5.7).
- En aparatos de conexión fija, el PE va dentro del mismo cable multipolar o en la misma canalización (771.18.5.7, pág. 128).
- F4 pide una resistencia de tierra menor a 4 Ω (F1 dice "menor a 4", sin unidad). Es un pedido del fabricante, más exigente que los 40 Ω de la norma (ficha 06): anotar la medición en la entrega.

## Unidad exterior e intemperie
- Cajas con dispositivos a la intemperie: **IP44** sin chorros de agua; **IP55** con chorros (770.6.5, ficha 07; 771.7.6 nota 2, pág. 22).
- Tomas a la intemperie: la 771 las pone en circuito **TUE** (771.7.6 b, pág. 23). La 770 no trae esa obligación: en vivienda es un criterio recomendado. El IP de la toma vale **sin la ficha puesta**; si tiene que mantenerlo enchufado, usar tomas IEC 60309 (en 220 V, azul "6 h") (771.7.6 nota 2).
- Instalación a la intemperie: **IP54**, con las uniones caño-caja selladas (771-B.3, pág. 169).
- Cablecanal a la intemperie: IP543 y protección solar **alta** (Tablas 771.12.IV y V, págs. 60-61).
- Cable con envoltura (IRAM 2178 / 62266) fijado sobre la fachada: solo a **más de 2,5 m** de altura (771.12.2 e9, pág. 50; 770.10.1).
- Cable expuesto al sol: factor de corrección **0,85** (771.16.2.3.2, pág. 101).
- Cajas de acero solo esmaltadas: no se admiten a la intemperie (ficha 07).

## Antes de conectar
- Medir la tensión y compararla con el rango del manual del modelo. Los manuales de esta biblioteca no coinciden (y uno se contradice): no publicar un rango único.
- Si la instalación existente no es segura, **frenar** y explicárselo al cliente (F1 p. 13). Es un buen momento para presupuestar el circuito nuevo.
- Después de un corte de luz, los equipos con motor que arrancan solos pueden necesitar precauciones (771.19.6, pág. 141). Varios equipos traen un retardo de 3 minutos del compresor (F2).
