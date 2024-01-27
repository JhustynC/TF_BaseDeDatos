# TF_BaseDeDatos

Trabajo final de base de datos donde se implementara un cliente que enviara consultas SQL a la base de datos local, el dominio del proyecto es una agencia de binenes raices

## Entorno Virtual (Crear)

> python -m venv venv

## Dependencias para ejecucion

Instalar dependencias para la ejecucion del programa
todas se encuentran especificadas en el archivo
requirements.txt

> Instalacion de la dependencias:

    pip install -r requirements.txt

## Acceso a base de datos mediante .env

Crear un archivo .env en la ruta principal del proyecto
en esta se encotraran las credenciales par ingresar a la
Base de Datos

> Estructura del .env:

    DATABASE_USER = userName

    DATABASE_PASSWORD = password

    DATABASE_HOST = localhost

    DATABASE_NAME = DataBaseName

> El uso de estas variables se muestra en src/postgress_conexion
