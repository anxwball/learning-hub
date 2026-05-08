"""
Problema  : Invertir una cadena de texto.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Mostrar cómo invertir una cadena usando slicing `[::-1]` y comentar
      la complejidad de la operación. El ejemplo mantiene la cadena como
      constante para centrarse en la técnica.

Complejidad: Tiempo O(n) | Espacio O(n)
    - Invertir una cadena crea una nueva cadena de tamaño n, por lo que el
      coste temporal y espacial es lineal en la longitud de la cadena.

Casos límite:
    - Cadena vacía: la inversión debe devolver una cadena vacía.
    - Cadenas con caracteres multibyte (UTF-8): la inversión opera a nivel
      de caracteres Unicode en Python y mantiene correctamente los símbolos.

Revisión:
    - 2026-05-03: Normalizado el header y la documentación al formato
      común del repositorio.
"""

def main():
    """Invertir una cadena y mostrar el resultado.

    Uses slicing to reverse the string and prints both original and
    reversed versions.

    Returns:
        None
    """
    cadena: str = "Hola Mundo!"
    cadena_invertida: str = cadena[::-1]

    print(f"La cadena original es: '{cadena}'")
    print(f"La cadena invertida es: '{cadena_invertida}'")


if __name__ == '__main__':
    main()
