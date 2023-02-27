from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, delete, update
from database.connect_db import engine
from models.models import Employee
from utils.convert_dict import convert_dict

routes = Blueprint('routes', __name__)
# session = Session(engine)

# list the employees
@routes.route('/', methods=('GET',))
def list():
    try:
        stmt = select(Employee)
        with engine.connect() as conn:
            employees = conn.execute(stmt)
            return [convert_dict(employee) for employee in employees]
    except Exection as err:
        return print(err)

# get a employee
@routes.route('/employee/<int:id>', methods=('GET',))
def get_one(id):
    try:
        stmt = select(Employee).where(Employee.id == id)
        with engine.connect() as conn:
            matches = conn.execute(stmt)
            employee = [convert_dict(match) for match in matches]
            return jsonify(employee[0])
    except Exception as err:
        print(err)

# new employee
@routes.route('/employee', methods=('POST',))
def create():
    try:
        stmt = insert(Employee).values(
            name=request.json['name'],
            age=request.json['age'],
            hired_at=request.json['hired_at']
            )
        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            return jsonify({"status": "success"})
    except Exception as err:
        return print(err)

@routes.route('/employee/<int:id>', methods=('PUT',))
def edit(id):
    try:
        with engine.connect() as conn:
            stmt = update(Employee).values(
                name=request.json['name'],
                age=request.json['age'],
                hired_at=request.json['hired_at']
            ).where(Employee.id == id)
            employee = conn.execute(stmt)
            conn.commit()
            return jsonify({"status": "done"})
    except Exection as err:
        print(err)

@routes.route('/employee/<int:id>', methods=('DELETE',))
def delete(id):
    try:
        with Session(engine) as session:
            employee = session.get(Employee, id)
            session.delete(employee)
            session.commit()
            return jsonify({"status": "done"})
    except Exection as err:
        print(err)
