"""
Problema  : Función para crear un archivo de texto plano.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : archivos, io, operaciones-de-ficheros
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Crear una función que escribe contenido en un archivo de texto
      usando context manager (with statement) para manejo seguro.
    - Demuestra operaciones básicas de I/O: crear, escribir y cerrar
      archivos de forma automática.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es O(n), donde n es la longitud del contenido a escribir.
    - El espacio es O(1), no almacena datos en memoria significativamente.

Casos límite:
    - Archivo vacío: contenido="" -> archivo sin datos
    - Archivo con saltos de línea: "Línea1\nLínea2" -> archivo multilínea
    - Nombres especiales: "archivo.txt" vs "archivo_123.txt"
    - Contenido con caracteres especiales: "Hola, ¡Mundo!" -> preservado

Casos de uso:
  - Guardar logs de aplicaciones.
  - Exportar reportes o datos procesados.
  - Crear plantillas o archivos de configuración.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""
def crear_archivo(nombre_archivo: str, contenido: str) -> None:
    """Crear un archivo de texto plano con contenido.

    Args:
        nombre_archivo (str): Nombre del archivo a crear.
        contenido (str): Contenido a escribir en el archivo.

    Returns:
        None
    """
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)


def main() -> None:
    """Crear un archivo de texto plano.

    Llama crear_archivo() para crear un archivo con contenido
    de ejemplo.

    Returns:
        None
    """
    crear_archivo('archivo_ejemplo.txt', 'Este es un archivo de texto plano creado desde Python.')

if __name__ == '__main__':
    main()
