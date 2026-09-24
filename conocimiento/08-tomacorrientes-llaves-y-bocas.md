# 08 · Tomacorrientes, llaves y bocas

Fuente: AEA 90364-7-770, edición 2017.

## Tipos de toma (770.6.6, pág. 11)
- Uso general: 2P+T **10 A** según **IRAM 2071**.
- Uso especial: 2P+T **20 A** IRAM 2071, o tomas IRAM-IEC 60309 / IEC 60309 hasta 16 A.
- La posición de los bornes de la toma está en IRAM 2071, que **no** está en esta biblioteca.

## Alturas y ubicación (770.7.2, pág. 13)
- Tomas sobre zócalo: el borde inferior de la caja entre **0,20 y 0,30 m** del piso terminado.
- Como la 770 considera que hay **niños** (BA2), las tomas a nivel de zócalo o hasta **0,90 m** del piso son 2 × 10 A + T (IRAM 2071) **con pantalla** que impide meter objetos (IRAM-NM 60884-1 / IEC 60884-1).
- Sobre mesadas de baño, cocina y lavadero: borde inferior de la caja a **no menos de 0,10 m** sobre la mesada, respetando las distancias al agua de la Sección 701.
- Donde se limpia **baldeando**: borde inferior a **0,30 m o más** del piso (toma IP20 como mínimo); si queda más abajo, el conjunto caja + toma + tapa tiene que ser **IP54**.
- Se recomienda **no** poner tomas en superficies horizontales con los agujeros hacia arriba (se acumula material conductor).
- Tomas y llaves pueden montarse en el tablero, en cualquier circuito; hasta 4 tomas del mismo circuito cuentan como 1 boca.

## Llaves (interruptores de efecto)
- **Pasillos interiores de más de 3 m:** llaves de **combinación** en cada extremo (770.7.2, pág. 13).
- Van siempre dentro de cajas (770.10.3.1).
- Alimentación a llaves y retornos: 1 mm² mínimo (Tabla 770.11.I). Color del retorno: ficha 03.
- Que la llave unipolar corta la **fase** es una regla de la AEA 90364 que **no** está escrita en la 770. Citar solo "reglamentación AEA 90364", sin número.

## Bocas mixtas y tomas comandadas (770.7.1 m, págs. 12-13)
- Si después de cumplir los puntos mínimos hace falta una boca **mixta** (llave + toma), la toma se conecta al circuito de iluminación de esa caja y se identifica en forma indeleble con el símbolo IEC 60417-5012. Para el máximo de bocas por circuito cuenta como **1 boca**; para la demanda se usa el valor de 770.8.1 (un IUG con tomas derivadas se computa con 2200 VA por circuito). Ojo: un IUG que incluye tomas de uso general lleva 2,5 mm² como mínimo (Tabla 770.11.I).
- **No** se permiten tomas del circuito de iluminación a **menos de 0,90 m** del piso.
- Si hace falta una toma comandada por llave por debajo de 0,90 m, esa toma es del **circuito de tomas**, y su llave no puede compartir caja con llaves del circuito de iluminación (va en caja propia o en la caja de la toma). La capacidad de corte de la llave se coordina con la corriente de la toma que comanda.

## Bocas de iluminación (770.7.1 b, c, d)
- Una luminaria (una o varias lámparas) por boca, carga máxima 10 A.
- Ventiladores de techo y extractores: pueden ir en el circuito de iluminación; cuentan como una boca de iluminación.
- Escaleras y rampas: una boca de iluminación cada 5 m de largo o fracción, o en cada descanso.
- Bocas en semicubiertos: artefactos IP44 como mínimo; a la intemperie: IP54 (770.6.6 a).

## Baños (fuera de esta biblioteca)
- La 770 remite a la **AEA 90364-7-701** para baños, cocinas y lavaderos (770.7.1 e). Zonas, volúmenes y distancias al agua se verifican ahí.
- Toilette (sin ducha ni bañera): su toma puede ir en el circuito de iluminación (770.7.1 k).

## Distancia al gas y accesibilidad (770.17 y 770.18, pág. 57)
- Tableros y cajas (bocas, registros, pases, derivaciones) a **no menos de 50 cm** de las bocas de salida o llaves de las instalaciones de **gas**.
- Telecomunicaciones y video pueden necesitar distancias o blindajes adicionales (compatibilidad electromagnética).
- Cajas, tableros y bandejas quedan accesibles para operar, probar, inspeccionar, mantener y reemplazar componentes.

## Verificaciones en la inspección (770.19.3.1, pág. 58)
- Todas las tomas tienen el PE conectado a su borne de tierra (c).
- En todas las tomas, fase, neutro y PE están en el borne que corresponde (d).
