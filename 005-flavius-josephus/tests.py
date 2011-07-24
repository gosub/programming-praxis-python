import unittest
from flavius_josephus import josephus, \
    iterator_josephus, imperative_josephus
    

class JosephusTestCase(unittest.TestCase):

    def test_iterator_version(self):
        """ Iterator version must give same results
        of imperative version. """
        from random import randrange
        for i in xrange(50):
            n = randrange(1,100)
            m = randrange(1, 20)
            a = iterator_josephus(n, m)
            b = imperative_josephus(n, m)
            self.assertEqual(a, b)

    def test_meaningful_values(self):
        """ Must raise an assertion error with zero
        or negative parameters. """
        self.assertRaises(AssertionError, josephus, 0, 9)
        self.assertRaises(AssertionError, josephus, 9, 0)
        self.assertRaises(AssertionError, josephus, -1, 9)
        self.assertRaises(AssertionError, josephus, 9, -1)

    def test_known_sequence(self):
        """ Test the generated seq with a known one. """
        sequence = josephus(41, 3)
        known = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29,  \
                     32, 35, 38, 0, 4, 9, 13, 18, 22,  \
                     27, 31, 36, 40, 6, 12, 19, 25, 33,\
                     39, 7, 16, 28, 37, 10, 24, 1, 21, \
                     3, 34, 15, 30]
        self.assertEqual(sequence, known)

    def test_programming_praxis(self):
        """ Find the safe position for Flavius Josephus
        to put himself. """
        sequence = josephus(41, 3)
        self.assertEqual(sequence[-1], 30)



if __name__ == '__main__':
    unittest.main(verbosity=2)
