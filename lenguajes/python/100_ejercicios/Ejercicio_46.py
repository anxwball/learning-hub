"""
Problema  : Solicitar al usuario un número y contar cuántos dígitos tiene.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, números, aritmética
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Solicitar un entero al usuario y contar sus dígitos mediante
      divisiones enteras sucesivas.

Complejidad: Tiempo O(log10(n)) | Espacio O(1)

Casos límite:
    - Entrada 0 debe considerarse como 1 dígito.
    - Números negativos: se cuenta la magnitud (valor absoluto).

Casos de uso:
  - Validación y análisis de longitud de entradas numéricas.

Revisión:
    - 2026-05-10: Normalizado. Añadidos type hints y docstring de `main`.

"""

def main() -> None:
    """Contar y mostrar la cantidad de dígitos de un número entero.

    Solicita al usuario un número entero, calcula cuántos dígitos tiene
    (considerando el valor absoluto). El número 0 se considera de un
    dígito.

    Returns:
        None
    """
    print("Contar dígitos de un número\n")
    numero: int = int(input("Ingrese un número: "))
    n: int = abs(numero)

    if n == 0:
        contador: int = 1
    else:
        contador = 0
        while n != 0:
            n //= 10
            contador += 1

    print(f"El número tiene {contador} dígitos.")


if __name__ == '__main__':
    main()
