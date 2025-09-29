import pytest
from src.vigenere import cifrar_vigenere, descifrar_vigenere

def test_cifrado_y_descifrado():
    texto = "ATAQUE"
    clave = "CLAVE"
    cifrado = cifrar_vigenere(texto, clave)
    assert cifrado == "CEALYG"
    descifrado = descifrar_vigenere(cifrado, clave)
    assert descifrado == texto
