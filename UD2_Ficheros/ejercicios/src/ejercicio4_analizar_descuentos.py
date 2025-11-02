# -*- coding: utf-8 -*-
"""
Módulo para analizar descuentos de libros.

Este módulo lee la base de datos de libros y analiza
los descuentos para encontrar las mejores ofertas.

Author: Urtzi Díaz
Version: 1.2
"""

import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import os

# Configuración de directorios y logs
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Crear directorio logs si no existe
LOG_DIR.mkdir(exist_ok=True)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "ejercicio4_analizar.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Constantes
ARCHIVO_LIBROS = "libros.txt"
ENCODING = 'utf-8'

def cargar_libros(archivo: Path) -> Optional[List[Dict]]:
    """
    Carga los libros almacenados con repr().

    Args:
        archivo: Ruta del archivo a cargar

    Returns:
        List[Dict]: Lista de libros cargados
        None: Si hubo error al cargar
    """
    try:
        libros = []
        with open(archivo, "r", encoding=ENCODING) as f:
            for linea in f:
                libros.append(eval(linea.strip()))
        logging.info(f"Cargados {len(libros)} libros")
        return libros
    except FileNotFoundError:
        logging.error(f"No se encontró el archivo {archivo}")
        return None
    except Exception as e:
        logging.error(f"Error cargando libros: {str(e)}")
        return None

def libro_mayor_descuento(libros: List[Dict]) -> Optional[Tuple[Dict, float]]:
    """
    Encuentra el libro con mayor descuento porcentual.

    Args:
        libros: Lista de diccionarios con datos de libros

    Returns:
        Tuple[Dict, float]: (libro, porcentaje_descuento)
        None: Si la lista está vacía
    """
    if not libros:
        logging.error("No hay libros para analizar")
        return None

    max_libro = None
    max_desc = 0.0
    
    for libro in libros:
        try:
            descuento = 100 * (libro["precio"] - libro["precio_descuento"]) / libro["precio"]
            if descuento > max_desc:
                max_desc = descuento
                max_libro = libro
        except ZeroDivisionError:
            logging.warning(f"Precio cero en libro: {libro['nombre']}")
            continue
            
    logging.info(f"Mayor descuento encontrado: {max_desc:.2f}%")
    return max_libro, max_desc

def main():
    """Función principal."""
    archivo = DATA_DIR / ARCHIVO_LIBROS
    libros = cargar_libros(archivo)
    
    if libros:
        resultado = libro_mayor_descuento(libros)
        if resultado:
            libro, descuento = resultado
            print(f"\nLibro con mayor descuento: {libro['nombre']}")
            print(f"Autor: {libro['autor']}")
            print(f"Descuento: {descuento:.2f}%")
            print(f"Precio original: {libro['precio']}€")
            print(f"Precio con descuento: {libro['precio_descuento']}€")
        else:
            print("\nNo se encontraron descuentos válidos")
    else:
        print("\nNo se pudieron cargar los libros")

if __name__ == "__main__":
    main()
