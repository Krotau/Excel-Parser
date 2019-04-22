# Klant Model
from sqlalchemy import Column, String, Integer
from Utils.Orchestrator import Orchestrator


class Klant(Orchestrator().base):

    __tablename__ = 'klant'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"User(first_name='{self.first_name}' | last_name='{self.last_name}' | nickname='{self.nickname}')"
