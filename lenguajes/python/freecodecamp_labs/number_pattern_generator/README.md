# Generador de patrones numéricos

## Descripción

En este laboratorio practicarás los conceptos básicos de Python creando una pequeña función que genera una secuencia de números en forma de cadena.

## Ubicación

`lenguajes/python/freecodecamp_labs/number_pattern_generator`

## Estado

- Laboratorio resuelto.
- Encabezado y documentación alineados con el formato del módulo Python.

## Estructura

- `main.py`: implementación de la función `number_pattern` y ejemplos de uso.
- `README.md`: documentación normalizada del laboratorio.

## Objetivo

Cumple las historias de usuario descritas más abajo y consigue que todas las pruebas pasen para completar el laboratorio.

## Historias de usuario

- Debes definir una función llamada `number_pattern` que reciba un único parámetro `n` (un entero positivo).
- `number_pattern` debe usar un bucle `for`.
- `number_pattern(n)` debe devolver una cadena con todos los enteros desde `1` hasta `n` (incluido), separados por un espacio. Por ejemplo, `number_pattern(4)` debe retornar `1 2 3 4`.
- Si el argumento pasado a la función no es un entero, la función debe devolver: `Argument must be an integer value.`
- Si el argumento pasado a la función es menor que `1`, la función debe devolver: `Argument must be an integer greater than 0.`

## Pruebas

1. Debes tener una función `number_pattern`.
2. La función `number_pattern` debe tener un parámetro llamado `n`.
3. `number_pattern(4)` debe devolver `1 2 3 4`.
4. `number_pattern(12)` debe devolver `1 2 3 4 5 6 7 8 9 10 11 12`.
5. `number_pattern` debe devolver una lista de números separados por espacios para cualquier entero positivo.
6. `number_pattern` debe devolver `Argument must be an integer value.` cuando se le pase un valor que no sea un entero.
7. `number_pattern` debe devolver `Argument must be an integer greater than 0.` cuando se le pase un entero no positivo.

## Demostración

[main.py](./main.py)

## Ejecución

Desde la raíz del repositorio:

```bash
python lenguajes/python/freecodecamp_labs/number_pattern_generator/main.py
```

## Última actualización

2026-05-21
