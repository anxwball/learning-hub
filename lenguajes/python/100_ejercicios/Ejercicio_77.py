"""
Problema  : Crear clase Persona con getters/setters, constructor (datos opcionales), mostrar(), es_mayor_de_edad().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : poo, propiedades, encapsulacion, decoradores
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Encapsular atributos con propiedades @property (getters/setters).
    - Permitir inicialización con datos opcionales.
    - Implementar validación en setters y métodos de utilidad.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Getters y setters son O(1): acceso/asignación de atributos.
    - mostrar() es O(1): impresión de dos valores.
    - El espacio es constante; se almacenan dos atributos privados.

Casos límite:
    - Constructor sin argumentos: Persona() (datos vacíos/por defecto).
    - Cambio de propiedades: modificar nombre y edad después de crear.
    - Edad en umbral: cambiar de 17 a 18 años (tester mayoredad).
    - Edad negativa: intento de establecer edad < 0 (rechazar).
    - Nombre vacío: "" (debería aceptar pero documentar).

Casos de uso:
  - Sistemas de usuario con perfiles editables.
  - Validación de cambios de datos sin exponer internals.
  - Bases educativas para encapsulación de POO.

Revisión:
    - 2026-05-13: Normalizado. Corregidas propiedades, docstrings completos, validación.
"""
class Persona:
    """Representa una persona con propiedades encapsuladas.

    Atributos privados:
        _nombre (str): Nombre de la persona.
        _edad (int): Edad en años (debe ser >= 0).

    Raises:
        ValueError: Si edad es negativa.
    """
    def __init__(self, nombre: str = "", edad: int = 0) -> None:
        """Inicializa una persona con datos opcionales.

        Args:
            nombre (str, optional): Nombre de la persona. Defaults to "".
            edad (int, optional): Edad en años (debe ser >= 0). Defaults to 0.

        Raises:
            ValueError: Si edad < 0.
        """
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._nombre: str = nombre
        self._edad: int = edad

    # Getter y Setter para nombre
    @property
    def nombre(self) -> str:
        """Obtiene el nombre de la persona.

        Returns:
            str: Nombre actual.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Establece el nombre de la persona.

        Args:
            nuevo_nombre (str): Nuevo nombre.
        """
        self._nombre = nuevo_nombre

    # Getter y Setter para edad
    @property
    def edad(self) -> int:
        """Obtiene la edad de la persona.

        Returns:
            int: Edad actual en años.
        """
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        """Establece la edad de la persona.

        Args:
            nueva_edad (int): Nueva edad (debe ser >= 0).

        Raises:
            ValueError: Si nueva_edad < 0.
        """
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = nueva_edad

    # Métodos 
    def mostrar(self) -> None:
        """Imprime los datos de la persona.

        Returns:
            None
        """
        print(f"Nombre: {self._nombre}, Edad: {self._edad} años")

    def es_mayor_de_edad(self) -> bool:
        """Verifica si la persona es mayor de edad legal.

        Returns:
            bool: True si edad >= 18, False en caso contrario.
        """
        return self._edad >= 18


def main() -> None:
    """Demuestra el uso de propiedades para encapsulación.

    Crea personas, accede/modifica sus atributos mediante propiedades,
    y verifica comportamiento de validación.

    Returns:
        None
    """
    print("=== Propiedades y Encapsulación ===\n")
    persona1: Persona = Persona("Juan", 25)
    print("Persona 1 inicial:")
    persona1.mostrar()
    print(f"¿Es mayor de edad? {persona1.es_mayor_de_edad()}\n")
    
    # Modificar propiedades
    print("Modificando persona 1...")
    persona1.nombre = "Carlos"
    persona1.edad = 17
    print("Persona 1 modificada:")
    persona1.mostrar()
    print(f"¿Es mayor de edad? {persona1.es_mayor_de_edad()}\n")
    
    # Crear persona con datos opcionales
    persona2: Persona = Persona()
    print("Persona 2 (datos vacíos):")
    persona2.mostrar()
    persona2.nombre = "Ana"
    persona2.edad = 30
    print("Persona 2 después de asignar datos:")
    persona2.mostrar()

if __name__ == '__main__':
    main()
