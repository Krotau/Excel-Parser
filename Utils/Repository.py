#
# This file is responsible as acting as the repository. The repository uses defined functions
# in order to communicate with a database given a connection string.
#

from Utils.Orchestrator import Orchestrator


class Repository:

    def __init__(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator

    def __repr__(self):
        return f"<Repository(using: {self.orchestrator.engine.engine})>"
