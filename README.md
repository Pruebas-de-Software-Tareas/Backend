# Proyecto de Gestión de Eventos - Backend

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Este repositorio contiene el código fuente del backend para la aplicación de **Gestión de Entradas para Micro-Eventos**. Provee una API RESTful para que el frontend pueda consumir y gestionar los datos.

## 📝 Descripción

El backend está construido con **FastAPI**, un framework moderno y de alto rendimiento para construir APIs con Python. Utiliza **SQLAlchemy** como ORM para interactuar con una base de datos **SQLite**, lo que facilita la configuración y el despliegue sin necesidad de un servidor de base de datos externo.

### Funcionalidades Clave
- **Endpoints CRUD:** Operaciones completas para Crear, Leer, Actualizar y Eliminar eventos.
- **Validación de Datos:** Uso de Pydantic para validar automáticamente los datos de entrada y salida, asegurando la integridad de la API.
- **Documentación Automática:** Gracias a FastAPI, la API genera automáticamente documentación interactiva (Swagger UI y ReDoc).

## 🛠️ Tecnologías Utilizadas

- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn
- **ORM:** SQLAlchemy
- **Base de Datos:** SQLite
- **Validación de Datos:** Pydantic
- **Lenguaje:** Python 3.10+

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el backend en tu entorno local.

### Prerrequisitos
- **Python:** Asegúrate de tener Python 3.10 o una versión superior instalada.
- **pip:** El gestor de paquetes de Python debe estar disponible.

### Pasos de Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_BACKEND>
    cd nombre-de-la-carpeta-backend
    ```

2.  **Crear y activar un entorno virtual:**
    Es una buena práctica trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

    ```bash
    # Crear el entorno virtual
    python -m venv venv
    ```

    ```bash
    # Activar en Windows
    .\venv\Scripts\activate
    ```

    ```bash
    # Activar en macOS/Linux
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    Instala todos los paquetes necesarios para que la aplicación funcione.
    ```bash
    pip install fastapi uvicorn sqlalchemy pydantic
    ```

## ▶️ Ejecutar el Servidor

Una vez que las dependencias estén instaladas, puedes iniciar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload


El servidor estará disponible en:  
http://127.0.0.1:8000

## 🌐 Documentación de la API

Una de las grandes ventajas de FastAPI es la documentación automática. Una vez que el servidor esté en ejecución, puedes acceder a:

- **Swagger UI (interactivo):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc (alternativo):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Desde la interfaz de Swagger, puedes probar todos los endpoints de la API directamente desde tu navegador.

## 🤝 Cómo Contribuir

Las contribuciones son bienvenidas. Por favor, sigue el flujo de trabajo basado en Pull Requests definido para el proyecto.

1. Crea una nueva rama:

```bash
git checkout -b feature/mi-funcionalidad
```

2. Realiza tus cambios y haz commits.
3. Sube tu rama:

```bash
git push origin feature/mi-funcionalidad
```

4. Abre un Pull Request en GitHub para su revisión.

## 📜 Licencia

Este proyecto está distribuido bajo la Licencia MIT.

