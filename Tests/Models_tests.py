import unittest
from Models.Klant import Klant
from Models.Auto import Auto
from Models.Kenteken import Kenteken


class TestKlant(unittest.TestCase):
    """
    Test the klant.. duh
    """

    def test_klant(self):
        self.assertEqual(Klant.__tablename__, 'klant')


class TestAuto(unittest.TestCase):
    """
    Test the klant.. duh
    """

    def test_auto(self):
        self.assertEqual(Auto.__tablename__, 'auto')


class TestKenteken(unittest.TestCase):
    """
    Test the klant.. duh
    """

    def test_kenteken(self):
        self.assertEqual(Kenteken.__tablename__, 'kenteken')


if __name__ == '__main__':
    unittest.main()
