"""
Problema  : Imprimir los números pares del 2 al 10 con "for".
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, rango, paso
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Utilizar el parámetro de `paso` (step) en `range()` para generar una
      secuencia de números con incremento diferente a 1.
    - Demuestra cómo controlar el intervalo de iteración en un bucle `for`
      sin necesidad de condiciones lógicas adicionales.
    - Introduce la sintaxis de `range(inicio, fin, paso)` para iteración
      con incrementos personalizados.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal en relación al número de iteraciones (5 números pares).
    - El espacio es constante; solo se utiliza la variable de iteración.

Casos límite:
    - Rango con paso: `range(2, 11, 2)` produce exactamente 5 números.
    - Si el paso no alinea correctamente con el rango, se itera hasta el
      último múltiplo que no exceda el límite.
    - Pasos negativos: podrían usarse para iteración descendente.

Casos de uso:
  - Procesar subconjuntos de datos en intervalos regulares.
  - Iteración alternada o cada n elementos.
  - Generación de secuencias aritméticas para análisis o reportes.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Imprimir números pares del 2 al 10.

    Utiliza `range(2, 11, 2)` para generar una secuencia de números pares
    del 2 al 10 con incremento de 2 en cada iteración. Imprime cada número.
    Ejemplifica el uso del parámetro de paso en `range()`.

    Returns:
        None
    """
    print("Números pares del 2 al 10:\n")
    for numero in range(2, 11, 2):
        print(numero)


if __name__ == '__main__':
    main()
