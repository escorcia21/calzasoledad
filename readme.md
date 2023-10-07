# Calzado API
## Descripción
API para el manejo de calzado
## Instalación
1. Clonar el repositorio
2. Crear el entorno virtual:
```bash
python3.10 -m venv env
```
3. Activar el entorno virtual:
```bash
# Linux
source env/bin/activate
# Windows
env\Scripts\activate
```
4. Instalar las dependencias:
```bash
pip install -r requirements.txt
```
5. Crear el archivo .env:
```bash
touch .env
```
6. Agregar las variables de entorno:
```bash
API_VERSION = "1.0"
APP_NAME = "Calzado"
SQLALCHEMY_DATABASE_URI = database_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_MODE = True
```
7. Agregar el archivo .flaskenv:
```bash
touch .flaskenv
```
8. Agregar las variables de entorno:
```bash
#.flaskenv
FLASK_APP=main
FLASK_ENV=development
FLASK_RUN_PORT=8080
FLASK_DEBUG=1
```
6. Ejecutar el proyecto:
```bash
flask run
```
