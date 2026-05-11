"""
Problema  : Hacer un menú con suma y resta; el usuario elige la operación.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, entrada, operaciones, aritmética
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Mostrar un menú simple, leer opción y dos operandos, y mostrar
      el resultado de la operación seleccionada.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Manejo de opciones fuera de rango (se informa al usuario).
    - Entradas no numéricas no son validadas explícitamente.

Casos de uso:
  - Ejercicios introductorios de control de flujo y E/S por consola.

Revisión:
    - 2026-05-10: Normalizado. Añadidos type hints y docstring de `main`.

"""

def main() -> None:
    """Mostrar un menú para suma o resta y ejecutar la operación.

    Solicita al usuario elegir entre suma y resta, luego pide dos números
    y muestra el resultado. Las entradas se convierten a `float` para
    permitir números con punto decimal.

    Returns:
        None
    """
    print("Menú de operaciones\n")
    print("1. Suma")
    print("2. Resta")

    opcion: int = int(input("Seleccione una opción (1 o 2): "))

    num1: float = float(input("Ingrese el primer número: "))
    num2: float = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        resultado: float = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == 2:
        resultado: float = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")


if __name__ == '__main__':
    main()
