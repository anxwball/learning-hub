"""
Problema  : Escribir una función para calcular el tiempo de viaje dado la distancia y la velocidad.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, fisica, cinematica, validacion, entrada-usuario
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Calcular tiempo de viaje usando la fórmula: tiempo = distancia / velocidad
      (derivada de velocidad = distancia / tiempo).
    - Obtener distancia y velocidad mediante entrada interactiva del usuario.
    - Implementar validación defensiva: lanzar `ValueError` si velocidad <= 0
      para evitar división por cero o lógica física inválida.
    - Demuestra entrada de usuario, validación de precondiciones, y manejo
      de casos inválidos.

Complejidad: Tiempo O(1) | Espacio O(1)
    - División es operación primitiva O(1).
    - El espacio es constante; solo parámetros y resultado.

Casos límite:
    - Velocidad = 0: invalida (sin movimiento no hay tiempo determinado).
      → Lanza `ValueError` como es correcto.
    - Velocidad negativa: invalida en contexto físico (retroceso).
      → Lanza `ValueError` (podría permitirse con interpretación diferente).
    - Distancia = 0: tiempo = 0 (válido; viaje instantáneo).
    - Distancia negativa: sin sentido físico típico; idealmente validar > 0.
    - Entrada no numérica: `float()` lanza `ValueError`.

Casos de uso:
  - Aplicaciones de navegación: calcular ETA (tiempo de llegada estimado).
  - Simuladores de física: movimiento con velocidad constante.
  - Planificación de rutas: estimar duración de viajes.
  - Ejemplos educativos de física y validación de entrada.

Revisión:
    - 2026-05-13: Encabezado expandido. Docstring limpiado (entrada vía input).
"""
def tiempo_viaje() -> float:
    """Calcula el tiempo de viaje dado la distancia y la velocidad.

    Returns:
        float: El tiempo de viaje en horas.

    Raises:
        ValueError: Si la velocidad es menor o igual a cero.
    """
    distancia: float = float(input("Introduzca la distancia recorrida en kilómetros: "))
    velocidad: float = float(input("Introduzca la velocidad en kilómetros por hora: "))

    if velocidad <= 0:
        raise ValueError("La velocidad debe ser mayor que cero.")
    return distancia / velocidad


def main():
    """plantilla base"""
    resultado: float = tiempo_viaje()
    print(f"El tiempo de viaje es: {resultado:.4f} horas.")

if __name__ == '__main__':
    main()
