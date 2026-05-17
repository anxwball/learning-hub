"""
Problema  : Crear una función para sumar dos números.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, aritmetica, funciones
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Implementar una función pura que devuelve la suma de dos enteros.
    - Utilizar anotaciones de tipo (type hints) para documentar los parámetros
      y el valor retornado, mejorando legibilidad y permitiendo validación
      estática en IDEs.
    - Demuestra el patrón básico de una función reutilizable: toma parámetros,
      realiza una operación, y devuelve un resultado sin efectos secundarios.

Complejidad: Tiempo O(1) | Espacio O(1)
    - La suma es una operación aritmética primitiva que se ejecuta en tiempo
      constante, independientemente de los valores de entrada.
    - El espacio es constante; solo se utiliza el stack para parámetros y
      el resultado temporal.

Casos límite:
    - Números negativos: la operación `+` funciona correctamente con enteros
      negativos, devolviendo el resultado aritméticamente correcto.
    - Cero: suma con cero devuelve el otro número (propiedad identidad).
    - Desbordamiento: en Python 3, los enteros tienen precisión arbitraria,
      por lo que no hay riesgo de overflow.

Casos de uso:
  - Operación base para contadores y acumuladores en aplicaciones.
  - Componente fundamental en cálculos complejos que requieren sumatoria.
  - Ejemplos didácticos para introducir funciones y type hints.

Revisión:
    - 2026-05-13: Encabezado expandido con análisis detallado.
"""
def suma(a: int, b: int) -> int:
    """Suma dos números enteros.

    Args:
        a (int): El primer número a sumar.
        b (int): El segundo número a sumar.

    Returns:
        int: La suma de los dos números.
    """
    return a + b


def main():
    """plantilla base"""
    print(suma(3, 5))
    

if __name__ == '__main__':
    main()
