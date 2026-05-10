"""
Problema  : Intercambiar valores de variables con asignación múltiple.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, operadores
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Aplicar desempaquetado múltiple para intercambiar los valores de dos
            variables sin utilizar una variable temporal.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El intercambio se resuelve con asignación directa y memoria fija.

Casos límite:
        - Si ambas variables tienen el mismo valor, el intercambio no cambia
            visualmente el resultado.

Casos de uso:
    - Reasignar valores en algoritmos de intercambio temporal.
    - Rotar estados simples en simuladores o flujos de control.
    - Simplificar lógica de reordenamiento de variables.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Intercambiar dos variables y mostrar el resultado.

    Usa asignación múltiple para intercambiar los valores de dos variables y
    mostrar el antes y el después.

    Returns:
        None
    """
    a = 10
    b = 20
    print(f"Antes del intercambio: a = {a}, b = {b}")
    a, b = b, a  # Intercambiar los valores de a y b
    print(f"Después del intercambio: a = {a}, b = {b}")

if __name__ == '__main__':
    main()
