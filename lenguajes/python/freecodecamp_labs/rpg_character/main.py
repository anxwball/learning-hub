"""
Problema  : Crear un personaje RPG.
Fuente    : freeCodeCamp Labs
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : fundamentos, poo, validacion
Fecha     : 2026-05-19
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
    - 2026-05-19: Encabezado documental agregado y lógica preservada.
"""

full_dot = '●'
empty_dot = '○'

def create_character (name, strenght, intelligence, charisma):
    """Crear y validar una ficha de personaje RPG.

    Recibe un nombre y tres estadísticas, valida que cumplan las reglas del
    laboratorio y devuelve un mensaje de error o una ficha formateada con
    puntuación visual para STR, INT y CHA.

    Args:
        name: Nombre del personaje.
        strenght: Puntuación de fuerza.
        intelligence: Puntuación de inteligencia.
        charisma: Puntuación de carisma.

    Returns:
        str: Mensaje de error o la ficha final del personaje.
    """

    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    if not isinstance(strenght, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"

    if strenght < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    if strenght > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if sum([strenght, intelligence, charisma]) != 7:
        return "The character should start with 7 points"

    strenght_dots = full_dot * strenght
    intelligence_dots = full_dot * intelligence
    charisma_dots = full_dot * charisma

    strenght_calc = strenght_dots + (empty_dot * (10 - strenght))
    intelligence_calc = intelligence_dots + (empty_dot * (10 - intelligence))
    charisma_calc = charisma_dots + (empty_dot * (10 - charisma))


    return f"{name}\nSTR {strenght_calc}\nINT {intelligence_calc}\nCHA {charisma_calc}"

print(create_character("ren", 4, 2, 1))