# 62 · Formularios DCI: texto verificado, normativa de referencia y nota de autorización de Edenor

Fuentes (PDF originales recibidos de Fran el 22/11/2026):
- COPITEC, formularios DCI: Planilla Monofásico (Anexo II), "Monofásico actualizado" (conexiondomiciliaria_formulariodci_feb2018-1), Trifásico Planilla A, Trifásico Planilla B, Distribuida Monofásico y Distribuida Trifásico.
- COPITEC, lista "Normativa de referencia" de su página de formularios (links copiados por Fran).
- Edenor, **"Nota de autorización"** PSC-1155-A, revisión 2 (edición 30/05/2023, actualización 01/03/2024).

Estado: **PRIMARIA**. Esta ficha **verifica con el texto exacto** lo que la ficha 61 tomó de un resumen automático. Donde difieren, gana esta ficha.

## Normativa de referencia (según la página del COPITEC)
- Res. ENRE 225/11: https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-225-2011-183582/texto (ficha 56)
- Res. ENRE 269/12: https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-269-2012-202726/texto (ficha 57)
- Res. CTPBA 717/10 (CAIE, Colegio de Técnicos PBA): https://tecnicosdistrito1.com.ar/n-71710-caie-certificado-de-aptitud-de-instalacion-electrica/ (ficha 60)
- Res. SICyM 92/98: https://servicios.infoleg.gob.ar/infolegInternet/anexos/45000-49999/49285/texact.htm (ficha 58)
- Reglamentación AEA vigente: https://aea.org.ar/reglamentaciones/digitales/

## DCI monofásica T1R: dos versiones del mismo formulario
| Dato | Versión ENRE (ficha 56) | Versión COPITEC "actualizada" |
|---|---|---|
| Vigencia | "dd/mm/aaaa" (en blanco) | **12/10/2012** |
| Verificación | Res. ENRE 225/2011 | **Res. ENRE 225/2011 y 269/2012 o modificatoria** |
| "Otorgada por" | En blanco | COPITEC (precargado) |
| Nota (2) | Cumplir Res. 225/2011 | Cumplir **Res. 269/2012** |
- Ítems a–e, notas (1) y (2) y nota final: **idénticos** en las dos.
- Conclusión: la versión COPITEC es el **Anexo II de la Res. 269/2012** con los datos del consejo. Para la app, usar el texto de esta versión y dejar "Otorgada por" editable.

## DCI trifásica: Planilla A (texto verificado)
- Casillas de trámite: **DE OBRA**, DEFINITIVA, AMP. POT., REHABILIT., CENSO CARGA, PREFACT. El **pilar de obra trifásico** usa esta planilla.
- Texto: conformidad con las Res. ENRE 225/11 y 269/12 o modificatoria. "Para ser válido deberá estar visado por el Colegio/Consejo de Técnicos/Profesional de la jurisdicción (*)".
- Datos del instalador: nombre, DNI, título, matrícula, **"Reg. Inst. COPITEC Nº"**, domicilio, localidad, teléfono.
- Declaración bajo responsabilidad: cumple la Res. del ENRE y el reglamento: ordenanza municipal, AEA 1987, AEA 2006 u otro, más otras normas. Tarea profesional.
- Datos del titular, del inmueble (circ., secc., mz., parc., subparc., expediente) y de la instalación (potencia total y máxima en kW; monofásica/trifásica; industrial/comercial/residencial; provincial/municipal/res. multifamiliar; tensión kV; In del interruptor principal A; polos; tarifa; Icc kA; sección mm²; disyuntor).
- Firmas: profesional, titular y **entidad habilitante (*)**. Pie: "Anexo I – Planilla A – Resolución Nº 717/10".

## DCI trifásica: Planilla B (texto verificado)
- "Planilla de inspección", **medidor trifásico**. Ítems 1 a 26 iguales a la ficha 60.
- **Error del formulario:** la columna de **resistencia de puesta a tierra (23–26)** dice "Valor medido en **MΩ**". Es un error de copia: la puesta a tierra se mide en **Ω**. La planilla del Colegio de Técnicos PBA (ficha 60) dice Ω. En la app usar **Ω**.
- Cierre: el titular acepta la inspección del **Gobierno de la Ciudad de Buenos Aires** y/o de un profesional matriculado en el COPITEC.

## DCI de generación distribuida (fotovoltaica)
- Monofásica: Anexo II, vigente desde **12/10/2012**. Trifásica: vigente desde **29/09/2012**.
- Mismo texto que la DCI T1R (ítems a–e, notas 1 y 2), con el título "Instalación y certificación del sistema de generación de energía fotovoltaica" y "Generación distribuida de energía renovable integrada a la red de distribución".

## Nota de autorización de Edenor (PSC-1155-A, rev. 2)
- El **titular** autoriza a otra persona (nombre y DNI) a hacer un trámite a su nombre en Edenor.
- Datos: trámite, número de cuenta, domicilio completo (calle, número, piso, depto, localidad, partido).
- Se adjunta **fotocopia del DNI del titular y del autorizado**.
- Firma, aclaración, documento, e-mail y teléfono del titular.
- Uso típico: el **electricista** gestiona el nuevo medidor o el aumento de potencia por su cliente.

## Para la app
- Generador de DCI con el **texto exacto** de esta ficha: monofásica (Anexo II), trifásica (Planillas A y B) y fotovoltaica.
- Planilla B: puesta a tierra en **Ω** (corregir el error del formulario).
- **Generar la Nota de autorización de Edenor** prellenada con los datos del cliente y del electricista. Recordar adjuntar los dos DNI.
- En la DCI, la casilla "Reglamento AEA 2006" está desactualizada: ofrecer "AEA vigente" en el campo "Reglamento".

## Pendiente
- Equivalente de Edesur a la nota de autorización.
- Edesur, "Consideraciones sobre el certificado DCI" (2025).
