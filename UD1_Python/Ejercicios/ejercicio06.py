"""
Ejercicio 6 _ Criptografía
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Crea una clase Criptográfo que contenga dos métodos: encriptar y desencriptar. Los dos
métodos recibirán un texto y devolverán otro texto. El funcionamiento de los métodos es el siguiente:
◦ encriptar(txt): El texto recibido se encriptará sustituyendo cada uno de los
caracteres por el siguiente caracter según su valor ASCII.
◦ desencriptar(txt): Realizará la acción inversa al metodo anterior, es decir sustituirá
cada carácter por el anterior según su valor ASCII.
Nota: Para realizar este ejercicio son muy útiles las funciones ord() y chr().

"""

def pedir_texto():
    """
    Pide al usuario un texto.

    Returns:
        str: El texto introducido por el usuario.
    """
    return input("Introduce un texto: ")


class Criptografo:
    """
    Clase que permite encriptar y desencriptar textos usando el desplazamiento ASCII.
    """
    def encriptar(self, texto):
        """
        Encripta el texto recibido sustituyendo cada carácter por el siguiente según su valor ASCII.
        Args:
            texto (str): El texto a encriptar.
        Returns:
            str: El texto encriptado.
        """
        
        texto_encriptado = ""
        for char in texto:
            texto_encriptado += chr(ord(char) + 1)
        return texto_encriptado

    def desencriptar(self, texto):
        """
        Desencripta el texto recibido sustituyendo cada carácter por el anterior según su valor ASCII.
        Args:
            texto (str): El texto a desencriptar.
        Returns:
            str: El texto desencriptado.
        """
        texto_desencriptado = ""
        for char in texto:
            texto_desencriptado += chr(ord(char) - 1)
        return texto_desencriptado

def main():
    """
    Función principal que ejecuta el programa.
    Args:
        None.
    Returns:
        None.
    """
    cripto = Criptografo()
    while True:
        texto = pedir_texto()
        print("Texto introducido:", texto)

        print("\nSelecciona una acción ---")
        print("1. Encriptar")
        print("2. Desencriptar")
        print("0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            print("\nTexto encriptado:", cripto.encriptar(texto),"\n")
        elif opcion == "2":
            print("\nTexto desencriptado:", cripto.desencriptar(texto),"\n")
        elif opcion == "0":
            print("Saliendo del programa...\n")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    main()
