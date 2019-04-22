from Utils.Orchestrator import Orchestrator


class Kenteken(Orchestrator):

    __tablename__ = 'kenteken'

    def __repr__(self):
        return f"User(first_name='{self.kenteken}' | last_name='{self.klant_id}' | nickname='{self.auto_id}')"
