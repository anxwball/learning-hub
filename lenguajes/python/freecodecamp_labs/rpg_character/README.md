# Crear un personaje RPG

## Descripción

Este laboratorio practica los fundamentos de Python mediante la construcción de una pequeña función que crea un personaje para una aventura de rol.

## Ubicación

`lenguajes/python/freecodecamp_labs/rpg_character`

## Estado

- Laboratorio resuelto.
- Documentación alineada con el formato del módulo Python.

## Estructura

- `main.py`: implementación de la función `create_character` y demostración mínima.
- `README.md`: reglas, pruebas y referencias del laboratorio.

## Objetivo

Cumple las historias de usuario siguientes y haz que todas las pruebas pasen para completar el laboratorio.

## Historias de usuario

- Debes tener una función llamada `create_character`.
- La función debe aceptar, en este orden, un nombre de personaje seguido de tres estadísticas: fuerza, inteligencia y carisma.
- El nombre del personaje debe validarse:
  - Si el nombre no es una cadena, la función debe retornar `The character name should be a string.`
  - Si el nombre está vacío, la función debe retornar `The character should have a name.`
  - Si el nombre tiene más de 10 caracteres, la función debe retornar `The character name is too long.`
  - Si el nombre contiene espacios, la función debe retornar `The character name should not contain spaces.`
- Las estadísticas también deben validarse:
  - Si una o más estadísticas no son enteros, la función debe retornar `All stats should be integers.`
  - Si una o más estadísticas son menores que 1, la función debe retornar `All stats should be no less than 1.`
  - Si una o más estadísticas son mayores que 4, la función debe retornar `All stats should be no more than 4.`
  - Si la suma de todas las estadísticas es distinta de 7, la función debe retornar `The character should start with 7 points.`
- Si todos los valores pasan la validación, la función debe retornar una cadena con cuatro líneas:
  - La primera línea debe contener el nombre del personaje.
  - Las líneas 2 a 4 deben comenzar con la abreviatura de la estadística, `STR`, `INT` o `CHA` en ese orden, seguida de un espacio y después una cantidad de puntos llenos (`●`) igual al valor de la estadística, y una cantidad de puntos vacíos (`○`) hasta completar 10. Ejemplo: si el valor de fuerza es 3, deben aparecer 3 puntos llenos seguidos de 7 puntos vacíos.
- La cadena que debe retornar `create_character('ren', 4, 2, 1)` es la siguiente:

## Ejemplo

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

- Aunque `str` e `int` son abreviaturas comunes para las estadísticas, recuerda que son palabras reservadas en Python y no deben usarse como nombres de variables.

## Pruebas

1. Debes tener una función llamada `create_character`.
2. Cuando `create_character` se llama con un primer argumento que no es una cadena, debe retornar `The character name should be a string.`
3. Cuando `create_character` se llama con un primer argumento que es una cadena, no debe retornar `The character name should be a string.`
4. Cuando `create_character` se llama con un primer argumento vacío, debe retornar `The character should have a name.`
5. Cuando `create_character` se llama con un primer argumento que no está vacío, no debe retornar `The character should have a name.`
6. Cuando `create_character` se llama con un primer argumento de más de 10 caracteres, debe retornar `The character name is too long.`
7. La función `create_character` no debe indicar que el nombre es demasiado largo cuando no supera los 10 caracteres.
8. Cuando `create_character` se llama con un primer argumento que contiene un espacio, debe retornar `The character name should not contain spaces.`
9. Cuando `create_character` se llama con un primer argumento que no contiene un espacio, no debe retornar `The character name should not contain spaces.`
10. Cuando `create_character` se llama con un segundo, tercer o cuarto argumento que no sea un entero, debe retornar `All stats should be integers.`
11. Cuando `create_character` se llama con un segundo, tercer y cuarto argumento que son enteros, no debe retornar `All stats should be integers.`
12. Cuando `create_character` se llama con un segundo, tercer o cuarto argumento menor que 1, debe retornar `All stats should be no less than 1.`
13. Cuando `create_character` se llama con un segundo, tercer y cuarto argumento que sean al menos 1, no debe retornar `All stats should be no less than 1.`
14. Cuando `create_character` se llama con un segundo, tercer o cuarto argumento mayor que 4, debe retornar `All stats should be no more than 4.`
15. Cuando `create_character` se llama con un segundo, tercer y cuarto argumento que sean como máximo 4, no debe retornar `All stats should be no more than 4.`
16. Cuando `create_character` se llama con un segundo, tercer o cuarto argumento cuya suma no sea 7, debe retornar `The character should start with 7 points.`
17. Cuando `create_character` se llama con un segundo, tercer y cuarto argumento cuya suma sea 7, no debe retornar `The character should start with 7 points.`
18. `create_character('ren', 4, 2, 1)` debe retornar `ren\nSTR ●●●●○○○○○○\nINT ●●○○○○○○○○\nCHA ●○○○○○○○○○`.
19. Cuando `create_character` se llama con valores válidos, debe mostrar las estadísticas del personaje como se requiere.

## Demostración

[main.py](./main.py)

## Ejecución

Desde la raíz del repositorio:

```bash
python lenguajes/python/freecodecamp_labs/rpg_character/main.py
```

## Última actualización

2026-05-21
