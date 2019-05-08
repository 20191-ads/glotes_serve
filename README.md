# Heroku Django Starter Template

An utterly fantastic project starter template for Django 2.0.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pipenv install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

## Alacance del sistema
Sistema que administra las cobranzas de una asociación de vivienda, Caso Las Américas
La admistración será por lote.

    1. Registro de lotes (Debe registrar los dueños del lote, sin embargo el dueño puede acceder a más de un lote)
    2. Cargar cobranza al estado de cuenta del lote (Se cargarán direferentes conceptos de cobranza, también deberá permitir la anulación de la cobranza, notificar al correo la fecha de pago)
    3. Registrar la cobranza (El usuario deberá subir el recibo al sistema para luego ser validado por el tesorero de la asociación)
    4. Control de asistencia a las reuniones (Vía lector QR, el asistente deberá traer su QR impreso o en su smartphone, deberá haber una opcion via DNI)
    5. Reportes
        a) Cantidad de lotes {vendidos, libres}
        b) Estado de cuenta {lote, total} (visualizar lo cobrado y por cobrar)
        c) Lotes {deudas, sin deudas}
        d) Registro de asistencia {Por día}

