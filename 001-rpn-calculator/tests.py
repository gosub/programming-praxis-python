import unittest
from rpn_calculator import rpn_calc_eval


class RpnCalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = []

    def test_empty_string(self):
        expr = ""
        self.assertEqual(rpn_calc_eval(expr, self.stack), self.stack)

    def test_gibberish(self):
        expr = "sdofcsdovnsi sdonsdofsdfoin sdonc cc"
        self.assertEqual(rpn_calc_eval(expr, self.stack), self.stack)

    def test_programming_praxis(self):
        expr = "19 2.14 + 4.5 2 4.3 / - *"
        expected = (19 + 2.14) * (4.5 - 2 / 4.3)
        result = rpn_calc_eval(expr, self.stack)
        self.assertEqual(result[-1], expected)


if __name__ == '__main__':
    unittest.main()
