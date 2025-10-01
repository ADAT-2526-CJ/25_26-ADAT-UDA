"""
Ejercicio 9 _ Persona datos por pantalla    
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Módulo ejecutable para crear objetos Persona solicitando los datos por terminal.

Permite introducir tantas personas como se desee. Para cada persona:
- Comprueba si está en su peso ideal, tiene sobrepeso o está por debajo de su peso ideal, mostrando un mensaje.
- Indica si es mayor de edad.
- Muestra toda la información del objeto.

"""
from UD1_Python.Ejercicios.ejercicio07 import Persona

def pedir_datos():
    """
    Pide los datos de diferentes personas al usuario.
    Args:
        None.
    Returns:
        Array[persona] : Lista de objetos Persona creados.
    Raises:
        ValueError: Si la entrada no es válida.
    """
    personas = []
    while True:
        print("\nIntroduce los datos de la persona:")
        nombre = input("Nombre: ")
        while True:
            try:
                edad = int(input("Edad: "))
                break
            except ValueError:
                print("Introduce un número entero válido para la edad.")
        while True:
            sexo = input("Sexo (H/M): ").upper()
            if sexo in [Persona.SEXO_HOMBRE, Persona.SEXO_MUJER]:
                break
            else:
                print("Introduce 'H' para hombre o 'M' para mujer.")
        while True:
            try:
                peso = float(input("Peso (kg): "))
                break
            except ValueError:
                print("Introduce un número válido para el peso.")
        while True:
            try:
                altura = float(input("Altura (m): "))
                break
            except ValueError:
                print("Introduce un número válido para la altura.")
        persona = Persona(nombre, edad, sexo, peso, altura)
        personas.append(persona)
        continuar = input("¿Quieres añadir otra persona? (si/no): ").lower()
        if continuar != 'si':
            break
    return personas



def main():
    """Ejecuta el programa principal del ejercicio 9.
    Args:
        None.
    Returns:
        None.
    """
    personas = pedir_datos()
    for persona in personas:
        persona.mostrar_info_persona()


if __name__ == "__main__":
    main()
