"""
Tests unitarios para el ejercicio 4 (actualizado).
"""
import sys
from pathlib import Path
from decimal import Decimal
import pytest

# Añadir el directorio src al path (hacerlo antes de importar los módulos del proyecto)
src_path = str(Path(__file__).parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from ejercicio4_crear_bd_libros import guardar_libros, Libro
from ejercicio4_analizar_descuentos import cargar_libros, libro_mayor_descuento

@pytest.fixture
def ejemplo_libros():
    return [
        Libro(
            nombre="Libro 1",
            autor="Autor 1",
            precio=Decimal("100.0"),
            precio_descuento=Decimal("80.0"),
            paginas=200
        ),
        Libro(
            nombre="Libro 2",
            autor="Autor 2",
            precio=Decimal("50.0"),
            precio_descuento=Decimal("25.0"),
            paginas=150
        )
    ]

@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "test_libros.txt"

def test_guardar_y_cargar_libros(ejemplo_libros, temp_file):
    assert guardar_libros(ejemplo_libros, temp_file, modo='w')
    libros_cargados = cargar_libros(temp_file)
    assert libros_cargados is not None
    assert len(libros_cargados) == len(ejemplo_libros)
    assert libros_cargados[0]["nombre"] == ejemplo_libros[0].nombre

def test_libro_mayor_descuento(ejemplo_libros):
    libros_dicts = [lib.to_dict() for lib in ejemplo_libros]
    resultado = libro_mayor_descuento(libros_dicts)
    assert resultado is not None
    libro, descuento = resultado
    assert libro["nombre"] == "Libro 2"
    assert abs(descuento - 50.0) < 0.01

def test_archivo_no_existe():
    assert cargar_libros(Path("no_existe.txt")) is None

def test_lista_vacia():
    assert libro_mayor_descuento([]) is None