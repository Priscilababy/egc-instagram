# 23 · Puesta a tierra: terreno, electrodos, cálculo y casos de obra

Fuente: artículos técnicos de la revista Ingeniería Eléctrica (Lote 3, ver ficha 00). Son **SECUNDARIA**: lo que dice la ficha 06 (AEA 90364-7-770) **manda** sobre esta ficha.
Las cláusulas que citan los autores son de la **AEA 90364-7-771**, no de la 770. Si no se verificaron en el original, citar solo "reglamentación AEA 90364".

Códigos de fuente: (PAT1) a (PAT7) = serie "Sistema de puesta a tierra" de Farina, partes 1 a 7 (2022-2023); (MIR1) = Miravalles, "Tierras extrañas" (2021); (MIR2) = Miravalles, "Calefacción eléctrica y falta de puesta a tierra" (2022).

## Resistencia y resistividad (PAT1, PAT5)
- **Resistividad** (ρ): propiedad del terreno. Unidad correcta: **Ω·m**. (Algunos artículos escriben "Ω/m": es un error, no copiarlo.)
- **Resistencia de puesta a tierra**: valor del conjunto electrodo + cables + uniones. En alterna es en realidad una impedancia.
- La resistividad cambia con la humedad (época del año, napas), las sales disueltas, la temperatura, el tamaño de los granos y las capas del suelo. Los rellenos son impredecibles.
- Si el terreno se calienta por corrientes de falla grandes o permanentes, la resistividad sube.
- Agua con sales puede corroer lo enterrado.

### Resistividades orientativas (PAT1, Tabla 1; repetida en PAT5)
| Terreno | ρ aproximada |
|---|---|
| Pantanoso | 30 Ω·m |
| Arcilloso, greda, tierra de cultivo | 100 Ω·m |
| Arena húmeda | 200 Ω·m |
| Grava húmeda | 500 Ω·m |
| Arena o grava seca | 1.000 Ω·m |
| Rocoso | 3.000 Ω·m |

- Son valores **de referencia**. En obras grandes la resistividad se mide antes de proyectar, con el **método Wenner** (cuatro electrodos en línea). En obras chicas el autor indica reconocer el terreno y usar la tabla (PAT5).
- Igual, lo que vale es la **medición final** de la toma con telurímetro y el límite de **40 Ω** → ficha 06.

## Cuánto da una jabalina (PAT7)
- Fórmula que usa el autor (dice que sale de la AEA 771, anexo C, "771-C.10"): R = ρ / (2·π·L) × ln(8·L/d − 1). L = largo enterrado, d = diámetro.
- **Aviso:** la fórmula clásica (Dwight) se escribe distinto y da entre 13 y 15 % menos. Antes de publicar la fórmula, verificarla en la norma. La tabla de abajo es conservadora (da valores más altos).

Tabla del autor con ρ = 50 Ω·m (resistencia en Ω):
| Diámetro | 1,5 m | 3 m | 4,5 m | 6 m |
|---|---|---|---|---|
| 1/2" | 36,3 | 20,0 | 14,1 | 10,9 |
| 5/8" | 35,2 | 19,4 | 13,7 | 10,6 |
| 3/4" | 34,2 | 18,9 | 13,3 | 10,4 |

- Lo práctico: **el largo pesa mucho más que el diámetro**. Pasar de 1/2" a 3/4" baja la resistencia alrededor de 5 %; pasar de 1,5 m a 3 m la baja alrededor de 45 %.
- La resistencia es proporcional a ρ: con terreno de 100 Ω·m los valores se duplican (cálculo derivado de la tabla, no lo dice el artículo). Por eso en terrenos secos o arenosos una sola jabalina corta puede no alcanzar los 40 Ω.
- Los fabricantes de jabalinas normalizadas publican sus propias tablas (PAT7).

## Materiales (PAT5, PAT6)
- **Jabalina IRAM 2309**: acero revestido de cobre, tramos acoplables de 1,5 y 3 m, diámetros comerciales de 1/2", 5/8" y 3/4" (coincide con ficha 06).
- **Conductor enterrado** para unir jabalinas: según el autor, cobre de **35 mm²** mínimo (7 hilos, IRAM 2004), o acero recubierto de cobre (IRAM 2466 / 2467).
- **Accesorios**: tomacable, caja de inspección, acople, punta y sufridera (estos tres últimos, según el caso).
- Unión cable-jabalina: soldadura cuproaluminotérmica, conector a presión o pieza diseñada para eso, siempre **desarmable para medir** (coincide con ficha 06).

## Configuraciones de electrodos (PAT4)
- **Jabalina simple**: lo más común en vivienda. También varias en paralelo, unidas con conductor desnudo enterrado.
- **Triángulo**: tres jabalinas unidas por conductor enterrado. Baja resistencia y buena dispersión de fallas y rayos.
- **Cruz** (dos conductores perpendiculares enterrados a 0,5–0,75 m) y **pata de ganso** (tres conductores en abanico, con jabalinas en las puntas si hace falta): usadas para pararrayos.
- **Placa** (cobre o acero galvanizado): el autor la recomienda para datos, comunicaciones y pisos técnicos.
- **Malla** (cuadrícula de ~0,8 m a 0,8–0,9 m de profundidad), **anillo perimetral** con jabalina en cada esquina, y **hierros de las bases de hormigón** soldados entre sí: son de edificios e industria; en vivienda, solo como mención.
- Según el autor, la resistividad del terreno puede decidir qué configuración conviene.

## Tensión de paso, de contacto y equipotencialización (PAT2)
- **Tensión de paso**: entre los dos pies, separados unos 0,8 a 1 m.
- **Tensión de contacto**: de la mano a los pies, o de una mano a la otra.
- **Equipotencializar**: unir todas las masas propias y las masas extrañas (caños de agua y gas metálicos, estructuras, escaleras y conductos metálicos) a la barra equipotencial principal. Evita diferencias de tensión y arcos, sobre todo con rayos.
- Según el autor, conviene llevar directo a la barra principal: pararrayos, equipos de aire acondicionado en la terraza, antenas, estructuras metálicas decorativas, tendederos y carcasas de reflectores grandes.

## Secciones según la AEA 771 (PAT6) — solo como dato de la 771
- PE que **no** forma parte del cable de alimentación: **2,5 mm²** de cobre si tiene protección mecánica; **4 mm²** si no la tiene.
- En vivienda manda la 770: PE mínimo 2,5 mm² siempre en la canalización del circuito, y cable de puesta a tierra **mínimo 4 mm²** → ficha 06. **No** usar la tabla del artículo que admite 2,5 mm² para el conductor enterrado.

## Cortocircuito y sección de cables (PAT6)
- Para protecciones que abren en menos de 0,1 s se verifica k² × S² ≥ I²t (el I²t lo da el fabricante del aparato).
- Valores de k: cobre con PVC hasta 300 mm² **115**; más de 300 mm² **103**; cobre con XLPE o EPR **143**; aluminio con PVC hasta 300 mm² **76**; más de 300 mm² **68**; aluminio con XLPE o EPR **94**.
- La protección también tiene que actuar con el **cortocircuito mínimo** (el punto más lejano del circuito).
- La sección final es la que cumple a la vez calentamiento, caída de tensión y cortocircuito.
- **No usar** las fórmulas de 0,1 a 5 s tal como salen en el artículo: están mal transcriptas. Tampoco su temperatura de referencia de 30 °C (la 770 usa 40 °C → ficha 04) ni la frase "la caída de tensión no es relevante en casas chicas" (la 770 pide verificarla siempre).

## Casos de obra (MIR1, MIR2) — opinión y práctica de un técnico
- **Ni el diferencial ni el PE avisan cuando dejan de funcionar.** El diferencial puede perder sensibilidad (bornes flojos que recalientan, tableros chicos, ambiente desfavorable).
- Probar el diferencial con su botón **según indique el fabricante** (el autor dice "generalmente una vez por mes"). Es recomendación del fabricante, no de la AEA.
- Conectar los tomas al PE (y a fase y neutro) **con derivación**, sin usar los bornes del toma como empalme: coincide con la prohibición de la "guirnalda" de la ficha 06.
- **"Tierras extrañas"**: ejemplo de termotanque con falla, unido al PE por la ficha y a un caño metálico que más adelante sigue en plástico: la masa puede electrificar la cañería. Por eso las masas extrañas se equipotencializan.
- **Instalaciones viejas sin PE**:
  - Poner un toma de tres espigas sin PE da una **falsa sensación de seguridad**: la espiga de tierra no está conectada a nada.
  - Los tomas "binorma" tienen menos superficie de contacto y recalientan con cargas como estufas.
  - Para dar tierra **no** usar canillas ni caños metálicos: su continuidad es incierta. Pasar un PE nuevo por un caño ya ocupado puede dañar los cables existentes.
  - Recomendación del autor: materiales certificados y diferencial si no hay, o si el que hay no responde a la prueba.
- **No usar**:
  - La "prueba concluyente del PE" de MIR1 (hacer circular corriente por el PE anulando el diferencial): es riesgosa y no es método normalizado. El método de la norma está en la ficha 12.
  - Usar una pinza amperométrica para "probar" un diferencial.
  - "Los adaptadores están prohibidos": el autor no cita cláusula; no afirmarlo como norma.
  - Poner el aire acondicionado "lo más bajo posible" para calefaccionar: contradice los manuales → ficha 16.

## Fuera de ámbito (no usar en contenido domiciliario)
- Parte 3 completa (puesta a tierra del neutro de transformadores y generadores, media tensión). Solo se rescata que los **esquemas de conexión a tierra** (TT, TN, IT) están normalizados en **IRAM 2379**.
- Equipos y estructuras de obradores (grúas, andamios) y la verificación de continuidad "cada dos o tres días", que es de obra, no de vivienda (en vivienda: inspección periódica cada 5 años como máximo → ficha 12).
