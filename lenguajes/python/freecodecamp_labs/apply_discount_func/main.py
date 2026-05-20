"""
Problema  : Función de cálculo de descuento.
Fuente    : freeCodeCamp Labs
Plataforma: freeCodeCamp (https://www.freecodecamp.org/learn/python-v9/)
Etiquetas : fundamentos, validacion, aritmetica, funciones
Fecha     : 2026-05-19
Estado    : resuelto

Enfoque:
    - Validar tipos de datos (price y discount deben ser int o float).
    - Verificar rangos válidos (price > 0, 0 <= discount <= 100).
    - Calcular el descuento como porcentaje y retornar el precio final.
    - Retornar mensajes descriptivos para errores de validación.

Complejidad: Tiempo O(1) | Espacio O(1)

Casos límite:
    - Precio no numérico: retorna mensaje de error.
    - Descuento no numérico: retorna mensaje de error.
    - Precio <= 0: retorna mensaje de error.
    - Descuento < 0 o > 100: retorna mensaje de error.
    - Descuento del 0%: retorna el precio original.
    - Descuento del 100%: retorna 0.

Casos de uso:
    - Calcular el precio final de una compra con descuento.
    - Validar entrada de usuario para transacciones comerciales.
    - Aplicar descuentos porcentuales en sistemas de venta.

Revisión:
    - 2026-05-19: Encabezado documental agregado y estructura mejorada.
"""


def apply_discount(price: int | float, discount: int | float) -> str | int | float:
    """Calcular el precio final después de aplicar un descuento porcentual.

    Valida que los parámetros sean números en los rangos correctos,
    luego calcula el precio final restando el descuento porcentual.

    Args:
        price: El precio original del artículo (int o float).
        discount: El porcentaje de descuento a aplicar (0-100, int o float).

    Returns:
        El precio final (int o float) si la validación es exitosa,
        o un mensaje de error (str) si los datos no son válidos.
    """
    if type(price) not in (int, float):
        return "The price should be a number"
    
    if type(discount) not in (int, float):
        return "The discount should be a number"
        
    if price <= 0:
        return "The price should be greater than 0"
        
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
        
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    return final_price


if __name__ == "__main__":
    # Ejemplo de uso
    print(apply_discount(100, 20))    # 80
    print(apply_discount(200, 50))    # 100
    print(apply_discount(50, 0))      # 50