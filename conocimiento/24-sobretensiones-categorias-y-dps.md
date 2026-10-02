# 24 · Sobretensiones: origen, categorías, DPS y varistores

Fuente: artículos técnicos de la revista Ingeniería Eléctrica (Lote 3, ver ficha 00). Son **SECUNDARIA**. Lo que dice la ficha 05 sobre DPS (cuándo es obligatorio) **manda**.
Las partes de la AEA que citan (90364-3, 90364-4-44, secciones 442 y 443) **no están en esta biblioteca**: citar "reglamentación AEA 90364" salvo que se verifique el número en el original.

Códigos de fuente: (SOB2), (SOB3), (SOB4) = Farina, "Protección contra las sobretensiones", partes 2 (2024), 3 (2025) y 4 (2025); (MOV) = Santos y otros, "Los varistores de óxido metálico" (2026).

## Lo que **no** hay en estas fuentes
- No hay datos de DPS para obra: tipo o clase (1, 2, 3), Up, In, Iimp, ubicación, coordinación entre DPS ni largo de los cables de conexión. **No completar con memoria.**
- No hay datos sobre efectos de la corriente en el cuerpo humano.

## De dónde vienen las sobretensiones (SOB2)
1. **Rayos** (directos o inducidos en las líneas).
2. **Electricidad estática** (fricción entre cuerpos; en industria puede causar explosiones: Decreto 351/79, reglamentario de la Ley 19.587).
3. **Contacto** con un sistema de mayor tensión.
4. **Resonancia** eléctrica.
5. **Maniobras**: conexión o desconexión de cargas grandes o de líneas.
- Las sobretensiones de **maniobra** son menores que las de rayo: proteger contra rayos normalmente cubre también las de maniobra (SOB3, SOB4).

## Nivel ceráunico (SOB2, SOB3)
- **Nivel ceráunico**: días por año en que se oye al menos un trueno. Se dibuja en mapas con isolíneas.
- **Ng** (densidad de rayos a tierra): impactos por km² por año. **No** es lo mismo que el nivel ceráunico.
- Clasificación de influencias externas AQ (AEA 90364-3, según SOB3):
  - **AQ1**: despreciable; el riesgo llega por la red de alimentación.
  - **AQ2**: exposición indirecta; instalaciones alimentadas por **líneas aéreas**.
  - **AQ3**: exposición directa; partes de la instalación afuera del edificio expuestas a caídas directas.
- Los umbrales de días por año: usar los de la **ficha 05** (AQ1 ≤ 25, AQ2 > 25). El artículo los trae invertidos.
- Quién publica el mapa: la ficha 05 dice AEA 92305-11; un artículo dice IRAM. Gana la ficha.

## Categorías de sobretensión (SOB4) — VERIFICAR antes de publicar
La AEA 90364-4-44 (443) agrupa los materiales en cuatro categorías según dónde se instalan, y pide que cada material soporte un impulso mínimo.

| Categoría | Dónde | Ejemplos (según el artículo) |
|---|---|---|
| **IV** | Origen de la instalación, antes del tablero principal | Medidor, protección principal, DPS general |
| **III** | Instalación fija | Tableros, interruptores, tomacorrientes, cables, cajas, motores fijos |
| **II** | Aparatos que se enchufan | Electrodomésticos con programador mecánico, herramientas portátiles |
| **I** | Equipos que necesitan protección especial | Computadoras, electrodomésticos con electrónica; solo en circuitos terminales |

Tensión de impulso que tiene que soportar el material, red **230/400 V** (fila que corresponde a la red argentina 3 × 380/220 V): **IV 6 kV · III 4 kV · II 2,5 kV · I 1,5 kV** (según SOB4, Tabla 44.3).
- **Aviso:** el artículo trae además una fila "monofásica 220-240 V con punto medio" con valores un escalón más bajos. Esa fila corresponde a redes con punto medio que **no** existen en Argentina. Una vivienda monofásica de 220 V sale de una red 380/220 V. **No usar esa fila** y no publicar la tabla sin verificarla en la AEA original.
- El artículo ubica los medidores en la categoría IV y también los nombra en la III. Usar IV.
- Las filas de 400/690 V y 1.000 V son industriales: fuera de ámbito.

## Control natural y control de protección (SOB4)
- **Control natural**: la red, por cómo es, no deja pasar sobretensiones mayores a lo que soportan los materiales.
- **Control de protección**: se logra con medios específicos, como el **DPS**.
- La sección 443 **no** cubre la caída directa de un rayo sobre la línea de baja tensión o la instalación (AQ3): eso va por protección contra rayos (AEA 92305).
- Hay un método de evaluación de riesgo simplificado (AEA 92305) que combina el largo de la línea de alimentación con el nivel de consecuencias. El nivel más bajo es "una persona" (vivienda o local chico).

## DPS: requisitos generales
- Si el inmueble tiene **pararrayos**, lleva DPS (SOB4; coincide con ficha 05).
- El DPS tiene que cumplir **IEC 61643** (SOB4). (No repetir que la tabla de categorías "está en relación con la IEC 61643": la IEC 61643 es norma de producto del DPS.)
- Los DPS modernos traen un **desconectador térmico** en serie con el varistor: abre antes de que el varistor se recaliente y rompa la envoltura (MOV).
- Conviene un **fusible o termomagnética** asociado al DPS para evitar fallas peligrosas por sobrecarga (MOV).
- La calidad del DPS depende también de sus conexiones internas y su envoltura, no solo del varistor (MOV).

## Cómo funciona un varistor (MOV)
- Disco de óxido de zinc. A tensión normal deja pasar solo una fuga de **microamperes**.
- Ante una sobretensión su resistencia baja de megaohms a pocos ohms en **nanosegundos** y deriva la energía; después vuelve solo a su estado normal.
- Parámetros que figuran en las hojas de datos:
  - **Uc (o MCOV)**: tensión máxima que soporta en forma permanente. Tiene que superar la tensión máxima de la red con sus tolerancias. Si es baja, el varistor conduce de más y se quema; si es alta, deja pasar más tensión al equipo.
  - **Vc** (tensión de limitación): lo que queda en bornes durante el impulso. Tiene que estar por debajo de lo que soporta el equipo protegido.
  - **E**: energía que absorbe (joules).
  - **Imax**: corriente máxima de impulso con onda normalizada **8/20 µs**. (Es dato del componente; no confundir con In del DPS.)
  - **IL**: corriente de fuga. Si crece con el tiempo, el varistor se está degradando.
- **Se gasta**: con cada impulso grande, con la tensión permanente y con el calor. Al degradarse aumenta la fuga, se calienta más y puede terminar en cortocircuito o rotura. Por eso un DPS no es eterno y conviene revisarlo, sobre todo después de tormentas.

## No usar
- Marcas y empresas de los artículos, correos de autores.
- Las cifras de "porcentaje de incendios de origen eléctrico" sin fuente.
- Contenido de laboratorios de **media tensión** (valores de resistencia de contacto y calentamiento de equipos MT).
- La nota de opinión "Accidentes eléctricos": no trae datos que citar.
