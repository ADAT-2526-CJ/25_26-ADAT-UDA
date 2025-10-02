# Práctica 1 - Algoritmo de Vigenère en Python

Este proyecto implementa el algoritmo de **cifrado y descifrado de Vigenère** en Python.  
Se puede usar tanto con textos como con ficheros.

## Estructura del proyecto
```
Practica_Vigenere/
├── data/                # Archivos de entrada/salida (mensaje.txt, etc.)
├── src/                 # Código fuente (aquí va tu implementación)
│   └── vigenere.py
├── tests/               # Tests oficiales (no modificar)
│   └── test_vigenere.py
├── requirements.txt     # Dependencias específicas de esta práctica
├── setup.py             # (opcional) configuración como paquete
└── README.md
```

---

## Instalación de dependencias

Cada práctica tiene su propio `requirements.txt` para mantener las dependencias aisladas.  
Ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará al menos:

- `pytest` → para ejecutar tests.  
- `pylint` → para analizar calidad y estilo del código.

---

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

---

## Cómo ejecutar los tests

Ejecuta los tests oficiales desde la raíz de la práctica:

```bash
PYTHONPATH=src pytest -v tests
```

- `PYTHONPATH=src` asegura que el código dentro de `src/` se pueda importar en los tests.  
- Los tests validan tanto la **funcionalidad** de tu código como algunos aspectos de **documentación**.

---

## Análisis estático (linting)

Puedes ejecutar pylint para comprobar estilo y errores comunes en tu código:

```bash
pylint src/*.py
```

En GitHub Actions el `pylint` se ejecuta automáticamente.
Los tests (`pytest`) sí deben pasar correctamente.

---

## Recomendaciones de entrega

1. Implementa tu código únicamente en la carpeta `src/`.  
2. No modifiques los tests oficiales.  
3. Asegúrate de que al menos todos los tests de `pytest` pasen correctamente antes de subir.  
4. Revisa las advertencias de `pylint`.
5. Haz commits frecuentes y claros para que se pueda seguir tu progreso.  

---

## Integración Continua (CI)

Este proyecto incluye un workflow de GitHub Actions que:  
- Instala dependencias de `requirements.txt`.  
- Ejecuta `pylint` sobre tu código en `src/`.  
- Ejecuta los tests oficiales con `pytest`.  
- Copia automáticamente los tests desde el repositorio central si no estás en este repo.  

De este modo, tendrás feedback inmediato de si tu práctica funciona correctamente.



## Nota
Este proyecto es únicamente educativo. El algoritmo de Vigenère no es seguro para usos reales de criptografía.
