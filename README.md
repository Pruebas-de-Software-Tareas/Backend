# Backend - Gestión de Micro-Eventos

## Descripción
Este es el backend de la aplicación de micro-eventos, desarrollado con **FastAPI** y **SQLite**. Permite gestionar eventos, incluyendo creación, consulta, actualización y eliminación (CRUD). Está preparado para conectarse con un frontend (React/JS).

## Tecnologías
- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite (base de datos ligera incluida con Python)
- Pydantic (validación de datos)

## Instalación

1. Clonar repositorio:
```bash
git clone <URL_DEL_REPOSITORIO>
cd backend
```
2. Activar VENV:

```bash  
python -m venv venv

venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install fastapi uvicorn sqlalchemy pydantic

```
4. Ejecutar servidor:
```bash
uvicorn app.main:app --reload
```