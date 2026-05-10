"""
Problema  : Invertir una cadena de texto.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Mostrar cómo invertir una cadena usando slicing con `[::-1]`.
    - Comentar la complejidad y eficiencia de la operación.
    - El ejemplo mantiene la cadena como constante para centrarse en la
      técnica de inversión.

Complejidad: Tiempo O(n) | Espacio O(n)
    - Invertir una cadena crea una nueva cadena de tamaño n, por lo que
      el coste temporal y espacial es lineal en la longitud de la cadena.

Casos límite:
    - Cadena vacía: la inversión debe devolver una cadena vacía.
    - Cadenas con caracteres multibyte (UTF-8): la inversión opera a nivel
      de caracteres Unicode en Python y mantiene correctamente los símbolos.
    - Palíndromes: cadenas que son iguales invertidas (p. ej. "radar").

Casos de uso:
  - Validar palíndromos o simetrías simples en textos.
  - Mostrar efectos de transformación de cadenas en interfaces educativas.
  - Preparar contenido para análisis inverso o depuración textual.

Revisión:
    - 2026-05-03: Normalizado el header y la documentación al formato
      común del repositorio.
    - Didáctico: demuestra idioma Python (slicing negativo) y optimización
      de operaciones con cadenas respecto a enfoque iterativo.
"""

def main():
    """Invertir una cadena y mostrar el resultado.

    Crea una cadena de ejemplo, invierte su contenido mediante slicing
    negativo `[::-1]` y muestra ambas versiones (original e invertida)
    para comparación y claridad.

    Returns:
        None
    """
    cadena: str = "Hola Mundo!"
    cadena_invertida: str = cadena[::-1]

    print(f"La cadena original es: '{cadena}'")
    print(f"La cadena invertida es: '{cadena_invertida}'")


if __name__ == '__main__':
    main()
