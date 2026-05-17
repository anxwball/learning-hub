"""
Problema  : Listar 10 números y calcular el cuadrado de cada uno con for.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, transformacion, operadores
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Iterar sobre una lista predefinida y aplicar una transformación matemática
      (elevar al cuadrado) a cada elemento.
    - Demuestra cómo combinar iteración con operaciones aritméticas para
      procesar y mostrar datos transformados.
    - Introduce el concepto de aplicar la misma operación a múltiples elementos
      de una colección.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal; se realiza una operación por cada elemento (10 elementos).
    - El espacio es lineal para almacenar la lista de 10 números.

Casos límite:
    - Números negativos: el cuadrado resultará en valores positivos.
    - Números muy grandes: Python maneja cálculos de precisión arbitraria.
    - Listas de diferentes tamaños: la lógica es general para cualquier cantidad
      de números.

Casos de uso:
  - Normalización de datos aplicando transformaciones uniformes.
  - Cálculo de métricas cuadráticas (varianza, desviación estándar).
  - Procesamiento por lotes de números en operaciones matemáticas.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Calcular y mostrar el cuadrado de los números 1 al 10.

    Define una lista de 10 números enteros (1 a 10), itera sobre cada uno,
    calcula su cuadrado usando `pow(n, 2)` y lo muestra con un mensaje
    descriptivo. Ejemplifica transformación de datos mediante iteración.

    Returns:
        None
    """
    print("Cuadrados de los números 1 al 10:\n")
    numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for numero in numeros:
        cuadrado: int = pow(numero, 2)
        print(f"El cuadrado de {numero} es: {cuadrado}")


if __name__ == '__main__':
    main()
