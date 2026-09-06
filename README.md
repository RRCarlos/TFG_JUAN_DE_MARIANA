# Proyecto Autores — Historia General de España

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).
> Trabajo de Fin de Grado · revisión final del proyecto en septiembre de 2026

---

## 1. Qué investigamos

Juan de Mariana (1536–1624), jesuita e historiador, publicó en 1601 la primera traducción al castellano de su *Historia General de España* (*Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana*). En los cuatro primeros libros —desde los orígenes míticos de Hispania hasta la caída del Imperio romano de Occidente—, Mariana recurre a un conjunto de autoridades que puede reconstruirse con precisión a partir de la tabla principal del proyecto.

La pregunta que guía esta investigación es:

> **¿Para qué cita Mariana a cada autor?**

No se trata de determinar si Mariana tuvo acceso físico directo a cada obra citada, sino de identificar la **función historiográfica** de cada mención dentro de la construcción del relato. Cuando Mariana aborda un tema dudoso —reyes fabulosos, etimologías problemáticas, genealogías fantásticas, falsificaciones, autoridades patrísticas o cronológicas— suele contrastar varias voces antes de adoptar o rechazar una versión.

El objeto de estudio del proyecto son las **apariciones registradas en los Libros I–IV**, en la edición de Toledo de 1601, con clasificación por contexto, función y temática.

---

## 2. Estado actual del proyecto

El README anterior estaba desactualizado. La revisión final del proyecto en la documentación del repositorio establece los siguientes datos definitivos:

- **Citas registradas en la tabla principal**: 194.
- **Autores externos distintos**: 83.
- **Autores distintos en total** (incluyendo a Juan de Mariana): 84.
- **Autoreferencias de Mariana**: 2.
- **Citas colaterales del Libro IV**: 13, localizadas en una pasada redundante y no integradas en el total principal.
- **Cobertura documental**: Libros I–IV de la *Historia General de España*.

> La verificación manual de citas se considera completa para la tabla principal; la sección de citas colaterales queda documentada como material complementario, no como parte del conteo principal.

### Resultados relevantes

- La relación de citas no se reduce a una mera lista de autoridades, sino a un sistema de **funciones argumentativas** dentro del relato.
- Mariana combina fuentes clásicas, geográficas, cronológicas, patrísticas, hagiográficas, etimológicas y críticas.
- El análisis distingue entre la cita que **fundamenta**, la que **contrasta**, la que **desacredita** y la que **remite a otra tradición documental**.
- El proyecto trabaja con una base textual que incorpora artefactos OCR propios de la tipografía antigua y aplica corrección ortográfica para la columna de **Cita normalizada**.

---

## 3. Metodología del proyecto

### 3.1. Pregunta de investigación

La pregunta original —¿tuvo Mariana acceso real a autores que menciona?— fue reformulada porque no era suficiente para explicar la práctica efectiva del texto. El proyecto se centró en una pregunta más productiva:

> **¿Para qué usa Mariana a cada autor?**

Esto permite analizar la **lógica historiográfica** de la obra, no solo la existencia de una edición o una fuente.

### 3.2. Fuentes materiales

La base textual del estudio es la edición de Toledo, 1601, de la *Historia General de España*, con la versión OCR digitalizada como soporte de trabajo y la lectura manual del texto como referencia principal.

La documentación del repositorio identifica dos fuentes clave:

1. **Edición base**: la edición de Toledo de 1601.
2. **Notas del investigador**: el documento principal de recolección de citas y funciones, conservado en [Notas/Apuntes sobre HGE Cap I-IV.txt](Notas/Apuntes%20sobre%20HGE%20Cap%20I-IV.txt).

### 3.3. Criterio de clasificación

La tabla principal clasifica cada cita según su función en el argumento de Mariana. Las categorías relevantes son, entre otras:

- geografía,
- etnografía,
- cronología,
- genealogía,
- política y militar,
- religión,
- arqueología,
- lingüística,
- historiografía.

Este criterio no pretende identificar una única “fuente verdadera”, sino describir la manera en que Mariana articula autoridad, duda, tradición y crítica dentro de su historia.

---

## 4. Fuentes y edición base

### Edición de 1601 — texto base

La edición de referencia es la **primera traducción al castellano**, publicada en Toledo en 1601 por Pedro Rodríguez.

| Campo | Valor |
|-------|-------|
| Título completo | *Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana* |
| Lugar | Toledo |
| Imprenta | Pedro Rodríguez |
| Fecha | 5 de octubre de 1601 |
| Formato | 2 tomos en folio |
| OCLC | 36264560 |
| USTC | 5006449 |

Los archivos de texto correspondientes a la edición OCR se conservan en la carpeta [Ediciones_HGE](Ediciones_HGE), y el trabajo analítico del proyecto se apoya en esos textos, aunque no constituye el objeto principal del análisis.

### Nota sobre el OCR

Los textos extraídos de la digitalización contienen artefactos propios del reconocimiento óptico: ſ→s, confusiones v/u, ligaduras, abreviaturas de imprenta. Estos elementos se normalizan antes de comparar o resumir una cita. La columna **Cita normalizada** de la tabla principal aplica esa corrección.

---

## 5. Estructura del repositorio

```
proyecto-autores/
├── README.md
├── Análisis de datos/
│   └── Autores y obras.md
├── Notas/
│   └── Apuntes sobre HGE Cap I-IV.txt
├── Tablas/
│   ├── Tabla de autores.md
│   ├── Tabla de capítulos.md
│   └── Capítulos sin citas.md
├── Ediciones_HGE/
│   ├── 00_portada_indice.txt
│   ├── 01_libro_primero.txt
│   ├── 02_libro_segundo.txt
│   ├── 03_libro_tercero.txt
│   ├── 04_libro_cuarto.txt
│   └── HGE_TomosI-II.txt
└── .gitignore
```

### Archivos principales

- [README.md](README.md): bitácora general del proyecto y estado del trabajo.
- [Análisis de datos/Autores y obras.md](Análisis%20de%20datos/Autores%20y%20obras.md): identificación de citas en las que Mariana menciona explícitamente una obra del autor.
- [Notas/Apuntes sobre HGE Cap I-IV.txt](Notas/Apuntes%20sobre%20HGE%20Cap%20I-IV.txt): fuente primaria de observación y clasificación.
- [Tablas/Tabla de autores.md](Tablas/Tabla%20de%20autores.md): tabla principal del proyecto, con autores, capítulos, citas normalizadas, contexto y temática.
- [Tablas/Capítulos sin citas.md](Tablas/Capítulos%20sin%20citas.md): listado de capítulos sin cita de autor y sección de citas colaterales.
- [Tablas/Tabla de capítulos.md](Tablas/Tabla%20de%20capítulos.md): índice de capítulos y referencia de línea inicial en el OCR.

---

## 6. La tabla de autores

La tabla principal ([Tablas/Tabla de autores.md](Tablas/Tabla%20de%20autores.md)) organiza las citas por libro y capítulo y contiene las siguientes columnas:

| Columna | Contenido |
|---------|-----------|
| # | Número de entrada |
| Autor | Nombre del autor tal como aparece en Mariana |
| Capítulo | Libro y capítulo de referencia |
| Cita normalizada | Extracto textual con normalización ortográfica |
| Contexto | Descripción del uso historiográfico de la cita |
| Temática | Grupo temático según la función en el argumento |

Además, la tabla incorpora:

- **Autoreferencias de Juan de Mariana** (2 entradas).
- **Resumen por autor** con frecuencia y temática.
- **Conteo de citas por libro**.
- **Citas colaterales** del Libro IV, que no forman parte del total principal.

---

## 7. Capítulos sin cita

[Tablas/Capítulos sin citas.md](Tablas/Capítulos%20sin%20citas.md) recoge los capítulos de los Libros I–IV en los que no se localizó una cita explícita de autor. El documento confirma la ausencia de autor citado en determinados pasajes y documenta además las citas colaterales identificadas en una pasada redundante.

---

## 8. Catálogos y referencias

### Catálogos de verificación

| Catálogo | URL |
|----------|-----|
| Library of Congress (LOC) | https://www.loc.gov |
| Biblioteca Nacional de España (BNE) | https://www.bne.es |
| Biblioteca de Castilla-La Mancha | https://patrimoniodigital.castillalamancha.es |
| VIAF | https://viaf.org |
| USTC | https://ustc.ac.uk |
| GW | https://gesamtkatalogderwiegendrucke.de |
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

## 9. Nota de actualización

El anterior README reproducía cifras anteriores a la revisión final del proyecto y no reflejaba la estructura documental definitiva del repositorio. La versión actual se ha actualizado a la evidencia disponible en la tabla principal, los apuntes del investigador y el análisis de capítulos.

*Última actualización: 6 de septiembre de 2026*

[Repositorio en GitHub](https://github.com/RRCarlos/proyecto-autores)
