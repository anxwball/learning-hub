"""
Problema  : Combinar dos listas en pares usando la función `zip()`.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Emparejar dos listas con `zip()` para mostrar cómo se recorren en
            paralelo y se forman pares de valores.

Complejidad: Tiempo O(n) | Espacio O(n)
        - La función recorre hasta la longitud de la lista más corta y crea una
            nueva colección de pares.

Casos límite:
        - Si una lista es más corta, el resultado se detiene al agotarse.
        - Con listas vacías, el resultado es vacío.

Casos de uso:
    - Emparejar datos de dos fuentes para comparaciones.
    - Construir tablas rápidas de correspondencia clave-valor.
    - Fusionar listas paralelas en reportes o vistas resumidas.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Combinar dos listas en pares y mostrar el resultado.

    Usa `zip()` para emparejar dos listas de ejemplo y mostrar cada par como
    una lista de tuplas.

    Returns:
        None
    """
    lista1 = [1, 2, 3]
    lista2 = ['a', 'b', 'c']
    combinada = list(zip(lista1, lista2)) #zip() combina las listas en pares, luego se convierte a lista para mostrar el resultado
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Listas combinadas: {combinada}")

if __name__ == '__main__':
    main()
