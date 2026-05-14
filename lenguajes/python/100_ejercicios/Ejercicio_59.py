"""
Problema  : Pedir al usuario un número y mostrar la tabla de multiplicar de ese número del 1 al 12.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, entrada usuario, iteración
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Solicitar entrada del usuario, convertirla a entero y usar ese valor
      en iteraciones posteriores.
    - Generar y mostrar una tabla de multiplicar mediante un bucle que itera
      del 1 al 12, multiplicando el número ingresado por cada iterador.
    - Introduce interacción usuario-programa y cómo pasar datos de entrada
      a lógica de procesamiento iterativo.

Complejidad: Tiempo O(n) | Espacio O(1)
    - El tiempo es lineal; genera 12 productos (n=12 iteraciones fijas).
    - El espacio es constante; solo se almacenan variables numéricas.

Casos límite:
    - Número cero: 0 * 1..12 = siempre 0.
    - Números negativos: la tabla mostrará productos negativos.
    - Entrada no numérica: causará ValueError en `int()` (sin manejo en versión actual).
    - Números muy grandes: Python maneja precisión arbitraria sin problema.

Casos de uso:
  - Herramienta educativa para repasar tablas de multiplicar.
  - Generador rápido de secuencias aritméticas para cualquier número.
  - Base para ejercicios interactivos de matemáticas.

Revisión:
    - 2026-05-02: Normalizado. Añadidos type hints y docstring de `main`.
"""


def main() -> None:
    """Mostrar la tabla de multiplicar de un número ingresado por el usuario.

    Solicita al usuario que ingrese un número entero, luego itera del 1 al 12
    y muestra el producto de ese número por cada iterador. Ejemplifica
    entrada de usuario combinada con generación de secuencias iterativas.

    Returns:
        None
    """
    numero: int = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
    print(f"\nTabla de multiplicar del {numero}:\n")
    for multiplicador in range(1, 13):
        producto: int = numero * multiplicador
        print(f"{numero} × {multiplicador} = {producto}")


if __name__ == '__main__':
    main()
