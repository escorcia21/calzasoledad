# Footwear API
## Description
API for footwear management
## Installation
1. Clone the repository
2. Create the virtual environment:
```bash
python3.10 -m venv env
```
3. Activate the virtual environment:
```bash
# Linux
source env/bin/activate
# Windows
env\Scripts\activate
```
4. Install the dependencies:
```bash
pip install -r requirements.txt
```
5. Create the .env file:
```bash
# Linux
touch .env
# Windows
type nul > .env
```
6. Add the environment variables:
```bash
API_VERSION = "1.0"
APP_NAME = "Calzado"
SQLALCHEMY_DATABASE_URI = database_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_MODE = True
```
7. Add the .flaskenv file:
```bash
# Linux
touch .flaskenv
# Windows
type nul > .flaskenv
```
8. Add the environment variables:
```bash
#.flaskenv
FLASK_APP=main
FLASK_ENV=development
FLASK_RUN_PORT=8080
FLASK_DEBUG=1
```
6. Run the project:
```bash
flask run
```

# Database [<a href="https://mermaid.js.org/syntax/entityRelationshipDiagram">docs</a> - <a href="https://mermaid.live/edit#pako:eNo9kMluwjAQhl_F-AykQMuSA1WrbuLQQ3v1ZbAnsVXHkzrjVhHi3etQwKfRv4w-z0FqMihL2eF3wqDxyUEdoVHhwTuNk-12RzaU4g29JzHMY2HpV0BE0VO6V8ETtdkGz1Zb1F8qiPyG5LX84mrLAmpwoWNh-5a0pWCiAxUwGBXeiVHEU4oq8V_6AHYUwAu2lLLTjVQ4bc1rT2yleI0IfJG320faZ9ABbk-Jz3hZnFxBduR9L2oiM5Jj2WBswJn8-cMArSRbbFDJMo8GK0ielVThmKOpNcD4bBxTlGUFvsOxhMT02QctS44JL6HzAS-iJzCYOwfJfTscunYd542aQuXqQU_RZ9kyt11ZFIM9rR3btJ9qaorOGQuR7c9mWSznyzXMF7hcLeBusTB6P9usq_ntrDKrm9kc5PF4_AMJE56Z">live editor</a>]
```mermaid
erDiagram
    employees ||--|| roles : has
    employees ||--|{ production : make
    roles {
        roleId Int
        userType varchar(255)
    }
    employees {
        cc varchar(255)
        name varchar(255)
        lastName varchar(255)
        role Int
        password varchar(255)
    }

    porducts ||--|{ production : be
    roles ||--|{ porducts : belongs
    porducts {
        porductID Int
        porductName varchar(255)
        price Int
        unitCompensation Float
        packagesCompensation Float
        productRoleId Int
    }
    production {
        productionId Int
        employeeId Int
        productId Int
        productionDate date
        ammount Int
    }
```
