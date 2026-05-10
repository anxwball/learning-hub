"""
Problema  : Calcular 2 elevado a la 4a potencia sin usar el operador **.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, operadores, aritmética
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Usar la función `pow()` para calcular la potencia de forma directa
            y mostrar el resultado por consola.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El cálculo se resuelve con una operación aritmética fija, sin
            depender del tamaño de una entrada variable.

Casos límite:
        - Al trabajar con exponentes fijos, no hay variaciones de entrada que
            alteren el comportamiento del ejemplo.

Casos de uso:
    - Aplicar cálculos de escalado en capacidad o presupuesto.
    - Estimar crecimiento compuesto o expansión de recursos.
    - Generar resultados de referencia para fórmulas fijas.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Calcular 2 elevado a la 4a potencia y mostrar el resultado.

    Usa `pow(2, 4)` para obtener el valor sin recurrir al operador `**`.

    Returns:
        None
    """
    resultado: int = pow(2, 4)  # Se usa la función pow() para calcular la potencia
    print(f"2 elevado a la 4a potencia es: {resultado}")

if __name__ == '__main__':
    main()
