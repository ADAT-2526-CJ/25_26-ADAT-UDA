import pytest
from pathlib import Path
from src.ejercicio1 import rnd_word

@pytest.fixture
def temp_files(tmp_path):
    input_file = tmp_path / "test_input.txt"
    output_file = tmp_path / "test_output.txt"
    return input_file, output_file

def test_archivo_no_existe():
    assert rnd_word("archivo_no_existe.txt", "salida.txt") is None

def test_archivo_vacio(temp_files):
    input_file, output_file = temp_files
    input_file.write_text("")
    assert rnd_word(input_file, output_file) is True
    assert output_file.read_text() == ""

def test_proceso_exitoso(temp_files):
    input_file, output_file = temp_files
    input_file.write_text("palabra1 palabra2\npalabra3 palabra4")
    assert rnd_word(input_file, output_file) is True
    assert len(output_file.read_text().splitlines()) == 2