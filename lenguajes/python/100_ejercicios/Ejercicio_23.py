"""
Problema  : Verificar si una cadena es un palíndromo.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Comparar una cadena con su versión invertida para determinar si se
            lee igual de izquierda a derecha y viceversa.

Complejidad: Tiempo O(n) | Espacio O(n)
        - Invertir la cadena requiere recorrer sus caracteres y construir una
            nueva cadena de tamaño lineal.

Casos límite:
        - Una cadena vacía se considera palíndromo por comparación directa.
        - La comparación es sensible a mayúsculas, espacios y signos.

Casos de uso:
    - Validar nombres o frases simétricas en aplicaciones educativas.
    - Detectar entradas que se leen igual en ambos sentidos.
    - Implementar mini retos de verificación textual.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Verificar si una cadena es un palíndromo.

    Compara la cadena original con su versión invertida y muestra si cumple
    la condición de palíndromo.

    Returns:
        None
    """
    palabra: str = "radar"
    es_palindromo: bool = palabra == palabra[::-1]
    print(f"Palabra: {palabra}.")
    if es_palindromo:
        print(f"La palabra \"{palabra}\" es un palíndromo.")
    else:
        print(f"La palabra \"{palabra}\" no es un palíndromo.")


if __name__ == '__main__':
    main()
