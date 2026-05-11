"""
Problema  : Pedir y determinar si un carácter es una vocal o una consonante.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Lectura de un carácter desde entrada estándar, normalización a
      minúsculas y comparación contra el conjunto de vocales.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Entrada vacía o más de un carácter: el programa toma la cadena
      completa y la compara tal cual (comportamiento simple y didáctico).

Casos de uso:
  - Validaciones básicas de caracteres en formularios educativos.

Revisión:
    - 2026-05-02: Normalización de docstring y anotaciones de tipo.
"""

def main() -> None:
    """Pide un carácter y determina si es vocal o consonante.

    Lee un carácter desde la entrada, lo normaliza a minúsculas y
    verifica si pertenece al conjunto de vocales en español.

    Returns:
        None
    """
    caracter: str = input("Ingrese un carácter: ").lower()
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u']

    if caracter in vocales:
        print(f"El carácter '{caracter}' es una vocal.")
    else:
        print(f"El carácter '{caracter}' es una consonante.")


if __name__ == '__main__':
    main()
