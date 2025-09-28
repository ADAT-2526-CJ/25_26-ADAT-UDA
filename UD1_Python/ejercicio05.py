"""
Ejercicio 5 _ Menú con funciones
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Este programa solicita 10 números impares y permite operar con ellos
(sumatorio, media, máximo, mínimo) usando funciones específicas.
"""

def sumatorio(lista):
    """
    Calcula la suma de los elementos de una lista.

    Args:
        lista (list[int]): Lista de números enteros.

    Returns:
        int: La suma de todos los elementos de la lista.
    """
    return sum(lista)


def media(lista):
    """
    Calcula la media aritmética de los elementos de una lista.

    Args:
        lista (list[int]): Lista de números enteros.

    Returns:
        float: La media de los elementos de la lista.
    """
    return sum(lista) / len(lista)


def maximo(lista):
    """
    Devuelve el valor máximo de una lista.

    Args:
        lista (list[int]): Lista de números enteros.

    Returns:
        int: El valor más alto de la lista.
    """
    return max(lista)


def minimo(lista):
    """
    Devuelve el valor mínimo de una lista.

    Args:
        lista (list[int]): Lista de números enteros.

    Returns:
        int: El valor más bajo de la lista.
    """
    return min(lista)


def pedir_impares():
    """
    Pide al usuario números impares hasta completar 10 elementos.

    Returns:
        list[int]: Lista con los números impares introducidos.
    """
    numeros = []
    while len(numeros) < 10:
        num = int(input(f"Introduce un número impar ({len(numeros)+1}/10): "))
        if num % 2 != 0:
            numeros.append(num)
    return numeros


def mostrar_menu(numeros):
    """
    Muestra un menú para operar con la lista de números usando funciones.

    Args:
        numeros (list[int]): Lista de números impares.
    """
    while True:
        print("\n¿Qué desea hacer con la lista?")
        print("1. Sumatorio")
        print("2. Media")
        print("3. Máximo")
        print("4. Mínimo")
        print("0. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            print("Sumatorio:", sumatorio(numeros))
        elif opcion == 2:
            print("Media:", media(numeros))
        elif opcion == 3:
            print("Máximo:", maximo(numeros))
        elif opcion == 4:
            print("Mínimo:", minimo(numeros))
        elif opcion == 0:
            break
        else:
            print("Opción no válida.")


def main():
    """Ejecuta el programa principal del ejercicio 5."""
    lista = pedir_impares()
    mostrar_menu(lista)


if __name__ == "__main__":
    main()
