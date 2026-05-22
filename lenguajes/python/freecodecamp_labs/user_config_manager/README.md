# Gestor de configuración de usuario (Python) - Proyecto para Certificación (1/5)

---

## Descripción

Este laboratorio implementa un gestor de configuraciones simple que permite
añadir, actualizar, eliminar y mostrar ajustes de usuario (tema, notificaciones,
volumen, etc.).

## Ubicación

`lenguajes/python/freecodecamp_labs/user_config_manager`

## Estado

- Laboratorio resuelto.
- Encabezado y documentación alineados con el formato del módulo Python.

## Estructura

- `main.py`: Implementación de `add_setting`, `update_setting`, `delete_setting` y `view_settings`.
- `README.md`: Documentación del laboratorio.

## Objetivo

Cumplir las historias de usuario y pasar las pruebas del laboratorio.

## Historias de usuario

- Definir un diccionario llamado `test_settings` con algunas configuraciones.
- Implementar las funciones `add_setting`, `update_setting`, `delete_setting` y `view_settings` con la semántica descrita en el módulo.

## Cómo ejecutar (local)

1. Requisitos

- Python 3.8+

1. Configuración

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Unix/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. Ejecutar

```bash
python main.py
```

## Pruebas

El runner del laboratorio verifica las funciones y el diccionario `test_settings`.

## Ejemplos

```python
from main import add_setting, view_settings

settings = {"theme": "dark"}
print(add_setting(settings, ("volume", "high")))
print(view_settings(settings))
```

## Notas

- Las claves y valores se normalizan a minúsculas para mantener consistencia.
- `view_settings` formatea las claves con la primera letra en mayúscula.

## Última actualización

2026-05-21
