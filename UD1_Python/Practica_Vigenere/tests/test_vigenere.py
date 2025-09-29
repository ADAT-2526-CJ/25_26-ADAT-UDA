"""
Prueba que cifrar y luego descifrar devuelve el texto original.
Revisa que los módulos, clases y funciones tengan docstring.
Verifica que sigan PEP 257 (mayúscula inicial, punto final).
Revisa que los parámetros de cada función estén documentados en el docstring.          
"""
from UD1_Python.Practica_Vigenere.src.vigenere import cifrar_vigenere, descifrar_vigenere

def test_cifrado_y_descifrado():
    """Prueba que cifrar y luego descifrar devuelve el texto original.
    Arguments:
        None
    Returns:
        None    
    """
    texto = "ATAQUE"
    clave = "CLAVE"
    cifrado = cifrar_vigenere(texto, clave)
    assert cifrado == "CEALYG"
    descifrado = descifrar_vigenere(cifrado, clave)
    assert descifrado == texto
