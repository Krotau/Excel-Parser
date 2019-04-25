from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from utils.singleton import Singleton


class Orchestrator(metaclass=Singleton):

    def __init__(self, connection_string: str = 'sqlite:///test.db', deployment_level: str = 'staging'):
        self.engine = create_engine(connection_string, echo=False)
        self.base = declarative_base(bind=self.engine)
        self.deployment = deployment_level

    def __repr__(self) -> str:
        return f"<Orchestrator: (engine: {self.engine.engine}, deployment level: {self.deployment})>"
