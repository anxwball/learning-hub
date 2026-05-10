"""
Problema  : Calcular el promedio de una lista de números.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas, matemáticas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Utilizar `sum()` y `len()` para obtener el promedio de una lista
      de números de forma clara y didáctica.
    - El ejemplo usa una lista constante para mantener la demostración
      sencilla y enfocada en la lógica de cálculo.

Complejidad: Tiempo O(n) | Espacio O(1)
    - Se recorre la lista una vez para sumar sus elementos (coste O(n));
      el uso de memoria es constante respecto al tamaño de la entrada.

Casos límite:
    - Lista vacía: evitar división por cero (en este ejemplo la lista es
      no vacía). Si se permitiera entrada dinámica, validar y manejar
      este caso explícitamente con condicionales.
    - Valores no numéricos: generar `TypeError` en `sum()`. Validar tipos
      si la lista proviene de entrada externa.
    - Valores muy grandes: riesgo de overflow en otros lenguajes, pero
      Python maneja enteros de precisión arbitraria.

Casos de uso:
  - Calcular promedios de calificaciones o encuestas.
  - Resumir indicadores de rendimiento en paneles simples.
  - Obtener una métrica central para lotes de datos pequeños.

Revisión:
    - 2026-05-03: Normalizado el header y la documentación al formato
      estándar del repositorio.
    - Didáctico: combinación de funciones incorporadas para estadística
      básica, patrón reutilizable.
"""

def main() -> None:
    """Calcular y mostrar el promedio de una lista de números.

    Define una lista de enteros, calcula su promedio dividiendo la suma
    (con `sum()`) por la cantidad de elementos (con `len()`) y muestra
    el resultado formateado. No toma entrada del usuario para mantenerlo
    directo y didáctico.

    Returns:
        None
    """
    numeros: list[int] = [10, 20, 30, 40, 50]
    promedio: float = sum(numeros) / len(numeros)

    print(f"El promedio de la lista {numeros} es: {promedio}")


if __name__ == '__main__':
    main()
