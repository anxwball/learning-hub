"""
Problema  : Crear una clase Planet para modelar un planeta y su órbita.
Fuente    : FreeCodeCamp Labs
Plataforma: FreeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : clases, poo, validacion, freecodecamp
Fecha     : 2026-05-23
Estado    : resuelto

Enfoque:
    - Validar que nombre, tipo de planeta y estrella sean cadenas no vacías.
    - Exponer un método orbit() y una representación __str__ clara para pruebas.
    - Mantener instancias de demostración al final del módulo para mostrar la salida.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Entradas que no sean cadenas: se lanza TypeError.
    - Cadenas vacías: se lanza ValueError.
    - Demostración con tres instancias fijas.

Casos de uso:
    - Laboratorio educativo de programación orientada a objetos.
    - Ejercicio de validación básica de tipos y valores.
    - Representación textual de objetos simples.

Revisión:
    - 2026-05-23: Módulo normalizado con validaciones, type hints y guard de ejecución.
"""


class Planet:
    def __init__(self, name: str, planet_type: str, star: str) -> None:
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")

        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self) -> str:
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self) -> str:
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


def main() -> None:
    """Crear y mostrar tres instancias de Planet para la demostración."""
    planet_1 = Planet("The Earth", "Rocky", "The Sun")
    planet_2 = Planet("Mars", "Rocky", "The Sun")
    planet_3 = Planet("TOI-150 b", "Gaseous", "TOI-150")

    print(planet_1)
    print(planet_2)
    print(planet_3)

    print(planet_1.orbit())
    print(planet_2.orbit())
    print(planet_3.orbit())


if __name__ == "__main__":
    main()