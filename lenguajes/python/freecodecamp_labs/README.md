# FreeCodeCamp Labs (Python)

---

Breve descripción: Conjunto de labs y ejercicios tomados de FreeCodeCamp: Python Certification implementados en Python. Cada ejercicio vive en su propia subcarpeta con un `main.py` como punto de entrada y un `README.md` explicativo.

## Rol y alcance

- Rol: Colaborador / Mantenedor
- Alcance: Colección de ejercicios/labs independientes (mini-ejercicios para práctica y referencia)

## Contexto

- Fuente: FreeCodeCamp (adaptaciones en Python)
- Etiquetas: python, ejercicios, freecodecamp, labs

## Stack tecnológico

- Lenguajes: Python 3.8+
- Frameworks: Ninguno (scripts autónomos)
- Datos: Archivos de entrada/salida simples cuando aplica

## Qué incluye

- Puntos de entrada: `main.py` en cada subcarpeta
- Documentación por ejercicio: `README.md` en cada subcarpeta

### Subcarpetas incluidas

- [lenguajes/python/freecodecamp_labs/debug_isbn_validator/README.md](lenguajes/python/freecodecamp_labs/debug_isbn_validator/README.md) — Ejercicio `debug_isbn_validator` (`main.py`).
- [lenguajes/python/freecodecamp_labs/apply_discount_func/README.md](lenguajes/python/freecodecamp_labs/apply_discount_func/README.md) — Ejercicio `apply_discount_func` (`main.py`).
- [lenguajes/python/freecodecamp_labs/number_pattern_generator/README.md](lenguajes/python/freecodecamp_labs/number_pattern_generator/README.md) — Ejercicio `number_pattern_generator` (`main.py`).
- [lenguajes/python/freecodecamp_labs/rpg_character/README.md](lenguajes/python/freecodecamp_labs/rpg_character/README.md) — Ejercicio `rpg_character` (`main.py`).
- [lenguajes/python/freecodecamp_labs/travel_weather_planner/README.md](lenguajes/python/freecodecamp_labs/travel_weather_planner/README.md) — Ejercicio `travel_weather_planner` (`main.py`).
- [lenguajes/python/freecodecamp_labs/user_config_manager/README.md](lenguajes/python/freecodecamp_labs/user_config_manager/README.md) — Ejercicio `user_config_manager` (`main.py`).
- [lenguajes/python/freecodecamp_labs/planet_class/README.md](lenguajes/python/freecodecamp_labs/planet_class/README.md) — Ejercicio `planet_class` (`main.py`).

## Cómo ejecutar (local)

1. Requisitos

- Python 3.11 o superior

1. Configuración (Windows - PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # opcional: si la subcarpeta lo incluye
python main.py
```

Unix / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # opcional
python3 main.py
```

> Nota: ejecutar los comandos dentro de la subcarpeta del ejercicio que se desea probar.

## Tests

Actualmente no hay una suite de tests centralizada. Si un ejercicio incluye pruebas, su `README.md` indicará cómo ejecutarlas.

## Ejemplos

- Ver los `README.md` individuales para ejemplos concretos de entrada/salida y casos de uso por ejercicio.

## Notas

- Mantener cada ejercicio independiente y autocontenido facilita la revisión y la ejecución.
- Para agregar un nuevo ejercicio: crear subcarpeta con `main.py`, `README.md` (siguiendo [docs/PROJECT_README_TEMPLATE.md](../../../../docs/PROJECT_README_TEMPLATE.md)) y opcionalmente `requirements.txt` y tests.

## Última actualización

2026-05-23
