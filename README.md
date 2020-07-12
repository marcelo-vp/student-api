## Setting up the environment
### Create a virtualenv
    mkvirtualenv student-api -p python3
### Install dependencies
    make requirements

## To Do
- create student model with schema
- configure MySQL ORM for Python
- add command to create DB and add student table
- add Flask app with test route
- add POST, GET (list), GET(filter), PATCH and DELETE routes and views

- **create docker to abstract services from OS**
- **add cache**

## Database
### Student model
- id
- nome
- idade
- serie
- nome_do_pai
- nome_da_mae
- data_matricula
- notas_do_semestre
- mensalidades_em_atraso
