#
# Description:  This program parses Excel Files (.xlsx) and optionally uploads the information to
#               a remote database if a connection string and models are provided in advanced
#
# Author:       Tim Smeets
#

from utils.orchestrator import Orchestrator
from utils.repository import Repository


def main():
    orchestrator = Orchestrator()
    repository = Repository(orchestrator)
    repository.create_all()
    repository.add_dummy_data()
    repository.read_all_klant()


if __name__ == "__main__":
    main()
