# 04 · Secciones, corriente admisible y caída de tensión

Fuente: AEA 90364-7-770, edición 2017. Tablas verificadas sobre la imagen de las páginas.

## Tipo de cable (770.10, pág. 19)
- En instalaciones fijas solo cables **no propagantes de la llama** y de **450/750 V** como mínimo.
- Unipolar sin envoltura: IRAM NM 247-3 (PVC) o IRAM 62267 (LS0H), siempre dentro de caño o cablecanal.
- Con envoltura de protección (los llamados "subterráneos"): IRAM 2178 o IRAM 62266, en caños, cablecanales o enterrados (770.10.2).
- **Prohibidos** en instalación fija: cables de alambre **macizo** (un solo alambre), cordones flexibles tipo taller e IRAM NM 247-5 / 2039 / 2188 (770.10.1 h y k, págs. 19-20). Lista completa en ficha 07.

## Secciones mínimas (Tabla 770.11.I, págs. 36-37)
Aunque el cálculo dé menos, nunca por debajo de:

| Uso | Sección mínima |
|---|---|
| Línea principal | 4 mm² |
| Circuitos seccionales | 2,5 mm² |
| IUG (luminarias conectadas fijas o enchufadas a una toma) | 1,5 mm² |
| TUG (tomacorrientes de uso general) | 2,5 mm² |
| IUG que incluye tomas de uso general | 2,5 mm² |
| TUE (uso especial) | 2,5 mm² |
| Uso específico (salvo MBTF) | 2,5 mm² |
| Uso específico que alimenta MBTF | 1,5 mm² |
| Alimentación a llaves (interruptores de efecto) | 1 mm² |
| **Retornos** de llaves | 1 mm² |
| Conductor de protección PE | 2,5 mm² |

- Circuitos de control que no transmiten potencia (por ejemplo, domótica): se admite desde 0,5 mm², verificando el resto de las condiciones (nota de la tabla).
- La sección se elige por corriente admisible y caída de tensión, y se verifica por cortocircuito (770.11).
- Temperatura máxima del conductor con aislación de PVC: 70 °C (770.12.1).

## Corriente admisible · cables IRAM NM 247-3 / IRAM 62267 en cañería (Tabla 770.12.I, pág. 38)
Temperatura ambiente de cálculo **40 °C**. "2x" = 2 cables cargados + PE (monofásico). "3x" = 3 cargados + N + PE (trifásico).

| Cobre | 1 | 1,5 | 2,5 | 4 | 6 | 10 | 16 | 25 | 35 |
|---|---|---|---|---|---|---|---|---|---|
| 2x (A) | 11 | 15 | 21 | 28 | 36 | 50 | 66 | 88 | 109 |
| 3x (A) | 10 | 14 | 18 | 25 | 32 | 44 | 59 | 77 | 96 |

- Vale para cañerías embutidas o a la vista, cablecanales a la vista o embutidos en piso.
- Temperatura de referencia 40 °C en aire y 25 °C en suelo; para otra temperatura, ver Anexo B de AEA 90364-5-52 (770.12.2.1, pág. 37-38).
- En la zona del ENRE la temperatura ambiente regional es 40 °C (nota de 770.12.2.1.1).

## Varios circuitos en el mismo caño (Tabla 770.12.II, pág. 39)
- 2 circuitos monofásicos (hasta 4 cables cargados): factor **0,80**.
- 3 circuitos monofásicos (hasta 6 cables cargados): factor **0,70**.
- 2 trifásicos: 0,80. 3 trifásicos: 0,70.
- El PE **no** cuenta como cable cargado.
- Cuándo se permite agrupar circuitos en un caño: ficha 07.

## Cables con envoltura (IRAM 2178 / 62266) en caño o enterrados
- Tabla 770.12.III (pág. 40): aire a 40 °C; enterrado a 0,7 m, suelo a 25 °C y 1 K·m/W. El texto extraído de esa tabla salió desordenado: **no usar valores de memoria**; verificar en la tabla original o en el fabricante.
- Si el conductor es flexible (clase 5) en vez de rígido (clase 2), multiplicar por 0,95 (nota 2 de esa tabla).

## Coordinación cable-protección (770.15.2.1 y 770.15.3, págs. 47-49)
- **IB ≤ In ≤ Iz**: corriente de proyecto ≤ corriente nominal de la termomagnética ≤ corriente admisible del cable.
- Ejemplo con la tabla: 2,5 mm² en caño, monofásico, Iz = 21 A → admite termomagnética de hasta **20 A** (por eso el TUG con 2,5 mm² y 20 A cumple). Si hay 2 circuitos en el mismo caño: 21 × 0,8 = 16,8 A → ya no admite 20 A.
- La condición de sobrecarga I2 ≤ 1,45 Iz queda cumplida por usar termomagnéticas IEC 60898-1 (770.15.3).
- Cortocircuito: la capacidad de ruptura del dispositivo tiene que ser ≥ la corriente de cortocircuito presunta donde está instalado (770.15.2.2.2). En IEC 60898-1 viene marcada dentro de un rectángulo (por ejemplo 3000).
- Protección del cable al cortocircuito: k² · S² ≥ I²t, con k = 115 para cobre/PVC (Tabla 770.15.II). El I²t lo garantiza el fabricante.

## Caída de tensión (770.15.6, pág. 50)
Desde los bornes de salida del tablero principal hasta cualquier punto de uso:
- Circuitos terminales de iluminación y tomas (uso general o especial): **3 %** máximo.
- Circuitos que alimentan solo motores: **5 %** en régimen y **15 %** en el arranque.
- Se recomienda no pasar del 1 % en los circuitos seccionales.
- Para el cálculo, IUG y tomas se consideran con su demanda en el extremo más lejano; IUG con 2/3 de la carga total en el extremo.
- Fórmula: ΔU = k · I · L · (R cos φ + X sen φ), con k = 2 en monofásico y √3 en trifásico; L en km (distancia, no metros de cable). A falta de datos: cos φ = 0,85; en arranque de motores cos φ = 0,30.

### Tabla rápida (Tabla 770.15.IV, pág. 51) · monofásico, unipolares en caño, cos φ = 0,8
| mm² | 1,5 | 2,5 | 4 | 6 | 10 | 16 | 25 | 35 |
|---|---|---|---|---|---|---|---|---|
| V/(A·km) | 26 | 15 | 10 | 6,5 | 3,8 | 2,4 | 1,6 | 1,2 |

- Ejemplo: 10 A por 2,5 mm² a 20 m → 15 × 10 × 0,020 = 3 V ≈ 1,4 % de 220 V.
- Orden de cálculo completo (corriente de proyecto → cable → protección → cortocircuito → caída): Tabla 770-B.I del Anexo B (pág. 65).
