# Clase Planet

---

Este laboratorio crea una clase `Planet` con validaciones básicas, un método para describir su órbita y una representación textual para pruebas y demostración.

## Rol y alcance

- Rol: Colaborador / Mantenedor
- Alcance: Laboratorio independiente de clases en Python

## Contexto

- Fuente: FreeCodeCamp (Python Certification)
- Etiquetas: python, freecodecamp, labs, poo, clases, validacion

## Stack tecnológico

- Lenguajes: Python 3.8+
- Frameworks: Ninguno
- Datos: Objetos en memoria y salida estándar

## Qué incluye

- `main.py`: clase `Planet`, validaciones, método `orbit()` y tres instancias de demostración.
- `README.md`: enunciado, reglas de prueba y ejemplos esperados.

## Cómo ejecutar (local)

1. Requisitos

- Python 3.8 o superior

1. Configuración

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

1. Ejecutar

```powershell
python main.py
```

## Tests

El laboratorio se valida con pruebas automáticas que verifican la clase, las excepciones, el método `orbit()` y la representación `__str__()`.

## Ejemplos

- `Planet("The Earth", "Rocky", "The Sun")` -> `Planet: The Earth | Type: Rocky | Star: The Sun`
- `Planet("Mars", "Rocky", "The Sun").orbit()` -> `Mars is orbiting around The Sun...`
- `Planet(1, "Rocky", "The Sun")` -> `TypeError: name, planet type, and star must be strings`
- `Planet("", "Rocky", "The Sun")` -> `ValueError: name, planet_type, and star must be non-empty strings`

## Notas

- Los mensajes de error deben mantenerse exactos para que coincidan con las pruebas.
- El módulo incluye una demostración ejecutable protegida por el guard `if __name__ == "__main__":`.

## Última actualización

2026-05-23
