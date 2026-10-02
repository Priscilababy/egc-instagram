# 23 · DPS: el varistor de óxido metálico (MOV)

Fuente: SAN (Santos, Busse y Rosa, "Los varistores de óxido metálico", 2026-09-18, editores.com.ar/node/8619). SECUNDARIA, confiabilidad alta. Detalle en ficha 00.
Cuándo es obligatorio un DPS en vivienda: ficha 05 (Tabla 770.15.III). Esta ficha explica el componente, no la obligación.
SAN cita IEC 61643-11:2025 e IEC TR 61643-333:2026. No están en esta biblioteca: no citar sus cláusulas.

## Qué es
- El MOV es el componente no lineal más usado dentro de los DPS.
- Es una resistencia que depende de la tensión. Con tensión normal casi no conduce. Con sobretensión, conduce y desvía la energía.
- Material: disco sinterizado de granos de **óxido de zinc (ZnO)** con dopantes (bismuto, cobalto, manganeso, entre otros).
- El grano de ZnO conduce. El límite entre granos forma una barrera de potencial que bloquea la corriente a tensión normal.

## Cómo actúa (SAN, figuras 2 y 3)
- Con tensión de red: solo una corriente de fuga del orden de **microamperios**.
- Con sobretensión: su resistencia baja de **megaohmios a pocos ohmios** en **nanosegundos**.
- Al terminar el transitorio vuelve solo a alta impedancia.
- No tiene conmutación mecánica.

## Parámetros de la hoja de datos (SAN)
| Parámetro | Qué es | Si se elige mal |
|---|---|---|
| **V1mA** · tensión del varistor | Tensión en bornes con 1 mA de corriente continua. Referencia del inicio de conducción. | Muy baja: calienta y se degrada. Muy alta: protege tarde. |
| **Uc** (MCOV) · tensión máxima de funcionamiento continuo | Mayor tensión eficaz (CA) o continua aplicable en forma permanente. | Menor a la de la red: conduce siempre, calienta y falla. Muy alta: deja pasar más tensión a la carga. |
| **E** · energía absorbible | Energía de sobretensión que soporta, en joules. Depende de la forma de onda de ensayo. | Pulsos repetidos o largos lo degradan. |
| **Vc** · tensión de limitación (clamping) | Tensión aproximada en bornes con una corriente de sobretensión dada. Es lo que todavía recibe el equipo. | Tiene que quedar debajo de lo que soporta el equipo protegido. |
| **IL** · corriente de fuga | Corriente con la tensión normal de trabajo. | Si sube con el tiempo, indica degradación. |
| **Imáx** · corriente de sobretensión | Máxima corriente transitoria sin falla inmediata. Se da con onda normalizada, por ejemplo **8/20 µs**. | Subdimensionado: aguanta los primeros eventos y pierde capacidad. |

- Uc tiene que superar la tensión permanente máxima de la red (tolerancias y sobretensiones sostenidas incluidas).
- Compromiso de Vc: más baja protege mejor, pero el varistor conduce y disipa más.
- Todos los parámetros se evalúan juntos.
- La calidad del DPS también depende de las conexiones y la envolvente, no solo del MOV.

## Degradación y fin de vida (SAN)
- Degradarse = perder la no linealidad. Sube la fuga, sube el calor (efecto Joule).
- Mecanismo principal: baja la altura de la barrera Schottky en los límites de grano.
  - Migración de iones por el campo eléctrico permanente y la temperatura.
  - Sobretensiones repetidas de alta corriente: calentamiento local y pérdida de oxígeno en la interfaz. La barrera colapsa en forma permanente.
- Tres factores aceleran la degradación: tensión de red aplicada siempre, sobretensiones repetidas y **temperatura ambiente alta**.
- La resistencia baja al subir la temperatura. Si el calor supera lo que se disipa: **avalancha térmica** → cortocircuito, rotura o explosión del componente.
- Por eso los DPS modernos tienen un **desconectador térmico** en serie con el MOV. Abre el circuito antes de que la avalancha destruya la envolvente.
- Un DPS se evalúa también por su estabilidad en el tiempo y por **fallar de forma controlada**.

## Para los posteos
- Se puede explicar qué hay dentro del DPS y por qué envejece, con cita "según Santos, Busse y Rosa (2026)".
- **No** afirmar cada cuánto cambiar un DPS: la fuente no lo dice.
- **No** afirmar qué significa el indicador o la ventanita del frente de un DPS comercial: la fuente no lo describe. Manda el manual del fabricante.
- **No** dar valores de Uc, Imáx o Vc para elegir un DPS de vivienda: no están en esta biblioteca (IEC 61643-11, secciones 443 y 534 de AEA 90364).
- Una función de la PAT es dar baja resistencia a los descargadores de sobretensión (FA1, ficha 06).
