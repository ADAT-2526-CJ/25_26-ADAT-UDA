# Tests automáticos local – UD1 (Python)

Este repositorio incluye los ejercicios de la **UD1 de Python** junto con **agunos tests automáticos** para validar tu código y obtener **feedback inmediato**.

---

## 1) Requisitos previos

Necesitas:

- **Python 3.11** o superior.  
- El paquete [`pytest`](https://docs.pytest.org/).

Instalación recomendada:

```bash
pip install pytest
```

Si `pip` no funciona, prueba:

```bash
python -m pip install pytest
```

> 💡 Recomendación: crea un entorno virtual para aislar dependencias:  
> ```bash
> python -m venv venv
> # Windows
> .\venv\Scripts\activate
> # macOS/Linux
> source venv/bin/activate
> pip install pytest
> ```

---

## 2) Importancia de los tests

En programación profesional, los **tests automáticos** son una práctica esencial porque:

- **Verifican la corrección**: comprueban automáticamente que el programa funciona como se espera.  
- **Facilitan el mantenimiento**: permiten detectar rápidamente si un cambio rompe el código.  
- **Aumentan la productividad**: reducen la necesidad de pruebas manuales repetitivas.  
- **Son estándar en la industria**: se usan frameworks como `pytest` (Python), `JUnit` (Java), `NUnit` (C#).  
- **Autoevaluación**: en este curso, además, los tests te proporcionan una **nota objetiva sobre 10**.

---

## 3) Organización de los tests

La carpeta `UD1_Python/tests/` contiene:

```
UD1_Python/
├── ejercicio6.py
├── ejercicio7.py
├── ejercicio8.py
└── tests/
    ├── test_criptografo.py         # Tests del Ejercicio 6
    ├── test_persona.py             # Tests de los Ejercicios 7–8
```
---

## 4) Cómo ejecutar los tests

Ejecuta **siempre desde la raíz del repositorio** (`25_26-ADAT-XXX`).

### 🔹 Ejercicio 6 – Criptógrafo
```bash
python -m pytest UD1_Python/tests/test_criptografo.py -v 
or
python -m pytest -s UD1_Python/tests/test_criptografo.py -v
```

### 🔹 Ejercicios 7–8 – Persona
```bash
python -m pytest UD1_Python/tests/test_persona.py -v 
or
python -m pytest -s UD1_Python/tests/test_persona.py -v

```
---

## 5) Interpretación del feedback

Durante la ejecución, cada test muestra:

- **verde** → test correcto.  
- **rojo** → test incorrecto.  

---

## 6) Buenas prácticas

- Ejecuta los tests **antes de entregar tu trabajo**.  
- Si un test falla, **lee el mensaje de error**: indica qué parte del programa no cumple lo esperado.  
- Diseña tu código pensando en **casos límite** (entradas vacías, valores extremos, etc.).  
- Itera: corrige → vuelve a ejecutar → valida de nuevo.  
- Versiona con commits claros (`feat: ejercicio7`, `fix: IMC sobrepeso`).

---

**En resumen**:  
Los tests no son un obstáculo, sino una herramienta que te permite **aprender de tus errores**, mejorar la calidad de tu código y adquirir una práctica profesional clave en el desarrollo de software.

# Automatización de tests y revisión de código en GitHub Actions

Este repositorio integra dos tipos de comprobaciones automáticas:

1. **Tests con pytest**: validan la funcionalidad de los ejercicios.  
2. **Linter con pylint**: revisa la documentación (docstrings) y algunas reglas básicas de calidad de código.

---

## 1) Cómo funciona

Cada vez que se hace `git push` o un Pull Request hacia `main`:

- **Pytest** se ejecuta automáticamente sobre los tests de `UD1_Python/tests/`.  
  - Si un test falla, el flujo se marca como fallido y no se puede mergear.  
- **Pylint** revisa el código de `UD1_Python/` usando el archivo de configuración `.pylintrc`.  
  - Señala la ausencia de docstrings o problemas básicos de código.  
  - Este paso se ejecuta en modo "no bloqueante": los avisos aparecen en los logs pero no impiden hacer merge.

---

## 2) Configuración de pylint

El archivo `.pylintrc` está en la raíz del repositorio.  
Se ha configurado para que:

- **Sea obligatorio documentar** módulos, clases y funciones con docstrings (según PEP 257).  
- Revise errores básicos como:
  - Variables definidas pero no usadas.
  - Variables usadas sin definir.
  - Sentencias inútiles.
  - Código duplicado.  
- Ignore convenciones de estilo estrictas (longitud de línea, nombres de variables, etc.).

De esta forma se obtiene una validación **profesional pero manejable**.

---

## 3) Ejecución en local

Puedes ejecutar los mismos análisis que en GitHub Actions en tu ordenador:

```bash
python -m pytest UD1_Python/tests/ -v -s
python -m pylint UD1_Python

