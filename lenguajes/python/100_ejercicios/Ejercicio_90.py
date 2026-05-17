"""
Problema  : Duplicar cada elemento de una lista usando map() y lambda.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, map, lambda
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Combinar `map()` con una función lambda para duplicar (multiplicar por 2)
      cada elemento de una lista simultáneamente.
    - Demuestra cómo lambda se usa directamente con map() sin definir
      una función separada.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, procesando cada uno de los n elementos.
    - El espacio es lineal, creando una nueva lista de n elementos duplicados.

Casos límite:
    - Lista vacía: [] -> []
    - Un elemento: [5] -> [10]
    - Ceros: [0] -> [0]
    - Números negativos: [-3, -5] -> [-6, -10]

Casos de uso:
  - Escalado de valores: multiplicar precios, distancias o medidas.
  - Transformación de datos: normalizar o ajustar rangos.
  - Operaciones vectoriales rápidas.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Duplicar elementos de una lista usando map() y lambda.

    Aplica una función lambda que multiplica cada elemento por 2 mediante
    map(), demostrando transformación de colecciones sin bucles.

    Returns:
        None
    """
    lista: list[int] = [1, 2, 3, 4, 5]
    lista_duplicada: list[int] = list(map(lambda x: x * 2, lista))
    print(f"Lista original: {lista}")
    print(f"Lista duplicada: {lista_duplicada}")

if __name__ == '__main__':
    main()
