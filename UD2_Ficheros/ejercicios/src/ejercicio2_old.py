# -*- coding: utf-8 -*-
"""
Módulo para contar palabras en archivos de texto.

Este módulo implementa funciones para contar palabras con soporte
para diferentes codificaciones y archivos grandes.

Author: Urtzi Díaz
Version: 1.2
"""

import logging
from pathlib import Path
from typing import Optional, Dict
from tqdm import tqdm
import chardet

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constantes
DEFAULT_ENCODING = 'utf-8'
CHUNK_SIZE = 1024 * 1024  # 1MB
DATA_DIR = Path(__file__).parent.parent / "data"

def detect_encoding(file_path: Path) -> str:
    """Detecta la codificación del archivo."""
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read(CHUNK_SIZE)
            result = chardet.detect(raw_data)
            return result['encoding'] or DEFAULT_ENCODING
    except Exception as e:
        logging.warning(f"Error al detectar codificación: {e}")
        return DEFAULT_ENCODING

def count_words(input_file: str | Path, 
                output_file: str | Path, 
                encoding: str = None,
                force: bool = False) -> Optional[Dict[str, int]]:
    """
    Cuenta las palabras en un archivo con soporte para diferentes codificaciones.

    Args:
        input_file: Ruta del archivo de entrada
        output_file: Ruta del archivo de salida
        encoding: Codificación del archivo (auto-detectada si es None)
        force: Si es True, sobrescribe el archivo sin preguntar

    Returns:
        Dict[str, int]: Diccionario con las palabras y su frecuencia
        None: Si hay error en los archivos
    """
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        logging.error(f"Archivo de entrada no encontrado: {input_file}")
        return None

    if output_path.exists() and not force:
        respuesta = input(f"El archivo {output_file} ya existe. ¿Desea sobrescribirlo? (s/N): ")
        if respuesta.lower() != 's':
            logging.info("Operación cancelada por el usuario")
            return None

    # Detectar codificación si no se especifica
    file_encoding = encoding or detect_encoding(input_path)
    logging.info(f"Usando codificación: {file_encoding}")

    word_count: Dict[str, int] = {}
    total_lines = sum(1 for _ in open(input_path, 'rb'))
    
    try:
        with open(input_path, 'r', encoding=file_encoding) as f_in:
            # Mostrar barra de progreso
            for line in tqdm(f_in, total=total_lines, desc="Procesando"):
                for word in line.strip().split():
                    word_count[word] = word_count.get(word, 0) + 1

        with open(output_path, 'w', encoding=DEFAULT_ENCODING) as f_out:
            for word, count in sorted(word_count.items()):
                f_out.write(f"{word}: {count}\n")

        logging.info(f"Conteo completado. Resultados guardados en {output_file}")
        return word_count

    except UnicodeError as e:
        logging.error(f"Error de codificación: {e}")
        return None
    except Exception as e:
        logging.error(f"Error procesando archivos: {str(e)}")
        return None

def main():
    """Función principal de ejemplo."""
    input_file = DATA_DIR / "fitxategi1.txt"
    output_file = DATA_DIR / "resultado_conteo.txt"
    
    result = count_words(input_file, output_file)
    if result is None:
        logging.error("No se pudo completar el conteo")
    else:
        logging.info(f"Se encontraron {len(result)} palabras diferentes")

if __name__ == "__main__":
    main()
