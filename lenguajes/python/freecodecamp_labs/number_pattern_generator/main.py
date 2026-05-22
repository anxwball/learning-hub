"""
Problema  : Generador de patrones numéricos.
Fuente    : freeCodeCamp Labs
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : fundamentos, bucles, cadenas
Fecha     : 2026-05-21
Estado    : resuelto

Enfoque:
    - Construir una lista de números en formato texto con un bucle `for`.
    - Unir los elementos con espacios para cumplir el formato solicitado.
    - Validar tipo y rango antes de generar la secuencia.

Complejidad: Tiempo O(n) | Espacio O(n)

Casos límite:
    - `n` no entero: retorna `Argument must be an integer value.`
    - `n <= 0`: retorna `Argument must be an integer greater than 0.`

Casos de uso:
    - Generar secuencias didácticas para ejercicios introductorios.
    - Probar validaciones de entrada en funciones puras.

Revisión:
    - 2026-05-21: Documentación y estructura alineadas al estándar del módulo.
"""


def number_pattern(n: object) -> str:
    """Generar números de 1 a n separados por espacios.

    Args:
        n: Valor a validar para generar la secuencia numérica.

    Returns:
        Cadena con números separados por espacios, o un mensaje de error
        cuando la entrada no es válida.
    """
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    parts: list[str] = []
    for i in range(1, n + 1):
        parts.append(str(i))

    return " ".join(parts)


def main() -> None:
    """Ejecutar una demostración mínima del laboratorio."""
    print(number_pattern('1'))
    print(number_pattern(0))
    print(number_pattern(4))
    print(number_pattern(12))


if __name__ == "__main__":
    main()