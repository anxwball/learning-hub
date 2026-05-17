"""
Problema  : Sumar los números del 1 al 10 con "for".
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, acumulacion
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Acumular valores dentro de un bucle `for` utilizando un patrón de
      suma progresiva (acumulador).
    - Demuestra cómo mantener estado entre iteraciones mediante una variable
      que se actualiza en cada ciclo del bucle.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal, realizando una operación por cada número del 1 al 10.
    - El espacio es constante; solo se utiliza la variable acumuladora `suma`.

Casos límite:
    - Rango fijo (1..10); la lógica es válida para cualquier rango de enteros.
    - Si el rango está vacío, la suma devolvería 0 (valor inicial del acumulador).

Casos de uso:
  - Cálculo de totales en reportes o listas de datos.
  - Agregación de valores en simuladores o presupuestos.
  - Base para algoritmos más complejos que requieran acumulación.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Calcular la suma de números del 1 al 10.

    Itera a través de los números del 1 al 10 usando un bucle `for`,
    acumulando su suma en una variable. Al final, imprime el resultado
    total. Ejemplifica el patrón de acumulador para agregación de datos.

    Returns:
        None
    """
    print("Suma de números del 1 al 10:\n")
    suma: int = 0
    for i in range(1, 11):
        suma += i
    print(f"La suma de los números del 1 al 10 es: {suma}")


if __name__ == '__main__':
    main()
