"""
Problema  : Crear una cadena de texto y mostrar su longitud.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Mostrar el uso de la función incorporada `len()` para obtener la
      longitud de una cadena. El ejemplo usa una cadena constante para
      mantenerlo didáctico y directo.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Calcular la longitud de una cadena mediante `len()` es una operación
      que en CPython está optimizada y no depende de entrada adicional
      en este ejemplo simple.

Casos límite:
    - Cadena vacía: la longitud debe ser 0.
    - Cadenas con espacios o caracteres especiales se cuentan como
      caracteres individuales según la representación de Python.

Revisión:
    - 2026-05-03: Normalizado el header y la documentación al formato
      utilizado en otros ejercicios.
"""

def main():
    """Ejemplo: calcular y mostrar la longitud de una cadena.

    Se define una cadena de ejemplo, se calcula su longitud con `len()` y
    se imprime el resultado formateado.

    Returns:
        None
    """
    cadena: str = "Hola Mundo!"
    longitud: int = len(cadena)

    print(f"La longitud de la cadena '{cadena}' es: {longitud}")


if __name__ == '__main__':
    main()
