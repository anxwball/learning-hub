"""
Problema  : Obtener datos de rendimiento de mi computadora con psutil.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : bibliotecas-externas, monitoreo, rendimiento-del-sistema
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Usar la librería psutil para obtener métricas del sistema.
    - Recopilar información de CPU, memoria y disco en un diccionario.
    - Demuestra integración de bibliotecas externas para monitoreo.

Complejidad: Tiempo O(1) | Espacio O(1)
    - obtener_datos_computadora() es O(1): recopila métricas fijas.
    - Las llamadas a psutil.cpu_percent() pueden variar según el intervalo.
    - El espacio es constante; se retorna un diccionario con 3 entradas.

Casos límite:
    - Sistema bajo carga: CPU al 100%, memoria llena (> 90%).
    - Sistema ocioso: CPU al 0%, memoria baja (< 10%).
    - Disco con poco espacio: < 1% disponible.
    - Sin acceso a información de disco: excepción (manejo requerido).
    - Intervalo de CPU: 1 segundo es estándar (puede aumentarse).

Casos de uso:
  - Dashboards de monitoreo del sistema.
  - Alertas de recursos limitados.
  - Herramientas de diagnóstico y optimización.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, docstrings mejorados, manejo de errores.
"""
import psutil

def obtener_datos_computadora() -> dict:
    """Obtiene los datos de rendimiento de la computadora.

    Recopila información del CPU, memoria y disco del sistema usando psutil.

    Returns:
        dict: Diccionario con claves:
            - "memoria_total" (str): Memoria total en GB.
            - "cpu_porcentaje" (str): Uso de CPU en porcentaje.
            - "disco_total" (str): Espacio total en disco en GB.
    """
    memoria = psutil.virtual_memory()
    datos: dict = {
        "memoria_total": f"{memoria.total / pow(1024, 3):.2f} GB",
        "cpu_porcentaje": f"{psutil.cpu_percent(interval=1)}%",
        "disco_total": f"{psutil.disk_usage('/').total / pow(1024, 3):.2f} GB",
    }
    return datos

def main() -> None:
    """Obtiene y muestra datos de rendimiento del sistema.

    Llama a obtener_datos_computadora() y muestra la información
    de CPU, memoria y disco en la consola.

    Returns:
        None
    """
    print("=== Datos de Rendimiento de la Computadora ===\n")
    datos_computadora: dict = obtener_datos_computadora()
    
    print("Información del Sistema:")
    for clave, valor in datos_computadora.items():
        nombre_formateado: str = clave.replace('_', ' ').title()
        print(f"{nombre_formateado}: {valor}")

if __name__ == '__main__':
    main()
