"""
Problema  : Imprimir la suma de los números pares del 1 al 10 usando un bucle for.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, condicionales, acumulacion
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Combinar iteración, condición y acumulación para filtrar y sumar
      solo los elementos que cumplen un criterio (números pares).
    - Demuestra el patrón de `acumulador condicional`: mantener un acumulador
      que solo se actualiza cuando se cumple una condición.
    - Introduce la lógica de filtrado dentro de un bucle iterativo.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal; itera a través de todos los números (n=10 en este caso).
    - El espacio es constante; solo se utiliza la variable acumuladora.

Casos límite:
    - Rango sin números pares: la suma resultaría en 0 (valor inicial).
    - Todos los números son pares: se acumularía la suma de todos.
    - Números negativos: el módulo (%) funciona correctamente para detectar paridad.

Casos de uso:
  - Cálculo selectivo de totales (suma de números que cumplen criterios).
  - Agregación de datos filtrados en reportes y análisis.
  - Base para problemas de agregación condicional más complejos.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Calcular la suma de los números pares del 1 al 10.

    Itera a través de los números del 1 al 10, verifica si cada uno es par
    usando el operador módulo (%), y acumula solo los números pares en una
    suma. Al final, muestra el resultado total. Ejemplifica filtrado y
    acumulación condicional.

    Returns:
        None
    """
    print("Suma de números pares del 1 al 10:\n")
    suma: int = 0
    for numero in range(1, 11):
        if numero % 2 == 0:
            suma += numero
            print(f"Sumando {numero}, suma actual: {suma}")
    print(f"\nLa suma de los números pares del 1 al 10 es: {suma}")


if __name__ == '__main__':
    main()
