# -*- coding: utf-8 -*-
"""
Autor: Urtzi Díaz
Descripción: Visualiza el contenido de las listas guardadas con pickle
(verifica que tengan 1000 números en el rango -100 a 100).
"""

import os
import pickle


def cargar_lista(path: str):
    """Carga una lista desde un archivo pickle y devuelve su contenido."""
    with open(path, "rb") as f:
        return pickle.load(f)


def mostrar_info_lista(lista, nombre: str):
    """Muestra información resumida de una lista numérica."""
    print(f"\n{nombre}:")
    print(f" - Elementos: {len(lista)}")
    print(f" - Ejemplo de primeros 10: {lista[:10]}")
    print(f" - Rango: {min(lista):.2f} a {max(lista):.2f}")


if __name__ == "__main__":
    # Establece la ruta base al directorio actual del script
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, "..", "data")

    # Rutas absolutas a los archivos pickle
    ruta1 = os.path.join(data_dir, "lista1.pkl")
    ruta2 = os.path.join(data_dir, "lista2.pkl")

    # Verificación de existencia
    if not os.path.exists(ruta1) or not os.path.exists(ruta2):
        print("Error: No se encontraron los archivos lista1.pkl o lista2.pkl en la carpeta /data.")
    else:
        lista1 = cargar_lista(ruta1)
        lista2 = cargar_lista(ruta2)

        mostrar_info_lista(lista1, "Lista 1")
        mostrar_info_lista(lista2, "Lista 2")
