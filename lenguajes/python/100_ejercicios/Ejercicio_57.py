"""
Problema  : Imprimir los números del 5 al 1 en orden descendente.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, rango-inverso, paso-negativo
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Iterar en orden descendente utilizando un paso negativo en `range()`.
    - Demuestra que `range()` soporta iteración hacia atrás especificando
      un paso negativo como tercer parámetro.
    - Introduce el concepto de conteo inverso y cómo controlar la dirección
      de iteración.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal en relación al número de iteraciones (5 números).
    - El espacio es constante; solo se utiliza la variable de iteración.

Casos límite:
    - Rango con paso negativo: `range(5, 0, -1)` produce exactamente 5 números
      en orden descendente.
    - Si el paso es -1 pero el inicio es menor que el fin, el rango resulta vacío.
    - Pasos negativos más grandes funcionan correctamente (ej: -2).

Casos de uso:
  - Conteos regresivos (ej: cuentas atrás, timers).
  - Procesamiento de datos en orden inverso.
  - Algoritmos que requieren iteración hacia atrás en secuencias.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Imprimir números del 5 al 1 en orden descendente.

    Utiliza `range(5, 0, -1)` para generar una secuencia descendente
    desde 5 hasta 1 con paso -1. Imprime cada número. Ejemplifica
    iteración regresiva mediante paso negativo en `range()`.

    Returns:
        None
    """
    print("Números del 5 al 1 (orden descendente):\n")
    for numero in range(5, 0, -1):
        print(numero)


if __name__ == '__main__':
    main()
