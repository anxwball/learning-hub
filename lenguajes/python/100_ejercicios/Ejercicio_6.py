"""
Problema  : Crear una cadena de texto y mostrar su longitud.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Mostrar el uso de la función incorporada `len()` para obtener la
      longitud de una cadena de forma inmediata y precisa.
    - El ejemplo usa una cadena constante para mantenerlo didáctico
      y directo, enfocado en la operación básica.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Calcular la longitud de una cadena mediante `len()` en CPython está
      optimizado a constante (la longitud está almacenada en el objeto).
      No depende de recorrer la cadena en este caso.

Casos límite:
    - Cadena vacía: la longitud debe ser 0.
    - Cadenas con espacios: se cuentan como caracteres individuales.
    - Caracteres especiales y multibyte (UTF-8): se cuentan correctamente
      según la representación Unicode en Python.

Revisión:
    - 2026-05-03: Normalizado el header y la documentación al formato
      estándar del repositorio.
    - Aclarado que `len()` es O(1) en CPython por optimización interna,
      facilitando comprensión de eficiencia.
"""

def main():
    """Calcular y mostrar la longitud de una cadena.

    Define una cadena de ejemplo, calcula su longitud con la función
    incorporada `len()` y muestra el resultado formateado. Demuestra
    cómo acceder a propiedades básicas de estructuras de datos.

    Returns:
        None
    """
    cadena: str = "Hola Mundo!"
    longitud: int = len(cadena)

    print(f"La longitud de la cadena '{cadena}' es: {longitud}")


if __name__ == '__main__':
    main()
