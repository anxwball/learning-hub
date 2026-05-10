"""
Problema  : Eliminar un elemento específico de una lista.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Usar `remove()` para borrar un valor concreto de la lista y mostrar
            el resultado actualizado.

Complejidad: Tiempo O(n) | Espacio O(1)
        - La búsqueda del elemento es lineal y la eliminación se realiza sobre
            la estructura existente.

Casos límite:
        - Si el valor no existe, `remove()` lanza `ValueError`.
        - Si hay duplicados, solo se elimina la primera coincidencia.

Casos de uso:
    - Quitar artículos agotados de un carrito o inventario temporal.
    - Filtrar valores de listas de selección o listas negras.
    - Actualizar colecciones dinámicas en interfaces de gestión.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Eliminar un elemento de una lista y mostrar el resultado.

    Aplica `remove()` sobre la lista de ejemplo para quitar el valor
    seleccionado y mostrar la lista resultante.

    Returns:
        None
    """
    lista = [1, 2, 3, 4, 5]
    lista_nueva = lista.copy()  # Copiar la lista para no modificar la original
    lista_nueva.remove(3)
    print(f"Lista original: {lista}")
    print(f"Lista después de eliminar el elemento 3: {lista_nueva}")

if __name__ == '__main__':
    main()
