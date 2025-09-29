"""
Tests con pytest para la clase Criptografo (Ejercicio 6).
Cada test muestra feedback directo.
"""
import pytest

try:
    from UD1_Python.Ejercicios.ejercicio06 import Criptografo
except ModuleNotFoundError:
    pytest.skip("ejercicio06.py no está disponible, se omite test_criptografo", allow_module_level=True)


def test_encriptar_desplazamiento_simple():
    """Prueba básica de encriptación con desplazamiento ASCII.'ABC' debería encriptarse como 'BCD'.
    'ABC' debería encriptarse como 'BCD'.
    Arguments:
        None    
    Returns:
        None    
    """
    c = Criptografo()
    texto = "ABC"
    resultado = c.encriptar(texto)
    assert resultado == "BCD"
    print("\ntest_encriptar_desplazamiento_simple: encriptación correcta")


def test_desencriptar_simple():
    """Prueba básica de desencriptación con desplazamiento ASCII. 'XYZ' debería desencriptarse como 'WXY'.
    'XYZ' debería desencriptarse como 'WXY'.
    Arguments:
        None
    Returns:
        None    
    """
    c = Criptografo()
    texto = "XYZ"
    enc = c.encriptar(texto)
    dec = c.desencriptar(enc)
    assert dec == texto
    print("\ntest_desencriptar_simple: desencriptación correcta")


def test_encriptar_vacio():
    """Prueba de encriptación con cadena vacía. Debería devolver cadena vacía.
    Arguments:
        None
    Returns:
        None    
    """
    c = Criptografo()
    assert c.encriptar("") == ""
    print("\ntest_encriptar_vacio: cadena vacía manejada correctamente")


def test_desencriptar_vacio():
    """Prueba de desencriptación con cadena vacía. Debería devolver cadena vacía.
    Arguments:
        None
    Returns:
        None    
    """
    c = Criptografo()
    assert c.desencriptar("") == ""
    print("\ntest_desencriptar_vacio: cadena vacía manejada correctamente")


def test_simetria_varios_textos():
    """Prueba de simetría en varios textos. Encriptar y luego desencriptar debería devolver el texto original.
    Arguments:
        None
    Returns:
        None    
    """
    c = Criptografo()
    ejemplos = ["hola", "Python3", "1234", "áéíóú"]
    for txt in ejemplos:
        assert c.desencriptar(c.encriptar(txt)) == txt
    print("\ntest_simetria_varios_textos: simetría correcta")
