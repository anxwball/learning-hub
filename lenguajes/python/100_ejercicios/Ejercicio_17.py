"""
Problema  : Extraer una subcadena de una cadena dada.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Usar rebanado (`slice`) para obtener segmentos concretos de la
            cadena y mostrarlos por consola.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El acceso por índices y la creación de subcadenas tienen coste fijo
            para este ejemplo de tamaño acotado.

Casos límite:
        - Si los índices quedan fuera del rango, Python ajusta el rebanado sin
            lanzar error en la mayoría de los casos.
        - Una cadena vacía produciría subcadenas vacías.

Casos de uso:
    - Extraer códigos, prefijos o sufijos de identificadores.
    - Parsear fragmentos de texto en flujos de integración.
    - Mostrar subconjuntos de cadenas en vistas previas o análisis.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Extraer y mostrar dos subcadenas de una cadena base.

    Toma segmentos concretos con rebanado para ilustrar el acceso a partes de
    una cadena.

    Returns:
        None
    """
    cadena: str = "Hola, Mundo!"
    subcadena: str = cadena[0:4]  # Extrae los primeros 4 caracteres.
    subcadena2: str = cadena[6:12]  # Extrae "Mundo!" de la cadena.
    print(f"Cadena original: {cadena}")
    print(f"Primera subcadena extraída: {subcadena}")
    print(f"Segunda subcadena extraída: {subcadena2}")

if __name__ == '__main__':
    main()
