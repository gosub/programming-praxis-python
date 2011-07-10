import unittest
from sieve_of_eratosthenes import sieve_of_eratosthenes as sieve


class SieveOfEratosthenesTestCase(unittest.TestCase):

    def test_corner_cases(self):
        self.assertEqual(sieve(-1), [])
        self.assertEqual(sieve(0), [])
        self.assertEqual(sieve(1), [])
        self.assertEqual(sieve(2), [2])

    def test_some_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                  31, 37, 41, 43, 47, 53, 59, 61, 67,
                  71, 73, 79, 83, 89, 97]
        self.assertEqual(sieve(100), primes)

    def test_programming_praxis(self):
        magic_number = 15485863
        self.assertEqual(len(sieve(magic_number)), 1000000)


if __name__ == '__main__':
    unittest.main()
