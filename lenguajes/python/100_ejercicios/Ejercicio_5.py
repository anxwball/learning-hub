"""
Problema  : Multiplicar dos números y mostrar su resultado.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, operadores, aritmética
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Multiplicar dos valores numéricos (`a`, `b`) y mostrar el resultado.
    - Ejemplo mínimo y didáctico con valores constantes para ilustrar la
      operación fundamental y la anotación de tipos en Python.
    - Paralelo al ejercicio 1 (suma) para demostrar consistencia entre
      operadores aritméticos.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Operación aritmética constante que no depende del tamaño de entrada.

Casos límite:
    - Versión actual: valores constantes sin validación dinámica en tiempo
      de ejecución.
    - Si se habilita entrada del usuario, validar tipos numéricos y manejar
      posibles excepciones (`ValueError`).
    - Para floats, considerar precisión de punto flotante; para enteros,
      Python soporta precisión arbitraria.

Casos de uso:
  - Calcular escalados de precios, cantidades o presupuestos.
  - Estimar crecimiento proporcional en simulaciones simples.
  - Repetir operaciones de dimensionamiento en ejercicios técnicos.

Revisión:
    - 2026-05-03: Documentación completada con estructura estándar. Docstring
      de `main()` mejorado para claridad.
    - Didáctico: complementa ejercicio 1, demostrando patrón consistente
      entre operadores aritméticos binarios básicos.
"""

def main() -> None:
    """Multiplicar dos números y mostrar el resultado.

    Crea dos variables enteras locales (`a`, `b`) con valores predefinidos,
    calcula su producto mediante el operador `*` y muestra el resultado por
    consola. Ejemplifica patrón paralelo al ejercicio 1 (suma).

    Returns:
        None
    """
    a: int = 6
    b: int = 15
    resultado: int = a * b

    print("La multiplicación es:", resultado)

if __name__ == '__main__':
    main()
