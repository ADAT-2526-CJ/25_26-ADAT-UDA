# -*- coding: utf-8 -*-
"""
Módulo para generar y guardar listas aleatorias.

Este módulo genera listas de números aleatorios y las guarda
usando el módulo pickle para su posterior procesamiento.

Author: Urtzi Díaz
Version: 1.2
"""

import random
import pickle
import logging
from pathlib import Path
from typing import List

# Configuración de directorios y logs
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Crear directorios necesarios
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "ejercicio3_generar.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Constantes
CANTIDAD_NUMEROS = 1000
RANGO_MIN = -100
RANGO_MAX = 100
ARCHIVO_LISTA1 = "lista1.pkl"
ARCHIVO_LISTA2 = "lista2.pkl"

def generar_lista() -> List[float]:
    """
    Genera una lista de números aleatorios.

    Returns:
        List[float]: Lista de números aleatorios entre -100 y 100
    """
    logging.info(f"Generando lista de {CANTIDAD_NUMEROS} números aleatorios...")
    return [random.uniform(RANGO_MIN, RANGO_MAX) for _ in range(CANTIDAD_NUMEROS)]

def guardar_lista(archivo: Path, lista: List[float]) -> bool:
    """
    Guarda una lista en un archivo usando pickle.

    Args:
        archivo: Ruta del archivo donde guardar
        lista: Lista de números a guardar

    Returns:
        bool: True si se guardó correctamente, False en caso contrario
    """
    try:
        with open(archivo, 'wb') as f:
            pickle.dump(lista, f)
        logging.info(f"Lista guardada exitosamente en {archivo}")
        return True
    except Exception as e:
        logging.error(f"Error guardando lista en {archivo}: {str(e)}")
        return False

def main():
    """Función principal."""
    logging.info("Iniciando generación de listas...")
    
    lista1 = generar_lista()
    lista2 = generar_lista()
    
    guardar_lista(DATA_DIR / ARCHIVO_LISTA1, lista1)
    guardar_lista(DATA_DIR / ARCHIVO_LISTA2, lista2)
    
    logging.info("Proceso completado.")

if __name__ == "__main__":
    main()
