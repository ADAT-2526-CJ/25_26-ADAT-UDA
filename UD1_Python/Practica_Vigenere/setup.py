"""
Script de configuración para crear un ejecutable del programa de cifrado Vigenère.
"""

from cx_Freeze import setup, Executable
import sys
import os

# Ruta absoluta de este setup.py
base_path = os.path.dirname(__file__)

build_exe_options = {
    "packages": [],
    "excludes": ["tkinter"],
    "include_files": [(os.path.join(base_path, "data"), "data")],
}

base = None
if sys.platform == "win32":
    base = None  # o "Win32GUI" si no quieres consola

setup(
    name="Vigenere UDA",
    author="Urtzi Diaz Arberas",
    version="1.0",
    description="Cifrado y descifrado con el algoritmso de Vigenère",
    options={"build_exe": build_exe_options},
    executables=[Executable(os.path.join(base_path, "src", "vigenere.py"), base=base)]
)
