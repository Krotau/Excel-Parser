import unittest
from Models.Klant import Klant


class TestKlant(unittest.TestCase):
    """
    Test the klant.. duh
    """

    def test_klant(self):
        self.assertEqual(Klant().__tablename__, 'klant')


if __name__ == '__main__':
    unittest.main()
