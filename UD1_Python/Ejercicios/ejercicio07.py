"""
Ejercicio 7 _ Persona
Alumno/a: Urtzi Diaz Arberas
Unidad Didáctica: UD1 - Python

Módulo que define la clase Persona para gestionar información personal y métodos asociados.

Incluye:
- Generación automática de DNI válido.
- Cálculo del índice de masa corporal (IMC).
- Comprobación de mayoría de edad.
- Métodos para modificar atributos de la persona.

"""
import random

class Persona:
    """Clase que representa a una persona con varios atributos y métodos para manipularlos.
        Atributos:
            __nombre (str): Nombre de la persona.  
            __edad (int): Edad de la persona.
            __dni (str): DNI de la persona, generado automáticamente.
            __sexo (str): Sexo de la persona ('H' para hombre, 'M' para mujer).
            __peso (float): Peso de la persona en kg.
            __altura (float): Altura de la persona en metros.
        Métodos:
            calcularIMC(): Calcula el índice de masa corporal (IMC) y devuelve un valor según el estado del peso.
            esMayorDeEdad(): Indica si la persona es mayor de edad.
            toString(): Devuelve una representación en cadena de todos los atributos de la persona.
            setNombre(nombre): Establece el nombre de la persona.
            setEdad(edad): Establece la edad de la persona.
            setSexo(sexo): Establece el sexo de la persona.
            setPeso(peso): Establece el peso de la persona.
            setAltura(altura): Establece la altura de la persona.
        Constantes:
            HOMBRE (str): Constante para representar el sexo masculino.
            MUJER (str): Constante para representar el sexo femenino.
            IMC_BAJO (int): Constante para indicar bajo peso.
            IMC_IDEAL (int): Constante para indicar peso ideal.
            IMC_SOBREPESO (int): Constante para indicar sobrepeso.
    """
    # Constantes
    SEXO_HOMBRE = 'H'
    SEXO_MUJER = 'M'
    IMC_BAJO = -1
    IMC_IDEAL = 0
    IMC_ALTO = 1
    IMC_SOBREPESO = IMC_ALTO
    LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"


    # Constructor privado
    def __init__(self, nombre="", edad=0, sexo=SEXO_HOMBRE, peso=0.0, altura=0.0):
        """
        Inicializa una nueva instancia de la clase Persona con los atributos proporcionados o sus valores por defecto.
        El DNI se genera automáticamente al crear el objeto.
        Arguments:
            nombre (str): Nombre de la persona. Por defecto es una cadena vacía.
            edad (int): Edad de la persona. Por defecto es 0.
            sexo (str): Sexo de la persona ('H' para hombre, 'M' para mujer). Por defecto es 'H'.
            peso (float): Peso de la persona en kg. Por defecto es 0.0.
            altura (float): Altura de la persona en metros. Por defecto es 0.0.
        Returns:
            None
        """
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.__generaDNI()

    # Método privado para generar un DNI aleatorio
    def __generaDNI(self):
        """
        Genera un DNI aleatorio válido para la persona.
        Utiliza el módulo random para crear un número de 8 cifras y su letra correspondiente.
        Este método es privado y se invoca automáticamente al crear el objeto.
        Arguments:
            None
        Returns:
            str: El DNI generado.
        """
        numero = random.randint(10000000, 99999999)
        letra = self.LETRAS_DNI[numero % 23]
        return f"{numero}{letra}"
    
    def calcularIMC(self):
        """
        Calcula el índice de masa corporal (IMC) y devuelve un valor según el estado del peso.
        Fórmula: IMC = peso / (altura^2)
        Arguments:
            None
        Returns:
            int: -1 si está por debajo del peso ideal, 0 si está en el peso ideal, 1 si tiene sobrepeso.
        Raises:
            ValueError: Si la altura es menor o igual a cero.
        """
        if self.__altura <= 0:
            raise ValueError("La altura debe ser mayor que cero para calcular el IMC.")
        imc = self.__peso / (self.__altura ** 2)
        if imc < 20:
            return self.IMC_BAJO
        elif 20 <= imc <= 25:
            return self.IMC_IDEAL
        else:
            return self.IMC_ALTO

    def esMayorDeEdad(self):
        """
        Indica si la persona es mayor de edad.
        Arguments:
            None
        Returns:
            bool: True si la persona es mayor de edad (edad >= 18), False en caso contrario.
        """
        return self.__edad >= 18
    
    def toString(self):
        """
        Devuelve una representación en cadena de todos los atributos de la persona.
        Arguments:
            None
        Returns:
            str: Una cadena con toda la información de la persona.
        """
        return (f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}, "
                f"Sexo: {self.__sexo}, Peso: {self.__peso} kg, Altura: {self.__altura} m\n")
    
    def setNombre(self, nombre):
        """Establece el nombre de la persona.
        Arguments:
            nombre (str): El nuevo nombre de la persona.
        Returns:
            None
        """
        self.__nombre = nombre
    def setEdad(self, edad):
        """Establece la edad de la persona.
        Arguments:
            edad (int): La nueva edad de la persona.
        Returns:
            None
        """
        self.__edad = edad
    def setSexo(self, sexo):
        """Establece el sexo de la persona.
        Arguments:
            sexo (str): El nuevo sexo de la persona ('H' para hombre, 'M' para mujer).
        Returns:
            None
        """
        self.__sexo = sexo
    def setPeso(self, peso):
        """Establece el peso de la persona.
        Arguments:
            peso (float): El nuevo peso de la persona en kg.
        Returns:
            None
        """
        self.__peso = peso
    def setAltura(self, altura):
        """Establece la altura de la persona.
        Arguments:
            altura (float): La nueva altura de la persona en metros.
        Returns:
            None
        """
        self.__altura = altura 

    def getNombre(self):
        """
        Devuelve el nombre de la persona.
        Returns:
            str: El nombre de la persona.
        """
        return self.__nombre

    def getEdad(self):
        """
        Devuelve la edad de la persona.
        Returns:
            int: La edad de la persona.
        """
        return self.__edad

    def getSexo(self):
        """
        Devuelve el sexo de la persona.
        Returns:
            str: El sexo de la persona ('H' para hombre, 'M' para mujer).
        """
        return self.__sexo

    def getPeso(self):
        """
        Devuelve el peso de la persona.
        Returns:
            float: El peso de la persona en kg.
        """
        return self.__peso

    def getAltura(self):
        """
        Devuelve la altura de la persona.
        Returns:
            float: La altura de la persona en metros.
        """
        return self.__altura
    
    def mostrar_info_persona(self):
        """
        Muestra la información de una persona, incluyendo su estado de peso y si es mayor de edad.
        Args:
            persona (Persona): Objeto Persona.
        Returns:
            None
        """
        imc = self.calcularIMC()
        if imc == self.IMC_BAJO:
            print(f"{self.getNombre()} está por debajo de su peso ideal.")
        elif imc == self.IMC_IDEAL:
            print(f"{self.getNombre()} está en su peso ideal.")
        else:
            print(f"{self.getNombre()} tiene sobrepeso.")

        if self.esMayorDeEdad():
            print(f"{self.getNombre()} es mayor de edad.")
        else:
            print(f"{self.getNombre()} no es mayor de edad.")

        print(self.toString())
