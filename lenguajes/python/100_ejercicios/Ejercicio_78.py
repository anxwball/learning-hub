"""
Problema  : Crear clases Persona y Estudiante (herencia). Persona: atributo nombre, método mostrar_nombre(). Estudiante hereda y usa el método.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : herencia, POO, super()
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Demostrar herencia: Estudiante hereda de Persona.
    - Implementar método en clase base y reutilizarlo en subclase.
    - Usar super() para acceder a métodos de la clase padre.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Constructor y métodos son O(1) con asignaciones simples.
    - Acceso a super() es O(1): búsqueda en jerarquía de clases.
    - El espacio es constante; se almacena un atributo.

Casos límite:
    - Herencia simple: Estudiante hereda una funcionalidad de Persona.
    - Nombre válido: "Juan" (cadena normal).
    - Nombre vacío: "" (debería funcionar pero podría validarse).
    - Múltiples estudiantes: verificar que cada uno tiene su propio nombre.

Casos de uso:
  - Sistemas educativos con diferentes tipos de usuarios (Profesor, Estudiante).
  - Arquitecturas de aplicaciones que usan jerarquías de clases.
  - Reutilización de código común en familias de clases.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, docstrings mejorados.
"""
class Persona:
    """Clase base que representa una persona.

    Atributos:
        nombre (str): Nombre de la persona.
    """
    def __init__(self, nombre: str) -> None:
        """Inicializa una persona con nombre.

        Args:
            nombre (str): Nombre de la persona.
        """
        self.nombre: str = nombre

    def mostrar_nombre(self) -> str:
        """Retorna el nombre de la persona.

        Returns:
            str: Nombre almacenado.
        """
        return self.nombre

    
class Estudiante(Persona):
    """Clase que hereda de Persona para representar un estudiante.

    Atributos:
        nombre (str): Nombre del estudiante (heredado de Persona).
    """
    def __init__(self, nombre: str) -> None:
        """Inicializa un estudiante con nombre.

        Args:
            nombre (str): Nombre del estudiante.
        """
        super().__init__(nombre)

    def mostrar_nombre_estudiante(self) -> str:
        """Retorna el nombre del estudiante usando el método heredado.

        Returns:
            str: Nombre del estudiante.
        """
        return super().mostrar_nombre()

def main() -> None:
    """Demuestra herencia y reutilización de métodos de clase base.

    Crea instancias de Persona y Estudiante, demostrando cómo
    Estudiante reutiliza el método mostrar_nombre() de Persona.

    Returns:
        None
    """
    print("=== Herencia: Persona y Estudiante ===\n")
    
    # Crear una persona
    persona1: Persona = Persona("García")
    print(f"Persona: {persona1.mostrar_nombre()}\n")
    
    # Crear un estudiante
    estudiante1: Estudiante = Estudiante("Juan")
    print(f"Estudiante: {estudiante1.mostrar_nombre_estudiante()}")
    print(f"Nombre del estudiante (acceso directo): {estudiante1.nombre}\n")
    
    # Otro estudiante
    estudiante2: Estudiante = Estudiante("María")
    print(f"Estudiante 2: {estudiante2.mostrar_nombre_estudiante()}")

if __name__ == '__main__':
    main()
