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
    texto = texto.upper()
    return "".join(c for c in texto if c in string.ascii_uppercase)

def limpiar_texto_demo(texto: str) -> str:
    """
    Convierte un texto a mayúsculas y elimina cualquier carácter
    que no sea una letra de la A a la Z.
    Args:
        texto (str): Texto a limpiar.
    Returns:
        str: Texto limpio.
    """
    texto_mayus = texto.upper()  # 1. Convertir todo el texto a mayúsculas
    caracteres_validos = []  # 2. Crear una lista vacía para almacenar los caracteres válidos
    for c in texto_mayus:  # 3. Recorrer cada carácter del texto
        if c in string.ascii_uppercase:  # 4. Solo añadimos si está en el alfabeto inglés (A-Z)
            caracteres_validos.append(c)
    texto_limpio = "".join(caracteres_validos)  # 5. Unir la lista de caracteres válidos en una cadena final
    return texto_limpio


def leer_fichero(path: str) -> str:
    """
    Lee el contenido de un fichero de texto.
    Intenta primero en UTF-8 y, si falla, usa latin-1.
    Args:
        path (str): Ruta del fichero.
    Returns:
        str: Contenido del fichero o cadena vacía si hay error. 
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        print(f"[WARN] {path} no está en UTF-8, probando con latin-1...")
        with open(path, "r", encoding="latin-1") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] El fichero {path} no existe.")
        return ""
    except Exception as e:
        print(f"[ERROR] No se pudo leer {path}: {e}")
        return ""


def escribir_fichero(path: str, contenido: str) -> None:
    """Escribe contenido en un fichero de texto usando UTF-8.
    Args:
        path (str): Ruta del fichero.
        contenido (str): Contenido a escribir.
    Returns:
        None
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"[OK] Fichero escrito en {path}")
    except Exception as e:
        print(f"[ERROR] No se pudo escribir en {path}: {e}")


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
    clave = limpiar_texto(clave)
    if not clave:
        raise ValueError("La clave no puede estar vacía")
    return (clave * ((len(texto) // len(clave)) + 1))[:len(texto)]
    
def ajustar_clave_demo(texto: str, clave: str) -> str:
    """
    Ajusta la clave para que tenga la misma longitud que el texto.
    Si la clave es más corta, se repite; si es más larga, se corta.
    """
    clave = limpiar_texto(clave)  # 1. Limpiar la clave (quitar espacios, convertir a mayúsculas)
    if not clave:  # 2. Comprobar que la clave no esté vacía
        raise ValueError("La clave no puede estar vacía")
    repeticiones = (len(texto) // len(clave)) + 1 # 3. Calcular cuántas veces hay que repetir la clave
    clave_repetida = clave * repeticiones # 4. Repetir la clave las veces necesarias
    clave_ajustada = clave_repetida[:len(texto)] # 5. Cortar la clave repetida a la longitud del texto
    return clave_ajustada


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
    if not clave:
        raise ValueError("La clave no puede estar vacía")

    texto = limpiar_texto(texto)
    clave_ajustada = ajustar_clave(texto, clave)

    return "".join(
        chr(((ord(t) - 65 + ord(c) - 65) % 26) + 65)
        for t, c in zip(texto, clave_ajustada)
    )

def cifrar_vigenere_demo(texto: str, clave: str) -> str:
    """
    Cifra un texto usando el algoritmo de Vigenère.
    """
    if not clave:
        raise ValueError("La clave no puede estar vacía")

    # 1. Limpiar el texto (quitar espacios y símbolos, pasar a mayúsculas)
    texto = limpiar_texto(texto)

    # 2. Ajustar la clave a la longitud del texto
    clave_ajustada = ajustar_clave(texto, clave)

    # 3. Crear una lista vacía para ir guardando los caracteres cifrados
    resultado = []

    # 4. Recorrer texto y clave al mismo tiempo
    for t, c in zip(texto, clave_ajustada):
        # Convertir caracteres a números (A=65 → 0)
        valor_t = ord(t) - 65
        valor_c = ord(c) - 65

        # Fórmula de cifrado: (texto + clave) mod 26
        valor_cifrado = (valor_t + valor_c) % 26

        # Convertir número de vuelta a letra mayúscula
        letra_cifrada = chr(valor_cifrado + 65)

        # Añadir a la lista
        resultado.append(letra_cifrada)

    # 5. Unir todos los caracteres y devolver el texto cifrado
    return "".join(resultado)


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
    if not clave:
        raise ValueError("La clave no puede estar vacía")

    texto_cifrado = limpiar_texto(texto_cifrado)
    clave_ajustada = ajustar_clave(texto_cifrado, clave)

    return "".join(
        chr(((ord(t) - 65 - (ord(c) - 65)) % 26) + 65)
        for t, c in zip(texto_cifrado, clave_ajustada)
    )
def descifrar_vigenere_demo(texto_cifrado: str, clave: str) -> str:
    """
    Descifra un texto cifrado con el algoritmo de Vigenère.
    """
    if not clave:
        raise ValueError("La clave no puede estar vacía")

    # 1. Limpiar el texto cifrado
    texto_cifrado = limpiar_texto(texto_cifrado)

    # 2. Ajustar la clave a la longitud del texto cifrado
    clave_ajustada = ajustar_clave(texto_cifrado, clave)

    # 3. Lista para ir guardando el descifrado
    resultado = []

    # 4. Recorrer texto cifrado y clave al mismo tiempo
    for t, c in zip(texto_cifrado, clave_ajustada):
        valor_t = ord(t) - 65
        valor_c = ord(c) - 65

        # Fórmula de descifrado: (texto - clave) mod 26
        valor_descifrado = (valor_t - valor_c) % 26

        letra_descifrada = chr(valor_descifrado + 65)
        resultado.append(letra_descifrada)

    # 5. Unir todo en una cadena final
    return "".join(resultado)


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
    try:
        if not CLAVE_DEMO:
            raise ValueError("La clave no puede estar vacía")

        # Ejemplo directo en consola
        cifrado = cifrar_vigenere(TEXTO_DEMO, CLAVE_DEMO)
        print(f"Texto original:   {TEXTO_DEMO}")
        print(f"Clave:    {CLAVE_DEMO}")
        print(f"Texto cifrado:    {cifrado}")

        descifrado = descifrar_vigenere(cifrado, CLAVE_DEMO)
        print(f"Texto descifrado: {descifrado}")

        # Crear directorio si no existe
        os.makedirs(DATA_DIR, exist_ok=True)

        # Crear mensaje inicial si no existe
        if not os.path.exists(FILE_ORIGINAL):
            escribir_fichero(FILE_ORIGINAL, "Este es un mensaje secreto que será cifrado con Vigenere.")

        # Leer, cifrar y escribir
        contenido = leer_fichero(FILE_ORIGINAL)
        if contenido:
            cifrado_fichero = cifrar_vigenere(contenido, CLAVE_DEMO)
            escribir_fichero(FILE_CIFRADO, cifrado_fichero)

            descifrado_fichero = descifrar_vigenere(cifrado_fichero, CLAVE_DEMO)
            escribir_fichero(FILE_DESCIFRADO, descifrado_fichero)

    except ValueError as ve:
        print(f"[ERROR] {ve}")
    except Exception as e:
        print(f"[ERROR] Error inesperado: {e}")


if __name__ == "__main__":
    main()