"""
Problema  : Depurar un validador de ISBN para entradas ISBN-10 e ISBN-13.
Fuente    : FreeCodeCamp Labs
Plataforma: FreeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : python, freecodecamp, labs, depuracion, validacion, isbn
Fecha     : 2026-05-22
Estado    : resuelto

Enfoque:
    - Se valida una entrada en formato ISBN,length desde consola.
    - Se separa el cálculo del dígito de control en funciones auxiliares
      para ISBN-10 e ISBN-13.
    - Se manejan errores de formato, conversión y caracteres inválidos
      con mensajes claros y retorno temprano.

Complejidad: Tiempo O(n) | Espacio O(n)
    - La validación recorre los dígitos del ISBN una sola vez para
      convertirlos a enteros y calcular el dígito de control.
    - El espacio auxiliar depende de la lista de dígitos convertidos.

Casos límite:
    - Entrada sin coma: se informa al usuario y la ejecución termina.
    - Longitud no numérica: se informa al usuario y la ejecución termina.
    - Longitud distinta de 10 o 13: se informa al usuario y la ejecución termina.
    - ISBN con caracteres no numéricos en los dígitos base: se informa al
      usuario y la ejecución termina.

Casos de uso:
    - Verificación de códigos ISBN-10 para catálogos y bibliotecas.
    - Verificación de códigos ISBN-13 para flujos de registro de libros.
    - Ejercicio de depuración y control de errores en Python.

Revisión:
    - 2026-05-23: Se añadió el guard `__main__` y se normalizaron los docstrings.
"""


def validate_isbn(isbn: str, length: int) -> None:
    """Validar un ISBN contra su dígito de control.

    Args:
        isbn: Código ISBN sin guiones.
        length: Longitud del ISBN, 10 o 13.

    Returns:
        None
    """
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[: length - 1]
    given_check_digit = isbn[length - 1].upper()

    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list: list[int]) -> str:
    """Calcular el dígito de control de un ISBN-10.

    Args:
        main_digits_list: Los primeros 9 dígitos del ISBN-10 como enteros.

    Returns:
        El dígito de control esperado como cadena.
    """
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def calculate_check_digit_13(main_digits_list: list[int]) -> str:
    """Calcular el dígito de control de un ISBN-13.

    Args:
        main_digits_list: Los primeros 12 dígitos del ISBN-13 como enteros.

    Returns:
        El dígito de control esperado como cadena.
    """
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)

    return expected_check_digit


def main() -> None:
    """Leer una entrada de consola y validar un ISBN.

    Returns:
        None
    """
    try:
        user_input = input('Enter ISBN and length: ')
        values = user_input.split(',')
        isbn = values[0]
        length = int(values[1])
    except IndexError:
        print('Enter comma-separated values.')
        return
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
        return

    print('Length should be 10 or 13.')


if __name__ == "__main__":
    main()
