import unittest
from roman_numerals import add_roman, roman_to_int, int_to_roman

nums = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI",
        "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
        "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII",
        "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI",
        "XXXVII", "XXXVIII", "XXXIX", "XL", "XLI", "XLII", "XLIII", "XLIV",
        "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L", "LI", "LII", "LIII",
        "LIV", "LV", "LVI", "LVII", "LVIII", "LIX", "LX", "LXI", "LXII",
        "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX",
        "LXXI", "LXXII", "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII",
        "LXXVIII", "LXXIX", "LXXX", "LXXXI", "LXXXII", "LXXXIII", "LXXXIV",
        "LXXXV", "LXXXVI", "LXXXVII", "LXXXVIII", "LXXXIX", "XC", "XCI",
        "XCII", "XCIII", "XCIV", "XCV", "XCVI", "XCVII", "XCVIII", "XCIX", "C"]


class RomanNumeralsTestCase(unittest.TestCase):

    def test_back_and_forth(self):
        """ Verify that an integer stay the same  after the
        coversion to roman numeral and back to integer. """
        for i in range(1, 5001):
            roman = int_to_roman(i)
            decimal = roman_to_int(roman)
            self.assertEqual(i, decimal)

    def test_known_numerals(self):
        """ Verify the conversion of a
        list of known roman numerals. """
        for i, numeral in enumerate(nums, 1):
            self.assertEqual(roman_to_int(numeral), i)
            self.assertEqual(int_to_roman(i), numeral)

    def test_programming_praxis(self):
        "Test the programming praxis roman sum."
        res = add_roman("CCCLXIX", "CDXLVIII")
        self.assertEqual(res, "DCCCXVII")


if __name__ == '__main__':
    unittest.main(verbosity=2)
