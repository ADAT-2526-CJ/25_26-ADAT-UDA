"""
Ejercicio 1 – Lista de números
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Este programa solicita al usuario 10 números y los guarda en una lista.
Finalmente, imprime la lista completa.
"""

def pedir_numeros():
    """
    Pide al usuario 10 números enteros.

    Returns:
        list[int]: Lista con los números introducidos por el usuario.
    """
    numeros = []
    for i in range(10):
        num = int(input(f"Introduce el número {i+1}: "))
        numeros.append(num)
    return numeros


def main():
    """Ejecuta el programa principal del ejercicio 1."""
    lista = pedir_numeros()
    print("Lista de números:", lista)


if __name__ == "__main__":
    main()
