"""
Ejercicio 3 – Lista de números
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Este programa modifica el programa anterior, de manera que al terminar de guardar los números en la lista
se impriman la lista, el sumatorio y la media de todos los número de dicha lista.

"""

def pedir_numeros_impares():
    """
    Pide al usuario 10 números impares.

    Returns:
        list[int]: Lista con los números impares introducidos por el usuario.
    """
    numeros = []
    while len(numeros) < 10:
        num = int(input(f"Introduce un número impar ({len(numeros)+1}/10): "))
        if num % 2 != 0:
            numeros.append(num)
        else:
            print("Ese número no es impar. Intenta de nuevo.")
    return numeros


def main():
    """Ejecuta el programa principal del ejercicio 2."""
    lista = pedir_numeros_impares()
    print("Lista de números:", lista)
    print("Sumatorio:", sum(lista))
    print("Media:", sum(lista) / len(lista))

if __name__ == "__main__":
    main()
