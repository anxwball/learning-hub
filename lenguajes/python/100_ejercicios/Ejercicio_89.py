"""
Problema  : Comprobar si una palabra es palíndromo usando lambda.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, lambda, validación-de-strings
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar una función lambda que compara una palabra con su reversa
      para detectar palíndromos.
    - Demuestra manipulación de strings con slicing inverso [::-1] dentro
      de lambda, incluyendo normalización de entrada.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, donde n es la longitud de la palabra.
    - El espacio es lineal, creando la cadena invertida.

Casos límite:
    - Una letra: "a" -> palíndromo
    - Dos letras iguales: "aa" -> palíndromo
    - Dos letras diferentes: "ab" -> no es palíndromo
    - Palíndromo clásico: "racecar" -> palíndromo

Casos de uso:
  - Validación de patrones en strings.
  - Puzzles y juegos de palabras.
  - Análisis lingüístico educativo.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Verificar si una palabra es palíndromo usando lambda.

    Lee una palabra del usuario, la normaliza (minúsculas, sin espacios),
    y usa una función lambda para verificar si se lee igual al revés.

    Returns:
        None
    """
    palabra_original: str = input("Introduzca una palabra para saber si es palíndromo: ")
    palabra: str = palabra_original.strip().lower()
    resultado: bool = (lambda pal: pal == pal[::-1])(palabra)
    if resultado:
        print(f"{palabra_original} es palíndromo.")
    else:
        print(f"{palabra_original} no es palíndromo.")

if __name__ == '__main__':
    main()
