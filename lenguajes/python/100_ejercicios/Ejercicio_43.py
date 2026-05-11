"""
Problema  : Solicitar al usuario un número N y mostrar el factorial de
            ese número.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, aritmética, factoriales
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Capturar número del usuario e iterar desde 1 hasta n (inclusive).
    - Usar acumulador multiplicativo para calcular el factorial de forma
      iterativa (n! = 1 × 2 × 3 × ... × n).
    - Demostrar el patrón de acumulación multiplicativa en contraposición
      a la adición del ejercicio anterior.
    - Importante: crecimiento factorial muy rápido para n > 20.

Complejidad: Tiempo O(n) | Espacio O(1)
    - Itera exactamente n veces, multiplicando en cada paso.
    - Espacio constante: solo variables de control y acumulador.

Casos límite:
    - Número cero: factorial de 0 es 1 por definición (correcto, el bucle
      no itera y devuelve el valor inicial 1).
    - Número negativo: el bucle no se ejecuta, devolviendo 1 incorrecto.
      Considerar validación.
    - Números grandes (n > 20): factorial crece exponencialmente; Python
      maneja la precisión, pero puede ser lento.

Casos de uso:
  - Cálculos combinatorios y permutaciones simples.
  - Validar fórmulas de combinatoria mediante computación iterativa.
  - Educación sobre acumuladores multiplicativos y bucles.

Revisión:
    - 2026-05-10: Normalizado según patrón estándar del repositorio.
      Docstring de main() mejorado, type hints completados, sección de
      Casos de uso añadida, Complejidad y Enfoque expandidos.
"""

def main() -> None:
    """Calcular el factorial de un número N.

    Solicita al usuario un número entero positivo, itera desde 1 hasta
    ese número multiplicando sucesivamente cada valor en un acumulador,
    y muestra el factorial resultante.

    Returns:
        None
    """
    num: int = int(input("Ingrese un número: "))
    factorial: int = 1
    contador: int = 1
    while contador <= num:
        factorial *= contador
        contador += 1
    print(f"El factorial de {num} es: {factorial}")

if __name__ == '__main__':
    main()
