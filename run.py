#
# Description:  This program parses Excel Files (.xlsx) and optionally uploads the information to
#               a remote database if a connection string and models are provided in advanced
#
# Author:       Tim Smeets
#

from Utils.Orchestrator import Orchestrator
from Utils.Repository import Repository


def main():
    orchestrator = Orchestrator()
    repository = Repository(orchestrator)


if __name__ == "__main__":
    main()

