"""
Ejercicio 2 – Lista de números sumatorio y la media
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Este programa modifica el programa anterior, de manera que al terminar de guardar los números en la lista
se impriman la lista, el sumatorio y la media de todos los número de dicha lista.

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
    """Ejecuta el programa principal del ejercicio 2."""
    lista = pedir_numeros()
    print("Lista de números:", lista)
    print("Sumatorio:", sum(lista))
    print("Media:", sum(lista) / len(lista))
if __name__ == "__main__":
    main()
