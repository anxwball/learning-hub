"""
Problema  : Determinar si un año es bisiesto. Reglas: divisible por 4 pero no
por 100, a menos que sea divisible por 400.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, condicionales, operadores
Fecha     : 2026-05-10
Estado    : resuelto

Enfoque:
        - Aplicar la regla del calendario gregoriano con condiciones anidadas
            sobre divisibilidad.

Complejidad: Tiempo O(1) | Espacio O(1)
        - Solo se evalúan unas pocas operaciones módulo y comparaciones.

Casos límite:
        - Los años divisibles por 400 sí son bisiestos aunque también lo sean
            por 100.
        - Entradas no numéricas generan `ValueError` al convertir.

Casos de uso:
    - Validar calendarios, agendas o ciclos anuales.
    - Comprobar años objetivo en recordatorios y reportes.
    - Automatizar reglas temporales en aplicaciones educativas.

Revisión:
        - 2026-05-10: Encabezado y docstring normalizados al formato de la serie.
"""

def main():
    """Determinar si un año es bisiesto y mostrar el resultado.

    Solicita un año por consola y aplica las reglas de bisiesto para mostrar
    el resultado final.

    Returns:
        None
    """
    año: int = int(input("Ingrese un año: "))
    # Usa mod para verificar las condiciones de bisiesto según las reglas establecidas
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")

if __name__ == '__main__':
    main()
