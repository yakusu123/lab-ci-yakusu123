import unittest

from app import saludar


class TestSaludar(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludar("UCN"), "Hola UCN")


if __name__ == "__main__":
    unittest.main()
