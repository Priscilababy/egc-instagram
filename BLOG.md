# Notas automáticas del blog · EGC

Este archivo lo sigue la rutina diaria, **después** del posteo de Instagram (o aunque el posteo se haya salteado).
La nota del blog es una tarea **independiente**: si falla, no afecta el posteo, y si el posteo falla, igual se intenta la nota.

Cada nota queda **programada 24 horas** y se publica sola en egc.globalepika.net.ar/blog. En ese margen Fran puede frenarla con un link.

La prioridad absoluta es la **exactitud técnica**. Es mejor no publicar una nota que publicar un error.

---

## Datos fijos

| Dato | Valor |
|---|---|
| Frecuencia | Una nota cada 2 días |
| Temas | `blog/temas-blog.md` |
| Índice de notas | `blog/indice.json` |
| Texto de cada nota | `blog/notas/<slug>.md` |
| Portada | `blog/img/<slug>.png` (1080 × 1350) |
| Publicación | día siguiente a las **19:00** (hora de Buenos Aires) |
| Blog | https://egc.globalepika.net.ar/blog/ |

La **clave de los links** (vista previa y frenar) viene en el mensaje de la rutina. **Nunca la escribas en ningún archivo del repositorio** (el repositorio es público).

---

## Paso a paso

### B0. ¿Toca nota hoy?
```bash
export HOY=$(TZ=America/Argentina/Buenos_Aires date +%F)
python3 - <<'PY'
import json, datetime as dt, os
hoy = dt.date.fromisoformat(os.environ.get('HOY') or dt.date.today().isoformat())
notas = json.load(open('blog/indice.json', encoding='utf-8'))['notas']
ult = max([dt.date.fromisoformat(n['creada'][:10]) for n in notas], default=None)
print('TOCA' if ult is None or (hoy - ult).days >= 2 else 'NO TOCA')
PY
```
Si da `NO TOCA`, terminá la parte del blog sin hacer nada y no la menciones en el resumen.

### B1. Elegir el tema
- Tomá el **primer tema `[ ]`** de `blog/temas-blog.md`.
- Revisá que no esté ya publicado en el blog: `curl -s https://egc.globalepika.net.ar/blog/sitemap.xml` (y las notas de `blog/indice.json`). Si se repite, marcalo `[=]` y pasá al siguiente.

### B2. Verificar la parte técnica
Mismas reglas que el paso 4 de `CLAUDE.md`, con una más estricta:
- **Solo se escribe lo que está en las fichas de `conocimiento/`** indicadas en el tema (y en los avisos de `conocimiento/README.md`). La web sirve para confirmar, no para agregar datos nuevos.
- Si las fichas no alcanzan para escribir la nota con seguridad, marcá el tema `[?]` con el motivo y pasá al siguiente (como máximo 3 intentos por corrida).
- Citá cláusula o tabla **solo si figura en la ficha**. Si no, "reglamentación AEA 90364".
- **Nunca** pongas una termomagnética máxima junto a una sección mínima que no la soporta. Si das un ejemplo de sección y térmica, tiene que ser una combinación que cumpla IB ≤ In ≤ Iz según la ficha 04.
- Nada de marcas comerciales. Nada de afirmar lo que los avisos de `conocimiento/README.md` prohíben.

### B3. Escribir la nota
Archivo `blog/notas/<slug>.md`.
- `slug`: minúsculas, sin acentos, palabras separadas por guiones, máximo 70 caracteres. Ej.: `que-seccion-de-cable-va-en-cada-circuito`.
- **Largo: entre 900 y 1.400 palabras.** Verificalo: `python3 -c "print(len(open('blog/notas/SLUG.md',encoding='utf-8').read().split()))"`
- Español rioplatense (vos). Tono técnico, claro y directo. Sin emojis. Sin fechas relativas ("este año", "hoy").
- **Formato permitido (solo esto):** párrafos separados por una línea en blanco; `## Subtítulo`; `**negrita**`; `*cursiva*`; `[texto](https://...)`; listas con líneas que empiezan con `- `. **No** uses tablas, `###`, listas numeradas, HTML ni imágenes dentro del texto. El título va en el índice, **no** dentro del .md.
- Estructura:
  1. Primer párrafo: la **respuesta directa** a la pregunta del título, en 2 o 3 frases.
  2. 3 a 5 secciones `##` con el desarrollo (qué dice la norma, cómo se aplica en obra, ejemplo práctico).
  3. `## Errores comunes en obra` con 3 a 5 viñetas.
  4. `## Preguntas frecuentes` con 3 preguntas: cada una en un párrafo que empieza con la pregunta en negrita, seguida de la respuesta.
  5. `## Cómo te ayuda EGC`: 2 o 3 frases y un enlace a la página que corresponda (ver tabla abajo).
  6. `## Fuentes`: viñetas con documento y cláusula/tabla tal como figuran en las fichas. Al final, una viñeta: `- Fichas de la base de conocimiento técnico de EGC.`

| Tema de la nota | Enlace en "Cómo te ayuda EGC" |
|---|---|
| Secciones, caída de tensión, térmicas, circuitos | `[calculadora AEA de EGC](https://egc.globalepika.net.ar/calculadora-seccion-cable/)` |
| Tableros, diferenciales, barra de tierra | `[tablero en EGC](https://egc.globalepika.net.ar/tablero-electrico/)` y/o `[esquema unifilar](https://egc.globalepika.net.ar/esquema-unifilar/)` |
| Puesta a tierra, mediciones, SRT 900/15 | `[protocolo SRT 900/15 en EGC](https://egc.globalepika.net.ar/protocolo-puesta-a-tierra-srt-900-15/)` |
| Mantenimiento, garantía, entrega del trabajo | `[constancia de garantía](https://egc.globalepika.net.ar/garantia-trabajos-electricos/)` |
| Aire acondicionado, presupuestos en general | `[EGC](https://egc.globalepika.net.ar/)` |

### B4. Portada
- Generá una placa 1080 × 1350 con `generador/placa.py` (mismo estilo que Instagram): el título corto de la nota en el encabezado y un esquema simple o el mensaje clave en el recuadro amarillo. Guardala en `blog/img/<slug>.png`.
- Pasá la **revisión visual** completa del paso 6 de `CLAUDE.md`. Si algo falla, corregí y regenerá.

### B5. Agregar la nota al índice
Agregá un objeto al final de la lista `notas` de `blog/indice.json` y validá el JSON con Python:
```json
{
  "slug": "<slug>",
  "titulo": "<título como pregunta o frase larga que busca un electricista, máx. 90 caracteres>",
  "descripcion": "<resumen de 1 o 2 frases, máx. 155 caracteres>",
  "imagen": "blog/img/<slug>.png",
  "creada": "<ahora, ISO con -03:00>",
  "publicar": "<MAÑANA>T19:00:00-03:00",
  "fichas": ["04", "05"],
  "palabras": 1100
}
```
```bash
python3 -c "import json;d=json.load(open('blog/indice.json',encoding='utf-8'));print(len(d['notas']),'notas OK')"
```
En `blog/temas-blog.md` marcá el tema como `[x]` y agregá al final de la línea `→ <slug>`.

### B6. Guardar en GitHub
Igual que el paso 8 de `CLAUDE.md` (commit, merge en `main`, push y `git ls-remote origin main`):
```bash
git add blog/
git commit -m "Blog: <título corto>"
```
Verificá que respondan `200`:
```bash
curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/Priscilababy/egc-instagram/main/blog/indice.json
curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/Priscilababy/egc-instagram/main/blog/notas/<slug>.md
curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/Priscilababy/egc-instagram/main/blog/img/<slug>.png
```
Si alguno da 404, esperá 15 segundos y reintentá (hasta 6 veces).

### B7. Links del aviso
Con la clave del mensaje de la rutina (variable `CLAVE`):
```bash
TOKEN=$(python3 -c "import hmac,hashlib,sys;print(hmac.new(sys.argv[1].encode(),sys.argv[2].encode(),hashlib.sha256).hexdigest()[:16])" "$CLAVE" "<slug>")
echo "https://egc.globalepika.net.ar/blog/nota/<slug>?previa=$TOKEN"
echo "https://egc.globalepika.net.ar/blog/frenar.php?slug=<slug>&t=$TOKEN"
```

### B8. Resumen
El resumen final de la corrida **empieza** con este bloque (antes de lo de Instagram):
```
NOTA DE BLOG NUEVA
<título>
Se publica sola el <día> a las 19:00.
Ver antes: <link de vista previa>
Frenarla: <link de frenar>
Fichas usadas: <números>
```
Si la parte del blog no se pudo completar, el bloque dice `NOTA DE BLOG: no se publicó` y el motivo.

---

## Si algo falla
- **Nunca** agregues al índice una nota sin verificar o con la portada sin revisar.
- Si un archivo de la nota no quedó en `main`, sacá la nota de `blog/indice.json` antes de terminar.
