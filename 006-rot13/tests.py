import unittest
from rot13 import rot13
from string import ascii_letters
from random import choice, randrange


lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


class Rot13TestCase(unittest.TestCase):

    def test_symmetric_encryption(self):
        "Applying rot13 two times to a string returns the original string"
        self.assertEqual(rot13(rot13(lorem)), lorem)

        for i in range(50):
            random_text = ""
            for l in range(randrange(1,101)):
                random_text += choice(ascii_letters)
            random_text = "".join(random_text)

            self.assertEqual(rot13(rot13(random_text)), random_text)

    def test_empty_string(self):
        "Rot13 of an empty string is an empty string"
        self.assertEqual(rot13(""), "")

    def test_programming_praxis(self):
        crypted = "Cebtenzzvat Cenkvf vf sha!"
        uncrypted = "Programming Praxis is fun!"
        self.assertEqual(rot13(crypted), uncrypted)



if __name__ == '__main__':
    unittest.main(verbosity=2)
