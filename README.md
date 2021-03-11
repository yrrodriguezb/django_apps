# DJANGO APPS

Proyecto de ejemplo para profundizar en la creación de aplicaciónes web con **[Django](https://www.djangoproject.com/)** y **[Python 3.8](https://www.python.org/downloads/release/python-386/)**


## Configuración Inicial

### Requisitos para el Sistema Operativo Ubuntu

1. Instalar la siguientes dependencias para **[mysqlclient](https://pypi.org/project/mysqlclient/)**
    ``` bash
    sudo apt-get install python-dev default-libmysqlclient-dev

    # and 

    sudo apt-get install python3-dev
    ```

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


## Configuración aplicación de autenticación con social auth

1. Para el funcionamiento de la autenticacion con **[social-auth-app-django](https://python-social-auth.readthedocs.io/en/latest/)**. Ejecutar la aplicacion ***runserver_plus*** proporcionado por el paquete **[django_extensions](https://django-extensions.readthedocs.io/en/latest/)** con el siguiente comando:

    ```bash
    # Proporciona un nombre de archivo al comando runserver_plus para el certificado SSL/TLS. 
    # Django Extensions generará una clave y un certificado automáticamente.
    
    python manage.py runserver_plus --cert-file cert.crt
    ```

    Esta configuracion se realiza debido a que algunos metodos de autenticacion unicamente funcionan sobre el protocolo **[https](https://es.wikipedia.org/wiki/Protocolo_seguro_de_transferencia_de_hipertexto)**. 

2.  Crear el archivo secrets.py en el directorio de configuracion del proyecto
    
    ```bash
    # django_apps/config/social_auth
    
    touch secrets.py
    ```

3.  Editar el archivo secrets.py con los keys y tokens de autenticacion de **[Facebook](https://developers.facebook.com)**, **[Twitter](apps.twitter.com/)** y **[Google](https://developers.google.com/)**

    ```python
    # Keys and tokens Social Auth

    SOCIAL_AUTH_FACEBOOK_KEY = 'SOCIAL_AUTH_FACEBOOK_KEY'
    SOCIAL_AUTH_FACEBOOK_SECRET = 'SOCIAL_AUTH_FACEBOOK_SECRET'
    SOCIAL_AUTH_TWITTER_KEY = 'SOCIAL_AUTH_TWITTER_KEY'
    SOCIAL_AUTH_TWITTER_SECRET = 'SOCIAL_AUTH_TWITTER_SECRET'
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'
    ```

## Aplicaciones

1. Aplicación Books - **[Introducción Django - Class-based views](https://docs.djangoproject.com/en/3.1/topics/class-based-views/)**
2. Aplicacion Blog
3. Aplicación Social Website

    