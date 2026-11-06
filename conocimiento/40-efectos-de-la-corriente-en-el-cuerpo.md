# 40 · Efectos de la corriente en el cuerpo humano

Fuente: *Manual del Instalador Electricista · Categoría III*, 2.ª edición, Fundación Relevando Peligros (Córdoba, 2020), secciones 2.19 y 2.20 (págs. 124-139) y 4.7 (págs. 347-349). Fuente **SECUNDARIA**.
El manual cita la IEC 60479-1 (que **no** está en esta biblioteca). Las cifras de abajo son las que da el manual.

## Conceptos (pág. 124)
- **Electrización:** la corriente pasa por el cuerpo. Hay un punto de entrada y uno de salida.
- **Electrocución:** la persona muere por el paso de la corriente.
- **Fibrilación ventricular:** el corazón se mueve sin ritmo y deja de bombear sangre. Es la causa principal de muerte por choque eléctrico (pág. 127).
- **Tetanización:** los músculos se contraen sin control. La persona puede no poder soltar.
- **Asfixia:** la corriente afecta el centro nervioso de la respiración.
- Las quemaduras profundas también pueden ser mortales.

## Umbrales (págs. 127-129)
- **Percepción:** 0,5 mA en corriente alterna; 2 mA en corriente continua.
- **No soltar:** 10 mA en corriente alterna. Por encima, la persona puede no soltar lo que agarró.
- **Fibrilación:** depende de la corriente y del tiempo. El manual da un ejemplo: en alterna, con menos de 100 mA, puede haber fibrilación si el contacto dura más de 500 ms (pág. 129).
- Con corriente alta y gran superficie de contacto puede haber fibrilación **sin marcas en la piel** (pág. 125).
- **Período vulnerable:** una parte chica del latido, cerca del 10 % del ciclo, donde el corazón es más sensible (pág. 128).

## Qué hace más grave un accidente (págs. 129-135)
- **Intensidad** y **duración** del contacto: son los dos factores principales.
- **Impedancia del cuerpo:** cambia con la tensión, la humedad de la piel, la superficie y la presión de contacto.
- Por encima de 50 V la resistencia de la piel cae rápido (pág. 130).
- El manual toma 2.500 Ω entre mano y pie como referencia (pág. 132).
- **Recorrido:** los recorridos que pasan por el tórax o la cabeza son los más graves (pág. 134).
- **Factor de corriente de corazón F:** compara recorridos. Mano derecha-pies: F = 0,8. Ejemplo del manual: 200 mA mano-mano equivalen en riesgo a 80 mA mano izquierda-pies (pág. 135).
- **Corriente continua vs. alterna:** la continua es en general menos peligrosa; es más fácil soltar y el umbral de fibrilación es más alto (pág. 134).
- **Frecuencia:** a frecuencias muy altas baja el riesgo de fibrilación, pero predominan las quemaduras (pág. 134).

## Tensiones de seguridad (págs. 132 y 349)
- La AEA acepta **24 V** en lugares secos y **12 V** en lugares húmedos, mojados o con el cuerpo sumergido, en alterna y en continua.
- Se logra con transformador de seguridad (ficha 10 y ficha 37).
- MBTS no es lo mismo que MBTF: la MBTF solo comparte el valor de tensión, no los demás requisitos (pág. 348).

## Contacto directo e indirecto (págs. 137-139)
- **Directo:** se toca una parte activa, que está en tensión en servicio normal (cables, barras, bornes).
- **Indirecto:** se toca una **masa** que quedó en tensión por una falla de aislación (carcasa metálica de un equipo).
- En el contacto indirecto solo una parte de la corriente pasa por la persona. El resto va a tierra por la puesta a tierra de la masa.
- Si la masa está mal puesta a tierra, el contacto indirecto se vuelve tan peligroso como el directo.
- "No hay riesgo cero": la puesta a tierra sola no garantiza la seguridad. Hace falta el diferencial (pág. 139).

## Medidas de protección según el manual (pág. 348)
- Contra contacto directo: aislación, barreras o envolventes, obstáculos, alejamiento, y diferencial de 30 mA como medida adicional.
- Contra contacto indirecto: corte automático de la alimentación, Clase II, local no conductor, conexión equipotencial no conectada a tierra, separación eléctrica.
- En baños, varias de estas medidas están **prohibidas** (ficha 37).

## No usar
- **Tiempos de disparo del diferencial del manual** (pág. 137: 0,2 s, 0,1 s y 0,04 s con 10 × IΔn): **no coinciden** con IEC 61008-1. Usar los de `CLAUDE.md`: hasta 300 ms con IΔn, 150 ms con 2 × IΔn, 40 ms con 5 × IΔn.

## Ideas para posteos "¿Sabías que...?"
- Con 10 mA en alterna una persona puede no poder soltar el cable.
- La corriente que se siente empieza en 0,5 mA.
- Puede haber un choque mortal sin quemaduras en la piel.
- El recorrido importa: mano a mano no es igual a mano a pie.
- La puesta a tierra sola no alcanza: el diferencial es el que corta.
