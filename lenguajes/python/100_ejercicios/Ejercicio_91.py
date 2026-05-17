"""
Problema  : Filtrar números pares de una lista usando filter().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, filter, validacion
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `filter()` con una función lambda para seleccionar solo los
      números pares de una lista.
    - Demuestra cómo `filter()` reduce una colección manteniendo solo
      elementos que cumplan una condición, sin bucles explícitos.

Complejidad: Tiempo O(n) | Espacio O(k)
    - El tiempo es lineal, procesando cada uno de los n elementos.
    - El espacio es O(k), donde k es el número de elementos pares resultantes.

Casos límite:
    - Lista vacía: [] -> []
    - Solo impares: [1, 3, 5] -> []
    - Solo pares: [2, 4, 6] -> [2, 4, 6]
    - Incluye cero: [-1, 0, 1] -> [0] (0 es par)

Casos de uso:
  - Selección de registros que cumplen criterios en bases de datos.
  - Procesamiento de datos: filtrar valores válidos de entradas ruidosas.
  - Segmentación: dividir datos en subconjuntos según condiciones.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Filtrar números pares usando filter() con lambda.

    Aplica filter() con una función lambda que retorna True para números
    pares (divisibles entre 2), obteniendo un subconjunto de la lista.

    Returns:
        None
    """
    numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numeros_pares: list[int] = list(filter(lambda x: x % 2 == 0, numeros))
    print(f"Números originales: {numeros}")
    print(f"Números pares: {numeros_pares}")

if __name__ == '__main__':
    main()
