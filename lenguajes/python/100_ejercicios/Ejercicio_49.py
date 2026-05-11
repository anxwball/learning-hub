"""
Problema  : Simular el lanzamiento de un dado hasta obtener el 6.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, aleatorio, bucles
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Simular lanzamientos de dado con `random.randint` hasta obtener
      el valor 6, contabilizando y mostrando cada intento.

Complejidad: Tiempo O(k) | Espacio O(1) (k = número de lanzamientos)

Casos límite:
    - El número de intentos es aleatorio; el programa termina cuando se
      obtiene un 6.

Casos de uso:
  - Ejemplos didácticos para bucles controlados por condición y uso de
    generación aleatoria.

Revisión:
    - 2026-05-10: Normalizado. Añadidos type hints y docstring de `main`.

"""
import random


def main() -> None:
    """Simular lanzamientos de un dado hasta obtener un 6.

    Muestra el resultado de cada lanzamiento y el conteo total de
    intentos cuando aparece el 6.

    Returns:
        None
    """
    print("Simulación de lanzamiento de dado\n")
    lanzamiento: int = 0
    intentos: int = 0
    while lanzamiento != 6:
        lanzamiento = random.randint(1, 6)
        intentos += 1
        print(f"Lanzamiento {intentos}: {lanzamiento}")
    print(f"¡Se obtuvo un 6 después de {intentos} intentos!")


if __name__ == '__main__':
    main()
