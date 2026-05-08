"""
Problema  : Calcular el promedio de una lista de números.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Utilizar `sum()` y `len()` para obtener el promedio de una lista
      de números. El ejemplo usa una lista constante para mantener la
      demostración sencilla y didáctica.

Complejidad: Tiempo O(n) | Espacio O(1)
    - Se recorre la lista una vez para sumar sus elementos; el uso de
      memoria es constante respecto al tamaño de la entrada.

Casos límite:
    - Lista vacía: evitar división por cero (en este ejemplo la lista es
      no vacía). Si se permitiera entrada dinámica, validar y manejar
      este caso explícitamente.
    - Valores no numéricos: validar tipos si la lista proviene de
      entrada externa.

Revisión:
    - 2026-05-03: Normalizado el header y la documentación al formato
      común del repositorio.
"""

def main():
    """Calcular y mostrar el promedio de una lista de números.

    Usa una lista de ejemplo, calcula su promedio dividiendo la suma de sus elementos por su longitud, y muestra el resultado formateado; no toma entrada del usuario para mantenerlo directo y didáctico.

    Returns:
        None
    """
    numeros: list[int] = [10, 20, 30, 40, 50]
    promedio: float = sum(numeros) / len(numeros)

    print(f"El promedio de la lista {numeros} es: {promedio}")


if __name__ == '__main__':
    main()
