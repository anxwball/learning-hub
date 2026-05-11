"""
Problema  : Calcular el IMC e interpretar el resultado.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Calcular índice de masa corporal (IMC) y clasificarlo según
      rangos estándar.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Altura igual a cero causaría división por cero; se asume entrada
      válida en este ejercicio didáctico.

Casos de uso:
  - Cálculo rápido de IMC en demostraciones educativas.

Revisión:
    - 2026-05-02: Normalización de docstring y anotaciones de tipo.
"""

def main() -> None:
    """Pide peso y altura, calcula el IMC e imprime la categoría.

    Returns:
        None
    """
    peso: float = float(input("Ingrese su peso en kilogramos: "))
    altura: float = float(input("Ingrese su altura en metros: "))

    imc: float = peso / pow(altura, 2)
    print(f"Su IMC es: {imc:.2f}")

    if imc < 18.5:
        print("Usted está por debajo del peso ideal.")
    elif 18.5 <= imc < 25:
        print("Usted tiene un peso normal.")
    elif 25 <= imc < 30:
        print("Usted tiene sobrepeso.")
    else:
        print("Usted tiene obesidad.")


if __name__ == '__main__':
    main()
