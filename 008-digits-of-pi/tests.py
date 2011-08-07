import unittest
from digits_of_pi import nth_digit_of_pi, digits_of_pi


hundred_decimals = [3, 
1, 4, 1, 5, 9, 2, 6, 5, 3, 5,
8, 9, 7, 9, 3, 2, 3, 8, 4, 6,
2, 6, 4, 3, 3, 8, 3, 2, 7, 9,
5, 0, 2, 8, 8, 4, 1, 9, 7, 1,
6, 9, 3, 9, 9, 3, 7, 5, 1, 0,
5, 8, 2, 0, 9, 7, 4, 9, 4, 4,
5, 9, 2, 3, 0, 7, 8, 1, 6, 4,
0, 6, 2, 8, 6, 2, 0, 8, 9, 9,
8, 6, 2, 8, 0, 3, 4, 8, 2, 5,
3, 4, 2, 1, 1, 7, 0, 6, 7, 9]


class DigitsOfPiTestCase(unittest.TestCase):

    def test_a_hundred_decimals(self):
        "Verifiy the first one hundred and one digits of pi."
        self.assertEqual(digits_of_pi(101), hundred_decimals)
    
    def test_programming_praxis(self):
        "The one-thousandth decimal of pi is 9."
        self.assertEqual(nth_digit_of_pi(1000), 9)



if __name__ == '__main__':
    unittest.main(verbosity=2)
