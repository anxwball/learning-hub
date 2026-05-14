"""
Problema  : Multiplicar todos los elementos de una lista por 2 usando un bucle for.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, transformación, operadores aritméticos
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Iterar sobre cada elemento de una lista y aplicar una transformación
      escalar (multiplicación por 2) a cada uno.
    - Demuestra cómo realizar operaciones uniformes sobre todos los elementos
      de una colección sin modificar la lista original.
    - Introduce el concepto de map/transformación: aplicar la misma función
      a múltiples elementos.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal; se realiza una operación por cada elemento (10 elementos).
    - El espacio es lineal para almacenar la lista de entrada.

Casos límite:
    - Números cero: multiplicar por 2 resulta en cero.
    - Números negativos: la multiplicación mantiene el signo.
    - Números flotantes: la operación funciona también con decimales.
    - Listas vacías: el bucle no se ejecuta.

Casos de uso:
  - Escalado de datos (multiplicar por constantes).
  - Aplicación de descuentos o incrementos uniformes.
  - Normalización de valores mediante transformación escalar.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Multiplicar cada elemento de una lista por 2.

    Define una lista de 10 números enteros (1 a 10), itera sobre cada uno,
    lo multiplica por 2 y muestra el resultado con un mensaje descriptivo.
    Ejemplifica transformación de elementos sin modificar la lista original.

    Returns:
        None
    """
    print("Elementos de la lista multiplicados por 2:\n")
    numeros: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for numero in numeros:
        resultado: int = numero * 2
        print(f"{numero} multiplicado por 2 es: {resultado}")


if __name__ == '__main__':
    main()
