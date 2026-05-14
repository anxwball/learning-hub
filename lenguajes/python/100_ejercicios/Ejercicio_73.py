"""
Problema  : Crear una clase Libro con atributos: título, autor, editorial, año de publicación. Método: constructor.
Fuente    : Entrenamiento Python con 100 Ejercicios - Facultad Autodidacta
Plataforma: Youtube (https://youtube.com/playlist?list=PLoRfWwOOv4jyO61oMnqpD6i_0GBNXqzTZ&si=K9eMCCoefGVWzqB0)
Etiquetas : POO, encapsulación, atributos
Fecha     : 2026-05-13
Estado    : resuelto

Enfoque:
    - Crear una clase que modele un libro con metadatos básicos.
    - Almacenar información de publicación (autor, editorial, año).
    - Demuestra inicialización de atributos de instancia.

Complejidad: Tiempo O(1) | Espacio O(1)
    - El constructor realiza asignaciones constantes.
    - El espacio es constante; se almacenan cuatro atributos de tamaño fijo.

Casos límite:
    - Libro válido: título largo, autor conocido, año histórico (1967).
    - Año futuro: 2050 (predicción de publicación).
    - Año muy antiguo: 1000 (manuscritos antiguos).
    - Campos vacíos: título o autor vacíos (debería validarse).

Casos de uso:
  - Sistemas de bibliotecas digitales y catálogos.
  - Aplicaciones de reseñas y recomendaciones de libros.
  - Gestión de inventarios en librerías.

Revisión:
    - 2026-05-13: Normalizado. Encabezado completo, agregado método __str__.
"""
class Libro:
    """Representa un libro con metadatos de publicación.

    Atributos:
        titulo (str): Título del libro.
        autor (str): Nombre del autor.
        editorial (str): Editorial que publicó el libro.
        año_publicacion (int): Año de publicación.
    """
    def __init__(self, titulo: str, autor: str, editorial: str, año_publicacion: int) -> None:
        """Inicializa un libro con sus metadatos.

        Args:
            titulo (str): Título del libro.
            autor (str): Nombre del autor.
            editorial (str): Editorial que publicó el libro.
            año_publicacion (int): Año de publicación (debe ser positivo).
        """
        self.titulo: str = titulo
        self.autor: str = autor
        self.editorial: str = editorial
        self.año_publicacion: int = año_publicacion

    def __str__(self) -> str:
        """Retorna una representación legible del libro.

        Returns:
            str: Resumen formateado del libro.
        """
        return (f"Libro: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Editorial: {self.editorial}\n"
                f"Año: {self.año_publicacion}")


def main() -> None:
    """Crea instancias de Libro y muestra su información.

    Demuestra el almacenamiento de metadatos de libros y su representación.

    Returns:
        None
    """
    print("=== Información de Libros ===\n")
    libro1: Libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 
                           "Editorial Sudamericana", 1967)
    print(libro1)
    print()
    libro2: Libro = Libro("Don Quijote", "Miguel de Cervantes", 
                           "Real Academia Española", 1605)
    print(libro2)

if __name__ == '__main__':
    main()
