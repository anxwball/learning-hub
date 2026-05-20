# Checklist para convertir un ejercicio en mini‑proyecto desplegable

1. Seleccionar ejercicio objetivo

- Elegir un ejercicio representativo y con posibilidad de ampliación.

1. Crear estructura de proyecto

- Crear `proyectos/<nombre>/` con `app/`, `requirements.txt` y `README.md`.

1. Documentar con la plantilla

- Completar `README.md` usando `docs/PROJECT_README_TEMPLATE.md`.

1. Añadir datos de ejemplo

- Incluir `data/sample/` y scripts para poblar la base de datos si aplica.

1. Añadir Dockerfile

- Crear un `Dockerfile` mínimo que permita ejecutar la aplicación.

1. Tests y calidad

- Añadir tests básicos y (opcional) un `Makefile` o scripts para ejecutarlos.

1. CI básico

- (Opcional) Añadir un workflow en `.github/workflows/ci.yml` que instale dependencias y ejecute tests en cada Pull Request.

1. Despliegue (opcional)

- Opcional: desplegar en Heroku/GCP/Vercel u otra plataforma; anotar la URL en `README.md` si corresponde.

1. Ejemplos de uso

- Incluir ejemplos `curl`/Postman y capturas de pantalla cuando sea posible.

1. Actualizar `README.md` raíz

- Añadir el proyecto a la sección "Portfolio destacado" del `README.md`.

1. Revisar licencias y datos sensibles

- No incluir credenciales ni claves en el repositorio.

## Última actualización

2026-05-20
