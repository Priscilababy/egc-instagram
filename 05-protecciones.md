# 05 · Protecciones

Fuente: AEA 90364-7-770, edición 2017, salvo donde se indica otra.

## Qué hay que proteger (770.13.1, pág. 41)
- **Obligatorio:** fallas a tierra, contactos directos, contactos indirectos y sobrecorrientes (sobrecargas y cortocircuitos).
- **Altamente recomendable:** sobretensiones transitorias (rayos, maniobras), sobretensiones permanentes (por ejemplo, corte del neutro) y subtensiones.
- Estas protecciones cuidan a las personas, animales, bienes y a los circuitos; no pretenden proteger a los equipos conectados, que tienen sus propias normas.

## Diferencial de 30 mA en todos los circuitos terminales (770.14.2.3, pág. 43)
- **Todos los circuitos terminales** llevan interruptor diferencial de **IΔn ≤ 30 mA**, de actuación **no retardada** (instantánea).
- Es protección **complementaria** contra contactos directos: no reemplaza a la aislación, barreras o envolturas. No protege si una persona toca a la vez dos conductores activos (fase y neutro).
- Nota de la norma: según IEC 61008 hay distintos tipos; el más habitual en este ámbito es el **tipo AC** (fallas de alterna senoidal). La 770 **no exige** tipo A (no afirmar que lo exige).

## Contactos indirectos en esquema TT (770.14.3.2, pág. 44)
- En TT la **única** protección por corte automático aceptada es el **diferencial**. La termomagnética **no** sirve como protección contra contactos indirectos.
- Objetivo: que la tensión de contacto no pase de **24 V**.
- Con diferencial ≤ 30 mA y **Ra ≤ 40 Ω**, esa parte de la instalación se considera protegida contra contactos indirectos.
- Entre tablero principal y seccional (o entre seccionales) se puede usar diferencial de hasta **300 mA**, y se recomienda que sea **selectivo** (marcado **S**) respecto de los de 30 mA de aguas abajo. Con Ra ≤ 40 Ω también cumple los 24 V.
- El diferencial también ayuda a evitar incendios: una fuga a tierra del orden de 300 a 500 mA puede iniciar un incendio (nota 1).

## Doble aislación · Clase II (770.14.3.1, pág. 44)
- Se consideran Clase II: cables con envoltura cuya tensión nominal es al menos el doble de la tensión a tierra (por ejemplo IRAM 2178 / 62266 de 1 kV en 220/380 V), y unipolares dentro de caños o cablecanales **aislantes** normalizados y autoextinguibles.
- Las partes metálicas que tocan esos cables o caños no son masas, pero igual se equipotencializan a tierra.

## Contactos directos (770.14.2.1 y 770.14.2.2, pág. 43)
- Partes activas totalmente aisladas (la pintura o el barniz no cuentan como aislación).
- O detrás de barreras o envolturas de al menos **IP2X / IPXXB** (aberturas menores de 12 mm), que solo se sacan con llave o herramienta.

## Termomagnéticas y dispositivos en tableros (770.16.5, págs. 55-56)
- Las cabeceras de **todos** los tableros **seccionan el neutro**.
- En monofásico, las protecciones de circuitos son **bipolares con los dos polos protegidos**; en trifásico, tetrapolares.
- **Prohibido** en monofásico: termomagnéticas **unipolares**, bipolares con "neutro no protegido", "neutro pasante" o marcadas **1P+N**, y los combinados termomagnética-diferencial con la protección en un solo polo (770.16.5.1).
- Solo termomagnéticas que cumplan **IEC 60898-1**, que se puedan **bloquear en abierto** (candado o precinto) y que abran y cierren todos los polos a la vez (770.16.5.2).
- Cada circuito terminal y cada seccional queda protegido contra contactos directos e indirectos, sobrecargas y cortocircuitos (770.16.5.3).

## Cabecera del tablero principal (770.16.5.3, pág. 56)
- Interruptor automático (termomagnético) de **63 A como máximo** (más de 63 A → AEA 90364-7-771). Puede tener un diferencial asociado.
- Monofásico: bipolar con los dos polos protegidos. Trifásico: tetrapolar con todos los polos protegidos.

## Cabecera de tableros seccionales (770.16.5.4, pág. 56)
- Un dispositivo de corte general con aptitud de seccionamiento garantizada: interruptor-seccionador bipolar/tetrapolar, termomagnética bipolar (ambos polos protegidos) o tetrapolar, o un diferencial IEC 61008 / 61009.
- Si la cabecera no es diferencial, los circuitos que lo necesitan llevan diferencial propio o agrupado.
- Cada circuito derivado lleva su termomagnética.
- Si el neutro trifásico tiene menos sección que las fases, necesita protección de sobreintensidad propia.
- Se **recomienda** instalar detectores de arco (**AFDD**) en tableros principal y seccionales (nota, pág. 57).

## Proteger al diferencial (770.15.2.2.5, págs. 48-49, y Anexo 770-B.2.4, pág. 73)
- Sobrecarga: la corriente nominal del diferencial ≥ la de la termomagnética en serie aguas arriba, **o** ≥ la suma de las termomagnéticas que tiene aguas abajo.
- Cortocircuito: el diferencial tiene capacidad de ruptura baja (como mínimo 500 A o 10 × In, lo que sea mayor; Tabla 770-B.X). Hay que verificar que soporte el cortocircuito del lugar; si no, protegerlo con un dispositivo contra cortocircuitos **aguas arriba**, según indique su fabricante (como excepción se admite que lo protejan las termomagnéticas de aguas abajo en el mismo tablero, con los valores que dé el fabricante).
- Si se cambia un diferencial por otro de distinta marca o características, se vuelve a verificar.

## Tiempos del diferencial (IEC 61008-1 · verificado en web, no está en esta biblioteca)
- Tipo general: hasta 300 ms con IΔn, 150 ms con 2 × IΔn, 40 ms con 5 × IΔn.
- "30 mA" es la **sensibilidad**, no un tiempo.

## Motores de instalación fija (770.13.3, pág. 41)
- Dispositivo de maniobra que arranque y pare el motor abriendo **fase y neutro** si es monofásico, o todas las fases a la vez si es trifásico.
- Trifásicos: dispositivo que detecte la falta de una fase y corte.
- Protección **dedicada** contra sobrecarga y protección (propia o compartida) contra cortocircuito y fuga a tierra.
- **Los fusibles y las termomagnéticas no sirven como protección de sobrecarga de motores** La norma pide protección de sobrecarga **dedicada** al motor, pero no nombra el dispositivo: no afirmar un aparato puntual sin verificarlo.

## Sobretensiones
### Transitorias · DPS (770.15.4 y Tabla 770.15.III, pág. 50)
Nivel ceráunico AQ = días de tormenta por año (mapas de AEA 92305-11).

| Situación del inmueble | AQ ≤ 25 (AQ1) | AQ > 25 (AQ2) |
|---|---|---|
| Tiene pararrayos | **Obligatorio** | **Obligatorio** |
| Alimentado por red aérea total o parcial | No obligatorio | **Obligatorio** (salvo análisis de riesgo según AEA 92305-2 que lo justifique) |
| Alimentado por red totalmente subterránea | No obligatorio | No obligatorio |

- La obligación por red aérea no aplica si la línea aérea es de conductores aislados con pantalla metálica a tierra o incluye un conductor a tierra (nota 2).
- Aunque no sea obligatorio, puede hacer falta para proteger equipos críticos según el análisis de riesgo (nota 4).
- Ubicación e instalación de DPS: secciones 443 y 534 de AEA 90364 (no están en esta biblioteca).

### Permanentes (770.15.5, pág. 50)
- Queda **a criterio del proyectista**. (La 770.13.1 la califica como altamente recomendable.)
