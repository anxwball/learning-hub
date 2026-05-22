"""
Problema  : Gestor de configuración de usuario — añadir, actualizar,
                        eliminar y mostrar ajustes.
Fuente    : FreeCodeCamp (inferred) <!-- inferred -->
Plataforma: FreeCodeCamp Python Certification <!-- inferred -->
Etiquetas : configuracion, usuario, diccionario, freecodecamp
Fecha     : 2026-05-21
Estado    : resuelto

Enfoque:
    - Uso de diccionario en memoria para almacenar ajustes.
    - Normalizar claves y valores a minúsculas para consistencia.
    - Mensajes claros de éxito/error para cada operación.

Complejidad: Tiempo O(1) por operación | Espacio O(n) para almacenamiento

Casos límite:
    - Diccionarios vacíos, claves inexistentes, diferencias de mayúsculas.

Casos de uso:
    - Laboratorios de aprendizaje, pruebas unitarias, ejemplos didácticos.

Revisión:
    - 2026-05-21: Documentación traducida y estandarizada; `main()` añadido.
"""

from typing import Dict, Tuple


# Configuración de ejemplo usada por pruebas y demostraciones
test_settings: Dict[str, str] = {"theme": "onedarkpro", "sound": "mid"}


def add_setting(settings: Dict[str, str], setting_tuple: Tuple[str, str]) -> str:
    """Añadir una nueva configuración al diccionario proporcionado.

    Las claves y valores se normalizan a minúsculas. Si la clave ya existe,
    se devuelve un mensaje de error y no se modifica el diccionario.

    Args:
        settings: Diccionario con las configuraciones actuales.
        setting_tuple: Tupla (clave, valor) a añadir.

    Returns:
        Mensaje de éxito o de error.
    """
    key, value = setting_tuple
    key, value = key.lower(), value.lower()

    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with "
            "this name."
        )
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: Dict[str, str], setting_tuple: Tuple[str, str]) -> str:
    """Actualizar una configuración existente en el diccionario.

    Clave y valor se normalizan a minúsculas. Si la clave no existe,
    se devuelve un mensaje de error.

    Args:
        settings: Diccionario con las configuraciones actuales.
        setting_tuple: Tupla (clave, valor) a actualizar.

    Returns:
        Mensaje de éxito o de error.
    """
    key, value = setting_tuple
    key, value = key.lower(), value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: Dict[str, str], key: str) -> str:
    """Eliminar una configuración por clave del diccionario.

    La clave se normaliza a minúsculas antes de la búsqueda.

    Args:
        settings: Diccionario con las configuraciones actuales.
        key: Clave a eliminar.

    Returns:
        Mensaje de éxito o de error.
    """
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"


def view_settings(settings: Dict[str, str]) -> str:
    """Devolver una cadena formateada con las configuraciones actuales.

    Si el diccionario está vacío, devuelve un mensaje claro.

    Args:
        settings: Diccionario con las configuraciones actuales.

    Returns:
        Cadena multilínea que comienza con "Current User Settings:" o
        "No settings available." cuando está vacío.
    """
    if not settings:
        return "No settings available."
    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")
    return "\n".join(lines) + "\n"


def main() -> None:
    """Demostrar el uso básico de las funciones de configuración de usuario.

    Las operaciones se ejecutan de forma demostrativa; las funciones están
    diseñadas para ser probadas por el runner del laboratorio.
    """
    local_settings: Dict[str, str] = {"theme": "light"}
    add_setting(local_settings, ("volume", "high"))
    update_setting(local_settings, ("theme", "dark"))
    delete_setting(local_settings, "volume")


if __name__ == "__main__":
    main()