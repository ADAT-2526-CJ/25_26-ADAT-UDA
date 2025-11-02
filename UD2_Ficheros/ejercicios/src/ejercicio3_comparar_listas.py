# -*- coding: utf-8 -*-
"""
Módulo para comparar listas guardadas.

Este módulo carga listas guardadas con pickle y calcula
el promedio de las diferencias absolutas entre sus valores.

Author: Urtzi Díaz
Version: 1.2
"""

import pickle
import logging
from pathlib import Path
from typing import Optional, List, Tuple
from statistics import mean

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
        logging.FileHandler(LOG_DIR / "ejercicio3_comparar.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Constantes
ARCHIVO_LISTA1 = "lista1.pkl"
ARCHIVO_LISTA2 = "lista2.pkl"

def cargar_lista(archivo: Path) -> Optional[List[float]]:
    """
    Carga una lista desde un archivo pickle.

    Args:
        archivo: Ruta del archivo a cargar

    Returns:
        List[float]: Lista cargada
        None: Si hubo error al cargar
    """
    try:
        with open(archivo, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        logging.error(f"Error cargando {archivo}: {str(e)}")
        return None

def calcular_promedio_diferencias(archivo1: Path = None, archivo2: Path = None) -> Optional[float]:
    """
    Calcula el promedio de diferencias entre las listas.

    Args:
        archivo1: Ruta opcional del primer archivo
        archivo2: Ruta opcional del segundo archivo

    Returns:
        float: Promedio de las diferencias
        None: Si hubo error en el proceso
    """
    logging.info("Iniciando cálculo de diferencias...")
    
    # Usar rutas por defecto si no se proporcionan
    ruta1 = archivo1 if archivo1 else DATA_DIR / ARCHIVO_LISTA1
    ruta2 = archivo2 if archivo2 else DATA_DIR / ARCHIVO_LISTA2
    
    # Cargar las listas
    lista1 = cargar_lista(ruta1)
    lista2 = cargar_lista(ruta2)
    
    if not lista1 or not lista2:
        return None
    
    if len(lista1) != len(lista2):
        logging.error("Las listas tienen tamaños diferentes")
        return None
    
    try:
        diferencias = [abs(a - b) for a, b in zip(lista1, lista2)]
        promedio = mean(diferencias)
        logging.info(f"Promedio calculado: {promedio:.2f}")
        return promedio
    except Exception as e:
        logging.error(f"Error calculando el promedio: {str(e)}")
        return None

def main():
    """Función principal."""
    promedio = calcular_promedio_diferencias()
    if promedio is not None:
        print(f"\nPromedio de las diferencias: {promedio:.2f}")
    else:
        print("\nNo se pudo calcular el promedio")

if __name__ == "__main__":
    main()
