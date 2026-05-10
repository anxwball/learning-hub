"""
Problema  : Calcular el área de un círculo dado su radio.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, geometría, matemáticas
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Calcular el área de un círculo usando la fórmula `pi * radio**2`.
    - Importar `math` para acceder a la constante `pi` de forma precisa.
    - Ejemplo didáctico con valores constantes para ilustrar el cálculo
      y la salida formateada con precisión controlada.

Complejidad: Tiempo O(1) | Espacio O(1)
    - El cálculo requiere una cantidad constante de operaciones y memoria,
      independientemente del valor del radio.

Casos límite:
    - Versión actual: el radio es una constante en el código, sin validación
      en tiempo de ejecución.
    - Si se cambia a entrada dinámica, validar que `radio >= 0` y manejar
      entradas no numéricas (capturar `ValueError`).
    - Para floats, considerar precisión de punto flotante en la representación
      y en los cálculos con `pi`.

Casos de uso:
  - Estimar superficies de terrenos circulares o espacios físicos.
  - Calcular material necesario para tapas, discos o paneles redondos.
  - Generar ejemplos de fórmulas matemáticas en cursos introductorios.

Revisión:
    - 2026-05-02: Documentación completada con estructura estándar del
      repositorio; incorpora uso de módulo `math`.
    - Mejora didáctica: formato de salida con `.2f` para legibilidad en
      contexto geométrico. Extensible a entrada dinámica con validación.
"""
import math

def main() -> None:
    """Calcular y mostrar el área de un círculo.

    Define una variable `radio` (float) con valor constante, calcula el área
    mediante la fórmula `math.pi * radio**2` y muestra el resultado con
    formato decimal de dos posiciones para claridad geométrica.

    Returns:
        None
    """
    radio: float = 5.0
    area: float = math.pi * radio ** 2

    print(f"El área del círculo con radio {radio} es: {area:.2f}")

if __name__ == '__main__':
    main()
