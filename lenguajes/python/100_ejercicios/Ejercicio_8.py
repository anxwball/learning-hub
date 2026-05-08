"""
Problema  : Crear una tupla con elementos y mostrar su contenido.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, tuplas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Demostrar la creación de una tupla heterogénea y cómo imprimir
      su contenido. El ejemplo usa una tupla constante para mantener la
      explicación simple y enfocada en la inmutabilidad de la estructura.

Complejidad: Tiempo O(1) | Espacio O(1)
    - La construcción e impresión de una tupla de tamaño fijo es una
      operación constante respecto a la entrada mostrada en este ejemplo.

Casos límite:
    - Tupla vacía: su impresión debe mostrar `()`.
    - Inmutabilidad: intentar modificar elementos generará excepciones
      (`TypeError`). Para operaciones mutables, usar listas.

Revisión:
    - 2026-05-03: Ajustado header y documentación al formato común del
      repositorio.
"""

def main():
    """Crear una tupla de ejemplo y mostrar su contenido.

    Returns:
        None
    """
    tupla: tuple = ("manzana", 1, False, 3.47, 6**2)

    print(f"Contenido de la tupla: {tupla}")


if __name__ == '__main__':
    main()
