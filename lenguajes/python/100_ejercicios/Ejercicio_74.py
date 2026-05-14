"""
Problema  : Crear una clase Persona con atributos: nombre, edad, dni. Métodos: constructor, es_mayor_de_edad().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : POO, lógica condicional, validación
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Modelar una persona con atributos básicos de identificación.
    - Implementar método que valida si es mayor de edad (>= 18).
    - Demuestra lógica condicional dentro de métodos de clase.

Complejidad: Tiempo O(1) | Espacio O(1)
    - El constructor es O(1) con asignaciones constantes.
    - es_mayor_de_edad() es O(1): comparación simple.
    - El espacio es constante; se almacenan tres atributos.

Casos límite:
    - Mayor de edad válido: 25 años (claro mayor).
    - Exactamente mayor de edad: 18 años (umbral).
    - Menor de edad: 17 años (uno menos del umbral).
    - Edad cero o negativa: debería rechazarse con ValueError.
    - Edad muy grande: 150 años (valor irreal pero válido).

Casos de uso:
  - Control de acceso a contenido restringido por edad.
  - Validación en formularios de registro.
  - Sistemas de consentimiento y legalidad.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, validaciones, docstrings mejorados.
"""
class Persona:
    """Representa una persona con información básica de identificación.

    Atributos:
        nombre (str): Nombre de la persona.
        edad (int): Edad en años (debe ser >= 0).
        dni (str): Número de documento de identidad.

    Raises:
        ValueError: Si edad es negativa.
    """
    def __init__(self, nombre: str, edad: int, dni: str) -> None:
        """Inicializa una persona con validación de edad.

        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad en años (debe ser >= 0).
            dni (str): Número de documento de identidad.

        Raises:
            ValueError: Si edad < 0.
        """
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.nombre: str = nombre
        self.edad: int = edad
        self.dni: str = dni

    def es_mayor_de_edad(self) -> bool:
        """Verifica si la persona es mayor de edad legal.

        Returns:
            bool: True si edad >= 18, False en caso contrario.
        """
        return self.edad >= 18


def main() -> None:
    """Crea instancias de Persona y verifica mayoredad.

    Demuestra la creación de personas y el cálculo de mayoredad.

    Returns:
        None
    """
    print("=== Información de Personas ===\n")
    persona1: Persona = Persona("Juan", 25, "12345678A")
    print(f"{persona1.nombre} (DNI: {persona1.dni}, Edad: {persona1.edad})")
    print(f"¿Es mayor de edad? {persona1.es_mayor_de_edad()}\n")
    
    persona2: Persona = Persona("María", 17, "87654321B")
    print(f"{persona2.nombre} (DNI: {persona2.dni}, Edad: {persona2.edad})")
    print(f"¿Es mayor de edad? {persona2.es_mayor_de_edad()}")

if __name__ == '__main__':
    main()
