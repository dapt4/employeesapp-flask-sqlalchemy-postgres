# employeesapp-flask-sqlalchemy-postgres

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requirements

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_NAME='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'

finally the project run with: 

`$ flask --app app run`

open your browser or your REST Client in: 

### get all employees
`GET http://localhost:5000`
### get a employee
`GET http://localhost:5000/employee/5`
### create a new employee
`POST http://localhost:5000/employee`
### edit a employee
`PUT http://localhost:5000/employee/5`
### delete a employee
`DELETE http://localhost:5000/employee/5`

