"""
Ejercicio 8 _ Persona ejecutable
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Módulo ejecutable para probar la clase Persona.

Este script crea tres objetos de la clase Persona y, para cada uno:
- Comprueba si está en su peso ideal, tiene sobrepeso o está por debajo de su peso ideal, mostrando un mensaje.
- Indica si es mayor de edad.
- Muestra toda la información del objeto.

"""
from UD1_Python.Ejercicios.ejercicio07 import Persona

def main():
    """Función principal para ejecutar el ejercicio 8.
    Args:
        None.
    Returns:
        None.
    """
    # Crear lista de objetos Persona
    personas = [
        Persona("Urtzi", 25, Persona.SEXO_HOMBRE, 80, 1.80),
        Persona("María", 30, Persona.SEXO_MUJER, 60, 1.65),
        Persona("Pedro", 17, Persona.SEXO_HOMBRE, 10, 1.80)
    ]

    # Mostrar información de cada persona
    for i, persona in enumerate(personas, 1):
        print(f"--- Persona {i} ---")
        persona.mostrar_info_persona()
        print()

if __name__ == "__main__":
    main()