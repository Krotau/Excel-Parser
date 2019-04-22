from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from Utils.Singleton import Singleton


class Orchestrator(metaclass=Singleton):

    def __init__(self):
        self.base = declarative_base()
        self.engine = create_engine('sqlite:///test.db', echo=True)