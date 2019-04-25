import unittest
from utils.orchestrator import Orchestrator


class TestOrchestrator(unittest.TestCase):
    """
    Test the orchestrator.. duh
    """

    def test_singleton(self):
        self.assertTrue(Orchestrator() is Orchestrator())

    def test_declarative_base(self):
        self.assertTrue(Orchestrator().base is not None)

    def test_engine(self):
        self.assertTrue(Orchestrator().engine is not None)


if __name__ == '__main__':
    unittest.main()
