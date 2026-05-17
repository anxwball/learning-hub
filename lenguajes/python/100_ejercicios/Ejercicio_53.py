"""
Problema  : Imprimir los elementos de una lista con "for".
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas, iteracion, tipos-heterogeneos
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Iterar directamente sobre elementos de una lista usando `for element in lista`
      en lugar de usar índices.
    - Demuestra que Python permite iteración sobre colecciones heterogéneas
      (listas con múltiples tipos de datos).
    - Introduce el concepto de iteración de colecciones y acceso a elementos
      sin necesidad de gestionar índices manualmente.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, iterando a través de todos los elementos de la lista.
    - El espacio es lineal en el tamaño de la lista (almacenar la colección).

Casos límite:
    - Listas heterogéneas (diferentes tipos): la iteración funciona sin problema.
    - Listas vacías: el bucle simplemente no se ejecuta.
    - Elementos complejos (objetos, listas anidadas): la iteración accede a cada
      elemento correctamente.

Casos de uso:
  - Procesamiento de datos en listas de diferentes tipos.
  - Recorrido de resultados de búsquedas o consultas heterogéneas.
  - Validación o transformación de colecciones de elementos.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""

from typing import Union


def main() -> None:
    """Iterar e imprimir elementos de una lista.

    Define una lista heterogénea que contiene diferentes tipos de datos
    (enteros, booleano, cadenas) y la itera usando un bucle `for`, imprimiendo
    cada elemento. Ejemplifica la flexibilidad de listas en Python y la
    iteración sobre colecciones de tipos mixtos.

    Returns:
        None
    """
    print("Elementos de la lista:\n")
    lista: list[Union[int, bool, str]] = [1, 2, True, 'cuatro', 'cinco']
    for elemento in lista:
        print(elemento)


if __name__ == '__main__':
    main()
