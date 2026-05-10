"""
Problema  : Extraer un elemento específico de una tupla.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, tuplas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Acceder a una posición concreta de la tupla mediante indexación para
            mostrar el valor seleccionado.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El acceso por índice en una tupla es directo y no requiere memoria
            adicional apreciable.

Casos límite:
        - Un índice fuera de rango provoca `IndexError`.
        - Para tuplas de un solo elemento, el índice válido es únicamente `0`.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Extraer un elemento de una tupla y mostrarlo.

    Toma un valor concreto de la tupla de ejemplo usando su índice y lo
    imprime por consola.

    Returns:
        None
    """
    tupla = (1, 2, 3, 4, 5)
    elemento = tupla[2]  # Extraer el elemento en la posición 2 (valor 3)
    print(f"Tupla original: {tupla}")
    print(f"Elemento extraído: {elemento}")

if __name__ == '__main__':
    main()
