"""
Práctica _ Cifrado y Descifrado con el algoritmo de Vigenère.    
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Implementación del cifrado Vigenère con ejemplos de uso en ficheros.

Incluye:
- Funciones para cifrar y descifrar textos.
- Funciones auxiliares para leer y escribir ficheros.
- Control de errores y codificación.
- Ejemplo de uso en la función main().
"""

import string
import os

# --- Constantes de configuración ---
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

# Ficheros de ejemplo
FILE_ORIGINAL = os.path.join(DATA_DIR, "mensaje.txt")
FILE_CIFRADO = os.path.join(DATA_DIR, "mensaje_cifrado.txt")
FILE_DESCIFRADO = os.path.join(DATA_DIR, "mensaje_descifrado.txt")

# Texto y clave de ejemplo (solo para la demo en main)
TEXTO_DEMO = "ATAQUE"
CLAVE_DEMO = "CLAVE"


# --- Funciones auxiliares ---
def limpiar_texto(texto: str) -> str:
    """Convierte a mayúsculas y elimina caracteres no alfabéticos.
    Args:
        texto (str): Texto a limpiar.
    Returns:
        str: Texto limpio.
    """


def leer_fichero(path: str) -> str:
    """
    Lee el contenido de un fichero de texto.
    Intenta primero en UTF-8 y, si falla, usa latin-1.
    Args:
        path (str): Ruta del fichero.
    Returns:
        str: Contenido del fichero o cadena vacía si hay error. 
    """


def escribir_fichero(path: str, contenido: str) -> None:
    """Escribe contenido en un fichero de texto usando UTF-8.
    Args:
        path (str): Ruta del fichero.
        contenido (str): Contenido a escribir.
    Returns:
        None
    """



# --- Algoritmo Vigenère ---
def ajustar_clave(texto: str, clave: str) -> str:
    """
    Ajusta la clave para que coincida con la longitud del texto.

    Args:
        texto (str): Texto a procesar.
        clave (str): Clave de cifrado.

    Returns:
        str: Clave ajustada.

    Raises:
        ValueError: Si la clave está vacía.
    """

def ajustar_clave_demo(texto: str, clave: str) -> str:
    """
    Ajusta la clave para que tenga la misma longitud que el texto.
    Si la clave es más corta, se repite; si es más larga, se corta.
    """


def cifrar_vigenere(texto: str, clave: str) -> str:
    """Cifra un texto usando el algoritmo de Vigenère.
    Args:
        texto (str): Texto a cifrar.
        clave (str): Clave de cifrado.
    Returns:
        str: Texto cifrado.
    Raises:
        ValueError: Si la clave está vacía.
    """

def descifrar_vigenere(texto_cifrado: str, clave: str) -> str:
    """Descifra un texto cifrado con el algoritmo de Vigenère.
    Args:
        texto_cifrado (str): Texto cifrado a descifrar.
        clave (str): Clave de cifrado usada.
    Returns:
        str: Texto descifrado.
    Raises:
        ValueError: Si la clave está vacía.
    """



# --- Programa principal ---
def main():
    """Ejemplo de uso del cifrado Vigenère con consola y ficheros.
    Arguments:
        None
    Returns:
        None
    Raises:
        ValueError: Si la clave está vacía.
        Exception: Para otros errores inesperados.
    """

if __name__ == "__main__":
    main()