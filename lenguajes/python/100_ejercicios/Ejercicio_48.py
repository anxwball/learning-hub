"""
Problema  : Simular el lanzamiento de una moneda.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, aleatorio, simulación
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Utilizar el módulo `random` para seleccionar aleatoriamente entre
      dos resultados: "Cara" o "Cruz".

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Sin entradas por parte del usuario; comportamiento determinado
      por el generador aleatorio del sistema.

Casos de uso:
  - Simulaciones simples, pruebas y ejemplos didácticos de generación
    de eventos aleatorios.

Revisión:
    - 2026-05-10: Normalizado. Añadidos type hints y docstring de `main`.

"""
import random


def main() -> None:
    """Simular un lanzamiento de moneda y mostrar el resultado.

    El resultado se elige aleatoriamente entre 'Cara' y 'Cruz'.

    Returns:
        None
    """
    moneda: str = random.choice(["Cara", "Cruz"])
    print(f"El resultado del lanzamiento de la moneda es: {moneda}")


if __name__ == '__main__':
    main()
