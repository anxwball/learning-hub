"""
Problema  : Mostrar los números del 1 al 100 con la regla FizzBuzz.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, condiciones
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Iterar una secuencia y aplicar condiciones para sustituir valores
      por 'Fizz', 'Buzz' o 'FizzBuzz' según sus múltiplos.

Complejidad: Tiempo O(n) | Espacio O(1)

Casos límite:
    - Rango fijo (1..100); la lógica es válida para cualquier rango
      entero positivo.

Casos de uso:
  - Ejercicio clásico para practicar condicionales y bucles.

Revisión:
    - 2026-05-10: Normalizado. Añadidos type hints y docstring de `main`.

"""


def main() -> None:
    """Imprimir del 1 al 100 aplicando la regla FizzBuzz.

    Para múltiplos de 3 imprime 'Fizz', para múltiplos de 5 imprime
    'Buzz' y para múltiplos de ambos imprime 'FizzBuzz'.

    Returns:
        None
    """
    print("Números del 1 al 100 con FizzBuzz\n")
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)


if __name__ == '__main__':
    main()
