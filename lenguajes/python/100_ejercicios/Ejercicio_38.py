"""
Problema  : Determina si un número es divisible entre 5 y 7.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Leer un número entero y comprobar la divisibilidad por 5 y 7.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Entradas no numéricas provocan `ValueError` si no se validan.

Casos de uso:
  - Comprobaciones numéricas simples en ejercicios educativos.

Revisión:
    - 2026-05-02: Normalización de docstring y anotaciones de tipo.
"""

def main() -> None:
    """Lee un entero y verifica si es divisible por 5 y 7.

    Returns:
        None
    """
    numero: int = int(input("Ingrese un número: "))

    if numero % 5 == 0 and numero % 7 == 0:
        print(f"El número {numero} es divisible entre 5 y 7.")
    else:
        print(f"El número {numero} no es divisible entre 5 y 7.")


if __name__ == '__main__':
    main()
