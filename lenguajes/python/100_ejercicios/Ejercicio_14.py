"""
Problema  : Pasar una cadena de mayúsculas a minúsculas.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, metodos-de-string
Fecha     : 2026-05-09
Estado    : resuelto

Enfoque:
        - Definir una cadena en mayúsculas y convertirla a minúsculas con el
            método `lower()`.
        - Imprimir ambos valores para visualizar el cambio y reforzar el uso de
            métodos de transformación de texto.

Complejidad: Tiempo O(n) | Espacio O(n)
        - La conversión recorre la cadena y crea una nueva representación en
            minúsculas, con coste lineal según su longitud.

Casos límite:
        - Si la cadena ya está en minúsculas, el contenido efectivo no cambia.
        - Caracteres no alfabéticos (números, signos) se mantienen igual.
        - El comportamiento depende de reglas Unicode para ciertos caracteres
            especiales.

Casos de uso:
    - Normalizar texto antes de búsquedas o filtros.
    - Estandarizar etiquetas, usuarios o categorías.
    - Preparar contenido para comparaciones sin sensibilidad de caso.

Revisión:
        - 2026-05-09: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Convertir una cadena a minúsculas y mostrar el resultado.

    Toma una cadena de ejemplo en mayúsculas, aplica `lower()` y muestra por
    consola la cadena original junto con la versión convertida.

    Returns:
            None
    """
    cadena: str = "PYTHON"
    nueva_cadena: str = cadena.lower()
    
    print(f"Cadena original: {cadena}")
    print(f"Cadena modificada: {nueva_cadena}")

if __name__ == '__main__':
    main()
