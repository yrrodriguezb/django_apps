# DJANGO APPS

Proyecto de ejemplo para profundizar en la creación de aplicaciónes web con **[Django](https://www.djangoproject.com/)**


## Configuración Inicial

### Configuración del entorno virtual

1.  Crear entorno virtual
    ``` bash
    # django_apps

    python -m venv venv
    ```

2. Iniciar el entorno virtual
    ``` bash
    # Activar entorno virtual

    source venv/bin/activate
    ```

    ```bash
    # Desactivar entorno virtual

    deactivate
    ```

3. Instalar dependencias
    ```bash
    # Ejecutar el comando pip

    pip install -r requirements.txt
    ```

## Ejecutar la applicación

1. Para ejecutar el proyecto podemos ejecutar el siguiente comando:

    ```bash
    # Cambiar de ubicacion en la terminal a la carpeta src

    cd src

    # Modo local

    python manage.py runserver

    # Modo desarrollo

    python manage.py runserver --settings=django_apps.config.dev

    # Modo producción

    python manage.py runserver --settings=django_apps.config.prod    
    ```

2. Ejecutar las migraciones

    ```bash
    # Ejecutar la opción migrate

    python manage.py migrate 
    ```

3. Finalmente abrir un navegador en la dirección **[localhos:8080](http://localhost:8000/)**


## Aplicaciones

1. Aplicación Books - **[Introducción Django - Class-based views](https://docs.djangoproject.com/en/3.1/topics/class-based-views/)**

    