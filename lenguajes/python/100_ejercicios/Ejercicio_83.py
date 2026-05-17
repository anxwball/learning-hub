"""
Problema  : Calcular la longitud de una lista de palabras utilizando map().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, map, análisis-de-strings
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Aplicar `map()` con la función `len()` para obtener la longitud de cada
      palabra en una lista simultáneamente.
    - Demuestra cómo funciones incorporadas como `len()` pueden usarse con
      `map()` para operaciones sobre colecciones sin bucles explícitos.

Complejidad: Tiempo O(n*m) | Espacio O(n)
    - El tiempo es O(n*m), donde n es el número de palabras y m es la longitud
      promedio; `len()` revisa cada carácter de cada palabra.
    - El espacio es O(n), guardando n longitudes en la lista resultante.

Casos límite:
    - Cadena vacía: ["" , "a"] -> [0, 1]
    - Una palabra: ["Python"] -> [6]
    - Palabras con espacios/puntuación: ["Hola, Mundo!"] -> [12]
    - Palabras muy largas: ["Hipopomonstrosesquipedaliofobia"] -> [34]

Casos de uso:
  - Análisis de textos: calcular estadísticas de palabras (longitud promedio).
  - Validación de entrada: verificar que contraseñas superen longitud mínima.
  - Procesamiento de logs: obtener longitudes de líneas para auditoría.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Calcular la longitud de palabras utilizando map().

    Usa `map()` con `len()` para obtener la longitud de cada palabra,
    emparejando cada palabra con su longitud y mostrando resultados.

    Returns:
        None
    """
    cadenas: list[str] = ["Manzana", "Python", "Hola, Mundo!", "Perro", "Hipopomonstrosesquipedaliofobia"] 
    resultado: list[int] = list(map(len, cadenas))
    for palabra, longitud in zip(cadenas, resultado):
        print(f"La palabra '{palabra}' tiene {longitud} caracteres.")

if __name__ == '__main__':
    main()
