"""
Problema  : Filtrar cadenas que contienen un carácter específico usando filter().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, filter, búsqueda-de-strings
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `filter()` con una función lambda para buscar cadenas que
      contengan un carácter específico ingresado por el usuario.
    - Demuestra búsqueda condicional en colecciones, combinando entrada
      de usuario con procesamiento funcional.

Complejidad: Tiempo O(n*m) | Espacio O(k)
    - El tiempo es O(n*m), donde n es el número de cadenas y m es la
      longitud promedio (búsqueda del carácter en cada cadena).
    - El espacio es O(k), donde k es el número de cadenas con coincidencia.

Casos límite:
    - Carácter no encontrado: "x" en lista sin "x" -> []
    - Carácter encontrado en todas: "a" en ["manzana", "banana"] -> ambas
    - Carácter especial: "!" en ["¡Hola!", "Mundo"] -> ["¡Hola!"]
    - Búsqueda sensible a mayúsculas: "A" vs "a" son diferentes

Casos de uso:
  - Búsqueda en registros: encontrar emails con dominio específico.
  - Filtrado de datos: seleccionar mensajes con palabras clave.
  - Validación: descartar entradas que contienen caracteres prohibidos.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Filtrar cadenas que contienen un carácter usando filter().

    Lee un carácter del usuario y filtra una lista de palabras para
    mostrar solo las que contienen ese carácter.

    Returns:
        None
    """
    cadenas: list[str] = ["manzana", "banana", "cereza", "durazno", "mango"]
    caracter: str = input("Introduzca un carácter para filtrar las cadenas: ")
    cadenas_filtradas: list[str] = list(filter(lambda x: caracter in x, cadenas))
    print(f"Lista de palabras: {cadenas}")
    if not cadenas_filtradas:
        print(f"No se encontraron palabras que contengan '{caracter}'.")
    else:
        print(f"Palabras que contienen '{caracter}': {cadenas_filtradas}")

if __name__ == '__main__':
    main()
