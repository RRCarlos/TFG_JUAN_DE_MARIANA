# Proyecto Autores — Historia General de España

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).
> Trabajo de Fin de Grado · Mayo 2026

---

## 1. Qué investigamos

Juan de Mariana (1536–1624), jesuita e historiador, publicó en 1601 la primera traducción al castellano de su *Historia General de España* (*Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana*). En los cuatro primeros libros —que abarcan desde los orígenes míticos de Hispania hasta la caída del Imperio romano de Occidente—, Mariana recurre a **82 autores distintos (81 fuentes externas + 1 autoreferencia de Juan de Mariana)** para fundamentar su relato.

La pregunta que guía este proyecto es:

> **¿Para qué cita Mariana a cada autor?**

No se trata de determinar si Mariana tuvo acceso físico a las obras que menciona, sino de identificar la **función historiográfica** de cada cita dentro de la construcción del relato. Cuando Mariana se refiere a un tema dudoso —reyes fabulosos, genealogías fantásticas, falsificaciones—, suele contrastar varios autores.

El objeto de estudio son **204 citas a fuentes externas y 2 autoreferencias distribuidas en los Libros I–IV**, referenciadas contra la edición de 1601 y clasificadas según su función en el argumento de Mariana.

---

## 2. Por qué lo investigamos

### Contexto académico

Este proyecto se enmarca en un **Trabajo de Fin de Grado** cuyo objetivo inicial era responder una pregunta binaria: ¿tuvo Mariana acceso real a los autores que cita? La verificación sistemática de 68 autores en seis catálogos internacionales aportó datos valiosos, pero también puso de manifiesto los límites de esa pregunta. Demostrar que una edición existía antes de 1592 no prueba que Mariana la leyera.

### El giro metodológico

La pregunta original —*¿tuvo acceso?*— se transformó en una más fértil:

> **¿Para qué usa Mariana a cada autor?**

Este cambio no abandona los resultados previos, sino que los recontextualiza. La verificación de existencias bibliográficas pasa a ser un dato de contexto, no el objetivo central. El objetivo nuevo es analizar la **tipología funcional de las citas**: qué categoría de autoridad representa cada autor (geográfica, narrativa, cronológica, bíblica, etimológica, crítica), y cómo se articulan esas autoridades dentro del sistema historiográfico de Mariana.

### Valor del estudio

Comprender el sistema de citas de Mariana permite:

- Reconstituir las **estrategias argumentativas** de un historiador del siglo XVI.
- Identificar las **tradiciones textuales** que nutrieron la historiografía española moderna.
- Detectar los casos en que Mariana opera con **escepticismo** (cita para desacreditar) frente a los que opera con **adhesión** (cita para fundamentar).
- Distinguir entre el uso de **fuentes directas** (ediciones impresas), **transmisión indirecta** (compilaciones medievales) y **fuentes problemáticas** (obras perdidas, falsificaciones).

### Estado actual del proyecto (Agosto 2026)

> **Nota de estado:** la **verificación manual** de las citas está **completa** (204 de 204 apariciones de autores externos, más 2 autoreferencias de Mariana, contrastadas con el OCR de los Libros Primero a Cuarto). Las cifras de este documento son definitivas salvo correcciones puntuales.

#### Verificación de autores

Se realizó una verificación exhaustiva de las **204 citas** contra los archivos OCR de la edición de 1601. Además, se hizo un barrido sistemático de los capítulos sin citas en busca de nuevas referencias. Resultados:

- **Autores verificados como fuentes citadas**: 82 autores externos resultaron ser citaciones genuinas (incluidos Casiodoro, Hilderico, San Ildefonso, San Agustín y Juan Margarite, localizados e indexados en julio de 2026)
- **Autores no encontrados en el OCR**: 1 autor no aparece como fuente citada en los Libros I–IV (Hernando del Pulgar)
- **Barrido de capítulos**: del barrido de capítulos sin citas se hallaron **6 citas nuevas** (Rufo Festo y Tito Livio en L.I CAP XXI; Trebellio Polión y San Jerónimo en L.IV; San Agustín ×2 en L.IV; Juan Margarite en L.III)

#### Tabla de autores

La tabla principal (`Tabla de autores 1.md`) contiene:

| Columna | Contenido |
|---------|-----------|
| # | Número de entrada (1–204) |
| Autor | Nombre del autor tal como aparece en Mariana |
| Capítulo | Libro y capítulo de la cita |
| Línea | Línea exacta en el archivo OCR |
| Cita | Extracto textual original del OCR — 3 líneas de contexto (línea anterior, línea de la cita, línea siguiente) |
| Cita normalizada | Misma cita con ortografía modernizada (ſ→s, separación de palabras, corrección de artefactos OCR) |
| Contexto | Descripción del contexto historiográfico de la cita |

Se incluyen además:
- **Resumen por autor** (82 autores con temática y frecuencia de aparición)
- **Autoreferencias de Juan de Mariana** (2 remisiones a su *Historiae de Rebus Hispaniae* de 1592)
- **Autores no encontrados** (1 autor sin citas genuinas en el OCR)
- **Notas sobre la revisión** (2 notas restantes: duplicación OCR en Libro IV (líneas 2580–2593 y 2678–2693), entrada 134 sobre atribución errónea (Silio, marido de Mesalina, no el poeta)

---

## 3. Fuentes

### Edición de 1601 — Texto base

La edición de referencia es la **primera traducción al castellano**, publicada en Toledo en 1601 por Pedro Rodríguez.

| Campo | Valor |
|-------|-------|
| Título completo | *Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana* |
| Lugar | Toledo |
| Imprenta | Pedro Rodríguez |
| Fecha | 5 de octubre de 1601 |
| Formato | 2 tomos en folio: Tomo I (4h + 1015 pág.), Tomo II (2h + 962 pág. + 13h) |
| OCLC | 36264560 |
| USTC | 5006449 |

El archivo de texto completo (`HGE_TomosI-II.txt`, ~6 MB, 98.805 líneas) fue obtenido del OCR de la digitalización BNE Digital. Para trabajar de forma más cómoda, se dividió en 5 archivos:

| Archivo | Contenido | Líneas |
|---------|-----------|--------|
| `00_portada_indice.txt` | Portada, privilegio, dedicatoria, índice | 254 |
| `01_libro_primero.txt` | Libro I completo | 2.863 |
| `02_libro_segundo.txt` | Libro II completo | 3.109 |
| `03_libro_tercero.txt` | Libro III completo | 2.902 |
| `04_libro_cuarto.txt` | Libro IV completo | 3.165 |

**Notas sobre el TXT**: El archivo proviene de un OCR de una digitalización del siglo XVI. Contiene artefactos de reconocimiento óptico propios de la tipografía de la época (ſ→f, v/u intercambiables, ligaduras rotas, abreviaturas de imprenta). Estos artefactos son predecibles y se mitigan con normalización ortográfica antes de la comparación textual. La columna **Cita normalizada** de la tabla aplica esta corrección automáticamente.

### Notas del investigador

El punto de partida empírico del proyecto es un **documento Word** (*Historia general de España.docx*) donde el investigador recogió, durante la lectura de la edición de 1601, las menciones a autores en los Libros I–IV. Una versión en texto plano de esas notas se incluye en el repositorio (`Notas/Apuntes sobre HGE Cap I-IV.txt`, 795 líneas). Cada entrada incluye:

- Libro y capítulo donde aparece la mención.
- Nombre del autor citado (tal como aparece en Mariana).
- Contexto de la cita.
- Función que cumple esa cita dentro del argumento.
- Tipo de fuente.

Esas notas constituyen la **fuente primaria** del proyecto: todo lo que sigue —tablas, validaciones, clasificaciones— se construirá a partir de ellas. El documento Word original no se incluye en el repositorio por derechos de autor.

La tabla resultante (`Tabla de autores 1.md`) fue verificada contra los archivos OCR y completada con las columnas **Cita** (extracto de 3 líneas del OCR) y **Cita normalizada** (ortografía modernizada: separación de palabras, corrección de ſ→s, eliminación de artefactos OCR). La columna **Contexto** describe la función historiográfica de cada cita.

### Catálogos de verificación

Para verificar la existencia de cada uno de los 68 autores y la disponibilidad de ediciones anteriores a 1592, se consultaron:

| Catálogo | Función |
|----------|---------|
| [Library of Congress (LOC)](https://www.loc.gov) | Autoridades y registros bibliográficos internacionales |
| [Biblioteca Nacional de España (BNE)](https://www.bne.es) | Catálogo nacional español |
| [Biblioteca de Castilla-La Mancha (CLM)](https://patrimoniodigital.castillalamancha.es) | Fondo del antiguo Colegio de Jesuitas de Toledo |
| [VIAF](https://viaf.org) | Archivos de autoridad internacionales |
| [USTC](https://ustc.ac.uk) | Ediciones europeas impresas antes de 1600 |
| [GW](https://gesamtkatalogderwiegendrucke.de) | Incunables (1450–1500) |
| [CCPB](https://bvpb.mcu.es) | Catálogo Colectivo del Patrimonio Bibliográfico Español |

---

## 4. Estructura del repositorio

```
proyecto-autores/
│
├── README.md                          — Bitácora del proyecto
│
├── Tablas/
│   ├── Tabla de autores 1.md          — Tabla principal: 204 citas con Cita y Contexto
│   ├── Tabla de autores 2.md          — Versión resumida: sin columnas Línea ni Cita
│   ├── Tabla de autores 2 (PDF).pdf   — Tabla 2 exportada a PDF (vista previa)
│   └── Tabla de capítulos.md          — Estructura de capítulos de los Libros I–IV
│
├── Datos/
│   └── Relación_de_datos.md           — Análisis cuantitativo y cualitativo de las citas
│
├── Notas/
│   └── Apuntes sobre HGE Cap I-IV.txt — Notas del investigador: menciones a autores en Libros I–IV
│
└── Ediciones_HGE/
    ├── HGE_TomosI-II.txt              — Texto completo de la edición de 1601 (backup, ~6 MB)
    ├── 00_portada_indice.txt          — Portada, privilegio, dedicatoria, índice
    ├── 01_libro_primero.txt           — Libro I (2.863 líneas)
    ├── 02_libro_segundo.txt           — Libro II (3.109 líneas)
    ├── 03_libro_tercero.txt           — Libro III (2.902 líneas)
    └── 04_libro_cuarto.txt            — Libro IV (3.165 líneas)
```

---

## 5. Análisis cuantitativo de las citas

El análisis completo se encuentra en [`Datos/Relación_de_datos.md`](Datos/Relación_de_datos.md). A continuación se presentan los resultados principales. **Cifras provisionales** mientras dure la fase de verificación manual.

### 5.1 Panorama general

| Métrica | Valor |
|---------|-------|
| Total de citas (apariciones) | 204 |
| Autores únicos | 82 (81 externos + 1 autoref) |
| Libros cubiertos | 4 (I–IV) |
| Capítulos con al menos 1 cita | 69 de 93 |
| Autores que acaparan el 50 % de las citas | 14 de 82 (17,1 %) |
| Autor más citado | Plinio (20 citas, 9,9 %) |
| Libro con más citas | Libro Cuarto (77 citas, 37,9 %) |
| Libro con más autores únicos | Libro Cuarto (43 autores) |
| Autores citados en 3+ libros | 7 de 82 (8,5 %) |
| Autores de una sola aparición | 46 de 82 (56,1 %) |

### 5.2 Ranking de frecuencia — Top 15

| Pos. | Autor | Apariciones | % | Libros | Categoría |
|------|-------|-------------|---|--------|-----------|
| 1 | Plinio | 20 | 9,9 % | I–IV | Geógrafo/enciclopedista |
| 2 | Claudio Ptolomeo | 13 | 6,4 % | I–IV | Geógrafo |
| 3 | Plutarco | 9 | 4,4 % | I–IV | Biógrafo/moralista |
| 4 | Dion Casio | 8 | 3,9 % | III, IV | Historiador |
| 5 | San Isidoro de Sevilla | 7 | 3,4 % | I, III, IV | Polígrafo eclesiástico |
| 6 | Tito Livio | 7 | 3,4 % | I, II, IV | Historiador |
| 7 | Séneca | 7 | 3,4 % | III, IV | Filósofo/orador |
| 8 | Prudencio | 6 | 3,0 % | IV | Poeta cristiano |
| 9 | Cayo Silio Italico | 5 | 2,5 % | I, II, IV | Poeta épico |
| 10 | Estrabón | 5 | 2,5 % | I, III | Geógrafo |
| 11 | Quintiliano | 5 | 2,5 % | IV | Retórico |
| 12 | Apiano | 5 | 2,5 % | I, III | Historiador |
| 13 | Cicerón | 4 | 2,0 % | III | Filósofo/orador |
| 14 | Justino | 4 | 2,0 % | I | Historiador |
| 15 | Polibio | 4 | 2,0 % | I, II | Historiador |

### 5.3 Curva de Pareto

| Grupo | Autores | % autores | Citas | % citas |
|-------|---------|-----------|-------|---------|
| Top 5 | Plinio, Ptolomeo, Plutarco, Dion, San Isidoro | 6,1 % | 57 | 28,1 % |
| Top 10 | + Tito Livio, Séneca, Prudencio, Silio Italico, Estrabón | 12,2 % | 87 | 42,9 % |
| Top 15 | + Quintiliano, Apiano, Cicerón, Justino, Polibio | 18,3 % | 109 | 53,7 % |
| Top 20 | + Aristóteles, Orosio, Amiano, Moro Rasis, Diodoro | 24,4 % | 124 | 61,1 % |
| Top 24 | + Eusebio Cesariense, Suetonio, Solino, San Basilio | 29,3 % | 135 | 66,2 % |
| Todos (82) | — | 100 % | 204 | 100 % |

**Interpretación:** Los 24 autores más citados (29,3 % del total) concentran el 66,5 % de las citas. Los 58 autores restantes se reparten entre 1 y 2 apariciones cada uno.

### 5.4 Distribución por libro

| Libro | Entradas | % | Autores únicos | Densidad (citas/cap.) |
|-------|----------|---|----------------|-----------------------|
| Libro Primero | 54 | 26,6 % | 30 | 3,0 |
| Libro Segundo | 26 | 12,8 % | 15 | 1,9 |
| Libro Tercero | 46 | 22,7 % | 23 | 2,7 |
| Libro Cuarto | 77 | 37,7 % | 43 | 4,5 |
| **Total** | **204** | **100 %** | **82** | **3,1** |

**Interpretación:** El Libro Cuarto concentra la mayor densidad de citas (4,5 por capítulo) y el mayor número de autores únicos (43). El Libro Segundo es el de menor densidad (1,9), con 26 citas de 15 autores.

### 5.5 Autores transculturales (presentes en varios libros)

| Libros | N.º autores | Ejemplos |
|--------|-------------|----------|
| 4 libros (I–IV) | 3 | Plinio, Claudio Ptolomeo, Plutarco |
| 3 libros | 4 | San Isidoro, Cayo Silio Italico, Tito Livio, Orosio |
| 2 libros | 11 | Aristóteles, Appiano, Estrabón, Lucano, Polibio, etc. |
| 1 libro | 64 | El resto |

**Interpretación:** Tres autores aparecen en los cuatro libros: Plinio, Claudio Ptolomeo y Plutarco. Los 64 autores de un solo libro representan referencias localizadas en un único libro.

### 5.6 Categorías de autores

| Categoría | Autores | Citas | % citas |
|-----------|---------|-------|---------|
| Historiadores | 15 | 55 | 25,6 % |
| Geógrafos | 4 | 41 | 19,1 % |
| Filósofos | 4 | 21 | 9,8 % |
| Poetas | 6 | 17 | 7,9 % |
| Eclesiásticos | 17 | 31 | 14,4 % |
| Biógrafos | 3 | 16 | 7,4 % |
| Compiladores | 5 | 20 | 9,3 % |
| Retóricos | 3 | 9 | 4,2 % |
| Comentaristas | 7 | 8 | 3,7 % |
| Fabulosos | 3 | 3 | 1,4 % |

**Interpretación:** Los historiadores son la categoría más numerosa (15 autores). Los geógrafos, pese a ser pocos (4), concentran 41 citas gracias a Plinio y Ptolomeo. Los eclesiásticos (17 autores) se concentran principalmente en el Libro Cuarto. La asignación de categorías está pendiente de la revisión manual completa.

### 5.7 Paganos versus cristianos

| Tipo | Autores | Citas | % |
|------|---------|-------|---|
| Paganos | 52 | 155 | 72,1 % |
| Cristianos | 18 | 38 | 17,7 % |
| Mixtos | 3 | 11 | 5,1 % |
| Indeterminados | — | 16 | 7,4 % |

**Interpretación:** Mariana se apoya predominantemente en fuentes paganas (72,1 %). La proporción de citas cristianas (17,7 %) aumenta en el Libro Cuarto, cuando el relato alcanza el Bajo Imperio y la romanización cristiana.

### 5.8 Distribución cronológica de las fuentes

| Período | Autores | Citas | % citas |
|---------|---------|-------|---------|
| Antigüedad clásica (s. V a.C.–II d.C.) | 30 | 110 | 51,2 % |
| Imperio romano tardío (s. III–V) | 12 | 34 | 15,8 % |
| Alta Edad Media (s. VI–X) | 10 | 22 | 10,2 % |
| Plena Edad Media (s. XI–XV) | 14 | 18 | 8,4 % |
| Renacimiento (s. XVI) | 9 | 15 | 7,0 % |
| Indeterminados | 2 | 10 | 4,7 % |

**Interpretación:** Más de la mitad de las citas (51,2 %) corresponden a autores de la Antigüedad clásica. Las fuentes altomedievales representan el 10,2 % (p. ej. San Isidoro); las renacentistas, el 7,0 % (p. ej. Juan Margarite).

### 5.9 Autores más densos por capítulo

| Capítulo | Libro | Citas | Autores principales |
|----------|-------|-------|---------------------|
| Cap. XII | IV | 14 | Prudencio (6), Quintiliano (5), Amiano (3) |
| Cap. XXIIII | III | 7 | Cicerón (1), Dion (×2), Isidoro (×3), Juan Margarite (1) |
| Cap. I | IV | 5 | San Agustín (1), Dion, Plinio, otros |
| Cap. XVII | III | 5 | Séneca (3), Dion Casio (2) |

**Interpretación:** El capítulo XII del Libro Cuarto es el de mayor número de citas (14).

### 5.10 Mariana como crítico (13 citas)

En 13 de las 204 citas, Mariana no cita para fundamentar, sino para **desacreditar o corregir** a un autor:

- **Juan Margarite** (III, XXIIII): Mariana corrige su cálculo sobre la Era del César.
- **San Agustín** (IV, I): Mariana señala la discrepancia en los nombres de los cónsules del año de fundación de Roma.
- **San Agustín** (IV, XII): Referencia a edictos contra los cristianos; Mariana usa su autoridad para situar la cronología.
- **Nepote, Floro, Orosio, M. Varrón, Eusebio**: Correcciones o matices en cálculos cronológicos.
- **Dion, Justino, Plutarco, Tito Livio**: Variantes narrativas o desacuerdos sobre hechos concretos.

**Interpretación:** En 13 de las 204 citas (6,4 %), Mariana corrige o matiza a un autor en lugar de limitarse a transmitir su contenido. El registro de estas correcciones figura en la columna **Contexto** de la tabla.

---

## 6. Referencias

### Catálogos

| Catálogo | URL |
|----------|-----|
| Library of Congress (LOC) | https://www.loc.gov |
| Biblioteca Nacional de España (BNE) | https://www.bne.es |
| Biblioteca de Castilla-La Mancha | https://patrimoniodigital.castillalamancha.es |
| VIAF | https://viaf.org |
| USTC | https://ustc.ac.uk |
| GW (Wiegendrucke) | https://gesamtkatalogderwiegendrucke.de |
| CCPB | https://bvpb.mcu.es |

### Bibliotecas digitales

| Biblioteca | URL |
|------------|-----|
| BNE Digital | https://bnedigital.bne.es |
| Gallica (BnF) | https://gallica.bnf.fr |
| Biblioteca Virtual Miguel de Cervantes | https://www.cervantesvirtual.com |
| Internet Archive | https://archive.org |

### Obra de referencia

Mariana, J. de. *Historia General de España*. Toledo, 1601.

---

*Última actualización: 11 de agosto de 2026*
[Repositorio en GitHub](https://github.com/RRCarlos/proyecto-autores)
