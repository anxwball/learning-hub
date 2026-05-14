"""
Problema  : Escribir una función para verificar si un número es par o impar.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, condicionales, operador módulo, clasificación
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Utilizar el operador módulo `%` para determinar la paridad de un entero.
    - Un número es par si `numero % 2 == 0`; impar si `numero % 2 != 0`.
    - Devolver un mensaje textual descriptivo que incluya el número y su
      clasificación, mejorando legibilidad de salida.
    - Demuestra el patrón de "clasificación" mediante condicionales simples.

Complejidad: Tiempo O(1) | Espacio O(n)
    - Donde n es la longitud de la cadena de resultado.
    - El cálculo de módulo es O(1) (operación primitiva).
    - El espacio depende de la cadena generada para el mensaje.

Casos límite:
    - Número negativo par (-2, -4...): `numero % 2 == 0` devuelve True
      correctamente (paridad se define en números negativos).
    - Cero: `0 % 2 == 0`, por lo que se clasifica correctamente como par.
    - Número negativo impar (-1, -3...): `numero % 2 != 0` funciona correctamente.

Casos de uso:
  - Algoritmos que necesitan procesar pares e impares por separado (coloreo
      de tableros, turnos).
  - Filtrado de datos en listas según paridad (índices, IDs).
  - Ejemplo educativo de condicionales y operador módulo.

Revisión:
    - 2026-05-13: Encabezado expandido. Docstring normalizado.
"""
def es_par_o_impar(numero: int) -> str:
    """Determina si un número es par o impar.

    Args:
        numero (int): El número a evaluar.

    Returns:
        str: Un mensaje indicando si el número es par o impar.
    """
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."

def main():
    """plantilla base"""
    resultado: str = es_par_o_impar(10)
    print(resultado)

if __name__ == '__main__':
    main()
