"""
Problema  : Crear un programa que permita leer, crear y agregar información en un archivo de texto plano.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : archivos, poo, io, operaciones-de-ficheros
Fecha     : 2026-05-17
Estado    : resuelto

Enfoque:
    - Diseñar una clase `Archivo` que encapsule operaciones de archivo
      (crear, leer, agregar) con propiedades y setters para gestionar
      estado interno.
    - Demuestra POO con encapsulación, properties y validación de datos
      antes de operaciones de I/O.

Complejidad: Tiempo O(n) | Espacio O(n)
    - El tiempo es O(n), donde n es el tamaño del contenido del archivo.
    - El espacio es O(n), almacenando contenido en memoria.

Casos límite:
    - Nombre de archivo vacío: lanza ValueError
    - Archivo no existente para lectura: puede lanzar FileNotFoundError
    - Agregar contenido a archivo inexistente: crea el archivo primero
    - Contenido vacío: archivo creado sin datos

Casos de uso:
  - Gestor de configuración: leer/escribir ficheros de settings.
  - Log manager: agregar eventos a archivos de registro.
  - Almacenamiento persistente: guardar datos de usuario entre sesiones.

Revisión:
    - 2026-05-17: Normalizado. Mejorados Enfoque, Complejidad, Casos límite.
"""
class Archivo:
    def __init__(self) -> None:
        """Inicializar instancia de Archivo.

        Initializes private attributes for file name and content.
        """
        self._nombre_archivo: str = ""
        self._contenido: str = ""

    # Getters
    @property
    def nombre_archivo(self) -> str:
        """Obtener el nombre del archivo.
        
        Returns:
            str: Nombre del archivo.
        """
        return self._nombre_archivo
    
    @property
    def contenido(self) -> str:
        """Obtener el contenido del archivo.
        
        Returns:
            str: Contenido del archivo.
        """
        return self._contenido

    # Setters
    @nombre_archivo.setter
    def nombre_archivo(self, nombre: str) -> None:
        """Establecer el nombre del archivo.
        
        Args:
            nombre (str): Nuevo nombre del archivo.
        
        Returns:
            None
        """
        self._nombre_archivo = nombre
    
    @contenido.setter
    def contenido(self, contenido: str) -> None:
        """Establecer el contenido del archivo.
        
        Args:
            contenido (str): Nuevo contenido del archivo.
        
        Returns:
            None
        """
        self._contenido = contenido

    # Métodos
    def crear_archivo(self) -> None:
        """Crear un archivo con contenido.
        
        Raises:
            ValueError: Si el nombre del archivo está vacío.
        
        Returns:
            None
        """
        if not self._nombre_archivo:
            raise ValueError("El nombre del archivo no puede estar vacío.")
        with open(self._nombre_archivo, 'w') as archivo:
            archivo.write(self._contenido)
    
    def leer_archivo(self) -> str:
        """Leer el contenido del archivo.
        
        Raises:
            ValueError: Si el nombre del archivo está vacío.
        
        Returns:
            str: Contenido del archivo.
        """
        if not self._nombre_archivo:
            raise ValueError("El nombre del archivo no puede estar vacío.")
        with open(self._nombre_archivo, 'r') as archivo:
            return archivo.read()

    def agregar_contenido(self, nuevo_contenido: str) -> None:
        """Agregar contenido al final del archivo.
        
        Args:
            nuevo_contenido (str): Contenido a agregar.
        
        Raises:
            ValueError: Si el nombre del archivo está vacío.
        
        Returns:
            None
        """
        if not self._nombre_archivo:
            raise ValueError("El nombre del archivo no puede estar vacío.")
        with open(self._nombre_archivo, 'a') as archivo:
            archivo.write(nuevo_contenido)


def main() -> None:
    """Crear, leer y agregar contenido a un archivo.

    Demuestra todas las operaciones de la clase Archivo:
    crear un archivo, leer su contenido, y agregar más información.

    Returns:
        None
    """
    file: Archivo = Archivo()
    file.nombre_archivo = 'archivo_ejemplo.txt'
    file.contenido = 'Este es un archivo de texto plano creado desde Python.\n'
    file.crear_archivo()
    print("Contenido del archivo después de la creación:")
    print(file.leer_archivo())
    file.agregar_contenido('Agregando una nueva línea al archivo.\n')
    print("Contenido del archivo después de agregar nueva información:")
    print(file.leer_archivo())

if __name__ == '__main__':
    main()
