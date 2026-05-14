"""
Problema  : Crear una función para calcular el área de un círculo.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, geometría, módulo math, fórmulas
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Implementar la fórmula matemática del área de círculo: A = π * r².
    - Utilizar `math.pi` para acceder a la constante π con precisión
      estándar de Python.
    - Aplicar `pow(radio, 2)` para la exponenciación, demostrando claridad
      frente a alternativas como `radio ** 2`.
    - Función pura que devuelve el área sin efectos secundarios, facilitando
      testing y reutilización.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Cálculo aritmético constante; la operación `pow(radio, 2)` es O(1).
    - El espacio es constante; solo parámetro y resultado temporal.

Casos límite:
    - Radio = 0: área es 0 (correctamente calculado).
    - Radio negativo: produce área positiva (π * r² siempre ≥ 0).
      Si se requiere validación, lanzar `ValueError` para radios negativos.
    - Valores muy grandes: Python maneja floats de precisión, pero el
      resultado podría ser `inf` en casos extremos.

Casos de uso:
  - Cálculos geométricos en aplicaciones CAD, gráficos, simulaciones.
  - Validación de superficies en problemas de ingeniería (tuberías, tanques).
  - Ejemplos educativos de funciones matemáticas y módulo `math`.

Revisión:
    - 2026-05-13: Encabezado expandido con análisis de fórmula y casos límite.
"""
import math

def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo calculada usando la fórmula A = π * r^2.
    """
    return math.pi * pow(radio, 2)

def main():
    """plantilla base"""
    resultado: float = area_circulo(5)
    print(resultado)

if __name__ == '__main__':
    main()
