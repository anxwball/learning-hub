"""
Problema  : Verificar si una cadena tiene 10 o más caracteres.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, cadenas, condicionales
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Medir la longitud de una cadena con `len()` y compararla con el
            umbral definido.

Complejidad: Tiempo O(1) | Espacio O(1)
        - En CPython, la longitud de la cadena ya está almacenada en el objeto.

Casos límite:
        - Una cadena vacía no cumple la condición.
        - Exactamente 10 caracteres sí cumple la condición.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Verificar la longitud de una cadena y mostrar el resultado.

    Compara la longitud de una cadena de ejemplo con el valor 10 y muestra un
    mensaje según el resultado.

    Returns:
        None
    """
    cadena: str = input("Ingrese una cadena: ")

    if len(cadena) >= 10:
        print("La cadena es mayor o igual a 10 caracteres.")
        print(f"Longitud de la cadena: {len(cadena)}")
    else:
        print("La cadena es menor a 10 caracteres.")

if __name__ == '__main__':
    main()
