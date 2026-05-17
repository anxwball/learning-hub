"""
Problema  : Elevar al cuadrado una lista de números utilizando map().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, funciones-orden-superior, map
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Aplicar la función `map()` para transformar cada elemento de una lista
      mediante una función personalizada.
    - Demuestra cómo `map()` aplica una función a cada elemento sin necesidad
      de un bucle explícito, introduciendo programación funcional.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, procesando cada uno de los n elementos de la lista.
    - El espacio es lineal, creando una nueva lista de resultado con n elementos.

Casos límite:
    - Lista vacía: map() devuelve un iterador vacío.
    - Un elemento: [5] -> [25]
    - Números negativos: [-2, -3] -> [4, 9] (el cuadrado siempre es positivo)
    - Números grandes: [1000] -> [1000000]

Casos de uso:
  - Transformación de datos: escalar valores en datasets.
  - Procesamiento de imágenes: ajustar brillo/contraste en píxeles.
  - Operaciones numéricas: normalización de datos con cuadrados de distancias.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""
def cuadrado(x: int) -> int:
    """Eleva un número al cuadrado.

    Args:
        x (int): El número a elevar al cuadrado.

    Returns:
        int: El resultado de elevar el número al cuadrado.
    """
    return pow(x, 2)


def main() -> None:
    """Elevar al cuadrado una lista de números usando map().

    Aplica la función `cuadrado()` a cada elemento de la lista utilizando
    `map()`, demostrando programación funcional y transformación de datos.

    Returns:
        None
    """
    numeros: list[int] = [1, 2, 3, 4, 5]
    resultado: list[int] = list(map(cuadrado, numeros))
    print(f"Lista original: {numeros}")
    print(f"Lista al cuadrado: {resultado}")

if __name__ == '__main__':
    main()
