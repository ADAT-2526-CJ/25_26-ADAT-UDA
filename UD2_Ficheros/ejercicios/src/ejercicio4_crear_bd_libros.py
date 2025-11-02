# -*- coding: utf-8 -*-
"""
Módulo para crear una base de datos de libros.

Este módulo permite crear y guardar información sobre libros,
incluyendo sus precios y descuentos.

Author: Urtzi Díaz
Version: 1.2
"""

import logging
import re
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Optional, Pattern

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
        logging.FileHandler(LOG_DIR / "ejercicio4_crear.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Constantes
ARCHIVO_LIBROS = "libros.txt"
ENCODING = 'utf-8'

# Constantes de validación
MIN_LONGITUD_NOMBRE = 2
MAX_LONGITUD_NOMBRE = 100
MIN_PAGINAS = 1
MAX_PAGINAS = 10000
MAX_PRECIO = 1000.0
PATRON_NOMBRE: Pattern = re.compile(r'^[\w\s.,;:¿?¡!áéíóúÁÉÍÓÚñÑ-]{2,100}$')

@dataclass
class Libro:
    """Clase para representar un libro con validación de datos."""
    nombre: str
    autor: str
    precio: Decimal
    precio_descuento: Decimal
    paginas: int

    def __post_init__(self):
        """Validación después de la inicialización."""
        if not self._validar_texto(self.nombre) or not self._validar_texto(self.autor):
            raise ValueError("Nombre o autor inválido")
        if not self._validar_precio(self.precio) or not self._validar_precio(self.precio_descuento):
            raise ValueError("Precio inválido")
        if not self._validar_paginas(self.paginas):
            raise ValueError("Número de páginas inválido")
        if self.precio_descuento > self.precio:
            raise ValueError("El precio con descuento no puede ser mayor que el precio original")

    @staticmethod
    def _validar_texto(texto: str) -> bool:
        """Valida que el texto cumpla con el patrón permitido."""
        return bool(PATRON_NOMBRE.match(texto))

    @staticmethod
    def _validar_precio(precio: Decimal) -> bool:
        """Valida que el precio esté en el rango permitido."""
        return Decimal('0') <= precio <= Decimal(str(MAX_PRECIO))

    @staticmethod
    def _validar_paginas(paginas: int) -> bool:
        """Valida que el número de páginas esté en el rango permitido."""
        return MIN_PAGINAS <= paginas <= MAX_PAGINAS

    def to_dict(self) -> Dict:
        """Convierte el libro a diccionario."""
        return {
            "nombre": self.nombre,
            "autor": self.autor,
            "precio": float(self.precio),
            "precio_descuento": float(self.precio_descuento),
            "paginas": self.paginas
        }

def solicitar_dato(prompt: str, tipo: str, intentos: int = 3) -> Optional[str]:
    """
    Solicita un dato al usuario con reintentos.

    Args:
        prompt: Mensaje para mostrar al usuario
        tipo: Tipo de dato ('texto', 'precio' o 'paginas')
        intentos: Número máximo de intentos permitidos

    Returns:
        Optional[str]: Valor válido o None si se agotan los intentos
    """
    for i in range(intentos):
        valor = input(prompt).strip()
        
        if tipo == 'texto' and len(valor) < MIN_LONGITUD_NOMBRE:
            print(f"Error: El texto debe tener al menos {MIN_LONGITUD_NOMBRE} caracteres.")
            logging.warning(f"Intento {i+1}/{intentos}: Texto demasiado corto: '{valor}'")
            continue
            
        if tipo == 'precio':
            try:
                precio = float(valor)
                if 0 <= precio <= MAX_PRECIO:
                    return valor
                print(f"Error: El precio debe estar entre 0 y {MAX_PRECIO}€")
                logging.warning(f"Intento {i+1}/{intentos}: Precio fuera de rango: {valor}")
            except ValueError:
                print("Error: Ingrese un número válido (ejemplo: 29.99)")
                logging.warning(f"Intento {i+1}/{intentos}: Precio inválido: '{valor}'")
            continue
            
        if tipo == 'paginas':
            try:
                paginas = int(valor)
                if MIN_PAGINAS <= paginas <= MAX_PAGINAS:
                    return valor
                print(f"Error: Las páginas deben estar entre {MIN_PAGINAS} y {MAX_PAGINAS}")
                logging.warning(f"Intento {i+1}/{intentos}: Páginas fuera de rango: {valor}")
            except ValueError:
                print("Error: Ingrese un número entero válido")
                logging.warning(f"Intento {i+1}/{intentos}: Número de páginas inválido: '{valor}'")
            continue
            
        return valor
        
    logging.error(f"Se agotaron los intentos solicitando {tipo}")
    return None

def solicitar_libro() -> Optional[Libro]:
    """
    Solicita los datos de un libro al usuario con validación mejorada y reintentos.

    Returns:
        Optional[Libro]: Instancia de Libro si los datos son válidos, None en caso contrario
    """
    try:
        # Solicitar nombre
        nombre = solicitar_dato("Nombre del libro: ", "texto")
        if nombre is None:
            print("\nDemasiados intentos fallidos para el nombre del libro.")
            return None

        # Solicitar autor
        autor = solicitar_dato("Autor: ", "texto")
        if autor is None:
            print("\nDemasiados intentos fallidos para el autor.")
            return None

        # Solicitar precio original
        precio_str = solicitar_dato("Precio original (€): ", "precio")
        if precio_str is None:
            print("\nDemasiados intentos fallidos para el precio original.")
            return None

        # Solicitar precio con descuento
        precio_desc_str = solicitar_dato("Precio con descuento (€): ", "precio")
        if precio_desc_str is None:
            print("\nDemasiados intentos fallidos para el precio con descuento.")
            return None

        # Validar que el descuento no sea mayor que el precio original
        precio = Decimal(precio_str)
        precio_descuento = Decimal(precio_desc_str)
        if precio_descuento > precio:
            print("Error: El precio con descuento no puede ser mayor que el precio original.")
            logging.error(f"Precio con descuento ({precio_descuento}) mayor que precio original ({precio})")
            return None

        # Solicitar páginas
        paginas_str = solicitar_dato("Número de páginas: ", "paginas")
        if paginas_str is None:
            print("\nDemasiados intentos fallidos para el número de páginas.")
            return None

        # Crear y validar el libro
        libro = Libro(
            nombre=nombre,
            autor=autor,
            precio=precio,
            precio_descuento=precio_descuento,
            paginas=int(paginas_str)
        )
        
        logging.info(f"Libro registrado exitosamente: {libro.nombre}")
        return libro
        
    except Exception as e:
        logging.error(f"Error inesperado creando libro: {str(e)}")
        print("\nOcurrió un error inesperado. Por favor, inténtelo de nuevo.")
        return None

def solicitar_modo_guardado(archivo: Path) -> Optional[str]:
    """
    Si el archivo existe, pregunta al inicio qué hacer:
    'a' añadir, 'w' sobrescribir, None cancelar.
    """
    if not archivo.exists():
        return "w"
    while True:
        opcion = input(
            f"\nEl archivo {archivo.name} ya existe. ¿Qué desea hacer?\n"
            "1. Añadir los nuevos libros\n"
            "2. Sobrescribir todo\n"
            "3. Cancelar\n"
            "Elija una opción (1-3): "
        ).strip()
        if opcion == "1":
            logging.info("Modo guardado: añadir (append)")
            return "a"
        if opcion == "2":
            logging.info("Modo guardado: sobrescribir (write)")
            return "w"
        if opcion == "3":
            logging.info("Operación cancelada por el usuario (inicio)")
            return None
        print("Opción no válida. Por favor, elija 1, 2 o 3.")

def guardar_libros(libros: List[Libro], archivo: Path, modo: Optional[str] = None) -> bool:
    """
    Guarda la lista de libros en un archivo de forma segura.
    Si `modo` es None y el archivo existe, pregunta (comportamiento heredado).
    """
    try:
        # Si se proporciona modo, usarlo; si no, conservar comportamiento anterior
        if modo is None:
            modo = "w"
            if archivo.exists():
                # Pregunta interactiva antigua (por compatibilidad)
                while True:
                    opcion = input(
                        f"\nEl archivo {archivo.name} ya existe. ¿Qué desea hacer?\n"
                        "1. Añadir los nuevos libros\n"
                        "2. Sobrescribir todo\n"
                        "3. Cancelar\n"
                        "Elija una opción (1-3): "
                    ).strip()
                    if opcion == "1":
                        modo = "a"
                        logging.info("Se añadirán los nuevos libros al archivo existente")
                        break
                    if opcion == "2":
                        logging.warning("Se sobrescribirá el archivo existente")
                        break
                    if opcion == "3":
                        logging.info("Operación cancelada por el usuario")
                        return False
                    print("Opción no válida. Por favor, elija 1, 2 o 3.")
        else:
            # validar modo recibido
            if modo not in ("a", "w"):
                logging.error(f"Modo inválido recibido para guardar: {modo}")
                return False

        with open(archivo, modo, encoding=ENCODING) as f:
            for libro in libros:
                f.write(repr(libro.to_dict()) + "\n")

        logging.info(f"Datos guardados en {archivo} (modo: {'añadir' if modo == 'a' else 'sobrescribir'})")
        return True

    except Exception as e:
        logging.error(f"Error guardando datos: {str(e)}")
        return False

def main():
    """Función principal."""
    logging.info("Iniciando registro de libros...")
    libros: List[Libro] = []
    archivo = DATA_DIR / ARCHIVO_LIBROS

    # Preguntar inmediatamente qué hacer con el fichero existente
    modo_inicial = solicitar_modo_guardado(archivo)
    if modo_inicial is None:
        print("\nOperación cancelada por el usuario. Saliendo.")
        return

    while True:
        libro = solicitar_libro()
        if libro:
            libros.append(libro)

        continuar = input("\n¿Deseas ingresar otro libro? (s/N): ").lower()
        if continuar != "s":
            break

    if libros:
        if guardar_libros(libros, archivo, modo=modo_inicial):
            print(f"\nSe procesaron {len(libros)} libros correctamente.")
        else:
            print("\nNo se guardaron los cambios.")
    else:
        logging.warning("No hay libros para guardar")
        print("\nNo se registraron libros.")

if __name__ == "__main__":
    main()
