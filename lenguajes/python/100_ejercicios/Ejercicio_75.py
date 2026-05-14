"""
Problema  : Crear una clase Coche con atributos: marca, modelo, matrícula, km. Métodos: constructor, avanzar(km).
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : POO, mutabilidad, métodos de actualización
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Modelar un vehículo con datos de identificación e histórico de km.
    - Implementar método que simula el desplazamiento (incremento de km).
    - Demuestra cambio de estado en objetos mediante métodos.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Constructor y avanzar() son operaciones constantes.
    - El espacio es constante; se almacenan cuatro atributos.

Casos límite:
    - Km inicial válido: 10000 km (uso realista).
    - Avance positivo: 1500 km (incremento normal).
    - Avance cero: 0 km (sin movimiento).
    - Avance negativo: -500 km (debería rechazarse con ValueError).
    - Km muy grandes: 1e7 km (odómetro extremo).

Casos de uso:
  - Simuladores de conducción o flotas vehiculares.
  - Sistemas de mantenimiento basados en km recorridos.
  - Registros de historial de vehículos.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, validaciones, docstrings mejorados.
"""
class Coche:
    """Representa un vehículo con identificación e historial de km.

    Atributos:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        matricula (str): Matrícula única del vehículo.
        km (int): Kilómetros acumulados (debe ser >= 0).

    Raises:
        ValueError: Si km es negativo.
    """
    def __init__(self, marca: str, modelo: str, matricula: str, km: int) -> None:
        """Inicializa un coche con validación de km.

        Args:
            marca (str): Marca del vehículo.
            modelo (str): Modelo del vehículo.
            matricula (str): Matrícula única.
            km (int): Kilómetros iniciales (debe ser >= 0).

        Raises:
            ValueError: Si km < 0.
        """
        if km < 0:
            raise ValueError("Los kilómetros no pueden ser negativos.")
        self.marca: str = marca
        self.modelo: str = modelo
        self.matricula: str = matricula
        self.km: int = km

    def avanzar(self, km: int) -> None:
        """Incrementa los kilómetros del coche.

        Args:
            km (int): Kilómetros a añadir (debe ser >= 0).

        Raises:
            ValueError: Si km < 0.
        """
        if km < 0:
            raise ValueError("No se pueden restar kilómetros.")
        self.km += km


def main() -> None:
    """Crea un coche y simula su desplazamiento.

    Demuestra la creación de un coche y el incremento de kilómetros.

    Returns:
        None
    """
    print("=== Información de Vehículo ===\n")
    coche1: Coche = Coche("Toyota", "Corolla", "1234ABC", 10000)
    print(f"Vehículo: {coche1.marca} {coche1.modelo}")
    print(f"Matrícula: {coche1.matricula}")
    print(f"Kilómetros iniciales: {coche1.km} km\n")
    
    print("Avanzando 1500 km...")
    coche1.avanzar(1500)
    print(f"Kilómetros después del desplazamiento: {coche1.km} km\n")
    
    coche1.avanzar(500)
    print(f"Kilómetros finales: {coche1.km} km")


if __name__ == '__main__':
    main()
