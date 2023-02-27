import sqlalchemy as db
from connect_db import engine

# create a metadata object
metadata_obj = db.MetaData()

employee = db.Table(
    'employee',
    metadata_obj,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String),
    db.Column('age', db.Integer),
    db.Column('hired_at', db.Integer)
)

metadata_obj.create_all(engine)
