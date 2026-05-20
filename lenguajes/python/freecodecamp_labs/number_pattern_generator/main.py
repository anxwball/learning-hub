"""
Problema : Number Pattern Generator
Fuente   : freeCodeCamp
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : fundamentos, bucles, cadenas
Fecha     : 2026-05-20
Estado    : resuelto

Enfoque:
    Uso de un bucle `for` para construir una lista de strings y unirlos con espacios.

Complejidad: Tiempo O(n) | Espacio O(n)

Casos límite:
    - `n` no entero
    - `n <= 0`

Casos de uso:
    - Generar secuencias numéricas para demostraciones y pruebas.

Revisión:
    - 2026-05-20: Añadido encabezado y refactor PEP8.
"""

def number_pattern(n: int) -> str:
    """Return numbers from 1 to n as a space-separated string.

    Args:
            n: positive integer

    Returns:
            A string with numbers from 1 to n separated by spaces, or an
            error message when the input is invalid.
    """
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    parts = []
    for i in range(1, n + 1):
        parts.append(str(i))

    return " ".join(parts)


if __name__ == "__main__":
    print(number_pattern("1"))
    print(number_pattern(0))
    print(number_pattern(4))
    print(number_pattern(12))