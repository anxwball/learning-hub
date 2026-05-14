"""
Problema  : Crear una función para calcular el volumen de un cilindro.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, geometría, fórmulas, módulo math, entrada de usuario
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Implementar la fórmula del volumen de cilindro: V = π * r² * h.
    - Accepta dos parámetros: radio (r) de la base y altura (h).
    - Utilizar `math.pi` para la constante π y `pow(radio, 2)` para la
      exponenciación.
    - Demuestra entrada interactiva del usuario con conversión a float y
      cálculos geométricos basados en fórmulas.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Cálculo aritmético primitivo: multiplicación, exponenciación.
    - El espacio es constante; solo parámetros y resultado temporal.

Casos límite:
    - Radio = 0: volumen es 0 (correctamente calculado: π * 0² * h = 0).
    - Altura = 0: volumen es 0 (cilindro sin altura es un disco sin volumen).
    - Valores negativos: producen resultado negativo. Idealmente validar
      que radio, altura > 0; lanzar `ValueError` si no.
    - Entrada inválida: `float()` lanza `ValueError` → propagar o capturar
      según contexto.

Casos de uso:
  - Ingeniería: cálculo de volúmenes de tuberías, tanques, cilindros.
  - Fabricación: determinar capacidad de recipientes cilíndricos.
  - Ejemplos educativos de geometría 3D y entrada/salida de usuario.

Revisión:
    - 2026-05-13: Encabezado expandido con casos límite y entrada de usuario.
"""
import math

def volumen_cilindro(radio: float, altura: float) -> float:
    """Calcula el volumen de un cilindro dado su radio y altura.

    Args:
        radio (float): El radio de la base del cilindro.
        altura (float): La altura del cilindro.

    Returns:
        float: El volumen del cilindro calculado usando la fórmula V = π * r^2 * h.
    """
    return math.pi * pow(radio, 2) * altura


def main():
    """plantilla base"""
    radio: float = float(input("Ingrese el radio del cilindro: "))
    altura: float = float(input("Ingrese la altura del cilindro: "))
    volumen: float = volumen_cilindro(radio, altura)
    print(f"El volumen del cilindro es: {volumen} unidades cúbicas.")


if __name__ == '__main__':
    main()
