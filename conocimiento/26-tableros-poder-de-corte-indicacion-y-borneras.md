# 26 · Tableros: poder de corte, indicación, borneras y temperatura

Fuente: artículos técnicos y notas de fabricantes de la revista Ingeniería Eléctrica (Lote 3, ver ficha 00). Son **SECUNDARIA**. Lo que dice la ficha 09 (tableros según la 770) **manda**.

Códigos de fuente: (SOB1) = Farina, "Protección contra las sobretensiones" parte 1 (2024; el título no coincide: trata de **sobrecorrientes**); (IND) = Farina, "Medición e indicación en tableros eléctricos" (2023); (BOR) = Farina, "Borneras" (2023); (TH) = nota de un fabricante sobre control de temperatura y humedad en tableros (2026).

## Poder de corte de las termomagnéticas (SOB1)
- Definiciones de la AEA 90364-4-43 (430.2): corriente de proyecto, corriente admisible, sobrecarga, cortocircuito, poder de corte, selectividad total y parcial, protección de respaldo ("back-up").
- Según IEC 60898 (termomagnéticas domiciliarias): **Icn** es el poder de corte asignado; **Ics** es el poder de corte de servicio, que sale de multiplicar Icn por un factor k:

| Icn | k = Ics / Icn | Ics mínimo |
|---|---|---|
| Hasta 6.000 A | 1 | — |
| Más de 6.000 A y hasta 10.000 A | 0,75 | 6.000 A |
| Más de 10.000 A | 0,50 | 7.500 A |

- Ejemplo: una termomagnética de 10 kA de Icn tiene Ics de 7.500 A (10.000 × 0,75).
- La exigencia de que las termomagnéticas cumplan IEC 60898-1 está en la ficha 05. Esta tabla viene de un artículo: verificarla antes de publicarla como norma.

## Indicación y medición (IND)
- Luces piloto ("ojo de buey") en la puerta: sus bornes quedan al alcance de quien trabaja adentro, por eso el autor **recomienda alimentarlas en 24 V**. Es recomendación, no cláusula.
- Hay instrumentos de tensión y corriente en formato de **22 mm** (mismo agujero que el ojo de buey): se leen sin abrir la puerta.
- Hay voltímetros, amperímetros e indicadores de presencia de tensión para **riel DIN**, del ancho de una termomagnética, que se ven por la caladura de la contratapa.
- Los instrumentos fijos permiten un primer diagnóstico sin abrir el tablero ni meter la pinza entre los cables.
- **Aviso:** una luz piloto **no garantiza** que la fase esté presente. Con lámparas en estrella al neutro, la de una fase faltante puede quedar encendida a medias por realimentación desde otras cargas.
- **No usar** la frase del artículo que llama "BA4" a los usuarios no idóneos: en la 770 BA1 = personas comunes y BA4/BA5 = personal capacitado → ficha 09.

## Borneras (BOR)
- **Borne**: pieza que conecta y fija cables. **Bornera**: conjunto de bornes con sus accesorios, montado sobre riel DIN fijo e identificado.
- Los circuitos de un tablero se dividen en fuerza, control y medición; las borneras se usan más en control y medición.
- Ubicación habitual: abajo de la placa de montaje, con lugar para acercar y conectar los cables. Si los cables entran por arriba, se pueden poner en vertical, a la derecha.
- Consejo práctico: elegir bornes que se sigan consiguiendo, para poder ampliar o reponer.
- Un cable por borne → ya está en fichas 07 y 09.

## Temperatura y humedad dentro del tablero (TH)
- Existen termostatos y termohigrostatos para riel DIN que comandan un calefactor o un ventilador según temperatura y humedad (datos de catálogo, no de norma).
- Para dimensionar calefacción o ventilación de un tablero se considera: calor que disipan los equipos, volumen y material del gabinete, y temperatura exterior.
- Coincide en lo conceptual con la verificación térmica del tablero de la ficha 09 (Anexo 770-B.3).
- La nota **no** da temperaturas ni humedades recomendadas: no inventarlas.

## No usar
- Marcas, series y configuradores de fabricantes; aplicaciones industriales (hornos, secaderos).
