"""
Problema  : Verificar si un número es par usando lambda.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, lambda, validacion
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar una función lambda que retorna un booleano para verificar paridad.
    - Demuestra cómo lambda puede encapsular lógica de validación y usarse
      con entrada de usuario.

Complejidad: Tiempo O(1) | Espacio O(1)
    - El tiempo es constante, realizando una operación módulo simple.
    - El espacio es constante, sin estructuras de datos dependientes.

Casos límite:
    - Cero: 0 % 2 == 0 -> par
    - Números pares: 2, 4, 100 -> pares
    - Números impares: 1, 3, 99 -> impares
    - Números negativos: -2 es par, -1 es impar

Casos de uso:
  - Validación de entrada de usuario.
  - Filtrado de números en listas (combinado con filter).
  - Lógica de bifurcación condicional basada en paridad.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Verificar si un número es par usando lambda.

    Lee un número del usuario y usa una función lambda para verificar
    si es par (divisible entre 2), mostrando el resultado.

    Returns:
        None
    """
    numero: int = int(input("Introduzca un número para saber si es par: "))
    resultado: bool = (lambda x: x % 2 == 0)(numero)
    if resultado:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")

if __name__ == '__main__':
    main()
