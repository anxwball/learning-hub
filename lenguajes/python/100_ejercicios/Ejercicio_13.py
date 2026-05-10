"""
Problema  : Reemplazar un carácter en una cadena.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, metodos-de-string
Fecha     : 2026-05-09
Estado    : resuelto

Enfoque:
        - Definir una cadena base y usar `str.replace()` para sustituir un
            carácter específico por otro.
        - Mostrar la cadena original y la modificada para comparar el resultado
            de la operación de reemplazo.

Complejidad: Tiempo O(n) | Espacio O(n)
        - `replace()` recorre la cadena y construye una nueva, por lo que tiempo
            y espacio dependen linealmente de su longitud.

Casos límite:
        - Si el carácter objetivo no existe en la cadena, el resultado permanece
            sin cambios.
        - Si aparece múltiples veces, `replace()` sustituye todas las ocurrencias
            por defecto.
        - La operación distingue mayúsculas y minúsculas (`"o"` es distinto de
            `"O"`).

Casos de uso:
    - Limpieza de datos textuales antes de guardar o analizar.
    - Anonimización de fragmentos sensibles en cadenas.
    - Normalización de nombres, etiquetas o plantillas.

Revisión:
        - 2026-05-09: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Reemplazar un carácter en una cadena y mostrar el resultado.

    Crea una cadena de ejemplo, reemplaza un carácter usando `replace()` y
    muestra tanto la versión original como la modificada.

    Returns:
            None
    """
    cadena: str = "Python"
    nueva_cadena: str = cadena.replace("o", "x")

    print(f"Cadena original: {cadena}")
    print(f"Cadena modificada: {nueva_cadena}")

if __name__ == '__main__':
    main()
