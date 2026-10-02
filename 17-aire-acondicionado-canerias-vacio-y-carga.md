# 17 · Aire acondicionado: cañerías, abocardado, vacío, fugas y carga

Fuentes: manuales F1 a F4 y BP (buenas prácticas, documento del programa del Protocolo de Montreal). Detalle en ficha 00.
**Regla madre:** los largos, diámetros, torques y cargas **del manual del modelo** mandan sobre cualquier tabla general.

## Diámetros de cañería (F1 p. 22 · F3 · F4; coinciden donde se superponen)
| Capacidad (código del modelo) | Líquido | Gas |
|---|---|---|
| 09 (≈ 2.250 frig/h) | 1/4" | 3/8" |
| 12 (≈ 3.000 frig/h) | 1/4" | 1/2" |
| 18 (≈ 4.500 frig/h) | 1/4" | 1/2" |
| 22 (≈ 5.500 frig/h) | 3/8" (F1) · 1/4" (F3) | 5/8" |

- Caño de cobre **para refrigeración**, sin costura, nuevo, limpio y seco. Espesor 0,8 mm hasta 1/2" y 1 mm en 5/8" (F1 p. 22).
- Aislar **los dos caños** (los 4 manuales). F3 pide aislar cada caño por separado, con polietileno de 6 mm.

## Largos y desniveles
| Dato | Rango en los manuales | Fuente |
|---|---|---|
| Largo máximo por equipo | **10 a 25 m** | F1 p. 22 (20-25) · F4 (10) · F3 (15 en texto, 20-25 en tabla) |
| Desnivel máximo entre unidades | 5 a 10 m (multisplit hasta 15 m) | F1 p. 22 · F2 p. 20 · F4 |
| Largo incluido en la carga de fábrica | **5 m** en 3 de 4 manuales; 15 m en uno (R-22, 2006) | F1 p. 22 · F4 · F3 |
| Carga adicional de gas por metro extra | **15 a 30 g/m** | F1 (20) · F3 (20-30) · F4 (15) |
| Largo mínimo | 3 m, para bajar ruido y vibración (solo F1) | F1 p. 22 |

- Pasado el largo precargado, **cada metro extra lleva gas adicional**. Es material y mano de obra aparte: sirve para presupuestar (ficha 22).
- **Trampa de aceite:** F1 y F2 la piden en el tramo vertical cuando el desnivel supera 5 m, cada 5 a 7 m (F1 p. 22-23). Los otros manuales no la mencionan.
- Radio de curvado mínimo 10 cm, con curvador (F1 p. 24). Un caño aplastado es una restricción (ficha 20).

## Corte y abocardado (los 4 manuales)
1. Cortar a 90° con **cortatubos** (no con sierra).
2. Sacar la rebaba con escariador, con la punta del caño hacia abajo para que no caigan limaduras adentro.
3. **Poner la tuerca antes de abocardar.**
4. Abocardar con la saliente que indica el manual sobre la matriz (en F1: 0,7 a 1,3 mm en 1/4"; 1 a 1,8 mm en 1/2").
5. Ajustar primero a mano y después con **doble llave**: una sostiene el cuerpo de la válvula y la otra aprieta.

## Torque de las tuercas flare (convertido a N·m)
| Diámetro | Rango en los manuales |
|---|---|
| 1/4" | 15 a 18 N·m |
| 3/8" | 25 a 29 N·m |
| 1/2" | 35 N·m (3 manuales) · 50 a 62 N·m (1 manual de R-22) |
| 5/8" | 45 a 47 N·m (F1) · 65 a 80 N·m (1 manual de R-22) |

- Los valores cambian entre marcas: usar **torquímetro** con la tabla del manual del modelo.
- Ojo con las tablas de los manuales: F1 mezcla N·cm y N·m, y F4 da una equivalencia en kgf·cm que no cierra.

## Prueba de estanqueidad con nitrógeno (BP p. 64-68)
- Presurizar **solo con nitrógeno seco**, siempre con **regulador**. **Nunca** oxígeno, aire comprimido ni acetileno (BP p. 67, 91).
- Subir de a poco. Para el barrido de equipos domésticos, BP recomienda arrancar en 30 psi y no pasar de 80 psi (BP p. 66). Los 80 a 100 psig que menciona para buscar fugas son para sistemas **industriales** (BP p. 67).
- Presión de prueba de referencia (EN 378, presión admisible × 1,1), en psig, lado de baja / lado de alta: R-410A 301,7 / 531,1 · R-32 308,9 / 545,5 · R-22 184,2 / 331,8 (BP p. 68). **Manda la placa y el manual del equipo.**
- Dejar presurizado y ver que el manómetro no baje (mínimo 10 min; algunos fabricantes piden una segunda etapa de 24 h) (BP p. 67, 94).
- Buscar la fuga con **agua jabonosa** en cada unión, o con detector electrónico y confirmar con espuma (BP p. 71-72; los 4 manuales).
- Al **soldar**, hacer circular nitrógeno seco a baja velocidad por dentro del caño, antes y durante la soldadura (BP p. 91).
- Los manuales de fabricante de esta biblioteca **no** describen prueba con nitrógeno; es buena práctica de BP.

## Vacío
- **Siempre con bomba de vacío.** Nunca "purgar" con el gas de la unidad exterior (F3) ni usar el compresor del equipo como bomba: puede quemar el motor (BP p. 73).
- **Lo que piden los manuales (los 4):** bomba y manifold por la válvula de baja, **15 minutos como mínimo**, hasta −76 cmHg (vacío total en un manómetro común). F1 agrega: cerrar, apagar la bomba y esperar 5 minutos sin que suba la aguja.
- **Buena práctica (BP p. 73-74):** medir con **vacuómetro**, porque el manómetro solo muestra que hay vacío, no cuánto.
  - Meta: **500 micrones** con aceite mineral; **250 micrones con aceite POE** (aceite sintético, usado con los HFC; confirmar el tipo en el manual del equipo).
  - **Prueba de retención:** cerrar y observar. Si sube y se estabiliza: queda humedad, seguir haciendo vacío. Si sube sin parar: hay fuga. Si no se mueve: listo para abrir o cargar.
  - Cerrar la válvula hacia el equipo **antes** de apagar la bomba.
  - Bomba residencial típica: 4 a 5 CFM (BP p. 49). Cambiar el aceite de la bomba seguido (BP p. 75).
- Abrir las válvulas de servicio con llave hexagonal **hasta el tope, sin forzar**, y volver a colocar las tapas (los 4 manuales).

## Carga de refrigerante (BP p. 75-76, 96)
- El método más seguro es **por peso**, con balanza: la carga de la placa más el adicional por metro que da el fabricante.
- Las **mezclas** (R-410A, R-407C) se cargan en **fase líquida**, para no cambiar su composición.
- Después de una fuga en R-407C (mezcla con deslizamiento de temperatura), se vacía y se recarga completo (MB p. 43-44; BP p. 14 explica el motivo).
- No se mezclan refrigerantes ni se pone un gas distinto del de la placa (F1 p. 3).

## Recuperación antes de abrir un circuito (BP p. 54-59)
- Antes de abrir un circuito con gas, **recuperar** el refrigerante. No se ventea.
- **Pump-down:** con el equipo andando, cerrar la llave de servicio; el compresor junta el gas en la unidad exterior. Cortar cuando el manómetro llega a unos 0 bar. Si hay una fuga, no dejar que entre en vacío (entraría aire).
- Cilindro de recuperación **retornable**, nunca descartable; llenado máximo 80 % (60 % si puede calentarse a más de 54 °C); sin mezclar gases; etiquetado; vertical y atado; **nunca calentar con llama**.
- BP cita el cilindro "DOT 400" para R-410A: es una norma de EE. UU. que usa como referencia, no una regla argentina.

## Prueba final y entrega
- Probar fugas y parte eléctrica **antes** de arrancar (los 4 manuales).
- Funcionamiento: al menos **30 minutos**, unos 5 minutos en cada modo (F1 p. 28-29).
- Revisar: sin fugas, desagote que corre, caños aislados, unidades firmes, bornes tapados, control remoto (checklist de F1 p. 28-29).
- Repasar fugas con el equipo andando: la presión sube y aparecen fugas que en reposo no se ven (F1 p. 28).
- BP recomienda dejar un **rótulo** con instalador, tipo de gas, carga y presión de prueba (BP p. 76, 99).
