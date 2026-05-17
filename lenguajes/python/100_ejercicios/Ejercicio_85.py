"""
Problema  : Contar el número de vocales en una lista de palabras utilizando map().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, map, análisis-de-strings
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Aplicar `map()` a una lista de palabras con una función personalizada
      que cuenta vocales en cada palabra.
    - Demuestra análisis de strings usando funciones de orden superior,
      combinando `map()` con lógica de procesamiento de caracteres.

Complejidad: Tiempo O(n*m) | Espacio O(n)
    - El tiempo es O(n*m), donde n es el número de palabras y m es la longitud
      promedio; cada palabra se itera carácter por carácter.
    - El espacio es O(n), almacenando n conteos de vocales.

Casos límite:
    - Palabra sin vocales: "xyz" -> 0
    - Palabra solo vocales: "aeiou" -> 5
    - Cadena vacía: "" -> 0
    - Mayúsculas/minúsculas: "AEIOu" -> 5 (normalizadas con lower())

Casos de uso:
  - Análisis lingüístico: estadísticas de vocales en textos.
  - Validación: verificar balance de vocales en inputs.
  - Procesamiento de poesía: análisis de patrones vocálicos.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""
def contar_vocales(palabra: str) -> int:
    """Cuenta el número de vocales en una palabra.

    Args:
        palabra (str): La palabra a analizar.
    
    Returns:
        int: El conteo de vocales en la palabra.
    """
    vocales: set[str] = {"a", "e", "i", "o", "u"}
    contador: int = 0
    for letra in palabra.lower():
        if letra in vocales:
            contador += 1
    return contador

def main() -> None:
    """Contar vocales en una lista de palabras usando map().

    Aplica contar_vocales() a cada palabra en la lista utilizando map(),
    mostrando pares de palabra-cantidad de vocales.

    Returns:
        None
    """
    lista_palabras: list[str] = ["Manzana", "Python", "Hola, Mundo!", "Perro", "Hipopomonstrosesquipedaliofobia"]
    resultado: list[int] = list(map(contar_vocales, lista_palabras))
    for palabra, num_vocales in zip(lista_palabras, resultado):
        print(f"La palabra '{palabra}' tiene {num_vocales} vocales.")

if __name__ == '__main__':
    main()
