"""
Problema  : Planificador de viajes según el clima.
Fuente    : freeCodeCamp Labs
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : fundamentos, condicionales, validacion
Fecha     : 2026-05-18
Estado    : resuelto

Enfoque:
    - Resolver la decisión de desplazamiento con una cadena de condicionales
      ordenada por tramos de distancia.
    - Evaluar primero el caso falsy, luego el tramo corto, el tramo medio y
      finalmente el tramo largo para mantener la lógica clara.
    - Conservar la salida booleana esperada por el laboratorio.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Distancia inexistente o falsy: se imprime `False`.
    - Distancia corta con lluvia: se imprime `False`.
    - Distancia media sin bicicleta: se imprime `False`.
    - Distancia larga sin automóvil ni app de viajes: se imprime `False`.

Casos de uso:
  - Determinar si conviene caminar una distancia corta sin lluvia.
  - Evaluar si un trayecto medio es viable en bicicleta.
  - Comprobar si un viaje largo requiere automóvil o app de transporte.

Revisión:
    - 2026-05-18: Encabezado documental agregado y lógica preservada en una
      función `main()` ejecutable.
"""


def main() -> None:
    """Determinar si el desplazamiento es posible según clima y distancia.

    Evalúa una distancia predefinida y las condiciones de lluvia y transporte
    disponible para imprimir un valor booleano acorde a las reglas del lab.

    Returns:
        None
    """
    distance_mi: int = 0
    is_raining: bool = False
    has_bike: bool = False
    has_car: bool = False
    has_ride_share_app: bool = False

    if not distance_mi:
        print(False)
    elif distance_mi <= 1:
        if is_raining:
            print(False)
        else:
            print(True)
    elif distance_mi > 1 and distance_mi <= 6:
        if has_bike and not is_raining:
            print(True)
        else:
            print(False)
    else:
        if has_car or has_ride_share_app:
            print(True)
        else:
            print(False)


if __name__ == "__main__":
    main()