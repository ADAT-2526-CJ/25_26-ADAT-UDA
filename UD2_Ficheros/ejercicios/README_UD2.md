# UD2_Ficheros – Ejercicios de manejo de ficheros en Python

## Descripción general
Colección de ejercicios prácticos sobre lectura/escritura de ficheros en Python.  
Objetivos principales: manejo de rutas, codificaciones, serialización, validación de entradas y pruebas automáticas.

---

## Estructura del proyecto (relevante)
```
UD2_Ficheros/
└── ejercicios/
    ├── data/                # ficheros de ejemplo y salidas
    ├── logs/                # ficheros de log generados por los scripts
    ├── src/                 # código fuente (.py)
    │   ├── ejercicio1.py
    │   ├── ejercicio2.py
    │   ├── ejercicio3_generar_listas.py
    │   ├── ejercicio3_comparar_listas.py
    │   ├── ejercicio4_crear_bd_libros.py
    │   └── ejercicio4_analizar_descuentos.py
    └── tests/               # pruebas unitarias (pytest)
```

---

## Cómo ejecutar
- Ejecutar un script de ejemplo desde la carpeta `ejercicios`:
  ```powershell
  cd path\to\UD2_Ficheros\ejercicios
  python -m src.ejercicio1    # si se usa paquete / ajustar según organización
  # o
  python src\ejercicio1.py
  ```
- Ejecutar tests (desde `ejercicios`):
  ```bash
  python -m pytest -v tests
  ```
- Dependencias opcionales (solo para algunos scripts):
  - tqdm, chardet — instalar solo si se usan funciones de barra de progreso o detección de codificación:
    ```bash
    pip install tqdm chardet
    ```

---

## Buenas prácticas aplicadas en este proyecto
A continuación se resumen las convenciones y decisiones que se han aplicado en los scripts para facilitar mantenimiento, seguridad y pruebas:

- Rutas y ficheros
  - Uso de `pathlib.Path` para manipular rutas (portabilidad Windows/Unix).
  - Definición de constantes para nombres de ficheros y directorios (ej. `DATA_DIR`, `LOG_DIR`, `ARCHIVO_*`).
  - Los scripts crean `data/` y `logs/` si no existen (`Path(...).mkdir(exist_ok=True)`).

- Codificación y I/O
  - Codificación explícita `utf-8` al abrir ficheros.
  - Detección de codificación opcional con `chardet` cuando es necesario (funciones que leen ficheros heterogéneos).
  - Manejo de errores de E/S con logs y flujos de control que evitan excepciones no controladas.

- Logging
  - Uso de `logging` en lugar de `print` para trazabilidad.
  - Configuración para registrar en consola y en fichero (ej. `logs/ejercicioX.log`).
  - Nivel por defecto `INFO`; errores y eventos relevantes se registran con `ERROR/WARNING`.

- Validación y seguridad
  - Validación estricta de entradas (tipos, rangos, expresiones regulares) antes de crear objetos.
  - Uso de `dataclasses` y `Decimal` para datos sensibles (precios) cuando procede.
  - Evitar `eval()` en lectura de datos; preferir `json`, `pickle` (con precaución) o `repr()`/parseo controlado.
  - Para serialización segura de objetos sencillos usar JSON o pickles sólo para datos internos confiables; añadir advertencia en código si se cargan pickles externos.

- Interactividad y modos no interactivos
  - Los prompts interactivos se diseñan con reintentos y logs para evitar fallos por entrada inválida.
  - Las funciones críticas aceptan parámetros como `force` o `modo` para ejecución sin interacción (útil en tests y CI).

- Tipado y documentación
  - Anotaciones de tipos (`typing`) en las funciones públicas.
  - Docstrings claros (propósito, args, returns, raises) en módulos y funciones.
  - Constantes en mayúsculas y agrupadas tras los imports.

- Pruebas
  - Estructura `tests/` con pytest; uso de `tmp_path` para ficheros temporales.
  - Los tests añaden `src` al `sys.path` para importar los módulos cuando no se empaqueta como paquete.
  - Tests verifican comportamiento: I/O, serialización, validación y manejo de errores.

- Linter / formateo
  - `.pylintrc` personalizado: activar reglas necesarias y excluir carpetas `tests` con `ignore` / `ignore-patterns`.
  - Recomendado usar `black` y `isort` para consistencia de estilo.

---

## Puntos clave al escribir código para gestión de ficheros
- Siempre especificar `encoding` al abrir ficheros de texto.
- Evitar asumir que los ficheros existen o que tienen el formato esperado — validar y manejar errores.
- No confiar en pickles procedentes de fuentes no seguras (riesgo de ejecución arbitraria). Si es imprescindible, documentar el riesgo.
- Registrar en log las operaciones de lectura/escritura importantes y cualquier fallo de validación.
- Diseñar funciones para ser reutilizables y testables: separar lógica de negocio de interacción con el usuario.
- Para datos sensibles usar tipos apropiados (`Decimal` para dinero) y límites razonables.
- Añadir modo no interactivo (flags/params) para permitir automatización y pruebas.

---
