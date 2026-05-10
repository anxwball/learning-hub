"""
Problema  : Ordenar una lista de números de menor a mayor.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas, ordenamiento
Fecha     : 2026-05-09
Estado    : resuelto

Enfoque:
        - Crear una lista de enteros, aplicar el método `sort()` para ordenarla
            de forma ascendente y mostrar el resultado.
        - Se usa ordenamiento in-place para introducir el comportamiento del
            método sobre listas mutables.

Complejidad: Tiempo O(n log n) | Espacio O(1)
        - `list.sort()` usa Timsort con coste promedio y peor caso O(n log n).
            Opera in-place; el espacio auxiliar adicional es acotado para este uso.

Casos límite:
        - Lista vacía o con un solo elemento: el resultado permanece válido sin
            cambios visibles.
        - Elementos repetidos: se conservan y quedan agrupados según el orden.
        - Para mezclar tipos no comparables (por ejemplo, `int` y `str`) se
            produciría `TypeError`.

Casos de uso:
    - Ordenar resultados de búsqueda, rankings o catálogos.
    - Preparar datos para reportes o listas de prioridad.
    - Estandarizar secuencias antes de exportarlas.

Revisión:
        - 2026-05-09: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Ordenar una lista de números y mostrarla por consola.

    Define una lista de enteros, la ordena en orden ascendente con `sort()` y
    muestra el resultado final.

    Returns:
        None
    """
    lista: list[int] = [812, 3231, 53, 1, 0, 965]
    lista.sort()

    print(f"Lista ordenada: {lista}")

if __name__ == '__main__':
    main()
