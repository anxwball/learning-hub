"""
Problema  : Verificar si la palabra ingresada es "Python".
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Lectura de una palabra y comparación insensible a mayúsculas.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Espacios en la entrada o mayúsculas/minúsculas; se normaliza con
      `str.lower()` antes de la comparación.

Casos de uso:
  - Validación simple de cadenas en entradas educativas.

Revisión:
    - 2026-05-02: Normalización de docstring, corrección de la
      comparación para ser insensible a mayúsculas.
"""

def main() -> None:
    """Pide una palabra y comprueba si es 'python' (sin distinguir case).

    Returns:
        None
    """
    palabra: str = input("Ingrese una palabra: ")
    if palabra.lower() == "python":
        print('La palabra ingresada es "python".')
    else:
        print('La palabra ingresada no es "python".')


if __name__ == '__main__':
    main()
