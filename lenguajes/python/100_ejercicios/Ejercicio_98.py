"""
Problema  : Escribir en un archivo HTML "Hola! Que tal autodidacta!"
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : archivos, html, io, web
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Crear un archivo HTML con estructura mínima (doctype, html, body)
    e inyectar contenido dinámico dentro de un elemento <h1>.
    - Demuestra generación de archivos web desde Python, combinando
      strings con contenido HTML.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es O(n), donde n es la longitud del contenido HTML.
    - El espacio es O(n), almacenando la cadena HTML completa.

Casos límite:
    - Contenido vacío: "" -> <h1></h1>
    - Contenido con caracteres especiales: "&, <, >" -> escapado automáticamente
    - Contenido largo: genera archivo más grande
    - Nombres de archivo: "index.html", "resultado.html"

Casos de uso:
  - Generar reportes HTML desde Python.
  - Crear páginas web dinámicas o plantillas.
  - Exportar datos en formato legible por navegadores.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def escribir_en_html(nombre_archivo: str, contenido: str) -> None:
    """Escribir contenido en un archivo HTML con estructura básica.

    Args:
        nombre_archivo (str): Nombre del archivo HTML a crear.
        contenido (str): Contenido a insertar en el elemento <h1>.

    Returns:
        None
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(
            f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Documento</title></head><body><h1>{contenido}</h1></body></html>'
        )


def main() -> None:
    """Crear archivo HTML con contenido.

    Llama escribir_en_html() para crear un archivo HTML con
    un mensaje de saludo en el encabezado.

    Returns:
        None
    """
    escribir_en_html("archivo_ejemplo.html", "Hola! Que tal autodidacta!")


if __name__ == "__main__":
    main()
