"""
Problema  : Solicitar un número N al usuario y mostrar la tabla de
            multiplicar de ese número desde 1 hasta 12.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, bucles, tablas de multiplicar, aritmética
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Capturar un número del usuario.
    - Iterar desde 1 hasta 12 (inclusive), multiplicando el número ingresado
      por cada valor del contador y mostrando el resultado.
    - Aplicación clásica de bucles para generar tablas de consulta.
    - Útil para consolidar comprensión de bucles while y formateo de salida.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Itera exactamente 12 veces (operación constante, no depende de
      tamaño de entrada variable).
    - Espacio constante: solo variables de control y resultado.

Casos límite:
    - Número cero: la tabla muestra 0 × 1 a 0 × 12 (correcto).
    - Número negativo: la tabla muestra productos negativos (correcto
      aritméticamente).
    - Números grandes: sin restricción; Python maneja precisión
      arbitraria en enteros.

Casos de uso:
  - Herramienta educativa interactiva para aprender tablas de multiplicar.
  - Generación de tablas de referencia rápidas en tiempo de ejecución.
  - Demostración de bucles simples con formateo de salida.

Revisión:
    - 2026-05-10: Normalizado según patrón estándar del repositorio.
      Docstring de main() mejorado, type hints completados, sección de
      Casos de uso añadida, Complejidad y Enfoque expandidos.
      Enunciado del Problema reformatado para legibilidad.
"""

def main() -> None:
    """Mostrar la tabla de multiplicar de un número.

    Solicita al usuario un número entero, luego itera desde 1 hasta 12
    (inclusive) y muestra cada multiplicación del número por el contador,
    formateando la salida de manera clara y legible.

    Returns:
        None
    """
    print("Tabla de multiplicar\n")
    numero: int = int(input("Ingrese un número: "))
    contador: int = 1
    while contador <= 12:
        resultado: int = numero * contador
        print(f"{numero} x {contador} = {resultado}")
        contador += 1

if __name__ == '__main__':
    main()
