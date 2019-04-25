from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from models.Kenteken import Kenteken
from utils.orchestrator import Orchestrator


class Auto(Orchestrator().base):

    __tablename__ = 'auto'

    id = Column(Integer, primary_key=True)
    merk = Column(String(16))
    kenteken = relationship("Kenteken", order_by=Kenteken.id, back_populates="auto")

    def __init__(self, merk: str):
        self.merk = merk

    def __repr__(self) -> str:
        return f"<Auto(merk='{self.merk}')>"
