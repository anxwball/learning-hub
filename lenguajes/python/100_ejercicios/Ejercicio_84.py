"""
Problema  : Obtener el cuadrado de la suma de dos listas de números utilizando map().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, map, operaciones-vectoriales
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `map()` con múltiples iterables para aplicar una función a pares
      de elementos de dos listas simultáneamente.
    - Demuestra operaciones vectoriales sin bucles, combinando elementos
      paralelos de dos colecciones.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, donde n es la longitud de las listas.
    - El espacio es lineal, creando una lista resultante con n elementos.

Casos límite:
    - Listas vacías: [], [] -> []
    - Listas de diferente longitud: map() se detiene en la más corta
    - Números negativos: [-1, 2], [3, -2] -> [4, 0]
    - Valores cero: [0, 1], [0, 1] -> [0, 4]

Casos de uso:
  - Cálculos vectoriales: operaciones elemento-a-elemento en 2 arrays.
  - Física: aplicar fórmulas a pares de magnitudes simultáneamente.
  - Datasets: normalización o transformación paralela de columnas.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""
def suma_cuadrados(a: int, b: int) -> int:
    """Calcula el cuadrado de la suma de dos números.

    Args:
        a (int): El primer número.
        b (int): El segundo número.
    
    Returns:
        int: El resultado de elevar al cuadrado la suma de a y b.
    """
    return pow(a + b, 2)


def main() -> None:
    """Calcular el cuadrado de la suma de elementos paralelos.

    Usa `map()` con dos listas para aplicar suma_cuadrados() a pares
    de elementos, demostrando operaciones vectoriales.

    Returns:
        None
    """
    lista1: list[int] = [1, 2, 3]
    lista2: list[int] = [4, 5, 6]
    resultado: list[int] = list(map(suma_cuadrados, lista1, lista2))
    print(f"Listas originales: {lista1} y {lista2}")
    print(f"Resultado (suma al cuadrado): {resultado}")
    

if __name__ == '__main__':
    main()
