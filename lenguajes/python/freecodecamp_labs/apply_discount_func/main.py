"""
Problema  : Calculadora de descuentos.
Fuente    : freeCodeCamp Labs
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/lab-discount-calculator/build-a-discount-calculator)
Etiquetas : fundamentos, funciones, porcentajes, validacion, manejo-de-dinero
Fecha     : 2026-05-20
Estado    : resuelto

Enfoque:
    - Validar primero tipos y rangos para devolver mensajes de error claros
      antes de realizar el cálculo del descuento.
    - Interpretar `discount` como porcentaje entre 0 y 100 y convertirlo a
      fracción durante el cálculo final.
    - Conservar una función pura para facilitar pruebas y reutilización.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - `price` o `discount` no numéricos: se retorna un mensaje de error.
    - `price` menor o igual que cero: se retorna un mensaje de error.
    - `discount` fuera del rango 0..100: se retorna un mensaje de error.
    - Descuentos de `0` o `100`: retornan el precio original o `0`.

Casos de uso:
  - Calcular promociones sobre precios de productos.
  - Verificar descuentos válidos en formularios o scripts educativos.
  - Reutilizar la función en ejercicios introductorios de validación.

Revisión:
    - 2026-05-20: Laboratorio documentado y normalizado al formato del
      repositorio con función `apply_discount` y demostración ejecutable.
"""


def apply_discount(price: int | float, discount: int | float) -> int | float | str:
    """Aplicar un descuento porcentual a un precio con validaciones básicas.

    Args:
        price: Precio original sobre el que se aplicará el descuento.
        discount: Porcentaje de descuento expresado entre 0 y 100.

    Returns:
        El precio final con descuento o un mensaje de error cuando la entrada
        no cumple las reglas del laboratorio.
    """
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        return "The price should be a number"

    if isinstance(discount, bool) or not isinstance(discount, (int, float)):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    return price - (price * discount / 100)


def main() -> None:
    """Ejecutar una demostración mínima del laboratorio."""
    print(apply_discount(100, 20))


if __name__ == "__main__":
    main()
