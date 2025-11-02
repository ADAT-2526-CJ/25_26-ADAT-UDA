"""
Tests unitarios para el ejercicio 3.
"""

import pytest
import sys
from pathlib import Path

# Añadir el directorio src al path de forma más robusta
src_path = str(Path(__file__).parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from ejercicio3_generar_listas import generar_lista, guardar_lista
from ejercicio3_comparar_listas import cargar_lista, calcular_promedio_diferencias

@pytest.fixture
def temp_files(tmp_path):
    """Fixture para crear archivos temporales."""
    lista1_path = tmp_path / "test_lista1.pkl"
    lista2_path = tmp_path / "test_lista2.pkl"
    return lista1_path, lista2_path

def test_generar_lista():
    """Prueba la generación de lista aleatoria."""
    lista = generar_lista()
    assert len(lista) == 1000
    assert all(-100 <= x <= 100 for x in lista)

def test_guardar_y_cargar_lista(temp_files):
    """Prueba el guardado y carga de una lista."""
    lista1_path, _ = temp_files
    lista_original = [1.0, 2.0, 3.0]
    
    # Guardar lista
    assert guardar_lista(lista1_path, lista_original)
    
    # Cargar y verificar
    lista_cargada = cargar_lista(lista1_path)
    assert lista_cargada == lista_original

def test_calcular_promedio_diferencias(temp_files):
    """Prueba el cálculo del promedio de diferencias."""
    lista1_path, lista2_path = temp_files
    
    # Crear listas de prueba
    lista1 = [1.0, 2.0, 3.0]
    lista2 = [2.0, 4.0, 6.0]
    
    # Guardar listas
    guardar_lista(lista1_path, lista1)
    guardar_lista(lista2_path, lista2)
    
    # Calcular y verificar promedio usando las rutas de prueba
    promedio = calcular_promedio_diferencias(lista1_path, lista2_path)
    assert promedio is not None
    assert promedio == 2.0  # La diferencia es siempre 2