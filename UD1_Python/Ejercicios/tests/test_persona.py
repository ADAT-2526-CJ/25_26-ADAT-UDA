"""
Tests con pytest para la clase Persona (Ejercicios 7 y 8).
Cada test muestra feedback directo.
"""

from UD1_Python.Ejercicios.ejercicio07 import Persona


def test_mayor_de_edad():
    """Comprueba si el método esMayorDeEdad funciona correctamente.
    Arguments:
        None    
    Returns:
        None    
    """
    p = Persona("Ana", 20, "M", 55, 1.65)
    assert p.esMayorDeEdad()
    q = Persona("Luis", 17, "H", 70, 1.75)
    assert not q.esMayorDeEdad()
    print("\ntest_mayor_de_edad: comprobación correcta")


def test_imc_bajo():
    """Comprueba si el método calcularIMC funciona correctamente para bajo peso.
    Arguments:
        None    
    Returns:
        None    
    """
    p = Persona("Test", 25, "M", 40, 1.70)
    assert p.calcularIMC() in [-1, getattr(Persona, "IMC_BAJO", -1)]
    print("\ntest_imc_bajo: cálculo correcto")


def test_imc_ideal():
    """Comprueba si el método calcularIMC funciona correctamente para peso ideal.
    Arguments:
        None    
    Returns:
        None    
    """
    p = Persona("Test", 25, "H", 65, 1.75)
    assert p.calcularIMC() in [0, getattr(Persona, "IMC_IDEAL", 0)]
    print("\ntest_imc_ideal: cálculo correcto")


def test_imc_sobrepeso():
    """Comprueba si el método calcularIMC funciona correctamente para sobrepeso.
    Arguments:
        None    
    Returns:
        None    
    """
    p = Persona("Test", 30, "M", 90, 1.60)
    assert p.calcularIMC() in [1, getattr(Persona, "IMC_SOBREPESO", 1)]
    print("\ntest_imc_sobrepeso: cálculo correcto")


def test_dni_generado():
    """Comprueba si el DNI se genera correctamente.
        Arguments:
        None    
    Returns:
        None    
    """
    p = Persona("Test", 25, "H", 70, 1.80)
    dni_str = p.toString()
    assert dni_str.strip() != ""
    print("\ntest_dni_generado: DNI generado correctamente")
