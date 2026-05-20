# Calculadora de descuentos

## Descripción

Este laboratorio implementa una función para aplicar descuentos porcentuales a un precio, con validaciones de tipo y rango según las reglas del ejercicio.

## Ubicación

`lenguajes/python/freecodecamp_labs/apply_discount_func`

## Estado

- Laboratorio resuelto.
- Encabezado y documentación alineados con el formato del módulo Python.

## Estructura

- `main.py`: implementación de la función `apply_discount` y demostración mínima.
- `README.md`: descripción, reglas y referencias del laboratorio.

## Objetivo

Cumple las historias de usuario siguientes y haz que todas las pruebas pasen para completar el laboratorio.

## Historias de usuario

- Debes crear una función llamada `apply_discount`.
- La función `apply_discount` debe recibir exactamente dos parámetros:
  - `price`
  - `discount`
- Si `price` no es un número, la función debe retornar `The price should be a number`.
- Si `discount` no es un número, la función debe retornar `The discount should be a number`.
- Si `price` es menor o igual que `0`, la función debe retornar `The price should be greater than 0`.
- Si `discount` es menor que `0` o mayor que `100`, la función debe retornar `The discount should be between 0 and 100`.
- Si ambos valores son válidos, debes calcular el descuento como un porcentaje del precio original.
- La función debe retornar el precio final con el descuento aplicado.

## Pruebas

1. Debes definir una función llamada `apply_discount`.
2. La función `apply_discount` debe recibir exactamente dos parámetros.
3. Cuando `price` no sea un número, la función debe retornar `The price should be a number`.
4. Cuando `discount` no sea un número, la función debe retornar `The discount should be a number`.
5. Cuando `price` sea menor o igual que `0`, la función debe retornar `The price should be greater than 0`.
6. Cuando `discount` sea menor que `0` o mayor que `100`, la función debe retornar `The discount should be between 0 and 100`.
7. `apply_discount(100, 20)` debe retornar `80`.
8. `apply_discount(200, 50)` debe retornar `100`.
9. `apply_discount(50, 0)` debe retornar `50`.
10. `apply_discount(100, 100)` debe retornar `0`.
11. `apply_discount(74.5, 20.0)` debe retornar `59.6`.

## Demostración

[main.py](./main.py)

## Ejecución

Desde la raíz del repositorio:

```bash
python lenguajes/python/freecodecamp_labs/apply_discount_func/main.py
```

## Última actualización

2026-05-20
