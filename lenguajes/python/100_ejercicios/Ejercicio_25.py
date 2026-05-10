"""
Problema  : Generar una lista de números del 1 al 200.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, listas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Construir una lista con `range()` y convertirla a `list` para mostrar
          una secuencia completa de enteros.

Complejidad: Tiempo O(n) | Espacio O(n)
        - El rango genera `n` valores y la lista final ocupa memoria lineal.

Casos límite:
        - Si el rango inicial supera al final, la lista resultante es vacía.
        - El ejemplo utiliza límites fijos para mantener la demostración simple.

Casos de uso:
        - Generar secuencias para pruebas, simulaciones o paginación.
        - Crear datos de ejemplo para tableros o gráficos.
        - Construir listas de rangos para procesamiento posterior.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""


def main() -> None:
        """Generar una lista de números y mostrarla.

        Crea una lista con los números del 1 al 200 usando `range()` y la imprime
        por consola.

        Returns:
                None
        """
        numeros: list[int] = list(range(1, 201))
        print(numeros)


if __name__ == '__main__':
        main()
