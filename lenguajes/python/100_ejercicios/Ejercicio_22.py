"""
Problema  : Dividir una cadena en una lista de subcadenas.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, metodos-de-string
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Usar `split()` para separar una cadena en partes a partir de un
            delimitador y mostrar la lista resultante.

Complejidad: Tiempo O(n) | Espacio O(n)
        - La operación recorre la cadena y crea una nueva lista con las partes
            obtenidas.

Casos límite:
        - Si el delimitador no existe, la lista contiene la cadena completa.
        - Separadores consecutivos pueden producir elementos vacíos.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Dividir una cadena y mostrar las subcadenas.

    Usa `split()` para separar el texto de ejemplo en una lista de palabras y
    mostrar el resultado por consola.

    Returns:
        None
    """
    cadena = "Python es genial!"
    subcadenas = cadena.split()

    print(f"Cadena original: {cadena}")
    print(f"Subcadenas: {subcadenas}")

if __name__ == '__main__':
    main()
