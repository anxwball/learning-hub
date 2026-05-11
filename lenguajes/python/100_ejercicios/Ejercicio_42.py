"""
Problema  : Solicitar un número N al usuario y mostrar la suma de todos
            los números desde 1 hasta ese número.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, aritmética, acumulación
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Capturar entrada del usuario y validarla como entero positivo.
    - Usar acumulador (suma) para agregar valores en iteraciones sucesivas.
    - Demostrar el patrón de bucle con contador ascendente y acumulación.
    - Aplicación didáctica de la fórmula n*(n+1)/2, aunque implementada
      iterativamente para ilustrar bucles.

Complejidad: Tiempo O(n) | Espacio O(1)
    - Itera n veces, realizando suma constante en cada iteración.
    - Espacio constante: solo se usan dos variables (suma, contador).

Casos límite:
    - Número negativo: el bucle no se ejecuta (suma = 0). Considerar
      validación y mensajes de error si se requiere.
    - Número cero: suma es 0 (correcto, suma de enteros desde 1 a 0).
    - Números grandes: Python maneja enteros de precisión arbitraria,
      pero el tiempo aumenta linealmente.

Casos de uso:
  - Calcular sumas de progresiones aritméticas simples.
  - Verificar fórmulas matemáticas mediante implementación iterativa.
  - Educación sobre acumuladores y bucles controlados por entrada.

Revisión:
    - 2026-05-10: Normalizado según patrón estándar del repositorio.
      Docstring de main() mejorado, type hints completados, sección de
      Casos de uso añadida, Complejidad y Enfoque expandidos.
"""

def main() -> None:
    """Calcular la suma de números desde 1 hasta N.

    Solicita al usuario un número entero, itera desde 1 hasta ese número
    (inclusive) usando un acumulador, y muestra la suma total. Exemplifica
    el patrón de acumulación en bucles while.

    Returns:
        None
    """
    numero: int = int(input("Ingrese un número: "))
    suma: int = 0
    contador: int = 1
    while contador <= numero:
        suma += contador
        contador += 1
    print(f"La suma de los números desde 1 hasta {numero} es: {suma}")

if __name__ == '__main__':
    main()
