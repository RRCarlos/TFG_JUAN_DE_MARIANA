# Proyecto Autores — Historia General de España

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).
> Trabajo de Fin de Grado · Mayo 2026

---

## 1. Qué investigamos

Juan de Mariana (1536–1624), jesuita e historiador, publicó en 1601 la primera traducción al castellano de su *Historia General de España* (*Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana*). En los cuatro primeros libros —que abarcan desde los orígenes míticos de Hispania hasta la caída del Imperio romano de Occidente—, Mariana recurre a **76 autores distintos (75 fuentes externas + 1 autoreferencia de Juan de Mariana)** para fundamentar su relato.

La pregunta que guía este proyecto es:

> **¿Para qué cita Mariana a cada autor?**

No se trata de determinar si Mariana tuvo acceso físico a las obras que menciona, sino de identificar la **función historiográfica** de cada cita dentro de la construcción del relato. Cuando Mariana se refiere a un tema dudoso —reyes fabulosos, genealogías fantásticas, falsificaciones—, suele contrastar varios autores.

El objeto de estudio son **180 apariciones (178 a fuentes externas y 2 autoreferencias) distribuidas en los Libros I–IV**, referenciadas contra la edición de 1601 y clasificadas según su función en el argumento de Mariana.

---

## 2. Por qué lo investigamos

### Contexto académico

Este proyecto se enmarca en un **Trabajo de Fin de Grado** cuyo objetivo inicial era responder una pregunta binaria: ¿tuvo Mariana acceso real a los autores que cita? La verificación sistemática de autores en seis catálogos internacionales aportó datos valiosos, pero también puso de manifiesto los límites de esa pregunta. Demostrar que una edición existía antes de 1592 no prueba que Mariana la leyera.

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

> **Nota de estado:** la **verificación manual** de las citas está **completa** (180 de 180 apariciones —178 externas más 2 autoreferencias— contrastadas con el OCR de los Libros Primero a Cuarto). Las cifras de este documento son definitivas salvo correcciones puntuales.

Resultados:

- **Citas**: 180 apariciones totales (178 fuentes externas + 2 autoreferencias de Mariana a su *Historiae de Rebus Hispaniae* de 1592).
- **Autores distintos**: 76 (75 fuentes externas + Juan de Mariana).
- **Cobertura**: Libros I–IV (93 capítulos), referenciadas contra la edición de Toledo, 1601.
- Cada cita está clasificada en uno de **10 grupos temáticos** según su función en el argumento.

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

**Notas sobre el TXT**: El archivo proviene de un OCR de una digitalización del siglo XVI. Contiene artefactos de reconocimiento óptico propios de la tipografía de la época (ſ→f, v/u intercambiables, ligaduras rotas, abreviaturas de imprenta). Estos artefactos son predecibles y se mitigan con normalización ortográfica antes de la comparación textual. La columna **Cita normalizada** de la tabla aplica esta corrección.

### Notas del investigador

El punto de partida empírico del proyecto es un **documento Word** (*Historia general de España.docx*) donde el investigador recogió, durante la lectura de la edición de 1601, las menciones a autores en los Libros I–IV. Una versión en texto plano de esas notas se incluye en el repositorio (`Notas/Apuntes sobre HGE Cap I-IV.txt`, 795 líneas). Cada entrada incluye:

- Libro y capítulo donde aparece la mención.
- Nombre del autor citado (tal como aparece en Mariana).
- Contexto de la cita.
- Función que cumple esa cita dentro del argumento.
- Tipo de fuente.

Esas notas constituyen la **fuente primaria** del proyecto: todo lo que sigue —tablas, validaciones, clasificaciones— se construyó a partir de ellas. El documento Word original no se incluye en el repositorio por derechos de autor.

### Catálogos de verificación

Para verificar la existencia de los autores y la disponibilidad de ediciones anteriores a 1592, se consultaron:

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
│   ├── Tabla de autores.md            — Tabla principal: 180 citas con Cita normalizada, Contexto y Temática
│   ├── Tabla de autores.html          — Exportación imprimible de la tabla (nota: desactualizada respecto al .md)
│   └── Tabla de capítulos.md          — Índice de capítulos de los Libros I–IV (con línea inicial en el OCR)
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

### La tabla de autores

`Tablas/Tabla de autores.md` organiza las citas por libro (Primero a Cuarto) con las columnas:

| Columna | Contenido |
|---------|-----------|
| # | Número de entrada (1–178 para fuentes externas) |
| Autor | Nombre del autor tal como aparece en Mariana |
| Capítulo | Libro y capítulo de la cita |
| Cita normalizada | Extracto textual con ortografía modernizada (ſ→s, separación de palabras, corrección de artefactos OCR) |
| Contexto | Descripción del contexto historiográfico de la cita |
| Temática | Grupo temático (10 categorías) según la función en el argumento |

Se incluyen además:

- **Autoreferencias de Juan de Mariana** (2 remisiones a su *Historiae de Rebus Hispaniae* de 1592).
- **Conteo de citas** por libro.
- **Resumen por autor** (76 autores con temática y frecuencia de aparición).

---

## 5. Referencias

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

*Última actualización: 18 de agosto de 2026*
[Repositorio en GitHub](https://github.com/RRCarlos/proyecto-autores)
