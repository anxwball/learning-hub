# Planificador de viajes según el clima

## Descripción

Este laboratorio usa condicionales para determinar si un desplazamiento es posible según el clima, la distancia a recorrer y la disponibilidad de transporte.

## Ubicación

`lenguajes/python/freecodecamp_labs/travel_weather_planner`

## Estado

- Laboratorio resuelto.
- Encabezado y documentación alineados con el formato del módulo Python.

## Estructura

- `main.py`: implementación del ejercicio y salida esperada del laboratorio.
- `README.md`: descripción, reglas y referencias del laboratorio.

## Objetivo

Cumple las historias de usuario siguientes y haz que todas las pruebas pasen para completar el laboratorio.

## Historias de usuario

- Debes crear las siguientes variables:

`distance_mi` (número que representa la distancia a recorrer en millas)
`is_raining` (booleano que indica si actualmente está lloviendo)
`has_bike` (booleano que indica si la persona tiene bicicleta)
`has_car` (booleano que indica si la persona tiene automóvil)
`has_ride_share_app` (booleano que indica si la persona tiene una aplicación para solicitar un viaje)

- Debes usar condicionales para determinar si es posible desplazarse según los valores de estas variables.
- Debes usar sentencias `if`, `elif` y `else` para evaluar las categorías de distancia en orden ascendente.
- Si `distance_mi` es un valor falsy:
    - Debes imprimir `False`.
- Si la distancia es **menor o igual que 1 milla**:
    - Debes imprimir `True` solo si **no está lloviendo**.
    - En caso contrario, debes imprimir `False`.
- Si la distancia es **mayor que 1 milla y menor o igual que 6 millas**:
    - Debes imprimir `True` solo si la persona tiene bicicleta **y** no está lloviendo.
    - En caso contrario, debes imprimir `False`.
- Si la distancia es **mayor que 6 millas**:
    - Debes imprimir `True` si la persona tiene automóvil **o** tiene una aplicación de viajes compartidos.
    - En caso contrario, debes imprimir `False`.

## Pruebas

1. Debes tener una variable llamada `distance_mi`.
2. Debes asignar un número a la variable `distance_mi`.
3. Debes tener una variable llamada `is_raining`.
4. Debes asignar un valor booleano a la variable `is_raining`.
5. Debes tener una variable llamada `has_bike`.
6. Debes asignar un valor booleano a la variable `has_bike`.
7. Debes tener una variable llamada `has_car`.
8. Debes asignar un valor booleano a la variable `has_car`.
9. Debes tener una variable llamada `has_ride_share_app`.
10. Debes asignar un valor booleano a la variable `has_ride_share_app`.
11. Debes usar al menos una sentencia `if`.
12. Debes usar al menos una rama `elif` en tu programa.
13. Debes usar al menos un operador booleano (`and`, `or` o `not`) en tu código.
14. Debes usar la función `print()` para mostrar el resultado.
15. Cuando `distance_mi` sea un valor falsy, el programa debe imprimir `False`.
16. Cuando la distancia sea de `1` milla o menos y no esté lloviendo, el programa debe imprimir `True`.
17. Cuando la distancia sea de `1` milla o menos y esté lloviendo, el programa debe imprimir `False`.
18. Cuando la distancia esté entre `1` milla excluida y `6` millas incluidas, y esté lloviendo sin bicicleta disponible, el programa debe imprimir `False`.
19. Cuando la distancia esté entre `1` milla excluida y `6` millas incluidas, no esté lloviendo pero no haya bicicleta disponible, el programa debe imprimir `False`.
20. Cuando la distancia esté entre `1` milla excluida y `6` millas incluidas, haya bicicleta disponible y no esté lloviendo, el programa debe imprimir `True`.
21. Cuando la distancia sea mayor que `6` millas y haya una aplicación de viajes compartidos disponible, el programa debe imprimir `True`.
22. Cuando la distancia sea mayor que `6` millas y haya un automóvil disponible, el programa debe imprimir `True`.
23. Cuando la distancia sea mayor que `6` millas y no haya ni automóvil ni aplicación de viajes compartidos disponible, el programa debe imprimir `False`.

## Demostración

[main.py](./main.py)

## Ejecución

Desde la raíz del repositorio:

```bash
python lenguajes/python/freecodecamp_labs/travel_weather_planner/main.py
```

## Última actualización

2026-05-18
