"""
Problema  : Calcular máximo de tres números.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Lectura de tres números enteros desde entrada estándar y uso de
      la función incorporada `max()` para obtener el mayor.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Entradas no numéricas generan `ValueError` si se dejan sin validar.

Casos de uso:
  - Comparaciones simples entre tres métricas o valores numéricos.

Revisión:
    - 2026-05-02: Normalización de docstring y anotaciones de tipo.
"""

def main() -> None:
    """Lee tres enteros y muestra el máximo.

    Reads three integers from stdin and prints the maximum among them.

    Returns:
        None
    """
    num1: int = int(input("Ingrese el primer número: "))
    num2: int = int(input("Ingrese el segundo número: "))
    num3: int = int(input("Ingrese el tercer número: "))

    maximo: int = max(num1, num2, num3)
    print(f"El número máximo es: {maximo}")


if __name__ == '__main__':
    main()
