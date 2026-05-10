"""
Problema  : Crear una tupla con elementos y mostrar su contenido.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, tuplas
Fecha     : 2026-05-03
Estado    : resuelto

Enfoque:
    - Demostrar la creación de una tupla heterogénea y cómo imprimir
      su contenido de forma clara.
    - El ejemplo usa una tupla constante para mantener la explicación
      simple y enfocada en la estructura inmutable de datos.
    - Contraste implícito con listas (ejercicio 4) para evidenciar
      diferencias de mutabilidad.

Complejidad: Tiempo O(1) | Espacio O(1)
    - La construcción e impresión de una tupla de tamaño fijo es una
      operación constante respecto al cómputo principal del script.

Casos límite:
    - Tupla vacía: su impresión debe mostrar `()`.
    - Inmutabilidad: intentar modificar elementos generará excepciones
      (`TypeError`). Para operaciones mutables, usar listas.
    - Tupla con un solo elemento: requiere sintaxis especial `(x,)` para
      diferenciar de paréntesis de expresión.

Casos de uso:
  - Representar coordenadas o puntos fijos en mapas y gráficas.
  - Guardar configuraciones que no deben cambiar durante la ejecución.
  - Modelar registros inmutables en catálogos o resultados calculados.

Revisión:
    - 2026-05-03: Ajustado header y documentación al formato estándar
      del repositorio.
    - Mejora didáctica: enfatiza inmutabilidad como diferenciador clave
      respecto a listas.
"""

def main():
    """Crear una tupla de ejemplo y mostrar su contenido.

    Define una tupla heterog\u00e9nea (contiene m\u00faltiples tipos: str, int,
    bool, float) y la imprime por consola. Demuestra la sintaxis de tuplas
    y su naturaleza inmutable como estructura de datos.

    Returns:
        None
    """
    tupla: tuple = ("manzana", 1, False, 3.47, 6**2)

    print(f"Contenido de la tupla: {tupla}")


if __name__ == '__main__':
    main()
