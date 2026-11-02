# Posteos COMERCIALES de EGC (Instagram, sin Metricool)

Objetivo: que la gente se tiente con la app. Cada posteo muestra **una** función o ventaja de EGC y termina invitando a probarla.

## Cuándo se publican
- **Martes 19:00, jueves 19:00 y sábado 10:00** (hora de Buenos Aires). Unos 13 por mes.
- Los publica solo el workflow `.github/workflows/publicar-comerciales.yml` (corre cada 20 minutos).
- **Nunca** se programan en Metricool: el plan gratis (20 por mes) queda para los técnicos.

## Qué hacer en cada corrida
1. Calculá los próximos turnos (martes 19:00, jueves 19:00, sábado 10:00) dentro de los **4 días siguientes**.
2. Para cada turno, fijate si ya existe `comerciales/placas/AAAA-MM-DD-HHMM-*.py`. Si existe, no hagas nada para ese turno.
3. Si falta, armalo:
   - Tema: el **primer `[ ]`** de `comerciales/temas.md`. Marcalo `[x]` al terminar.
   - Placa: creá `comerciales/placas/AAAA-MM-DD-HHMM-com-<slug>.py` copiando el estilo de `comerciales/placas/2026-11-03-1900-com-unifilar.py`. Usá solo las funciones de `comerciales/placas/comercial.py`: `cabecera()`, `paso()`, `tilde()`, `texto()`, `cta()`, `pie()` y al final `salida(s, __file__)`.
   - Texto: creá `comerciales/posts/AAAA-MM-DD-HHMM-com-<slug>.txt` (mismo nombre).
4. Generá la placa y **mirala** antes de subir: `pip install resvg-py pillow && python3 comerciales/generar_placas.py`. Revisá que nada se superponga ni se corte y que todo el texto mida 32 px o más.
5. Commit y push a `main` de la placa (.py y .jpg), el .txt y `comerciales/temas.md`.
6. En el resumen final agregá una línea: `COMERCIAL: <fecha y hora> · <tema>`.

## Reglas del contenido (no se negocian)
- Fuente única de lo que hace la app: la landing https://egc.globalepika.net.ar/ y sus páginas de función. **No prometas nada que la landing no diga.**
- No pongas precio en pesos ni fechas en la placa. En el texto, solo si la landing lo dice: "30 días gratis, sin tarjeta".
- Nunca la palabra AAIERIC. Nada de marcas de terceros.
- Si se habla de unifilar, protocolo o tablero: aclarar "EGC arma el documento; la firma y la responsabilidad son del profesional interviniente."
- Datos técnicos que aparezcan (secciones, térmicas, diferenciales) tienen que respetar las reglas técnicas de `CLAUDE.md`.

## Placa
- 1080 × 1350. Estilo comercial: cabecera negra con título blanco y segunda línea en rojo, raya roja, fondo claro.
- 3 o 4 pasos o beneficios como máximo. Un llamado a la acción: `cta()` ("PROBALA 30 DÍAS GRATIS").
- Logo EGC abajo a la izquierda (`pie()`). Texto mínimo 32 px.

## Texto del posteo (.txt)
- Máximo 2.200 caracteres. Español rioplatense (vos). Sin emojis.
- Estructura: gancho en la primera línea · el problema que resuelve (1-2 frases) · "Cómo funciona:" en viñetas con guion · un detalle concreto · "Probala 30 días gratis, sin tarjeta. El link está en la bio." · una pregunta para comentarios · 5 a 7 hashtags (`#electricistas #instalacioneselectricas` + los del tema + `#EGC`).
