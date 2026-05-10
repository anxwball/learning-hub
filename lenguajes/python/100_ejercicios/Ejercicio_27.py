"""
Problema  : Realizar operaciones básicas con conjuntos: unión e intersección.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, conjuntos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Usar operadores de conjuntos para mostrar unión e intersección entre
            dos colecciones de ejemplo.

Complejidad: Tiempo O(n) | Espacio O(n)
        - Las operaciones recorren los elementos presentes en los conjuntos y
            crean nuevos resultados.

Casos límite:
        - Conjuntos vacíos producen resultados vacíos o equivalentes según la
            operación aplicada.
        - Elementos duplicados se eliminan automáticamente por la naturaleza de
            los conjuntos.

Casos de uso:
    - Comparar grupos de permisos o etiquetas compartidas.
    - Detectar coincidencias entre listas de elementos únicos.
    - Unir e intersectar catálogos, filtros o perfiles.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Mostrar unión e intersección de conjuntos.

    Crea dos conjuntos de ejemplo y muestra sus operaciones básicas para
    ilustrar el comportamiento de la estructura.

    Returns:
        None
    """
    conjunto_a = {1, 2, 3, 4}
    conjunto_b = {3, 4, 5, 6}

    union = conjunto_a.union(conjunto_b)
    interseccion = conjunto_a.intersection(conjunto_b)

    print(f"Conjunto A: {conjunto_a}")
    print(f"Conjunto B: {conjunto_b}")
    print(f"Unión de A y B: {union}")
    print(f"Intersección de A y B: {interseccion}")

if __name__ == '__main__':
    main()
