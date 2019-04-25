#
# This file is responsible as acting as the repository. The repository uses defined functions
# in order to communicate with a database given a connection string.
#
from models.Klant import Klant
from models.Auto import Auto
from models.Kenteken import Kenteken
from utils.orchestrator import Orchestrator
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from random import randint


class Repository:

    def __init__(self, orchestrator: Orchestrator):
        """
        :param orchestrator:
        :type orchestrator { Orchestrator }
        """
        self.orchestrator = orchestrator
        self.create_session = sessionmaker(bind=self.orchestrator.engine)
        self.session: Session = self.create_session()

    def __repr__(self):
        return f"<Repository(using: {self.orchestrator.engine.engine})>"

    def add_dummy_data(self):

        data_klant = [
            Klant(first_name="Janneke", last_name="Grooters", nickname="Janski"),
            Klant(first_name="Tim", last_name="Smeets", nickname="Tiem"),
            Klant(first_name="Tijmen", last_name="Bekkering", nickname="TijTij")
        ]

        data_auto = [
            Auto(merk="Audi"),
            Auto(merk="Tesla"),
            Auto(merk="Mercedes")
        ]

        self.session.add_all(data_klant)
        self.session.add_all(data_auto)
        self.session.commit()

        data_kenteken = []
        for index, paar in enumerate(zip(data_klant, data_auto)):
            data_kenteken.append(Kenteken(str(randint(0, 999999)), paar[0].id, paar[1].id))

        self.session.add_all(data_kenteken)
        self.session.commit()

    def voeg_entiteit_toe(self, entiteit):
        self.session.add(entiteit)

    def voeg_entiteiten_toe(self, entiteiten):
        self.session.add_all(entiteiten)

    def read_all_klant(self):
        for instance in self.session.query(Klant).order_by(Klant.id):
            print(instance.id, instance.first_name, instance.kenteken)
        print()
        print("=====")
        print()

    def create_all(self):
        self.orchestrator.base.metadata.create_all()
