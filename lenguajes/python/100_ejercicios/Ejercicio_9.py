"""
Problema  : Realizar la potencia de un número.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, operadores
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Mostrar el uso del operador de potencia (`**`) y la función
      equivalente `pow()` para elevar una base a un exponente. El ejemplo
      usa valores constantes para mantener el foco en la operación.

Complejidad: Tiempo O(1) | Espacio O(1)
    - La operación de exponenciación aplicada a números primitivos es una
      única operación aritmética en este ejemplo.

Casos límite:
    - Exponente negativo: produce un resultado fraccional si la base no es
      cero (p. ej. 2 ** -1 = 0.5).
    - Base cero y exponente cero: 0**0 en Python devuelve 1 por convención,
      considerar si se desea un comportamiento distinto.
    - Exponentes muy grandes: cuidado con overflow o tiempos de cálculo
      para enteros muy grandes (aunque Python maneja enteros de tamaño
      arbitrario, el coste puede ser significativo).

Revisión:
    - 2026-05-03: Ajustado header y documentación al formato estándar del
      repositorio.
"""

def main():
    """Calcular y mostrar la potencia de un número.

    Usa el operador `**` para elevar una base a un exponente, calcula el resultado y lo muestra formateado. No toma entrada del usuario para mantenerlo directo y didáctico.

    Returns:
        None
    """
    base: int = 5
    exponente: int = 3
    resultado: int = base ** exponente

    print(f"{base} elevado a la {exponente} es: {resultado}")


if __name__ == '__main__':
    main()
