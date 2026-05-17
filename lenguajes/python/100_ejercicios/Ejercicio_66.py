"""
Problema  : Crear una función para calcular el promedio de una lista de números.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas, estadistica, agregacion, manejo-errores
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Calcular el promedio (media aritmética) de una lista de números usando
      la fórmula: promedio = suma_total / cantidad_elementos.
    - Utilizar `sum()` para obtener el total y `len()` para contar elementos.
    - Implementar validación defensiva: lanzar `ValueError` si la lista está
      vacía, previniendo división por cero.
    - Demuestra el patrón de "función robusta" que valida precondiciones.

Complejidad: Tiempo O(n) | Espacio O(1)
    - Donde n es la cantidad de elementos en la lista.
    - `sum()` recorre la lista una vez; `len()` es O(1) en Python.
    - El espacio es constante; no se acumulan estructuras adicionales.

Casos límite:
    - Lista vacía: `len(lista) == 0` → lanza `ValueError` (previene 0/0).
    - Un elemento: promedio es ese elemento mismo.
    - Números negativos: se promedian correctamente.
    - Ceros: promedios se calculan correctamente (un promedio puede ser 0).
    - Números muy grandes: posible overflow en suma, pero Python maneja ints
      arbitrarios; floats podrían saturarse.

Casos de uso:
  - Cálculo de calificaciones promedio en sistemas educativos.
  - Promedios de mediciones en sensores/experimentos.
  - Análisis de datos simples, estadísticas en reportes.
  - Base para cálculos más complejos (desviación estándar, varianza).

Revisión:
    - 2026-05-13: Encabezado expandido con validación y casos de uso.
"""
def promedio(lista: list[float]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista (list[float]): Una lista de números.

    Returns:
        float: El promedio de los números en la lista, calculado como la suma de los elementos dividida por la cantidad de elementos.
    Raises:
        ValueError: Si la lista está vacía, se lanza una excepción para evitar la división por cero.
    """
    if len(lista) == 0:  # Pequeña validación para evitar división por cero
        raise ValueError("La lista no puede estar vacía.")
    return sum(lista) / len(lista)


def main():
    """plantilla base"""
    lista_numeros: list[float] = [10, 20, 30, 40, 50]
    print(f"El promedio de la lista de numeros es: {promedio(lista_numeros)}")

if __name__ == '__main__':
    main()
