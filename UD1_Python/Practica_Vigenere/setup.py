"""
Script de configuración para crear un ejecutable del programa de cifrado Vigenère.
"""

from cx_Freeze import setup, Executable
import sys
import os

# Opciones de compilación
build_exe_options = {
    "packages": [],
    "excludes": ["tkinter"],       # excluir si no lo usas
    "include_files": ["data/"],    # incluir la carpeta data dentro del ejecutable
}

# Detectar si es Windows para GUI (sin ventana de consola)
base = None
if sys.platform == "win32":
    base = None  # o "Win32GUI" si no quieres que se abra consola

setup(
    name="Vigenere",
    version="1.0",
    description="Cifrado y descifrado con el algoritmo de Vigenère",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/vigenere.py", base=base)]
)
