# Klant Model
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from Models.Kenteken import Kenteken

from Utils.Orchestrator import Orchestrator


class Klant(Orchestrator().base):

    __tablename__ = 'klant'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    nickname = Column(String(50))
    kenteken = relationship("Kenteken", order_by=Kenteken.id, back_populates="klant")

    def __init__(self, first_name: str, last_name: str, nickname: str):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname

    def __repr__(self) -> str:
        return f"<User(first_name='{self.first_name}' | last_name='{self.last_name}' | nickname='{self.nickname}')>"
