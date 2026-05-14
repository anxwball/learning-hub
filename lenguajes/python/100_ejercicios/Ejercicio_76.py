"""
Problema  : Crear una clase Animal con atributos: especie, nombre. Métodos: constructor, hablar() que retorna onomatopeya.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : POO, lógica condicional, polimorfismo
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Modelar un animal con su especie y nombre.
    - Implementar método que retorna sonido según especie.
    - Demuestra uso de condicionales para comportamiento polimórfico.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Constructor es O(1) con asignaciones simples.
    - hablar() es O(1): búsqueda en comparaciones de cadena.
    - El espacio es constante; se almacenan dos atributos.

Casos límite:
    - Especie conocida (perro): retorna "guau" (caso insensible).
    - Especie conocida (gato): retorna "miau" (caso insensible).
    - Especie desconocida (pajaro): retorna "sonido desconocido".
    - Especie con diferente capitalización: "PERRO" vs "perro" (debería funcionar).
    - Especie vacía: "" (debería retornar "sonido desconocido").

Casos de uso:
  - Juegos o simuladores que usan sonidos de animales.
  - Aplicaciones educativas de biología o zoología.
  - Sistemas de categorización de animales.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, manejo de mayúsculas mejorado.
"""
class Animal:
    """Representa un animal con capacidad de emitir sonidos.

    Atributos:
        especie (str): Nombre de la especie del animal.
        nombre (str): Nombre individual del animal.
    """
    def __init__(self, especie: str, nombre: str) -> None:
        """Inicializa un animal con especie y nombre.

        Args:
            especie (str): Especie del animal (ej: "perro", "gato").
            nombre (str): Nombre individual del animal.
        """
        self.especie: str = especie
        self.nombre: str = nombre
    
    def hablar(self) -> str:
        """Retorna el sonido característico del animal según su especie.

        Returns:
            str: Onomatopeya del sonido que emite la especie.
                 - "perro" → "guau"
                 - "gato" → "miau"
                 - otros → "sonido desconocido"
        """
        especie_lower: str = self.especie.lower()
        if especie_lower == "perro":
            return "guau"
        elif especie_lower == "gato":
            return "miau"
        else:
            return "sonido desconocido"


def main() -> None:
    """Crea instancias de Animal y muestra sus sonidos.

    Demuestra la creación de animales y la emisión de sus sonidos.

    Returns:
        None
    """
    print("=== Sonidos de Animales ===\n")
    animal1: Animal = Animal("Perro", "Rex")
    animal2: Animal = Animal("Gato", "Mittens")
    animal3: Animal = Animal("Pajaro", "Tweety")
    
    print(f"{animal1.nombre} ({animal1.especie}) dice: {animal1.hablar()}")
    print(f"{animal2.nombre} ({animal2.especie}) dice: {animal2.hablar()}")
    print(f"{animal3.nombre} ({animal3.especie}) dice: {animal3.hablar()}")

if __name__ == '__main__':
    main()
