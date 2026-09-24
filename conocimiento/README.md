# Base de conocimiento técnico · EGC

Fichas con lo que dice la normativa argentina sobre instalaciones eléctricas domiciliarias, **en palabras propias** y con la referencia exacta de dónde sale cada dato (documento, cláusula o tabla, página impresa).
Las armó Claude leyendo los documentos que juntó Fran. Los documentos originales **no** están en este repositorio: las normas AEA e IRAM tienen derechos de autor y este repo es público.

## Orden de fuentes (obligatorio para la rutina)

1. **Esta carpeta.** Si el dato está en una ficha, se usa tal cual, con su referencia.
2. **Web oficial o confiable** (AEA, IRAM, IEC, ENRE, entes provinciales, universidades, fabricantes reconocidos) para lo que no esté acá. Si la web contradice una ficha, gana la ficha: anotá la diferencia en el resumen de la corrida para que Fran la revise.
3. **Lo que no se pudo verificar no se afirma.** Tampoco se "completa" con memoria o sentido común.

## Cómo citar en los posteos

- Si la ficha trae cláusula o tabla (por ejemplo "770.14.2.3" o "Tabla 770.11.I"), se puede citar así: `AEA 90364-7-770, 770.14.2.3`.
- Si la ficha dice **"sin número verificado"**, se escribe solo `reglamentación AEA 90364`.
- Nunca inventar un número de artículo, tabla o página.

## Fichas

| Ficha | Qué tiene |
|---|---|
| [00-fuentes.md](00-fuentes.md) | Qué documentos se leyeron, cuáles sirven y cuáles **no** (y por qué) |
| [01-alcance-y-conceptos.md](01-alcance-y-conceptos.md) | Alcance de la 770, esquema TT, tensiones, líneas y circuitos, qué es una "boca" |
| [02-circuitos-y-grado-de-electrificacion.md](02-circuitos-y-grado-de-electrificacion.md) | IUG / TUG / TUE, grados de electrificación, circuitos y puntos mínimos, demanda |
| [03-colores-e-identificacion.md](03-colores-e-identificacion.md) | Código de colores, **retornos**, cables prohibidos por color |
| [04-secciones-intensidad-y-caida-de-tension.md](04-secciones-intensidad-y-caida-de-tension.md) | Secciones mínimas, corriente admisible, agrupamiento, IB ≤ In ≤ Iz, caída de tensión |
| [05-protecciones.md](05-protecciones.md) | Diferencial 30 mA, termomagnéticas bipolares, cabecera, selectividad, motores, DPS |
| [06-puesta-a-tierra.md](06-puesta-a-tierra.md) | 40 Ω, jabalina, cámara de inspección, cable de PAT, conductor PE, masas |
| [07-canalizaciones-cajas-y-uniones.md](07-canalizaciones-cajas-y-uniones.md) | Cables y caños prohibidos, curvas, cajas, agrupamiento, **empalmes**, medidas de caños |
| [08-tomacorrientes-llaves-y-bocas.md](08-tomacorrientes-llaves-y-bocas.md) | Alturas, tomas con pantalla, bocas mixtas, pasillos, escaleras, IP |
| [09-tableros.md](09-tableros.md) | Ubicación, IP, reserva 20 %, un cable por borne, barra PE, marcado |
| [10-muy-baja-tension-y-casos-especiales.md](10-muy-baja-tension-y-casos-especiales.md) | MBTS / MBTF, flotantes de tanque, timbres, LED, cercas eléctricas, piscinas |
| [11-subterraneas.md](11-subterraneas.md) | Cables enterrados dentro del terreno (770) y diferencia con la vía pública (95101) |
| [12-inspeccion-y-mediciones.md](12-inspeccion-y-mediciones.md) | Inspecciones, mediciones, aislación, periodicidad, mantenimiento |
| [13-habilitacion-cordoba.md](13-habilitacion-cordoba.md) | Ley 10281 de Córdoba y registro de instaladores (ERSeP) |

## Avisos sobre temas de `temas.md`

Antes de armar estos temas, leé la ficha indicada. Algunos cambian por completo lo que se puede dibujar.

- **La llave corta la fase, nunca el neutro:** la regla es correcta, pero no está escrita en la 770 (está en la parte general de la AEA 90364, fuera de esta biblioteca). Citar solo "reglamentación AEA 90364". Retornos en color no reservado → ficha 03.
- **Bomba de agua con automático de tanque (flotante eléctrico):** el circuito de comando del flotante dentro de tanques va en **MBTS** (muy baja tensión sin puesta a tierra), no en 220 V → ficha 10. El motor además necesita maniobra que corte fase y neutro y protección de sobrecarga propia → ficha 05. Un esquema con flotante a 220 V dentro del tanque es **incorrecto**.
- **Empalme retorcido con cinta vs. borne:** la AEA **admite** el empalme retorcido intercalando hebras en ciertos casos → ficha 07. El "MAL" no puede ser "retorcer"; tiene que ser algo que la norma prohíbe (más de 4 cables retorcidos, empalme dentro del caño, sin aislación equivalente, secciones mayores a 4 mm² retorcidas).
- **Tablero monofásico de vivienda:** termomagnéticas **bipolares con los dos polos protegidos**; no se permiten 1P+N ni "neutro pasante" → fichas 05 y 09.
- **Motor monofásico con capacitor / contactor:** requisitos de 770.13.3 → ficha 05.
- **Tira LED / fuente 12 V:** fuente con transformador de devanados separados (nunca autotransformador); cables fuente-LED de más de 3 m son parte de la instalación; canalización separada de la de 220 V → fichas 01, 07 y 10.
- **Aire acondicionado split y termotanque:** los circuitos "de uso específico" no están desarrollados en la 770 (remite a la 771, que no está en esta biblioteca). Verificar en web oficial antes de afirmar calibres o secciones.
- **Extractor de baño:** puede ir en el circuito de iluminación (cuenta como boca de iluminación) → ficha 08. Las zonas del baño están en la AEA 90364-7-701, que **no** está en esta biblioteca.
- **Tomacorriente con descarga a tierra:** la posición de cada borne es de IRAM 2071, que **no** está en esta biblioteca. Verificar antes de dibujar.
- **Selectividad, DPS, protector de tensión:** fichas 05 y 06.
- **Timbre / portero:** MBTF o MBTS cambian si las masas van a tierra → ficha 10.
