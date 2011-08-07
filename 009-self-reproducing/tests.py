# A Self-Reproducing Program
# The quintessential quine
# Programming Praxis Exercise 9
# http://programmingpraxis.com/2009/02/20/a-self-reproducing-program/

import unittest
from subprocess import check_output


class QuineTestCase(unittest.TestCase):
    def test_programming_praxis(self):
        """ Program output must be identical to program source. """
        filename = 'self_reproducing.py'
        source = open(filename).read()
        output = check_output(["python", filename])
        self.assertEqual(source, output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
