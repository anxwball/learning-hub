# Depurador de validación de ISBN

---

Este laboratorio corrige y valida códigos ISBN-10 e ISBN-13 a partir de una entrada en consola con formato `ISBN,length`.

## Rol y alcance

- Rol: Colaborador / Mantenedor
- Alcance: Laboratorio independiente de depuración en Python

## Contexto

- Fuente: FreeCodeCamp (Python Certification)
- Etiquetas: python, freecodecamp, labs, depuracion, validacion, isbn

## Stack tecnológico

- Lenguajes: Python 3.8+
- Frameworks: Ninguno
- Datos: Entrada por consola y salida estándar

## Qué incluye

- `main.py`: validador ISBN con funciones auxiliares para el cálculo del dígito de control.
- `README.md`: enunciado, pruebas y referencias del laboratorio.

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

El laboratorio se valida con pruebas automáticas. El módulo ya incluye el guard `if __name__ == "__main__":`, así que puede importarse sin ejecutar la demostración.

## Ejemplos

- `1530051126,10` -> `Valid ISBN Code.`
- `9781530051120,13` -> `Valid ISBN Code.`
- `1530051125,10` -> `Invalid ISBN Code.`
- `9781530051120,10` -> `ISBN-10 code should be 10 digits long.`
- `1530051126,13` -> `ISBN-13 code should be 13 digits long.`
- `15-0051126,10` -> `Invalid character was found.`
- `1530051125,9` -> `Length should be 10 or 13.`
- `1530051125,A` -> `Length must be a number.`
- `1530051125` -> `Enter comma-separated values.`

## Notas

- La entrada debe seguir el formato `ISBN,length` sin guiones en el ISBN.
- Para ISBN-10, el dígito de control puede ser un número del 0 al 9 o la letra `X` en mayúsculas.
- Para ISBN-13, el dígito de control siempre es numérico.

## Última actualización

2026-05-23
