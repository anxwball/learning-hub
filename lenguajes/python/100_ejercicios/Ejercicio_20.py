"""
Problema  : Encontrar y mostrar el último carácter de una cadena.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Acceder al último elemento de la cadena mediante índice negativo y
            mostrarlo por consola.

Complejidad: Tiempo O(1) | Espacio O(1)
        - El acceso por índice negativo es una operación directa sobre la
            cadena.

Casos límite:
        - Si la cadena está vacía, acceder al último carácter produciría un
            `IndexError`.
        - Para cadenas de un solo carácter, el último carácter coincide con el
            único elemento.

Casos de uso:
    - Revisar sufijos de códigos, archivos o tokens.
    - Validar marcas finales en identificadores o cadenas de control.
    - Extraer el carácter final para reglas simples de formato.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Obtener y mostrar el último carácter de una cadena de ejemplo.

    Usa el índice `-1` para acceder al último carácter de la cadena.

    Returns:
        None
    """
    cadena: str = "Python!"
    ultimo_caracter: str = cadena[-1]
    print(f"Cadena: {cadena}")
    print(f"Último caracter: {ultimo_caracter}")

if __name__ == '__main__':
    main()
