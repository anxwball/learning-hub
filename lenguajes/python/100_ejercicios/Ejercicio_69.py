"""
Problema  : Función para calcular la tasa de desempleo.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, estadistica, porcentajes, validacion, economia
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Calcular la tasa de desempleo usando la fórmula:
      tasa (%) = (desempleados / población_activa) * 100.
    - Obtener población_activa y desempleados mediante entrada del usuario.
    - Implementar validaciones defensivas:
      • población_activa > 0 (evita división por cero).
      • desempleados >= 0 (no puede ser negativo).
    - Devolver el porcentaje con formato legible (dos decimales).
    - Demuestra entrada, validación múltiple, y cálculos porcentuales.

Complejidad: Tiempo O(1) | Espacio O(n)
    - Donde n es la longitud de la cadena de salida.
    - Cálculo aritmético es O(1); la cadena con formato es O(n).

Casos límite:
    - Población activa = 0: invalida → `ValueError`.
    - Población activa negativa: invalida → `ValueError`.
    - Desempleados = 0: tasa = 0% (sin desempleo, válido).
    - Desempleados > población_activa: tasa > 100% (ilógico, pero
      matemáticamente válido; considerar validación adicional).
    - Desempleados negativo: invalida → `ValueError`.

Casos de uso:
  - Estadísticas macroeconómicas: cálculo de tasa oficial de desempleo.
  - Informes económicos: análisis de datos laborales.
  - Dashboards de monitoreo económico: actualización de indicadores.
  - Ejemplos educativos de indicadores económicos y validación.

Revisión:
    - 2026-05-13: Encabezado expandido. Agregado `if __name__`. Tipado variable.
"""
def tasa_desempleo() -> float:
    """Calcula la tasa de desempleo.

    Returns:
        float: Tasa de desempleo como un porcentaje.

    Raises:
        ValueError: Si la población activa es menor o igual a cero, o si el número de desempleados es negativo.
    """
    poblacion_activa: int = int(input("Ingrese el número total de personas en la población activa: "))
    desempleados: int = int(input("Ingrese el número de personas desempleadas: "))

    if poblacion_activa <= 0:
        raise ValueError("La población activa debe ser mayor que cero.")
    if desempleados < 0:
        raise ValueError("El número de desempleados no puede ser negativo.")
    
    tasa: float = (desempleados / poblacion_activa) * 100
    return tasa


def main():
    """plantilla base"""
    resultado: float = tasa_desempleo()
    print(f"La tasa de desempleo es: {resultado:.2f}%")

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
