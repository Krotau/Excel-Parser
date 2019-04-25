from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from utils.orchestrator import Orchestrator


class Kenteken(Orchestrator().base):

    __tablename__ = 'kenteken'

    # benamingen
    id = Column(Integer, primary_key=True)
    kenteken = Column(String(50))
    klant_id = Column(Integer, ForeignKey('klant.id'))
    auto_id = Column(Integer, ForeignKey('auto.id'))

    # relaties
    klant = relationship("Klant", back_populates="kenteken")
    auto = relationship("Auto", back_populates="kenteken")

    def __init__(self, kenteken: str, klant_id: int, auto_id: int):
        self.kenteken = kenteken
        self.klant_id = klant_id
        self.auto_id = auto_id

    def __repr__(self) -> str:
        return f"<Kenteken(kenteken='{self.kenteken}' | klant_id='{self.klant_id}' | auto_id='{self.auto_id}')>"
