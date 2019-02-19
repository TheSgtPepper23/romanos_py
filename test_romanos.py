import unittest
from Romanos import Romanos


class TestRomanos(unittest.TestCase):

    def test_descomponer_numero(self):
        romano = Romanos()
        self.assertIsNotNone(romano.descomponer_numero(200))
        self.assertIsInstance(romano.descomponer_numero(3987), list)
        self.assertEqual(romano.descomponer_numero(25), [2, 5])
        self.assertEqual(romano.descomponer_numero(3623), [3, 6, 2, 3])
        self.assertIsNone(romano.descomponer_numero(4000))
        self.assertIsNone(romano.descomponer_numero(0))
        self.assertIsNone(romano.descomponer_numero("Perro"))
        self.assertIsNone(romano.descomponer_numero([23, 23]))


    def test_transformar_numero(self):
        romano = Romanos()
        self.assertIsNotNone(romano.transformar_numero([1,2,3,4]))
        self.assertIsInstance(romano.transformar_numero([2,3,5,7]), str)
        self.assertEqual(romano.transformar_numero([2]), "II")
        self.assertEqual(romano.transformar_numero([2,5,7,9]), "MMDLXXIX")
        self.assertIsNone(romano.transformar_numero(None))

if __name__ == "__main__":
    unittest.main()