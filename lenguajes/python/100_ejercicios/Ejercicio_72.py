"""
Problema  : Crear una clase Circulo con atributo radio. Métodos: constructor, area(), perimetro().
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : POO, geometría, constantes matemáticas
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Modelar un círculo con atributo radio y cálculos geométricos.
    - Implementar métodos para calcular área (π×r²) y perímetro (2×π×r).
    - Demuestra uso de constantes (math.pi) y operaciones trigonométricas.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Cada operación es constante; solo operaciones aritméticas básicas.
    - El espacio es constante; se almacena un único atributo numérico.

Casos límite:
    - Radio positivo pequeño: 0.1 (casi un punto).
    - Radio positivo grande: 1000 (círculo muy grande).
    - Radio cero o negativo: debería rechazarse con ValueError.
    - Radio muy pequeño: 1e-6 (presición en cálculos).

Casos de uso:
  - Cálculos de área y perímetro en aplicaciones de geometría.
  - Diseño de interfaces visuales (dibujo de círculos).
  - Análisis de datos espaciales (distancia, área de cobertura).

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, validaciones, docstrings mejorados.
"""
import math

class Circulo:
    """Representa un círculo con operaciones geométricas.

    Atributos:
        radio (float): Radio del círculo en unidades.

    Raises:
        ValueError: Si el radio es menor o igual a cero.
    """
    def __init__(self, radio: float) -> None:
        """Inicializa un círculo con radio validado.

        Args:
            radio (float): Radio del círculo (debe ser > 0).

        Raises:
            ValueError: Si radio <= 0.
        """
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a cero.")
        self.radio: float = radio

    def area(self) -> float:
        """Calcula el área del círculo.

        Returns:
            float: Área = π × r².
        """
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        """Calcula el perímetro (circunferencia) del círculo.

        Returns:
            float: Perímetro = 2 × π × r.
        """
        return 2 * math.pi * self.radio

def main() -> None:
    """Crea un círculo, calcula su área y perímetro.

    Demuestra la creación de una instancia de Circulo y el uso de sus
    métodos para calcular propiedades geométricas con precisión.

    Returns:
        None
    """
    print("=== Cálculo de Propiedades de un Círculo ===\n")
    circulo_1: Circulo = Circulo(5.0)
    print(f"Radio: {circulo_1.radio} unidades")
    print(f"Área: {circulo_1.area():.4f} unidades²")
    print(f"Perímetro: {circulo_1.perimetro():.4f} unidades")
    print()
    # Ejemplo con otro círculo
    circulo_2: Circulo = Circulo(10.5)
    print(f"Círculo 2 - Radio: {circulo_2.radio}")
    print(f"Área: {circulo_2.area():.4f} unidades²")
    print(f"Perímetro: {circulo_2.perimetro():.4f} unidades")

if __name__ == '__main__':
    main()
