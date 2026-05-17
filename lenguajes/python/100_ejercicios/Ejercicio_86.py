"""
Problema  : Elevar un número al cuadrado utilizando lambda.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : fundamentos, lambda, operaciones-matemáticas
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Usar funciones `lambda` annónimas para definir operaciones matemáticas
      simples sin necesidad de una función nombrada.
    - Demuestra la sintaxis de lambda y su integración con `map()` para
      transformaciones rápidas en listas.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es lineal, procesando cada uno de los n elementos.
    - El espacio es lineal, creando una lista de n cuadrados.

Casos límite:
    - Cero: [0] -> [0]
    - Números negativos: [-2, -3] -> [4, 9]
    - Números grandes: [1000] -> [1000000]
    - Lista vacía: [] -> []

Casos de uso:
  - Transformaciones rápidas sin definir funciones separadas.
  - Integración con map/filter para pipelines de datos.
  - Cálculos puntuales en algoritmos.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""
def main() -> None:
    """Elevar números al cuadrado usando lambda con map().

    Aplica una función lambda que calcula x^2 a cada elemento usando map(),
    demostrando cómo lambda permite definiciones funcionales inline.

    Returns:
        None
    """
    numeros: list[int] = [1, 2, 3, 4, 5]
    resultado: list[int] = list(map(lambda x: pow(x, 2), numeros))
    print(f"Números originales: {numeros}")
    print(f"Números al cuadrado: {resultado}")
    

if __name__ == '__main__':
    main()
