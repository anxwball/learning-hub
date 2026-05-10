"""
Problema  : Contar las ocurrencias de un carácter específico en una cadena.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Usar el método `count()` para calcular cuántas veces aparece un
            carácter dentro de la cadena.

Complejidad: Tiempo O(n) | Espacio O(1)
        - `count()` recorre la cadena una sola vez, por lo que el tiempo
            crece linealmente con su longitud.

Casos límite:
        - Si el carácter no aparece, el conteo es cero.
        - Si la cadena está vacía, el resultado también es cero.

Casos de uso:
    - Contar palabras clave o caracteres en logs y textos.
    - Analizar frecuencia de letras en validaciones o juegos.
    - Detectar patrones repetidos en cadenas de datos.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Contar la ocurrencia de un carácter en una cadena de ejemplo.

    Usa `count()` para mostrar cuántas veces aparece la letra `a`.

    Returns:
        None
    """
    cadena: str = "Programación"
    ocurrencias: int = cadena.count("a")

    print(f"Cadena: {cadena}")
    print(f"Ocurrencias de 'a' en la cadena: {ocurrencias}")

if __name__ == '__main__':
    main()
