"""
Problema  : Crear una clase Rectangulo con atributos base, altura. Métodos: constructor, calcular_area(), calcular_perimetro().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : POO, geometría, métodos
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Modelar un rectángulo como objeto con atributos numéricos (base, altura).
    - Implementar métodos de cálculo geométrico (área y perímetro).
    - Demuestra encapsulación de datos y comportamiento en una clase.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Cada operación (constructor, calcular_area, calcular_perimetro) es constante.
    - El espacio es constante; solo se almacenan dos atributos numéricos.

Casos límite:
    - Base y altura positivas: 5.5 y 15.2 (valores reales válidos).
    - Base o altura cero: debería rechazarse con ValueError.
    - Base o altura negativa: debería rechazarse con ValueError.
    - Valores muy grandes: 1e6 x 1e6 (overflow en cálculos).

Casos de uso:
  - Cálculo de áreas y perímetros en aplicaciones de diseño o arquitectura.
  - Gestión de inventarios de espacios o superficie.
  - Base educativa para modelado de formas geométricas.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, validaciones, docstrings mejorados.
"""
class Rectangulo:
    """Representa un rectángulo con operaciones geométricas.

    Atributos:
        base (float): Ancho del rectángulo en unidades.
        altura (float): Alto del rectángulo en unidades.

    Raises:
        ValueError: Si base o altura son menores o iguales a cero.
    """
    def __init__(self, base: float, altura: float) -> None:
        """Inicializa un rectángulo con base y altura validadas.

        Args:
            base (float): Ancho del rectángulo (debe ser > 0).
            altura (float): Alto del rectángulo (debe ser > 0).

        Raises:
            ValueError: Si base o altura son <= 0.
        """
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores a cero.")
        self.base: float = base
        self.altura: float = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo.

        Returns:
            float: Área = base × altura.
        """
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del rectángulo.

        Returns:
            float: Perímetro = 2 × (base + altura).
        """
        return 2 * (self.base + self.altura)


def main() -> None:
    """Crea un rectángulo, calcula su área y perímetro.

    Demuestra la creación de una instancia de Rectangulo y el uso de sus
    métodos para calcular propiedades geométricas.

    Returns:
        None
    """
    print("=== Cálculo de Propiedades de un Rectángulo ===\n")
    rectangulo_1: Rectangulo = Rectangulo(5.5, 15.2)
    print(f"Base: {rectangulo_1.base} unidades")
    print(f"Altura: {rectangulo_1.altura} unidades")
    print(f"Área: {rectangulo_1.calcular_area():.2f} unidades²")
    print(f"Perímetro: {rectangulo_1.calcular_perimetro():.2f} unidades")
    print()
    # Ejemplo con valores diferentes
    rectangulo_2: Rectangulo = Rectangulo(10.0, 8.5)
    print(f"Rectángulo 2 - Base: {rectangulo_2.base}, Altura: {rectangulo_2.altura}")
    print(f"Área: {rectangulo_2.calcular_area():.2f} unidades²")
    print(f"Perímetro: {rectangulo_2.calcular_perimetro():.2f} unidades")

if __name__ == '__main__':
    main()
