"""
Problema  : Imprimir los caracteres de una cadena con "for".
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, iteración, caracteres
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Iterar sobre una cadena (string) carácter por carácter usando un bucle `for`.
    - Demuestra que en Python las cadenas son iterables, permitiendo acceso
      secuencial a cada carácter sin necesidad de índices.
    - Introduce el concepto de cadenas como colecciones de caracteres y su
      naturaleza iterable.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal en relación a la longitud de la cadena.
    - El espacio es constante; solo se accede a caracteres uno a uno sin
      acumular estructura adicional.

Casos límite:
    - Cadenas vacías: el bucle simplemente no se ejecuta.
    - Cadenas con caracteres especiales o espacios: se itera correctamente
      sobre cada carácter, incluyendo espacios en blanco.
    - Cadenas con acentos o caracteres Unicode: Python 3 maneja esto sin problema.

Casos de uso:
  - Análisis de caracteres individuales en procesamiento de texto.
  - Validación de contenido carácter por carácter.
  - Transformación de cadenas mediante procesamiento elemento a elemento.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Iterar e imprimir caracteres de una cadena.

    Define una cadena literal ('Python') e itera sobre cada carácter
    usando un bucle `for`, imprimiendo cada uno en una línea separada.
    Ejemplifica la naturaleza iterable de las cadenas en Python.

    Returns:
        None
    """
    print("Caracteres de la cadena 'Python':\n")
    cadena: str = "Python"
    for caracter in cadena:
        print(caracter)


if __name__ == '__main__':
    main()
