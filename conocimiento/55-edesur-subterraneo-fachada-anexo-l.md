# 55 · Edesur T1: pilar subterráneo trifásico, conexión en fachada y Anexo L (requisitos de seguridad)

Fuentes (recibidas de Fran el 22/11/2026, bajadas del sitio oficial de Edesur):
- Edesur, "Pilar para medidor T1 tipo subterráneo" (pilart1_planos_subterraneo.pdf, 4 hojas, archivo de 2015). Las hojas 1 (pilar monofásico) ya están en la ficha 53. Esta ficha suma las hojas 2, 3 y 4.
- Edesur, **"Requisitos de seguridad eléctrica (Anexo L)"** (Anexo-L.pdf, 1 hoja, archivo de 2015). Forma parte de cada disposición constructiva de acometidas de Edesur y debe acompañar al plano.

Estado: **PRIMARIA** (solo área Edesur). Complementa la ficha 53. Medidas en mm, como en los planos.

## Pilar T1 subterráneo trifásico con salida por pared (hoja 2)
- Pilar **450 × 450 mm**, fundación **600 mm**.
- Caja de medidor: **1.200 mm mínimo, 1.800 mm máximo**.
- Caja de toma: **600 mm mínimo, 1.200 mm máximo**.
- Materiales (lista de Edesur):
  - Caja de medidor trifásico sintética con dispositivo de corte y bloqueo.
  - Caja para tablero del cliente.
  - Caja de toma con seccionador fusible NH-00 y **3 fusibles NH-00 de 63 A**.
  - Caño de PVC rígido **Ø 90 mm**, 1,20 m (acometida).
  - Caño de PVC **Ø 32 mm interior mínimo** entre cajas (en monofásico: 19 mm).
  - Cable unipolar PVC **6 mm²** (12 m).
  - Interruptor termomagnético **tetrapolar 20 A**.
  - Llave de seccionamiento tetrapolar de 40 A o 63 A: **opcional**, a criterio de Edesur.
  - Tapón precinto de policarbonato.
- Notas: igual que el monofásico. Cajas y caños de material sintético aislante. Frente metálico a tierra independiente o equipotencial según AEA. **Nunca** la puesta a tierra al neutro.

## Conexión T1 subterránea sobre fachada (hojas 3 y 4)
| Dato | Monofásica | Trifásica |
|---|---|---|
| Caja de medidor sobre el piso | 1.200 mm mín. (base) · 1.800 mm máx. | 1.200 mm mín. (base) · 1.800 mm máx. |
| Caja de toma 60 A con seccionador fusible NH-00 | 600 mm mín. | 600 mm mín. |
| Caño de PVC entre cajas y al tablero | Ø 19 mm interior mín. | Ø 32 mm interior mín. |
| Cable unipolar PVC | 4 mm² mín. | 6 mm² mín. |

- Caños **embutidos a 5 cm de profundidad como mínimo**.
- Caja para tablero del cliente al lado de la caja de medidor (dibujo con línea de trazos: posición orientativa).

## Anexo L · requisitos de seguridad eléctrica de Edesur
Base: **Resolución ENRE N° 1098/2006**.
- **Doble aislación:** cajas, gabinetes, caños, codos y pipetas de material aislante o aislado. Todos los conductores aislados. Edesur garantiza que el cable de acometida llega sin empalmes a sus bornes.
- **Cerramientos:** cajas y gabinetes con cierre de seguridad que solo se abre con **herramienta especial**. Los normalizados por Edesur traen cierre con llave especial.
- **Grado de protección:** mínimo **IP43 e IK10** (el anexo lo escribe como "IP439"), o el que indique cada plano.
- **Protección de la instalación:** como mínimo, un **interruptor automático** (sobrecarga y cortocircuito) en el tablero principal del cliente. **Diferencial** donde lo indique cada plano. El cable de acometida queda protegido por el fusible de Edesur en su arranque.
- **Normas de los materiales:**
  - Cables: IRAM 2164, 2263, 63001, 2178, NM 247-3, 62266 y 62267, según el caso.
  - Protecciones: IEC 60898, 60947 y 61008.
  - Cajas, gabinetes y caños: los normalizados por Edesur (matrícula en cada plano).
- **Señalización:** cajas y gabinetes en vía pública e interiores con **etiqueta de advertencia de riesgo eléctrico**.

## Dato útil para leer la ficha de Edenor
- El Anexo L muestra la notación de tres cifras: "IP439" = IP43 + IK10. La tercera cifra indica la protección mecánica.
- Por eso el "IP549" que pide Edenor para la tapa del tablero principal (ficha 53) se lee como **IP54 con protección mecánica alta** (equivalente a IK10 según esa misma notación). **Inferencia:** confirmar con Edenor antes de publicarlo como dato cerrado.

## Para la app (EGC Pilar) y los posteos
- Edesur subterráneo: la app ya puede dibujar mono y trifásico, en pilar y en fachada.
- Checklist Edesur: doble aislación, cierre con herramienta, IP43/IK10, etiqueta de riesgo eléctrico, termomagnética en el TP, frente metálico a tierra (nunca al neutro).
- Citar "Anexo L de Edesur (Res. ENRE 1098/2006)" en el PDF del módulo.

## Pendiente
- Leer la Res. ENRE 1098/2006 completa (requisitos de seguridad de acometidas).
