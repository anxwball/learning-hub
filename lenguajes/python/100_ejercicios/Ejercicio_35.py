"""
Problema  : Comprobar si un número está en el rango de 0 a 100.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, condicionales, operadores, io
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Leer un número y validar con comparaciones encadenadas si está dentro
            del intervalo cerrado de 0 a 100.

Complejidad: Tiempo O(1) | Espacio O(1)
        - La verificación requiere un número fijo de comparaciones.

Casos límite:
        - Los extremos 0 y 100 sí pertenecen al rango.
        - Entradas no numéricas provocan `ValueError` al convertir.

Casos de uso:
        - Comprobar si una puntuación cae dentro de un rango válido.
        - Validar notas, porcentajes o indicadores de aceptación.
        - Aplicar reglas de control sobre valores de entrada.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main() -> None:
    """Comprobar si un número está en el rango de 0 a 100.

    Solicita un valor por consola y verifica si pertenece al intervalo usando
    comparaciones simples.

    Returns:
        None
    """
    num: int = int(input("Ingrese un número: "))
    if num >= 0 and num <= 100:
        print(f"El número {num} está en el rango de 0 a 100.")

if __name__ == '__main__':
    main()
