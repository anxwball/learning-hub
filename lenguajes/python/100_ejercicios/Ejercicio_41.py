"""
Problema  : Imprimir números del 1 al 10 en orden descendente.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, control de flujo
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
    - Iterar desde 10 hasta 1 usando un bucle while con decremento manual.
    - Demostrar cómo controlar bucles descendentes mediante condiciones
      de terminación y modificación de variables.
    - Patrón didáctico para comprender la relación entre variable de
      control, condición y actualización en bucles imperativos.

Complejidad: Tiempo O(n) | Espacio O(1)
    - Itera exactamente 10 veces (operación lineal en n=10), imprimiendo
      cada número; el espacio es constante ya que usa solo una variable
      de control.

Casos límite:
    - Rango desde 10 a 1: aplicable para cualquier rango descendente
      ajustando el inicio y la condición.
    - Si el rango es vacío (inicio < fin en descendente), el bucle no
      ejecuta, lo que es el comportamiento esperado.

Casos de uso:
  - Imprimir cuenta regresiva en juegos, temporizadores o simuladores.
  - Procesar listas o arrays en orden inverso de forma explícita.
  - Enseñar conceptos de bucles imperativos y control de flujo.

Revisión:
    - 2026-05-10: Normalizado según patrón estándar del repositorio.
      Docstring de main() mejorado, type hints completados, sección de
      Casos de uso añadida, Complejidad y Enfoque expandidos.
"""

def main() -> None:
    """Imprimir números del 1 al 10 en orden descendente.

    Inicializa un contador en 10 y decrementa su valor en cada iteración
    del bucle while hasta alcanzar 0. Imprime cada valor durante el
    recorrido, demostrando control de bucles descendentes.

    Returns:
        None
    """
    contador: int = 10
    while contador >= 1:
        print(contador)
        contador -= 1

if __name__ == '__main__':
    main()
