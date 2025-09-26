"""
Tests automáticos para validar los docstrings de los ejercicios.
- Comprueba que los módulos, clases y funciones tengan docstring.
- Verifica que sigan PEP 257 (mayúscula inicial, punto final).
- Revisa que los parámetros de cada función estén documentados en el docstring.
"""

import importlib
import inspect
import pytest

# Módulos de la UD1 a revisar
MODULOS = [
    "UD1_Python.ejercicio06",
    "UD1_Python.ejercicio07",
    "UD1_Python.ejercicio08",
    "UD1_Python.ejercicio09",
]


@pytest.mark.parametrize("modname", MODULOS)
def test_docstring_modulo(modname):
    """Cada módulo debe tener un docstring inicial no vacío."""
    modulo = importlib.import_module(modname)

    doc = modulo.__doc__
    assert doc is not None and doc.strip() != "", f"El módulo {modname} no tiene docstring."

    # PEP 257 básico
    doc = doc.strip()
    assert doc[0].isupper(), f"Docstring de {modname} debe empezar en mayúscula."
    assert doc.endswith("."), f"Docstring de {modname} debe terminar en punto."


@pytest.mark.parametrize("modname", MODULOS)
def test_docstrings_clases_funciones(modname):
    """Todas las clases y funciones públicas deben tener docstring válido."""
    modulo = importlib.import_module(modname)

    for nombre, obj in inspect.getmembers(modulo):
        if (inspect.isclass(obj) or inspect.isfunction(obj)) and obj.__module__ == modname:
            if not nombre.startswith("_"):  # ignoramos funciones privadas
                doc = obj.__doc__
                assert doc is not None and doc.strip() != "", f"'{nombre}' en {modname} no tiene docstring."
                # PEP 257 básico
                doc = doc.strip()
                assert doc[0].isupper(), f"Docstring de '{nombre}' en {modname} debe empezar en mayúscula."
                assert doc.endswith("."), f"Docstring de '{nombre}' en {modname} debe terminar en punto."


@pytest.mark.parametrize("modname", MODULOS)
def test_parametros_documentados(modname):
    """Cada parámetro de las funciones debe estar mencionado en el docstring."""
    modulo = importlib.import_module(modname)

    for nombre, obj in inspect.getmembers(modulo, inspect.isfunction):
        if obj.__module__ == modname and not nombre.startswith("_"):
            sig = inspect.signature(obj)
            doc = (obj.__doc__ or "").lower()

            for param in sig.parameters:
                assert param.lower() in doc, (
                    f"El parámetro '{param}' de la función '{nombre}' en {modname} "
                    f"no está documentado en el docstring."
                )
