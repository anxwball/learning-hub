# Función de cálculo de descuento

## Descripción

Este laboratorio implementa una función que calcula el precio final de un artículo después de aplicar un descuento porcentual. Por ejemplo, si el precio es 50 y se aplica un descuento del 20%, el monto del descuento es 10 y el precio final es 40.

## Ubicación

`lenguajes/python/freecodecamp_labs/apply_discount_func`

## Estado

- Laboratorio resuelto.
- Encabezado y documentación alineados con el formato del módulo Python.

## Estructura

- `main.py`: implementación de la función con validaciones y ejemplos de uso.
- `README.md`: descripción, reglas y referencias del laboratorio.

## Objetivo

Cumple las historias de usuario siguientes y haz que todas las pruebas pasen para completar el laboratorio.

## Historias de usuario

- Debes definir una función llamada `apply_discount`.
- La función `apply_discount` debe aceptar exactamente dos parámetros: `price` y `discount`.
- Si `price` no es un número (int o float), la función debe retornar la cadena "The price should be a number".
- Si `discount` no es un número (int o float), la función debe retornar la cadena "The discount should be a number".
- Si `price` es menor o igual a 0, la función debe retornar la cadena "The price should be greater than 0".
- Si `discount` es menor a 0 o mayor a 100, la función debe retornar la cadena "The discount should be between 0 and 100".
- Si ambas entradas son válidas, la función debe calcular el descuento como un porcentaje del precio.
- La función debe retornar el precio final después de aplicar el descuento.

## Pruebas

1. Debes tener una función llamada `apply_discount`.
2. Tu función `apply_discount` debe aceptar dos parámetros: `price` y `discount`.
3. Cuando `apply_discount` es llamada con un `price` (primer argumento) que no es un número (int o float), debe retornar "The price should be a number".
4. Cuando `apply_discount` es llamada con un `discount` (segundo argumento) que no es un número (int o float), debe retornar "The discount should be a number".
5. Cuando `apply_discount` es llamada con un `price` menor o igual a 0, debe retornar "The price should be greater than 0".
6. Cuando `apply_discount` es llamada con un `discount` menor a 0 o mayor a 100, debe retornar "The discount should be between 0 and 100".
7. `apply_discount(100, 20)` debe retornar 80.
8. `apply_discount(200, 50)` debe retornar 100.
9. `apply_discount(50, 0)` debe retornar 50.
10. Cuando `apply_discount` es llamada con un descuento de 100, debe retornar 0.
11. `apply_discount(74.5, 20.0)` debe retornar 59.6.

## Demostración

[main.py](./main.py)

## Ejecución

Desde la raíz del repositorio:

```bash
python lenguajes/python/freecodecamp_labs/apply_discount_func/main.py
```

## Última actualización

2026-05-19
