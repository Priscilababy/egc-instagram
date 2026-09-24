# 03 · Colores e identificación de cables

Fuente: AEA 90364-7-770, edición 2017, **770.10.3.8.5 y Tabla 770.10.XIII (pág. 34)**. Verificado sobre la imagen de la página.

## Código de colores

| Conductor | Designación | Color |
|---|---|---|
| Línea 1 (fase R) | L1 | **Castaño** (marrón) |
| Línea 2 (fase S) | L2 | **Negro** |
| Línea 3 (fase T) | L3 | **Rojo** |
| Neutro | N | **Celeste** (azul claro) |
| Protección | PE | **Verde-amarillo** (bicolor) |

## Reglas (en palabras propias)
- **Fases:** se usan los colores de la tabla. Si por fuerza mayor se usa otro color, nunca puede ser celeste, azul, verde, amarillo ni verde-amarillo, y cada cable se identifica en **los dos extremos de cada tramo** (cinta del color normalizado, anillo o marca indeleble) (a).
- **Monofásico:** la fase puede ir en cualquiera de los tres colores de fase. Si ese circuito monofásico sale de una instalación trifásica, la fase lleva el color de la fase de la que sale (b).
- **Retornos y demás funciones** (por ejemplo, retornos de llaves de iluminación) (c):
  - **No** se usan los colores de fase (castaño, negro, rojo), ni el de neutro, ni el de protección, ni el verde ni el amarillo por separado.
  - Solo por **fuerza mayor** se admite un color de fase (castaño, negro o rojo), y en ese caso cada cable se identifica en los dos extremos de cada tramo. Nunca celeste, azul, verde, amarillo ni verde-amarillo.
  - Conclusión práctica: el retorno va en un **color no reservado** (por ejemplo blanco, gris o violeta). La norma no nombra colores permitidos; solo dice cuáles no.
- **PE:** siempre verde-amarillo. Por eso no se permite usar cables verde-amarillo, verdes ni amarillos para otra cosa (d).
- **Neutro:** siempre celeste o azul. Por eso no se permiten cables celestes ni azules para otra función (e).
- Cuando varios circuitos comparten caja, los cables se identifican para no mezclarlos (colores, anillos numerados u otro medio indeleble) (770.10.3.8.2 e, pág. 30).
- La inspección inicial verifica que los colores de fase, neutro y PE coincidan con el código (770.19.3.1 j, pág. 58).

## Cómo aplicarlo en las placas de EGC
- Fase: castaño continuo. Neutro: celeste continuo. PE: verde-amarillo.
- **Retornos y viajeros: color no reservado** (en `placa.py`: `RET` gris oscuro y `RET2` violeta, punteados), rotulados "retorno" o "viajero" si hace falta.
- **No** dibujar retornos en negro ni rojo: en la 770 esos son colores de fase y solo se admiten por fuerza mayor.
- Los cables propios de un aparato (fotocélula, sensor, timer) pueden venir de fábrica en otros colores: se dibujan como indica el fabricante y se aclara que se confirma en el manual del modelo.

## Normas relacionadas (fuera de la 770; verificado en web en una sesión anterior)
- IRAM NM 247-3 es la norma del **cable** unipolar de PVC (reemplazó a IRAM 2183), no la del código de colores.
- IEC 60446 fue retirada; su contenido pasó a IEC 60445.
