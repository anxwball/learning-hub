"""
Problema  : Convertir una lista de cadenas que sean números a enteros usando map().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, conversión-tipos, map
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar `map()` con la función incorporada `int()` para convertir cadenas
      numéricas a enteros automáticamente.
    - Demuestra conversión de tipos en masa sin bucles explícitos, aplicable
      a lecturas de archivo o entrada de usuario.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, procesando cada una de las n cadenas.
    - El espacio es lineal, creando una lista de n enteros.

Casos límite:
    - Lista vacía: [] -> []
    - Un elemento: ["42"] -> [42]
    - Números negativos: ["-5", "-10"] -> [-5, -10]
    - Ceros: ["0", "00"] -> [0, 0]

Casos de uso:
  - Lectura de entrada: convertir entrada de usuario (siempre strings) a números.
  - Parsing de archivos: convertir columnas de CSV a valores numéricos.
  - API responses: transformar arrays JSON de strings a enteros.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Convertir cadenas numéricas a enteros usando map().

    Utiliza `map()` con `int()` para transformar una lista de strings
    que contienen números en una lista de enteros, sin usar bucles.

    Returns:
        None
    """
    cadenas: list[str] = ["1", "2", "3", "4", "5"]
    resultado: list[int] = list(map(int, cadenas))
    print(f"Cadenas originales: {cadenas}")
    print(f"Enteros convertidos: {resultado}")

if __name__ == '__main__':
    main()
