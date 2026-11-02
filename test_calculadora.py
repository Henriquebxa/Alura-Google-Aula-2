"""
Testes automatizados para o script calculadora.py
Garante que todas as 5 operações funcionem perfeitamente.
"""

import unittest
from calculadora import somar, subtrair, multiplicar, dividir, porcentagem


class TestCalculadora(unittest.TestCase):

    # 1. Testes de Adição
    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-2, 5), 3)
        self.assertEqual(somar(2.5, 3.5), 6.0)

    # 2. Testes de Subtração
    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(3.5, 1.5), 2.0)

    # 3. Testes de Multiplicação
    def test_multiplicar(self):
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(4, 0), 0)
        self.assertEqual(multiplicar(-3, 3), -9)
        self.assertEqual(multiplicar(2.5, 4), 10.0)

    # 4. Testes de Divisão
    def test_dividir(self):
        self.assertEqual(dividir(20, 4), 5.0)
        self.assertEqual(dividir(9, 2), 4.5)
        self.assertEqual(dividir(-10, 2), -5.0)

    def test_divisao_por_zero(self):
        self.assertEqual(dividir(10, 0), "Erro: Não é possível dividir por zero!")

    # 5. Testes da Nova Operação: Porcentagem
    def test_porcentagem(self):
        # 20% de 200 = 40.0
        self.assertEqual(porcentagem(20, 200), 40.0)
        # 50% de 80 = 40.0
        self.assertEqual(porcentagem(50, 80), 40.0)
        # 10% de 50 = 5.0
        self.assertEqual(porcentagem(10, 50), 5.0)
        # 100% de 120 = 120.0
        self.assertEqual(porcentagem(100, 120), 120.0)
        # 0% de 500 = 0.0
        self.assertEqual(porcentagem(0, 500), 0.0)


if __name__ == "__main__":
    unittest.main()
