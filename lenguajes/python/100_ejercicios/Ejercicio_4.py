"""
Problema  : Crear lista con diferentes elementos e imprimirla.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas, tipos
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
        - Crear una lista con elementos de distintos tipos (`int`, `str`,
            `float`, `bool`) y mostrarla en consola. Ejemplo didáctico con valores
            constantes para ilustrar la estructura de datos y la anotación de tipos.

Complejidad: Tiempo O(n) | Espacio O(n)
        - La complejidad depende del número de elementos en la lista; crear o
            copiar la lista requiere espacio y tiempo lineal en su longitud.

Casos límite:
        - Versión actual: lista definida en el código, por lo que no hay
            validación en tiempo de ejecución.
        - Si se acepta entrada dinámica, validar tipos de elemento y gestionar
            `None` o entradas inválidas. Para listas muy grandes, vigilar el uso
            de memoria.

Revisión:
        - 2026-05-02: Documentación completada y anotaciones de tipo añadidas.
"""
from typing import List, Union

def main():
    """Crear y mostrar una lista con elementos de distintos tipos.

    Define una lista local `lista_1` que contiene varios tipos (`int`,
    `str`, `float`, `bool`), imprime su contenido y demuestra la anotación
    de tipos con `typing.List` y `typing.Union`. Diseñada como ejemplo
    didáctico; no recibe argumentos ni devuelve valor.

    Returns:
        None
    """
    lista_1: List[Union[int, str, float, bool]] = [1, "Dos", 3.0, True, False]

    print(f"La lista es: {lista_1}")

if __name__ == '__main__':
    main()
