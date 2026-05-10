"""
Problema  : Eliminar duplicados de una lista.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Convertir la lista en un conjunto y luego volver a lista para eliminar
            valores repetidos en una secuencia de ejemplo.

Complejidad: Tiempo O(n) | Espacio O(n)
        - La conversión recorre todos los elementos y crea una nueva colección
            sin repetidos.

Casos límite:
        - El orden original puede no preservarse si se usa `set()` de forma
            directa.
        - Una lista vacía permanece vacía.

Casos de uso:
    - Limpiar catálogos de duplicados antes de publicar datos.
    - Construir listas únicas de categorías o etiquetas.
    - Reducir ruido en resultados de formularios o registros.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Eliminar duplicados de una lista y mostrar el resultado.

    Convierte la lista de ejemplo en un conjunto para filtrar repeticiones y
    muestra la colección resultante.

    Returns:
        None
    """
    lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
    lista_sin_duplicados = list(set(lista_con_duplicados)) #set() elimina duplicados, luego se convierte de nuevo a lista
    print(f"Lista original con duplicados: {lista_con_duplicados}")
    print(f"Lista sin duplicados: {lista_sin_duplicados}")

if __name__ == '__main__':
    main()
