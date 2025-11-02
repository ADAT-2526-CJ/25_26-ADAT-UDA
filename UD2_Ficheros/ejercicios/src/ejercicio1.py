# -*- coding: utf-8 -*-
"""
1.	Escribe una función en el lenguaje de programación Python llamada rnd_word(fitxategi1, fitxategi2)
que lea el primer archivo línea por línea, seleccione una palabra aleatoria de cada línea
y la escriba en el segundo archivo. Utiliza la función choice del módulo random.
--

Este módulo implementa funciones para seleccionar palabras aleatorias
de un archivo de texto y escribirlas en otro archivo.

Author: Urtzi Díaz
Version: 1.1
"""

import random
import os
import logging
from typing import Optional
from pathlib import Path

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constantes
ENCODING = 'utf-8'
DATA_DIR = Path(__file__).parent.parent / "data"
DEFAULT_INPUT_FILE = "fitxategi1.txt"
DEFAULT_OUTPUT_FILE = "fitxategi2.txt"

def rnd_word(input_file: str | Path, output_file: str | Path, force: bool = False) -> Optional[bool]:
    """
    Procesa un archivo seleccionando una palabra aleatoria de cada línea.

    Args:
        input_file: Ruta del archivo de entrada
        output_file: Ruta del archivo de salida
        force: Si es True, sobrescribe el archivo sin preguntar

    Returns:
        bool: True si el proceso fue exitoso, False si hubo errores
        None: Si los archivos no son válidos
    Raises:
        Ninguno: Maneja internamente los errores y los registra.
    """
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        logging.error(f"Archivo de entrada no encontrado: {input_file}")
        return None

    # Comprobar si el archivo de salida ya existe
    if output_path.exists() and not force:
        respuesta = input(f"El archivo {output_file} ya existe. ¿Desea sobrescribirlo? (s/N): ")
        if respuesta.lower() != 's':
            logging.info("Operación cancelada por el usuario")
            return False
        logging.info(f"Sobrescribiendo archivo existente: {output_file}")
    
    try:
        with open(input_path, 'r', encoding=ENCODING) as f_in, \
             open(output_path, 'w', encoding=ENCODING) as f_out:

            for line_num, line in enumerate(f_in, 1):
                words = line.strip().split()
                if not words:
                    logging.warning(f"Línea {line_num} vacía")
                    continue
                
                selected_word = random.choice(words)
                f_out.write(f"{selected_word}\n")

        logging.info(f"Archivo generado correctamente: {output_file}")
        return True

    except PermissionError:
        logging.error("Error de permisos al acceder a los archivos")
        return False
    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        return False

def main():
    """Función principal de ejemplo."""
    input_file = DATA_DIR / DEFAULT_INPUT_FILE
    output_file = DATA_DIR / DEFAULT_OUTPUT_FILE
    
    result = rnd_word(input_file, output_file, force=False)
    if result is None:
        logging.error("No se pudo completar la operación")

if __name__ == "__main__":
    main()
