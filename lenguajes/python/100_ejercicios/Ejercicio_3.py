"""
Problema  : Concatenar dos cadenas de texto.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, concatenacion
Fecha     : 2026-05-02
Estado    : resuelto

Enfoque:
    - Mostrar la concatenación de dos cadenas usando el operador `+`.
    - Ejemplo didáctico que utiliza valores constantes para enfatizar la
      operación básica de concatenación y la salida formateada.
    - Introduce f-strings como formato recomendado para legibilidad en
      salidas complejas.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo y espacio dependen de la longitud total de las cadenas
      concatenadas; la operación crea una nueva cadena de tamaño sumatorio.

Casos límite:
    - Versión actual: cadenas constantes sin validación en tiempo de ejecución.
    - Si se recibe entrada dinámica, validar tipos (asegurar que son cadenas)
      y considerar entradas vacías o `None`.
    - Para concatenaciones repetidas en bucles, preferir `str.join()` o
      acumuladores para evitar costes cuadráticos.

Casos de uso:
  - Construcción de mensajes automáticos en interfaces o notificaciones.
  - Composición de nombres completos, títulos o rutas legibles.
  - Unir fragmentos textuales en flujos de generación de contenido.

Revisión:
    - 2026-05-02: Documentación completada con estructura estándar del
      repositorio; enfatiza operador `+` para cadenas.
    - Mejora: usar f-strings para concatenación legible y eficiente.
      Extensible a entrada dinámica con validación de tipos.
"""

def main() -> None:
    """Concatenar dos cadenas y mostrar el resultado.

    Define dos variables de cadena con valores constantes, concatena ambas
    (añadiendo un espacio intermedio) y muestra la cadena resultante por
    consola usando f-string para claridad en la salida formateada.

    Returns:
        None
    """
    cadena_1: str = "Hola"
    cadena_2: str = "Mundo!!"
    concatenacion: str = cadena_1 + " " + cadena_2

    print(f"La cadena es: {concatenacion}")

if __name__ == '__main__':
    main()
