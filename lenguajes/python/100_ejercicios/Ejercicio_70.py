"""
Problema  : Función para clasificar el pH de una sustancia (ácida, neutra o básica).
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, química, clasificación, validación, rango
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Obtener el valor de pH del usuario y clasificar en tres categorías:
      • Ácida: pH < 7
      • Neutra: pH == 7
      • Básica: pH > 7
    - Implementar validación: pH debe estar en rango [0, 14].
      Fuera de este rango es inválido en química estándar → `ValueError`.
    - Devolver clasificación como cadena descriptiva.
    - Demuestra entrada, validación de rango, y lógica condicional multi-rama.

Complejidad: Tiempo O(1) | Espacio O(n)
    - Donde n es la longitud de la cadena de clasificación devuelta.
    - Comparación y condicionales son O(1).

Casos límite:
    - pH = 0: ácida (extremo; ácido muy fuerte).
    - pH = 7: neutra exactamente (agua pura a 25°C).
    - pH = 14: básica (extremo; base muy fuerte).
    - pH < 0 o pH > 14: fuera de escala estándar → `ValueError`.
    - pH entre 0 y 7 (no 7): ácida (incluyendo pH muy cercano a 7).
    - pH entre 7 y 14 (no 7): básica.

Casos de uso:
  - Laboratorio: clasificación rápida de soluciones químicas (agua, ácidos, bases).
  - Aplicaciones de monitoreo: validación de pH en piscinas, tratamiento de agua.
  - Instrumentos de medición: interfaz de usuario para lectura de pH.
  - Ejemplos educativos de clasificación, validación, y lógica condicional.

Revisión:
    - 2026-05-13: Encabezado expandido. Agregado `if __name__`. Tipado variable.
"""
def clasificar_ph() -> str:
    """Clasifica el pH de una sustancia.

    Returns:
        str: "ácida" si el pH es menor que 7, "neutra" si el pH es igual a 7, y "básica" si el pH es mayor que 7.

    Raises:
        ValueError: Si el valor del pH es menor que 0 o mayor que 14.
    """
    ph: float = float(input("Ingrese el valor del pH: "))

    if ph < 0 or ph > 14:
        raise ValueError("El valor del pH debe estar entre 0 y 14.")
    
    if ph < 7:
        return "ácida"
    elif ph == 7:
        return "neutra"
    else:
        return "básica"


def main():
    """plantilla base"""
    resultado: str = clasificar_ph()
    print(f"La sustancia es: {resultado}")

if __name__ == '__main__':
    main()
