"""
Tests unitarios para el módulo de mezcla de palabras.
"""

import pytest
from src.ejercicio2 import seleccionar_palabras, mezclar_palabras, procesar_oracion

def test_seleccionar_palabras_validas():
    """Prueba la selección de palabras con una oración válida."""
    oracion = "casa perro gato"
    resultado = seleccionar_palabras(oracion)
    assert resultado is not None
    assert len(resultado) == 2
    assert all(palabra in oracion.split() for palabra in resultado)
    assert resultado[0] != resultado[1]

def test_seleccionar_palabras_insuficientes():
    """Prueba con oración que no tiene suficientes palabras."""
    assert seleccionar_palabras("casa") is None
    assert seleccionar_palabras("") is None

def test_mezclar_palabras_longitud():
    """Verifica que la palabra mezclada tiene la longitud correcta."""
    palabra1, palabra2 = "casa", "perro"
    resultado = mezclar_palabras(palabra1, palabra2)
    assert len(resultado) == len(palabra1) + len(palabra2)

def test_mezclar_palabras_caracteres():
    """Verifica que solo se usan caracteres de las palabras originales."""
    palabra1, palabra2 = "casa", "perro"
    resultado = mezclar_palabras(palabra1, palabra2)
    caracteres_originales = set(palabra1 + palabra2)
    assert all(c in caracteres_originales for c in resultado)

def test_procesar_oracion_completo():
    """Prueba el proceso completo con una oración válida."""
    oracion = "La casa está en la montaña"
    resultado = procesar_oracion(oracion)
    assert resultado is not None
    assert isinstance(resultado, str)
    assert len(resultado) > 0