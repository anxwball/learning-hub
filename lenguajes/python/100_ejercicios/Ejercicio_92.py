"""
Problema  : Filtrar cadenas de longitud mayor que 3 usando filter().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, filter, validacion-de-strings
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `filter()` con una función lambda que verifica si la longitud
      de cada cadena excede un umbral.
    - Demuestra filtrado basado en propiedades de objetos (longitud),
      combinando `filter()` con predicados sobre strings.

Complejidad: Tiempo O(n*m) | Espacio O(k)
    - El tiempo es O(n*m), donde n es el número de cadenas y m es la
      longitud promedio (para calcular len()).
    - El espacio es O(k), donde k es el número de cadenas que pasan el filtro.

Casos límite:
    - Cadenas cortas: ["a", "ab"] -> []
    - Exactamente 3 caracteres: ["abc"] -> [] (no es > 3)
    - 4 caracteres: ["abcd"] -> ["abcd"]
    - Lista vacía: [] -> []

Casos de uso:
  - Validación de entrada: aceptar solo contraseñas suficientemente largas.
  - Procesamiento de texto: filtrar palabras cortas en análisis.
  - Limpieza de datos: descartar registros incompletos.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Filtrar cadenas por longitud usando filter().

    Aplica filter() con una función lambda que verifica si len(x) > 3,
    obteniendo solo las cadenas más largas que 3 caracteres.

    Returns:
        None
    """
    cadenas: list[str] = ["a", "ab", "abc", "abcd", "abcde"]
    cadenas_filtradas: list[str] = list(filter(lambda x: len(x) > 3, cadenas))
    print(f"Cadenas originales: {cadenas}")
    print(f"Cadenas filtradas (>3 caracteres): {cadenas_filtradas}")

if __name__ == '__main__':
    main()
