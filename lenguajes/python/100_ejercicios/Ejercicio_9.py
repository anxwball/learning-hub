"""
Problema  : Realizar la potencia de un número.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, operadores, aritmética
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Mostrar el uso del operador de potencia (`**`) y la función
      equivalente `pow()` para elevar una base a un exponente.
    - El ejemplo usa valores constantes para mantener el foco en la
      operación básica sin distracción.

Complejidad: Tiempo O(1) | Espacio O(1)
    - La operación de exponenciación aplicada a números primitivos es
      una única operación aritmética (para exponentes pequeños).
    - Nota: exponentes muy grandes pueden tener coste no trivial.

Casos límite:
    - Exponente negativo: produce un resultado fraccional si la base no es
      cero (p. ej. `2 ** -1 = 0.5`).
    - Base cero y exponente cero: `0**0` en Python devuelve 1 por
      convención matemática, considerar si se desea otro comportamiento.
    - Exponentes muy grandes: cuidado con tiempos de cálculo para
      enteros muy grandes (Python maneja precisión arbitraria con
      coste computacional creciente).

Casos de uso:
  - Modelar crecimiento compuesto o interés acumulado.
  - Estimar escalados de potencia, capacidad o volumen.
  - Calcular valores repetitivos en simulaciones matemáticas.

Revisión:
    - 2026-05-03: Ajustado header y documentación al formato estándar
      del repositorio.
    - Didáctico: muestra simetría con operadores aritméticos anteriores,
      extensible a validación de entrada con manejo de excepciones.
"""

def main() -> None:
    """Calcular y mostrar la potencia de un número.

    Define una base y un exponente con valores constantes, calcula la
    potencia mediante el operador `**` y muestra el resultado formateado.
    No toma entrada del usuario para mantenerlo directo y didáctico.

    Returns:
        None
    """
    base: int = 5
    exponente: int = 3
    resultado: int = base ** exponente

    print(f"{base} elevado a la {exponente} es: {resultado}")


if __name__ == '__main__':
    main()
