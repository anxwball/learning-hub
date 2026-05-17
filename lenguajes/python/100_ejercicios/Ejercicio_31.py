"""
Problema  : Pedir un número y verificar si es positivo, negativo o cero.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, condicionales, io
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Leer un número desde consola y clasificarlo con condicionales según
            su signo.

Complejidad: Tiempo O(1) | Espacio O(1)
        - La decisión se toma con un número fijo de comparaciones.

Casos límite:
        - Un valor igual a cero cae en la rama específica de cero.
        - Entradas no numéricas provocan `ValueError` durante la conversión.

Casos de uso:
    - Clasificar saldos, métricas o indicadores con umbral cero.
    - Validar estados básicos en formularios financieros o educativos.
    - Separar resultados en categorías de signo simple.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Clasificar un número por su signo y mostrar el resultado.

    Solicita un número por consola y evalúa si es positivo, negativo o cero.

    Returns:
        None
    """
    numero: float = float(input("Ingrese un número: "))
    if numero > 0:
        print(f"El número {numero} es positivo.")
    elif numero < 0:
        print(f"El número {numero} es negativo.")
    else:
        print("El número es cero.")

if __name__ == '__main__':
    main()
