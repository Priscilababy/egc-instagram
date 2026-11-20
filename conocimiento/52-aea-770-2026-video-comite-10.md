# 52 · AEA 90364-7-770 edición 2026: explicación del Comité 10 (video "Experiencia AEAconectada")

Fuente: video **"Experiencia AEAconectada"**, canal oficial de YouTube de la AEA (https://www.youtube.com/watch?v=fsa10yqfvFg), 1 h 37 min. Expositores: integrantes del **Comité 10**, redactores de la norma.
Se leyó la transcripción automática de YouTube (19/11/2026). Puede tener errores de reconocimiento de voz.
Estado: **OFICIAL, oral**. Es la explicación de los redactores, no el texto de la norma. Ante duda, gana el texto impreso.
Esta ficha **confirma o corrige** la ficha 51. Donde difieren, gana esta.

## Fechas
- Vigencia: **1/11/2026**. Aplicación: **1/3/2027**. Lo dijo el presidente de la AEA en la apertura.

## Diferencial tipo AC (aclaración oficial)
- Obra nueva: tipo **A como mínimo**.
- Instalaciones existentes: **no** hay que cambiar el AC de inmediato. Se **recomienda** migrar al tipo A en todo inmueble con carga electrónica.
- La 771 (oficinas y locales) y la 772 todavía no hablan del AC. Donde la norma no lo diga, el AC se puede seguir usando. Se tratará en esas secciones más adelante.
- La AEA pidió no comunicar en redes que "hay que cambiar todos los diferenciales".
- Por qué el AC no sirve: los armónicos y la corriente pulsante de los equipos inverter saturan su núcleo. Ante una fuga puede no actuar ("queda ciego").
- **Tipo A:** ve fugas con onda deformada.
- **Tipo F:** como el A, con deformaciones de frecuencia más alta (más de 1 kHz).
- **Tipo B:** además ve **corriente continua**. Contexto: inversores, instalaciones fotovoltaicas y **estaciones de carga en continua** (las grandes). El expositor aclaró que **no** se refería a los wallbox domiciliarios.
- El diferencial "superinmunizado" o "a prueba de ruido" es un **tipo A** con filtro adicional.
- El tema figura en el prólogo y en una cláusula de protecciones (número dudoso en la transcripción: **sin número verificado**).

## Puesta a tierra (TT)
- Máximo **100 Ω** con diferencial de **300 mA**. Respaldo: informe técnico **AEA 90479-5**.
- Hasta **200 Ω** solo donde la **autoridad de aplicación provincial** lo decida, por terreno de alta resistividad, y con diferencial de **30 mA** (no 300 mA).
- Historia del 40 Ω (edición 2017): 80 Ω daban ≤ 24 V de contacto con 300 mA. Se aplicó un margen del 100 % por el aumento de la resistencia con los años (≈ +87 % medido en 17 años).

## Proyecto
- **IUE:** demanda **120 VA por boca × 2/3** (antes 500 VA). Protección máxima **32 A**. **Confirmado por el redactor.**
- IUE ya no es solo para intemperie: se admiten bocas en semicubiertos y en interiores.
- Todos los circuitos de uso especial: **15 bocas** máximo (antes había 12 y 15).
- Se permite reemplazar un circuito de uso general exigido por el grado por uno de uso especial (para no sumar un circuito más). **Verificar alcance en el texto.**
- Ventilador de techo: se suman motor y luminarias; cuenta como **una boca**.
- Toma derivado en toilette: cable de **2,5 mm²** mínimo.
- Todo ambiente, cualquiera sea su uso: al menos **una boca de iluminación**.
- IUG: el límite pasa de "10 A por carga" a **10 A por boca**. En tomacorrientes sigue igual.
- Simultaneidad por circuitos **efectivamente instalados**: 2 → 1 · 3 a 5 → 0,7 · 6 a 9 → 0,6 · 10 o más → 0,5 (coincide con ficha 50).
- DPMS: se suman los circuitos de carga de vehículos eléctricos.
- Grado de electrificación, número mínimo de circuitos y puntos mínimos: **sin cambios**.
- Varias recomendaciones pasan a ser obligatorias (sin detalle en la charla).

## Otros sistemas
- Fotovoltaica: AEA 712 (nueva edición en preparación). En isla: AEA 90364-8-82, con anexo reglamentario para inmuebles.
- SAI y baterías estacionarias (litio o plomo-ácido): **AEA 90364-5-57**. Baterías accesibles a BA1/BA2; operación por BA4/BA5.
- Vehículo eléctrico: **AEA 90364-7-722, edición 2024**. Circuito específico y protección propia.

## Canalizaciones y conectores
- El caño trae grabados al menos 2 dígitos: **23**, **33** o **44**. Indican el ámbito de uso.
- Corrugado blanco = **liviano**: solo **obra en seco** (steel frame, placa de yeso).
- Mampostería: **33 y 44** en adelante, según la obra.
- Norma del caño: **IRAM 62386**. Certificar los **12 dígitos**, no solo la no propagación de llama.
- Mangueras sin norma: problema frecuente. Pedir certificados al distribuidor.
- Nueva tabla resumen de selección de caños en la subcláusula 12 (número exacto **sin verificar**).
- Conectores de empalme: **IEC 60947** o **IEC 60998**. Pedir el certificado.

## Tableros
- Alcance: operados por BA1, vivienda con BA1 y BA2, hasta 63 A y 10 kA.
- Gabinete vacío **IEC 60670** (verificación térmica: anexo D) o **IEC 62208** (verificación térmica: informe técnico **AEA 90890**). Dato clave: potencia máxima disipable que declara el fabricante.
- Sigue valiendo IEC 61439-1 y -3.
- Nueva definición: **aparamenta** (elementos de mando, maniobra, protección y medición).
- Cinco responsables: proyectista, tablerista, instalador, propietario y quien hace mantenimiento o modificaciones.

## AFDD
- Recomendado como protección suplementaria.
- **Obligatorio** con cañerías aislantes en construcciones de **madera** o con aislaciones **EPS** (telgopor, Euroclase F, propagante de llama).
- AFD = sensor + lógica (manda a un interruptor asociado). AFDD = sensor + lógica + dispositivo de corte.
- Arco serie ≈ **2,5 A en 1 s**; arco paralelo ≈ **75 A en 12 semiciclos** ("según tablas"). No usar sin el texto de la norma.

## Uso en EGC
- Diferencial AC: decir siempre "obra nueva" y "cambio recomendado en lo existente". Nunca "hay que cambiar todos".
- Tipo B: inversor FV o carga en continua. **No** afirmar que todo wallbox pide tipo B: remitir a la AEA 90364-7-722 y al manual.
- Calculadora: IUE 120 VA × 2/3 por boca y 15 bocas; simultaneidad por circuitos instalados.
- Antes de programar un valor nuevo, confirmar con el texto impreso.
