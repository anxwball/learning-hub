"""
Problema  : Calcular el área de un círculo dado su radio.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, geometría, matemáticas
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
Enfoque:
        - Calcular el área de un círculo usando la fórmula `pi * radio**2`.
        - Ejemplo didáctico con valores constantes para ilustrar el cálculo
            y la impresión del resultado. Puede adaptarse para recibir entrada
            del usuario si se desea validar y parsear el radio.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El cálculo requiere una cantidad constante de operaciones y memoria.

Casos límite:
        - Versión actual: el radio es una constante en el código, por lo que
            no hay casos de validación en tiempo de ejecución.
        - Si se cambia a entrada dinámica, validar que `radio >= 0` y manejar
            entradas no numéricas (capturar `ValueError`).
        - Para floats, considerar precisión de punto flotante en la representación.

Revisión:
        - 2026-05-02: Documentación completada; añadir validación si se habilita
            entrada interactiva.
"""
import math

def main():
    """Calcular y mostrar el área de un círculo.

    Usa una variable local `radio` (float) con valor constante, calcula el
    área mediante `math.pi * radio**2` y formatea la salida por consola.

    Returns:
        None
    """
    radio: float = 5.0
    area: float = math.pi * radio ** 2

    print(f"El área del círculo con radio {radio} es: {area:.2f}")

if __name__ == '__main__':
    main()
