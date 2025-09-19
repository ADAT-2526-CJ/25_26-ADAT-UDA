"""
Ejercicio 4 – Menú con operaciones sobre lista de impares
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Este programa solicita 10 números impares y ofrece un menú con operaciones
sobre la lista (sumatorio, media, máximo, mínimo).
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

def mostrar_menu(numeros):
    """
    Muestra un menú para operar con la lista de números impares.

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

        opcion = int(input("Elige una opción (0,1,2,3,4): "))

        if opcion == 1:
            print("Sumatorio:", sum(numeros))
        elif opcion == 2:
            print("Media:", sum(numeros) / len(numeros))
        elif opcion == 3:
            print("Máximo:", max(numeros))
        elif opcion == 4:
            print("Mínimo:", min(numeros))
        elif opcion == 0:
            break
        else:
            print("Opción no válida.")


def main():
    """Ejecuta el programa principal del ejercicio 2."""
    lista = pedir_numeros_impares()
    mostrar_menu(lista)

if __name__ == "__main__":
    main()
