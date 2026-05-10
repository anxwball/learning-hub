"""
Problema  : Convertir un número entero en una cadena.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, conversion-de-tipos, entrada-salida
Fecha     : 2026-05-09
Estado    : resuelto

Enfoque:
        - Solicitar un número entero al usuario, convertirlo desde `str` a `int`
            para validar el tipo numérico y luego transformarlo a `str` con `str()`.
        - Mostrar el tipo antes y después de la conversión para reforzar el
            aprendizaje sobre tipos de datos en Python.

Complejidad: Tiempo O(1) | Espacio O(1)
        - Las conversiones y operaciones de salida son constantes para una única
            entrada.

Casos límite:
        - Entradas no enteras (por ejemplo, letras o decimales) generan
            `ValueError` al ejecutar `int(...)`.
        - Enteros muy grandes son válidos en Python, pero su representación como
            cadena crecerá proporcionalmente al número de dígitos.

Revisión:
        - 2026-05-09: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
        """Convertir un entero a cadena y mostrar el tipo resultante.

        Lee un número entero desde consola, imprime su tipo original, lo convierte
        a `str` y muestra nuevamente el tipo para evidenciar el cambio.

        Returns:
                None
        """
    print("\nConvertir un número entero en una cadena\n")
    numero: int = int(input("Ingrese un número entero: "))
    print(f"El tipo actual de número es: {type(numero)}")
    cadena: str = str(numero)
    print(f"\nSu numero se ha convertido a cadena. El tipo actual de numero es: {type(cadena)}\n")

if __name__ == '__main__':
    main()
