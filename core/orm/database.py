from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey

from settings import database_name, database_user, database_password

try:
    database_string = "postgresql://{}:{}@database:5432/{}".format(database_user, database_password, database_name)
    database = create_engine(database_string)
except Exception as ex:
    database_string = "postgresql://{}:{}@localhost:5432/{}".format(database_user, database_password, database_name)
    database = create_engine(database_string)

Session = sessionmaker(database)
db_access = Session()

models = declarative_base()

class NCase(models):
    __tablename__ = 'ncase'

    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    solutions = Column(Integer)

class Solution(models):
    __tablename__ = 'solution'

    id = Column(Integer, primary_key=True)
    ncase_id = Column(Integer, ForeignKey('ncase.id'))
    solution = Column(String)

models.metadata.create_all(database)

