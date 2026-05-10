"""
Problema  : Multiplicar una cadena por un número entero.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, operadores
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Repetir una cadena con el operador `*` para mostrar cómo Python
            replica el contenido textual de forma directa.

Complejidad: Tiempo O(n) | Espacio O(n)
        - El coste depende de la longitud del resultado generado, que crece
            proporcionalmente al número de repeticiones.

Casos límite:
        - Un multiplicador de cero produce una cadena vacía.
        - Un multiplicador negativo también produce una cadena vacía en Python.

Casos de uso:
    - Construir banners, separadores o contenido repetitivo en interfaces.
    - Generar plantillas de texto con relleno simple.
    - Repetir mensajes para prototipos o pruebas rápidas.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Multiplicar una cadena y mostrar el resultado.

    Usa el operador `*` para repetir una cadena varias veces y mostrar la
    versión resultante por consola.

    Returns:
        None
    """
    cadena: str = "Hola"
    resultado: str = cadena * 5
    print(f"Cadena original: {cadena}")
    print(f"Cadena multiplicada: {resultado}")

if __name__ == '__main__':
    main()
