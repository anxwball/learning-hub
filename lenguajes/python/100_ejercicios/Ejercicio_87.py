"""
Problema  : Sumar dos números usando lambda.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, lambda, aritmetica
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Definir una función lambda que acepta dos parámetros y realiza una suma.
    - Demuestra la sintaxis de lambda para más de un parámetro y su invocación
      directa sin asignación a variable.

Complejidad: Tiempo O(1) | Espacio O(1)
    - El tiempo es constante, realizando una operación aritmética simple.
    - El espacio es constante, sin dependencia del tamaño de entrada.

Casos límite:
    - Números cero: 0 + 0 = 0
    - Números negativos: -5 + (-10) = -15
    - Números grandes: 999999 + 999999 = 1999998
    - Valores opuestos: 5 + (-5) = 0

Casos de uso:
  - Operaciones simples inline sin definir funciones.
  - Callbacks en bibliotecas funcionales.
  - Expresiones de una sola línea en código interactivo.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Sumar dos números usando lambda.

    Crea una función lambda que suma dos números y la invoca inmediatamente,
    demostrando lambda con múltiples parámetros e invocación directa.

    Returns:
        None
    """
    a: int = 5
    b: int = 10
    resultado: int = (lambda x, y: x + y)(a, b)
    print(f"La suma de {a} y {b} es: {resultado}")

if __name__ == '__main__':
    main()
