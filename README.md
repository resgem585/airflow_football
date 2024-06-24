# Airflow Deploy Football Leagues

## Requisitos previos
- **Docker:** Se requiere la instalación de Docker. En caso de no tenerlo instalado, se puede habilitar WSL para Ubuntu siguiendo las instrucciones correspondientes.
- **CLI de ASTRO en Linux:** Es necesario instalar la CLI de ASTRO en Linux. Las instrucciones detalladas se encuentran [aquí](https://docs.astronomer.io/astro/cli/install-cli).
- **Inicialización del proyecto:** Iniciar un proyecto con la versión 6.0.3 utilizando los siguientes comandos:


## Configuración inicial
- Utilizar `localhost:8080` para acceder a la CLI de Airflow.
- En caso de errores, verificar los LOGS del webserver de Docker. Se puede borrar la imagen en caso de error utilizando el comando de fuerza bruta de Docker para borrar todas las imágenes.

## Acceso a la interfaz de usuario de Airflow
- Utilizar las credenciales `ADMIN` para el usuario y la contraseña.

## Extracción y limpieza de datos
- Extraer datos de la URL de las ligas de fútbol y realizar limpieza de los datos utilizando Jupyter Notebook o instalando los paquetes del archivo `requirements.txt`.
- Utilizar el archivo `football_leagues.ipynb`.

## Conexión a Snowflake
- Crear una cuenta en Snowflake.
- Crear un worksheet SQL.
- Ejecutar las queries del archivo `set_up_snow_queries.sql` en el siguiente orden:
1. Crear la base de datos.
2. Crear las tablas.
3. Ejecutar los siguientes queries como stage, etc.
- Refrescar las bases de datos para asegurarse de que aparezcan correctamente.

## Configuración de conexión en Snowflake
- En la UI de Snowflake, ir a "Connections".
- Configurar la conexión con la siguiente información:
- URL: `https://{account_id}.{region_name}.snowflakecomputing.com` (por ejemplo, `https://gjb49692.us-east-1.snowflakecomputing.com`).
- Realizar el test de conexión y guardar los cambios.

## Configuración de variables de entorno
- En la sección de administración de Airflow, configurar las siguientes variables de entorno:
```json
{
  "path_file": "/usr/local/airflow/premier_positions.csv",
  "stage": "demo_stage",
  "table": "football_leagues",
  "DWH": "normal_wh",
  "DB": "leagues",
  "ROLE": "accountadmin"
}

## Para el tutorial paso a paso aqui les dejo la liga

https://drive.google.com/file/d/1frxcvJcs2D6ugMCEi4_M-8OWd3vQFe8l/view?usp=drive_link
