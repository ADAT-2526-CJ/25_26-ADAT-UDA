import random

# --------------------
# Ejercicio 1
# --------------------
def ejercicio1():
    # Creamos una lista vacía donde guardaremos los números
    numeros = []
    # Pedimos 10 números al usuario
    for i in range(10):
        num = int(input(f"Introduce el número {i+1}: "))
        numeros.append(num)  # añadimos cada número a la lista
    # Mostramos la lista completa
    print("Lista de números:", numeros)


# --------------------
# Ejercicio 2
# --------------------
def ejercicio2():
    numeros = []
    for i in range(10):
        num = int(input(f"Introduce el número {i+1}: "))
        numeros.append(num)

    # Mostramos la lista, la suma y la media
    print("Lista:", numeros)
    print("Sumatorio:", sum(numeros))  # sum() hace la suma de la lista
    print("Media:", sum(numeros) / len(numeros))  # len() cuenta los elementos


# --------------------
# Ejercicio 3
# --------------------
def ejercicio3():
    numeros = []
    # Solo aceptamos números impares
    while len(numeros) < 10:
        num = int(input(f"Introduce un número impar ({len(numeros)+1}/10): "))
        if num % 2 != 0:  # comprobamos que sea impar
            numeros.append(num)
        else:
            print("Ese número no es impar. Intenta de nuevo.")
    print("Lista de impares:", numeros)


# --------------------
# Ejercicio 4
# --------------------
def ejercicio4():
    numeros = []
    while len(numeros) < 10:
        num = int(input(f"Introduce un número impar ({len(numeros)+1}/10): "))
        if num % 2 != 0:
            numeros.append(num)

    # Mostramos un menú con varias opciones
    while True:
        print("\n¿Qué desea hacer con la lista?")
        print("1. Sumatorio")
        print("2. Media")
        print("3. Máximo")
        print("4. Mínimo")
        print("0. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            print("Sumatorio:", sum(numeros))
        elif opcion == 2:
            print("Media:", sum(numeros) / len(numeros))
        elif opcion == 3:
            print("Máximo:", max(numeros))  # max() devuelve el mayor de la lista
        elif opcion == 4:
            print("Mínimo:", min(numeros))  # min() devuelve el menor de la lista
        elif opcion == 0:
            break
        else:
            print("Opción no válida.")


# --------------------
# Ejercicio 5 (con funciones)
# --------------------
# Definimos funciones para cada operación
def sumatorio(lista): return sum(lista)
def media(lista): return sum(lista) / len(lista)
def maximo(lista): return max(lista)
def minimo(lista): return min(lista)

def ejercicio5():
    numeros = []
    while len(numeros) < 10:
        num = int(input(f"Introduce un número impar ({len(numeros)+1}/10): "))
        if num % 2 != 0:
            numeros.append(num)

    while True:
        print("\n¿Qué desea hacer con la lista?")
        print("1. Sumatorio")
        print("2. Media")
        print("3. Máximo")
        print("4. Mínimo")
        print("0. Salir")

        opcion = int(input("Elige una opción: "))

        # Llamamos a las funciones en lugar de repetir código
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


# --------------------
# Ejercicio 6 (Criptógrafo)
# --------------------
class Criptografo:
    # Cada caracter se convierte en su código ASCII con ord()
    # y se desplaza +1 o -1, para luego volver a texto con chr()

    def encriptar(self, txt):
        return "".join([chr(ord(c)+1) for c in txt])

    def desencriptar(self, txt):
        return "".join([chr(ord(c)-1) for c in txt])

def ejercicio6():
    c = Criptografo()
    texto = input("Introduce un texto para encriptar: ")
    encriptado = c.encriptar(texto)
    desencriptado = c.desencriptar(encriptado)
    print("Texto original:", texto)
    print("Encriptado:", encriptado)
    print("Desencriptado:", desencriptado)


# --------------------
# Ejercicio 7 (Clase Persona)
# --------------------
class Persona:
    # Constantes para sexo y estados del IMC
    HOMBRE = "H"
    MUJER = "M"
    IMC_BAJO = -1
    IMC_IDEAL = 0
    IMC_SOBREPESO = 1

    def __init__(self, nombre="", edad=0, sexo=HOMBRE, peso=0, altura=0):
        # Atributos privados (empiezan con __)
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__generaDNI()  # se genera automáticamente

    def calcularIMC(self):
        # Fórmula del índice de masa corporal
        imc = self.__peso / (self.__altura ** 2)
        if imc < 20:
            return Persona.IMC_BAJO
        elif 20 <= imc <= 25:
            return Persona.IMC_IDEAL
        else:
            return Persona.IMC_SOBREPESO

    def esMayorDeEdad(self):
        return self.__edad >= 18

    def __generaDNI(self):
        # Generamos un número aleatorio de 8 cifras
        numero = random.randint(10000000, 99999999)
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = letras[numero % 23]  # algoritmo oficial
        return f"{numero}{letra}"

    def toString(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Sexo: {self.__sexo}, Peso: {self.__peso}, Altura: {self.__altura}, DNI: {self.__dni}"

    # Métodos set (modifican los atributos desde fuera de la clase)
    def setNombre(self, nombre): self.__nombre = nombre
    def setEdad(self, edad): self.__edad = edad
    def setSexo(self, sexo): self.__sexo = sexo
    def setPeso(self, peso): self.__peso = peso
    def setAltura(self, altura): self.__altura = altura


# --------------------
# Ejercicio 8
# --------------------
def ejercicio8():
    # Creamos 3 personas con diferentes características
    p1 = Persona("Ana", 25, Persona.MUJER, 55, 1.65)
    p2 = Persona("Luis", 17, Persona.HOMBRE, 70, 1.75)
    p3 = Persona("Marta", 30, Persona.MUJER, 90, 1.60)

    personas = [p1, p2, p3]

    for p in personas:
        imc = p.calcularIMC()
        if imc == Persona.IMC_BAJO:
            print(p.toString(), "→ Por debajo del peso ideal")
        elif imc == Persona.IMC_IDEAL:
            print(p.toString(), "→ En el peso ideal")
        else:
            print(p.toString(), "→ Con sobrepeso")

        print("Mayor de edad:", p.esMayorDeEdad())
        print()


# --------------------
# Menú Principal
# --------------------
def main():
    while True:
        # Menú principal con todos los ejercicios
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7 (solo definición de clase)")
        print("8. Ejercicio 8")
        print("0. Salir")

        opcion = input("Selecciona un ejercicio: ")

        if opcion == "1": ejercicio1()
        elif opcion == "2": ejercicio2()
        elif opcion == "3": ejercicio3()
        elif opcion == "4": ejercicio4()
        elif opcion == "5": ejercicio5()
        elif opcion == "6": ejercicio6()
        elif opcion == "7": print("Clase Persona definida. Se usa en el Ejercicio 8.")
        elif opcion == "8": ejercicio8()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

# Punto de entrada del programa
# Ese bloque es una puerta de entrada al programa. Garantiza que main() solo se ejecute cuando corresponde,
# y evita que se dispare por accidente si importas el archivo en otro lado.
if __name__ == "__main__":
    main()
