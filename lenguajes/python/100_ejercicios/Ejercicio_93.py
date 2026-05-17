"""
Problema  : Filtrar números no negativos de una lista usando filter().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, filter, validación
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `filter()` para seleccionar solo números >= 0 de una lista
      que contiene positivos, negativos y cero.
    - Demuestra filtrado de valores basado en rangos, combinando
      números positivos con cero (no negativos).

Complejidad: Tiempo O(n) | Espacio O(k)
    - El tiempo es lineal, comparando cada uno de los n elementos.
    - El espacio es O(k), donde k es el número de elementos no negativos.

Casos límite:
    - Todos negativos: [-5, -3, -1] -> []
    - Todos positivos: [1, 2, 3] -> [1, 2, 3]
    - Solo cero: [0] -> [0] (0 es no negativo)
    - Mixtos: [-3, -1, 0, 1, 3] -> [0, 1, 3]

Casos de uso:
  - Validación: aceptar solo valores permitidos (no deudas, etc.).
  - Procesamiento de sensores: descartar lecturas anómalas negativas.
  - Análisis financiero: filtrar solo transacciones positivas o neutras.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Filtrar números no negativos usando filter().

    Aplica filter() con una función lambda que verifica x >= 0,
    obteniendo una lista con solo números no negativos.

    Returns:
        None
    """
    lista_numeros: list[int] = [-3, -2, -1, 0, 1, 2, 3]
    numeros_positivos: list[int] = list(filter(lambda x: x >= 0, lista_numeros))
    print(f"Lista original: {lista_numeros}")
    print(f"Números no negativos: {numeros_positivos}")

if __name__ == '__main__':
    main()
