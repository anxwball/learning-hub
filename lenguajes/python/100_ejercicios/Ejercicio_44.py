"""
Problema  : Generar un número aleatorio entre 1 y 10; luego solicitar al
            usuario que adivine el número hasta que lo logre.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, aleatoriedad, entrada interactiva
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Generar un número aleatorio usando random.randint() para el rango
      [1, 10].
    - Implementar un bucle interactivo que captura intentos del usuario
      hasta acertar.
    - Proporcionar retroalimentación comparativa (mayor/menor) para guiar
      al usuario.
    - Contar intentos y mostrar estadística final.

Complejidad: Tiempo O(k) | Espacio O(1)
    - k es el número de intentos (variable según entrada del usuario).
      En promedio, k ≈ log(n) para búsqueda óptima (binaria), pero sin
      guía ese promedio es mayor.
    - Espacio constante: solo variables de control.

Casos límite:
    - Primer intento correcto: se ejecuta 1 iteración (el contador se
      incrementa 0 veces dentro del bucle).
    - Muchos intentos: entrada del usuario puede incluir valores fuera
      del rango; sin validación, el programa continúa.
    - Números negativos o fuera de rango: no se validan; pueden generar
      comportamiento indefinido.

Casos de uso:
  - Juegos educativos interactivos y entretenimiento.
  - Demostración de aleatoriedad y retroalimentación en tiempo real.
  - Enseñanza de bucles controlados por entrada variable del usuario.

Revisión:
    - 2026-05-02: Corregida typo en Problema ("enntre" → "entre").
    - 2026-05-10: Normalizado según patrón estándar del repositorio.
      Docstring de main() mejorado, type hints completados, sección de
      Casos de uso añadida, Complejidad y Enfoque expandidos.
"""
import random

def main() -> None:
    """Juego de adivinanza de número aleatorio.

    Genera un número aleatorio en el rango [1, 10], luego solicita al
    usuario que lo adivine. Proporciona retroalimentación sobre si el
    número a adivinar es mayor o menor hasta que el usuario acierta.
    Registra y muestra el número de intentos realizados.

    Returns:
        None
    """
    print("Adivina el número entre 1 y 10!\n")
    num_aleatorio: int = random.randint(1, 10)
    respuesta: int = 0
    intentos: int = 0
    while respuesta != num_aleatorio:
        respuesta = int(input("Ingrese su respuesta: "))
        if respuesta < num_aleatorio:
            print("El número es mayor. Intente de nuevo.\n")
            intentos += 1
        elif respuesta > num_aleatorio:
            print("El número es menor. Intente de nuevo.\n")
            intentos += 1
    print(f"¡Felicidades! Has adivinado el número {num_aleatorio}.")
    print(f"Te tomó {intentos} intentos adivinar el número.")

if __name__ == '__main__':
    main()
