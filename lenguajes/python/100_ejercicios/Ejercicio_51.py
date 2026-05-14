"""
Problema  : Imprimir números del 1 al 5 con "for".
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, iteración
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Iterar secuencialmente a través de números usando un bucle `for` con
      `range()`, imprimiendo cada valor para familiarizar con la estructura
      de control de bucles básicos en Python.
    - Enfatiza claridad didáctica: mostrar cómo un bucle itera sobre un rango
      de valores enteros y ejecuta un bloque de código en cada iteración.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal en relación al número de iteraciones (5 en este caso).
    - El espacio es constante ya que solo se utiliza la variable de iteración.

Casos límite:
    - Rango fijo (1..5); la lógica es válida para cualquier rango entero
      positivo definido con `range()`.
    - Si el rango está invertido o vacío, el bucle simplemente no se ejecuta.

Casos de uso:
  - Iteración básica para entender flujo de control y bucles.
  - Base para procesamiento secuencial de datos en listas o rangos.
  - Educativo: fundamentación de conceptos para bucles más complejos.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Iterar e imprimir números del 1 al 5.

    Utiliza un bucle `for` con `range(1, 6)` para iterar secuencialmente
    a través de los números 1 al 5, imprimiendo cada uno en una línea
    separada. Ejemplifica el patrón básico de iteración en Python.

    Returns:
        None
    """
    print("Números del 1 al 5:\n")
    for i in range(1, 6):
        print(i)


if __name__ == '__main__':
    main()
