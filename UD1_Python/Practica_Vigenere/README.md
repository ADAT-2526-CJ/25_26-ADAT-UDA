# Práctica 1 - Algoritmo de Vigenère en Python

Este proyecto implementa el algoritmo de **cifrado y descifrado de Vigenère** en Python.  
Se puede usar tanto con textos como con ficheros.

## Estructura del proyecto
```
src/vigenere.py     # Código principal del algoritmo
tests/test_vigenere.py # Pruebas unitarias
data/               # Archivos de ejemplo (mensaje original, cifrado y descifrado)
```

## Uso
Ejecutar el programa principal:

```bash
python src/vigenere.py
```

Esto:
1. Cifra el texto definido en el código.
2. Descifra el texto para comprobar el funcionamiento.
3. Cifra y descifra un fichero `data/mensaje.txt`.

El resultado se guarda en:
- `data/mensaje_cifrado.txt`
- `data/mensaje_descifrado.txt`

## Pruebas
Las pruebas están implementadas con `pytest`.  
Ejecutarlas con:

```bash
pytest
```

## Nota
Este proyecto es únicamente educativo. El algoritmo de Vigenère no es seguro para usos reales de criptografía.
