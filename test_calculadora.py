import math
import unittest
from Calculadora import suma, resta, multiplicacion, division, exponenciacion, raiz_cuadrada, logaritmo


class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(6, 0), "Error: división por cero")

    def test_exponenciacion(self):
        self.assertEqual(exponenciacion(2, 3), 8)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(9), 3)

    def test_logaritmo(self):
        self.assertEqual(logaritmo(math.e), 1)
    
    def test_calcular_hipotenusa(self):
        self.assertEqual(calcular_hipotenusa(1,5),9)

if __name__ == "__main__":
    unittest.main()
