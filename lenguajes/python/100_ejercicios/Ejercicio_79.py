"""
Problema  : Representar una cuenta bancaria. Debe tener depósito, retiro, titular, saldo. Utilizar POO.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : poo, encapsulacion, manejo-de-dinero, validacion
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Modelar una cuenta bancaria con operaciones financieras básicas.
    - Implementar validaciones para depósitos y retiros.
    - Demostrar manejo de excepciones en operaciones críticas.

Complejidad: Tiempo O(1) | Espacio O(1)
    - Depositar y retirar son O(1): operaciones aritméticas.
    - mostrar_saldo() es O(1): acceso a atributo.
    - El espacio es constante; se almacenan dos atributos.

Casos límite:
    - Depósito válido: 500 EUR (monto positivo).
    - Depósito negativo: -100 EUR (debería rechazar con ValueError).
    - Retiro válido: 200 EUR (menos que saldo).
    - Retiro insuficiente: 2000 EUR (más que saldo 1500).
    - Retiro negativo: -50 EUR (debería rechazar).
    - Saldo inicial: 0 o valor positivo.

Casos de uso:
  - Aplicaciones bancarias y fintech.
  - Simuladores de presupuestos personales.
  - Sistemas de comercio electrónico.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, validaciones mejoradas, docstrings.
"""
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto: float) -> None:
        """Deposita un monto en la cuenta.

        Args:
            monto (float): Monto a depositar (debe ser > 0).

        Raises:
            ValueError: Si monto <= 0.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo:.2f}")

    def retirar(self, monto: float) -> None:
        """Retira un monto de la cuenta.

        Args:
            monto (float): Monto a retirar (debe ser positivo y <= saldo).

        Raises:
            ValueError: Si monto es inválido o hay fondos insuficientes.
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para realizar el retiro.")
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo:.2f}")
    
    def mostrar_saldo(self) -> float:
        """Retorna el saldo actual de la cuenta.

        Returns:
            float: Saldo actual.
        """
        return self.saldo


def main() -> None:
    """Demuestra operaciones de una cuenta bancaria.

    Crea una cuenta, realiza depósitos y retiros, mostrando el saldo.

    Returns:
        None
    """
    print("=== Operaciones de Cuenta Bancaria ===\n")
    cuenta1: CuentaBancaria = CuentaBancaria("Alice", 1000.0)
    print(f"Titular: {cuenta1.titular}")
    print(f"Saldo inicial: {cuenta1.mostrar_saldo():.2f}\n")
    
    print("Realizando depósito de 500.0 EUR...")
    cuenta1.depositar(500.0)
    print(f"Saldo después del depósito: {cuenta1.mostrar_saldo():.2f}\n")
    
    print("Realizando retiro de 200.0 EUR...")
    cuenta1.retirar(200.0)
    print(f"Saldo después del retiro: {cuenta1.mostrar_saldo():.2f}\n")
    
    # Intento de retiro inválido
    print("Intento de retiro de 2000.0 EUR (mayor que saldo):")
    try:
        cuenta1.retirar(2000.0)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
