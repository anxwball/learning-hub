"""
Problema  : Crear una excepción que ayude a determinar si el índice de una lista está fuera de rango.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : excepciones, manejo-errores, validacion
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar try-except para capturar la excepción `IndexError` cuando se
      intenta acceder a un índice inválido en una lista.
    - Demuestra manejo de errores defensivo, proporcionando mensajes
      informativos cuando ocurren errores.

Complejidad: Tiempo O(1) | Espacio O(1)
    - El tiempo es constante, verificando acceso a un solo elemento.
    - El espacio es constante, sin dependencia del tamaño de la lista.

Casos límite:
    - Índice positivo válido: lista[0] en [1, 2, 3] -> exitoso
    - Índice negativo válido: lista[-1] -> último elemento
    - Índice demasiado grande: lista[10] en lista de 5 -> IndexError
    - Lista vacía: [][0] -> IndexError

Casos de uso:
  - Validación de entrada de usuario: verificar ándices antes de acceder.
  - Procesamiento defensivo: proteger accesos a datos potencialmente inválidos.
  - Depuración: mensajes claros sobre errores de acceso.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""

def main() -> None:
    """Capturar IndexError al acceder a índice fuera de rango.

    Intenta acceder a un índice inválido en una lista y captura
    la excepción IndexError, proporcionando un mensaje de error.

    Returns:
        None
    """
    lista: list[int] = [1, 2, 3, 4, 5]
    try:
        print(lista[10])
    except IndexError:
        print("Error: El índice está fuera de rango. Por favor, ingrese un índice válido.")

if __name__ == '__main__':
    main()
