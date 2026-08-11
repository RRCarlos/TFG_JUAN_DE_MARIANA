#!/usr/bin/env python3
"""Fase 0: Preprocesamiento mecánico del OCR para Tabla de autores 1.

Limpia artefactos mecánicos del OCR en la columna 'Cita':
1. Elimina números de página sueltos (20, 30, 50, etc.)
2. Expande abreviaturas (q→que, có→con)
3. Normaliza espacios después de puntuación
4. Colapsa espacios múltiples
5. Separa palabras fusionadas donde el patrón es obvio

Las correcciones difíciles (ſ→s, palabras unidas complejas) quedan
para la fase de transcripción con IA, que tiene más contexto.
"""

import re
import sys
from pathlib import Path


# --- Funciones de preprocesamiento ---

def eliminar_numeros_pagina(texto):
    """Elimina números de página sueltos del OCR (20, 30, 50, etc.)."""
    # Patrones: número solo al inicio, al final, o entre espacios
    texto = re.sub(r'^\d+\s+', '', texto)
    texto = re.sub(r'\s+\d+\s+', ' ', texto)
    texto = re.sub(r'\s+\d+$', '', texto)
    return texto


def expandir_abreviaturas(texto):
    """Expande abreviaturas comunes del siglo XVI."""
    # q → que (solo q solitario o al inicio de palabra fusionada)
    # Cuidado: no cambiar "q" en medio de otra palabra
    texto = re.sub(r'\bq\b', 'que', texto)
    texto = re.sub(r'\bQ\b', 'Que', texto)
    
    # có → con (solo al inicio de palabra)
    texto = re.sub(r'\bcó\b', 'con', texto)
    texto = re.sub(r'\bCó\b', 'Con', texto)
    
    return texto


def normalizar_puntuacion(texto):
    """Añade espacios después de puntuación si faltan."""
    # Después de . , ; : ! ? — añadir espacio si no lo hay
    texto = re.sub(r'([.,;:!?])([^\s\d])', r'\1 \2', texto)
    # Después de paréntesis de cierre
    texto = re.sub(r'\)([^\s])', r') \1', texto)
    return texto


def colapsar_espacios(texto):
    """Colapsa múltiples espacios en uno solo y recorta."""
    texto = re.sub(r' {2,}', ' ', texto)
    return texto.strip()


def separar_fusiones_obvias(texto):
    """Separa palabras fusionadas donde el patrón es obvio.
    
    Patrones detectados:
    - Consonante seguida de 'los/las/los/les' → separar
    - 'del'/'al'/'el' al inicio fusionado con anterior
    """
    # "delosdemás" → "de los demás"
    texto = re.sub(r'(?<=[a-záéíóúñ])(delos\b)', r' \1', texto)
    texto = re.sub(r'(?<=[a-záéíóúñ])(delas\b)', r' \1', texto)
    
    # "alos" → "a los"
    texto = re.sub(r'\balos\b', 'a los', texto)
    
    # "yel" → "y el"
    texto = re.sub(r'\byel\b', 'y el', texto)
    
    # "ynos" → "y nos"  
    texto = re.sub(r'\byn(?:os|o)\b', lambda m: m.group().replace('n', 'n '), texto)
    
    return texto


# --- Pipeline completo ---

def preprocesar_cita(texto):
    """Aplica todas las transformaciones de preprocesamiento."""
    if not texto or texto.strip() == '':
        return texto
    
    texto = eliminar_numeros_pagina(texto)
    texto = expandir_abreviaturas(texto)
    texto = normalizar_puntuacion(texto)
    texto = separar_fusiones_obvias(texto)
    texto = colapsar_espacios(texto)
    
    return texto


def procesar_tabla(ruta_tabla):
    """Procesa la tabla markdown y rellena la columna 'Cita normalizada'."""
    lineas = Path(ruta_tabla).read_text(encoding='utf-8').splitlines()
    resultado = []
    cambios = 0
    total_citas = 0
    
    for linea in lineas:
        # Detectar líneas de datos de la tabla (empiezan con |)
        if linea.startswith('|') and not linea.startswith('|---') and not linea.startswith('| #'):
            partes = linea.split('|')
            # Formato: | # | Autor | Capítulo | Línea | Cita | Cita normalizada | Contexto |
            if len(partes) >= 7:
                cita_original = partes[5].strip()
                if cita_original and not cita_original.startswith('*'):
                    total_citas += 1
                    cita_preprocesada = preprocesar_cita(cita_original)
                    if cita_preprocesada != cita_original:
                        cambios += 1
                    # Columna 5 = Cita (original, NO tocar)
                    # Columna 6 = Cita normalizada (preprocesada)
                    partes[6] = ' ' + cita_preprocesada + ' '
                    linea = '|'.join(partes)
        resultado.append(linea)
    
    Path(ruta_tabla).write_text('\n'.join(resultado) + '\n', encoding='utf-8')
    return total_citas, cambios


if __name__ == '__main__':
    ruta = Path(__file__).parent / 'Tablas' / 'Tabla de autores 1.md'
    if not ruta.exists():
        print(f"Error: no se encuentra {ruta}")
        sys.exit(1)
    
    total, cambios = procesar_tabla(ruta)
    print(f"Procesadas {total} citas, {cambios} modificadas por preprocesamiento.")
    print("Siguiente paso: transcripción con IA de las citas preprocesadas.")
