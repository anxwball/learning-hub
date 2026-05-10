"""
Problema  : Pedir un número y verificar si es par o impar.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, condicionales, operadores
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Leer un número y usar el operador módulo para distinguir entre
            valores pares e impares.

Complejidad: Tiempo O(1) | Espacio O(1)
        - Solo se realiza una operación aritmética y una comparación.

Casos límite:
        - El cero se considera par.
        - Entradas no numéricas generan `ValueError` en la conversión.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Determinar si un número es par o impar.

    Solicita un número por consola, aplica el módulo 2 y muestra su
    clasificación.

    Returns:
        None
    """
    num: int = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")

if __name__ == '__main__':
    main()
