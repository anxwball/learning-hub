"""
Problema  : Crear una función para convertir grados Celsius a Fahrenheit.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, conversión, aritmética, temperatura
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Implementar la conversión de temperatura Celsius a Fahrenheit usando
      la fórmula: F = (C * 9/5) + 32.
    - Utilizar floats para permitir decimales en la temperatura.
    - Demostrar entrada interactiva del usuario mediante `input()` y
      conversión de cadena a número.
    - Función reutilizable que encapsula la lógica de conversión, facilitando
      su uso en diferentes contextos.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Cálculo aritmético primitivo: multiplicación, división, suma.
    - El espacio es constante; solo parámetro y resultado temporal.

Casos límite:
    - Cero grados Celsius: F = (0 * 9/5) + 32 = 32°F (punto de congelación).
    - -40°C: F = (-40 * 9/5) + 32 = -40°F (los dos sistemas coinciden).
    - Valores negativos en Celsius: conversión funciona correctamente.
    - Entrada inválida (no numérica): genera `ValueError` al hacer `float()`.

Casos de uso:
  - Conversión de temperaturas en aplicaciones meteorológicas (APIs, widgets).
  - Cocción/medicina (temperaturas de horno, fiebre).
  - Ejemplo educativo de fórmulas matemáticas y entrada/salida de usuario.

Revisión:
    - 2026-05-13: Encabezado expandido con análisis de fórmula y ejemplos.
"""
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
        celsius (float): La temperatura en grados Celsius.

    Returns:
        float: La temperatura convertida a grados Fahrenheit, calculada usando la fórmula F = (C * 9/5) + 32.
    """
    return (celsius * 9/5) + 32

def main():
    """plantilla base"""
    grados_celsius: float = float(input("Ingrese la temperatura en grados Celsius: "))
    grados_fahrenheit: float = celsius_a_fahrenheit(grados_celsius)
    print(f"{grados_celsius} grados Celsius son {grados_fahrenheit} grados Fahrenheit.")

if __name__ == '__main__':
    main()
