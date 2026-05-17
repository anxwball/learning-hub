"""
Problema  : Filtrar elementos que sean listas.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, filter, verificación-de-tipos
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `filter()` con `isinstance()` para seleccionar solo elementos
      que sean listas de una colección de tipos mixtos.
    - Demuestra verificación de tipo con `isinstance()` integrada en
      `filter()`, útil para procesamiento heterogéneo de datos.

Complejidad: Tiempo O(n) | Espacio O(k)
    - El tiempo es lineal, verificando el tipo de cada uno de los n elementos.
    - El espacio es O(k), donde k es el número de listas encontradas.

Casos límite:
    - Sin listas: [1, "Hola", 3.14] -> []
    - Solo listas: [[1, 2], [3, 4]] -> [[1, 2], [3, 4]]
    - Listas anidadas: [[[1, 2]], [3, 4]] -> [[[1, 2]], [3, 4]]
    - Listas vacías: [[], [1]] -> [[], [1]]

Casos de uso:
  - Separación de tipos: procesar solo listas de datos heterogéneos.
  - Limpieza de datos: descartar valores que no son colecciones.
  - Análisis de estructuras: identificar subarreglos en datos JSON.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Filtrar solo elementos que sean listas.

    Aplica filter() con isinstance() para extraer solo las listas
    de una colección que contiene múltiples tipos de datos.

    Returns:
        None
    """
    lista: list = [1, "Hola", [1, 2, 3], {"nombre": "Juan"}, (4, 5), 3.14, ['a', 'b']]
    listas_filtradas: list = list(filter(lambda x: isinstance(x, list), lista))
    print(f"Lista original: {lista}")
    print(f"Elementos que son listas: {listas_filtradas}")

if __name__ == '__main__':
    main()
