"""
Problema  : Convertir un número decimal a un número entero.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, conversion-de-tipos
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Aplicar `int()` sobre un valor decimal para truncar su parte
            fraccionaria y mostrar el resultado.

Complejidad: Tiempo O(1) | Espacio O(1)
        - La conversión es una operación directa sobre un valor escalar.

Casos límite:
        - Los valores positivos se truncan hacia cero.
        - Los valores negativos también se truncan hacia cero al convertirlos.

Casos de uso:
        - Truncar valores en reportes o cuadros de mando.
        - Convertir importes decimales a unidades enteras para conteos.
        - Simplificar datos antes de agregarlos a sistemas legados.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Convertir un decimal a entero y mostrar ambos valores.

    Usa `int()` para eliminar la parte decimal del número de ejemplo.

    Returns:
        None
    """
    decimal: float = 8.55
    entero: int = int(decimal)

    print(f"Decimal: {decimal}")
    print(f"Entero: {entero}")

if __name__ == '__main__':
    main()
