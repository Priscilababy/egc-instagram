# 36 · Incertidumbre de medición: tipo A, tipo B, combinada y expandida

Fuente: texto técnico "Evaluación de las incertidumbres de medición" (mediciones directas), difundido con aval de la AEA y entregado por Fran el 2026-10-31. Autor no indicado en el material recibido.
Tipo de fuente: **SECUNDARIA de confianza** (avalada por la AEA). Resume la Recomendación INC-1 del CIPM y la GUM (IRAM 35050), que **no** están en esta biblioteca.
Redacción propia. No es copia textual del documento.

## Marco
- CIPM, Recomendación INC-1 (1980): clasifica las incertidumbres en **tipo A** y **tipo B** y las trata a todas como variables aleatorias (varianzas).
- ISO/IEC GUM → **IRAM 35050 (2001)**. EA-4/02 (calibraciones) → **IRAM 35051 (2004)**.
- VIM JCGM 200:2008: 2.28 "Evaluación tipo A", 2.29 "Evaluación tipo B".
- La fuente trata **mediciones directas**. Las indirectas quedan para otra publicación (no recibida).

## Conceptos
- **Mensurando (μ):** magnitud que se mide. **Valor medido (V):** siempre aproximado. Solo el **conteo** da un valor exacto.
- La incertidumbre define el intervalo de validez del resultado.
- Antes de evaluar, corregir los efectos **sistemáticos**. Los **aleatorios** se tratan con estadística.

## Tipo A · u(A)
- Se evalúa con **n lecturas repetidas** en iguales condiciones operativas (repetibilidad).
- La fuente adopta la distribución de **Student (Gosset, 1908)**, por ser la más realista con pocas lecturas.
- t = (V − μ) / S*  →  (V − μ) = S* · t
- s = √[ Σ (vi − v̄)² / (n − 1) ]   (desvío estándar experimental)
- S* = s / √n   (desvío estándar experimental de la media)
- **u(A) = ± S* · t(p = 68,3 %; n − 1)**
- El intervalo 2·u(A) es la zona de pertenencia del mensurando.

### t de Student para p = 68,3 %
| n − 1 | t |
|---|---|
| 1 | 1,84 (fuente) |
| 2 | 1,32 (tabla de Student, no figura en la fuente) |
| 3 | 1,20 (tabla de Student) |
| 5 | 1,11 (tabla de Student) |
| 10 | 1,05 (fuente) |
| 100 | 1,005 (fuente) |
| ∞ | 1 (fuente) |
- Más lecturas → menor t → menor incertidumbre. Siempre t ≥ 1.

## Tipo B · u(B)
- No surge de repetir lecturas: juicio técnico con la información disponible (exactitud del instrumento, certificado, resolución, experiencia).
- Se asigna una distribución con límites conocidos ±a:
  - **Uniforme:** varianza = a² / 3  →  u(B) = a / √3
  - **Triangular:** varianza = a² / 6  →  u(B) = a / √6

## Combinada
- Mismas unidades → suma cuadrática (ley de propagación, teorema de las varianzas):
  uc = √[ u(A)² + u(B)² ]
- Se expresa en la unidad, en % o en ppm.

## Expandida
- **U = k(p) · u**. Para informes técnicos y certificados de calibración.
| Caso | k (95 %) | k (99 %) |
|---|---|---|
| Tipo A | 2 | 3 |
| Tipo B, uniforme | 1,65 | 1,71 |
| Tipo B, triangular | 2,33 (fuente) | 2,42 (fuente) |
- **Ojo, triangular:** con la definición u = a/√6, la GUM da k ≈ 1,90 (95 %) y ≈ 2,20 (99 %). Los valores 2,33 / 2,42 de la fuente no coinciden: **no publicarlos** sin verificar en IRAM 35050. Los de tipo A y uniforme sí coinciden con la GUM.
- En la práctica, para una combinada de varias fuentes se usa k = 2 (≈ 95 %). Informar siempre k y p.

## Ejemplo propio de EGC (no está en la fuente): PAT de vivienda, límite 40 Ω (ficha 06)
- Telurímetro supuesto ±(2 % lectura + 3 dígitos), resolución 0,1 Ω. Método del 62 %, 3 lecturas (ficha 06).
- Caso 1: 36,2 / 37,0 / 36,5 Ω → v̄ = 36,57; s = 0,40; S* = 0,23; u(A) = 1,32 × 0,23 = 0,31; a = 1,03 → u(B) = 0,60; uc = 0,67; U(k=2) = 1,34 → **36,6 ± 1,3 Ω**: cumple con margen.
- Caso 2: 39,0 / 39,6 / 39,3 Ω → v̄ = 39,3; u(A) = 0,23; u(B) = 0,63; uc = 0,67; U = 1,33 → **39,3 ± 1,3 Ω**: el intervalo cruza 40 Ω.
- Aplicar la incertidumbre a la decisión de conformidad es **buena práctica**; la AEA 770 no lo exige en forma explícita en esta biblioteca. Decirlo así.

## Uso en EGC
- Mensajes: tomar más de una lectura; anotar todas; instrumento calibrado; informar valor ± U con k; cerca del límite, mejorar la instalación.
- Protocolo SRT 900/15 (ficha 29): útil para explicar por qué conviene registrar las lecturas y el instrumento.

## Publicado con esta ficha
- Nota del blog "Incertidumbre de medición: por qué 'medí 39 Ω' no alcanza" y placa EGC-incertidumbre-de-medicion.png.
