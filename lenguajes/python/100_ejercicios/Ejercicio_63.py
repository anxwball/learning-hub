"""
Problema  : Escribir una función para generar un mensaje de saludo personalizado.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, f-strings, personalización
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Crear una función que acepte un parámetro `nombre` y devuelva un
      saludo personalizado usando f-strings (format strings).
    - Demuestra interpolación de variables en cadenas de forma legible y
      pythonica mediante f-strings (f"...").
    - Función pura que devuelve una cadena sin efectos secundarios, permitiendo
      reutilización en diferentes contextos (UI, APIs, logs).

Complejidad: Tiempo O(n) | Espacio O(n)
    - Donde n es la longitud de `nombre`. El tiempo depende de la creación
      de la cadena resultante.
    - El espacio es O(n) porque el resultado es una nueva cadena que contiene
      la interpolación.

Casos límite:
    - Nombre vacío: devuelve "¡Hola, !" (válido pero poco útil).
      Considerar validación si se requiere nombre no vacío.
    - Nombre muy largo: genera correctamente la cadena sin truncamiento.
    - Caracteres especiales, acentos, emojis: Python 3 maneja Unicode nativo,
      por lo que estos se interpolan correctamente.

Casos de uso:
  - Saludos personalizados en chatbots, asistentes virtuales.
  - Generación de mensajes en aplicaciones interactivas (CLI, web).
  - Base para patrones de personalización de mensajes en sistemas.

Revisión:
    - 2026-05-13: Encabezado expandido. Docstring completado con parámetro.
"""
def saludo(nombre: str) -> str:
    """Genera un mensaje de saludo.

    Args:
        nombre (str): El nombre a incluir en el saludo.

    Returns:
        str: Un mensaje de saludo personalizado.
    """
    return f"¡Hola, {nombre}!"

def main():
    """plantilla base"""
    mensaje: str = saludo("Mundo")
    print(mensaje)

if __name__ == '__main__':
    main()
