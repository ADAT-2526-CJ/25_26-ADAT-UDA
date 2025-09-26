"""
Tests para validar la documentación (docstrings) de los ejercicios.
Incluye validación de módulos, clases y funciones.
"""

import importlib
import inspect
import pytest

# Archivos a revisar
MODULOS = [
    "UD1_Python.ejercicio06",
    "UD1_Python.ejercicio07",
    "UD1_Python.ejercicio08",
    "UD1_Python.ejercicio09",
]


@pytest.mark.parametrize("modname", MODULOS)
def test_docstring_modulo(modname):
    """
    Cada módulo debe tener un docstring inicial no vacío.
    """
    modulo = importlib.import_module(modname)
    assert modulo.__doc__ is not None and modulo.__doc__.strip() != "", \
        f"El módulo {modname} no tiene docstring o está vacío."
    # Validación básica PEP 257
    doc = modulo.__doc__.strip()
    assert doc[0].isupper(), f"Docstring de {modname} debe empezar en mayúscula."
    assert doc.endswith("."), f"Docstring de {modname} debe terminar en punto."


@pytest.mark.parametrize("modname", MODULOS)
def test_docstrings_clases_funciones(modname):
    """
    Todas las clases y funciones públicas deben tener docstring.
    """
    modulo = importlib.import_module(modname)
    for nombre, obj in inspect.getmembers(modulo):
        if inspect.isclass(obj) or inspect.isfunction(obj):
            if obj.__module__ == modname and not nombre.startswith("_"):
                assert obj.__doc__ is not None and obj.__doc__.strip() != "", \
                    f"'{nombre}' en {modname} no tiene docstring."
