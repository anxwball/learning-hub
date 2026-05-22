"""
Problema  : Crear un personaje RPG.
Fuente    : freeCodeCamp Labs
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : fundamentos, poo, validacion
Fecha     : 2026-05-21
Estado    : resuelto

Enfoque:
    - Validar primero el nombre del personaje y después las estadísticas.
    - Construir la salida final solo cuando todas las condiciones sean válidas.
    - Mantener el formato exacto que espera el laboratorio.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Nombre vacío, con espacios o demasiado largo: se retorna un mensaje de error.
    - Estadísticas fuera de rango o no enteras: se retorna un mensaje de error.
    - Suma distinta de 7: se retorna un mensaje de error.

Casos de uso:
    - Crear fichas de personaje para un RPG de consola.
    - Validar entradas de usuario antes de construir una ficha.
    - Generar una representación visual simple de atributos.

Revisión:
    - 2026-05-21: Tipado, estilo y estructura `main()` normalizados.
"""

FULL_DOT: str = "●"
EMPTY_DOT: str = "○"


def create_character(
    name: str,
    strength: int,
    intelligence: int,
    charisma: int,
) -> str:
    """Crear y validar una ficha de personaje RPG.

    Recibe un nombre y tres estadísticas, valida que cumplan las reglas del
    laboratorio y devuelve un mensaje de error o una ficha formateada con
    puntuación visual para STR, INT y CHA.

    Args:
        name: Nombre del personaje.
        strength: Puntuación de fuerza.
        intelligence: Puntuación de inteligencia.
        charisma: Puntuación de carisma.

    Returns:
        Mensaje de error o la ficha final del personaje.
    """
    if not isinstance(name, str):
        return "The character name should be a string."

    if name == "":
        return "The character should have a name."

    if len(name) > 10:
        return "The character name is too long."

    if " " in name:
        return "The character name should not contain spaces."

    stats: tuple[int, int, int] = (strength, intelligence, charisma)
    if not all(isinstance(stat, int) and not isinstance(stat, bool) for stat in stats):
        return "All stats should be integers."

    if min(stats) < 1:
        return "All stats should be no less than 1."

    if max(stats) > 4:
        return "All stats should be no more than 4."

    if sum(stats) != 7:
        return "The character should start with 7 points."

    strength_dots: str = FULL_DOT * strength
    intelligence_dots: str = FULL_DOT * intelligence
    charisma_dots: str = FULL_DOT * charisma

    strength_calc: str = strength_dots + (EMPTY_DOT * (10 - strength))
    intelligence_calc: str = intelligence_dots + (EMPTY_DOT * (10 - intelligence))
    charisma_calc: str = charisma_dots + (EMPTY_DOT * (10 - charisma))

    return f"{name}\nSTR {strength_calc}\nINT {intelligence_calc}\nCHA {charisma_calc}"


def main() -> None:
    """Ejecutar una demostración mínima del laboratorio."""
    print(create_character("ren", 4, 2, 1))


if __name__ == "__main__":
    main()