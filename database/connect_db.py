from sqlalchemy import create_engine
from sqlalchemy.engine import URL

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

url = URL.create(
    drivername='postgresql',
    host=os.environ.get('ENV_host'),
    port=os.environ.get('ENV_port'),
    database=os.environ.get('ENV_database'),
    username=os.environ.get('ENV_username'),
    password=os.environ.get('ENV_password')
)

engine = create_engine(url)

