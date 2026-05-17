"""
Problema  : Calcular el área de un rectángulo a partir de base y altura.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, geometria, io
Fecha     : 2026-05-09
Estado    : resuelto

Enfoque:
        - Solicitar `base` y `altura` al usuario, convertir ambas entradas a
            `float`, multiplicarlas y mostrar el área resultante.
        - Se prioriza claridad didáctica para practicar entrada estándar,
            conversión de tipos y operaciones aritméticas básicas.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El programa realiza un número constante de operaciones y usa memoria
            constante independientemente de los valores ingresados.

Casos límite:
        - Entradas no numéricas provocan `ValueError` durante la conversión a
            `float`.
        - Valores negativos son aceptados por el script, aunque en un contexto
            geométrico normalmente se validaría `base >= 0` y `altura >= 0`.
        - Si `base` o `altura` es 0, el área resultante es 0.

Casos de uso:
    - Cálculo de áreas para diseño, arquitectura o jardinería.
    - Estimar materiales en superficies circulares.
    - Practicar fórmulas geométricas en cursos introductorios.

Revisión:
    - 2026-05-09: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Calcular y mostrar el área de un rectángulo.

    Pide al usuario la base y la altura, convierte ambos valores a `float`,
    calcula el área mediante una multiplicación y muestra el resultado en
    consola.

    Returns:
        None
    """
    print("Calcular el área de un rectángulo\n")
    base: float = float(input("Ingrese la base del rectángulo: "))
    altura: float = float(input("Ingrese la altura del rectángulo: "))
    area: float = float(base) * float(altura)

    print(f"El área del rectángulo es: {area}")

if __name__ == '__main__':
    main()
