"""
Problema  : Conectarse a una base de datos MySQL, hacer una consulta a una tabla y mostrar la información en la consola.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : bases-de-datos, POO, consultas-SQL, MySQL
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Diseñar clases para gestionar conexiones a MySQL y ejecutar consultas
      usando herencia (Conexion como clase base, Visitas como especialización).
    - Demuestra POO con encapsulación, herencia, y manejo de recursos
      (conexiones y cursores) mediante try-finally o context managers.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es O(n), donde n es el número de registros en la tabla.
    - El espacio es O(n), almacenando todos los registros en memoria.

Casos límite:
    - Tabla vacía: consulta devuelve lista vacía []
    - Conexión fallida: lanza excepción (mensaje de error)
    - Credenciales inválidas: MySQL rechaza la conexión
    - Base de datos/tabla no existe: error de SQL

Casos de uso:
  - Aplicaciones web: obtener datos de usuarios/sesiones.
  - Reportes: exportar información de bases de datos a consola.
  - Integración: automatizar consultas y procesamiento de datos.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite, Type hints.
"""
import mysql.connector
from typing import Any

class Conexion:
    """Clase base para gestionar conexiones a MySQL."""
    
    def conectar(self) -> Any:
        """Establecer conexión a la base de datos MySQL.
        
        Returns:
            Any: Objeto de conexión a MySQL.
        
        Raises:
            Exception: Si la conexión falla (credenciales inválidas, servidor no disponible, etc.).
        """
        try:
            conn: Any = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="visitas"
            )
            return conn
        except Exception as e:
            print(f"Error al conectar a MySQL: {e}")
            raise

class Visitas(Conexion):
    """Clase especializada para consultas en la tabla de visitas."""
    
    def consulta_select(self) -> list:
        """Ejecutar consulta SELECT en la tabla t_visitas.
        
        Returns:
            list: Lista de tuplas con id y paterno de cada registro.
        
        Raises:
            Exception: Si la conexión o consulta falla.
        """
        conn: Any = self.conectar()
        sql: str = "SELECT id, paterno FROM t_visitas"
        cursor: Any = conn.cursor()
        cursor.execute(sql)
        registros: list = cursor.fetchall()
        cursor.close()
        conn.close()
        return registros

    def imprimir_datos(self) -> None:
        """Obtener y mostrar todos los registros de la tabla.
        
        Returns:
            None
        """
        datos: list = self.consulta_select()
        for filas in datos:
            print(filas)


def main() -> None:
    """Consultar base de datos MySQL e imprimir resultados.

    Crea una instancia de Visitas, ejecuta una consulta SELECT
    en la tabla t_visitas y muestra los resultados.

    Returns:
        None
    """
    visita: Visitas = Visitas()
    visita.imprimir_datos()

if __name__ == '__main__':
    main()
