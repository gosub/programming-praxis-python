import unittest
from multiple_dwellings import dwellings_dict, names


class MultipleDwellingsTestCase(unittest.TestCase):

    def test_programming_praxis(self):
        # solution is a dict in the form {Dweller: floor}
        solution = dwellings_dict()

        # solution containts every dweller
        self.assertSetEqual(set(solution.keys()), set(names))

        # each dweller is assigned to a different floor
        self.assertSetEqual(set(solution.values()), set(range(1, len(names) + 1)))

        # Baker does not live on the top floor
        self.assertNotEqual(solution['Baker'], 5)
        # Cooper does not live on the bottom floor
        self.assertNotEqual(solution['Cooper'], 1)
        # Fletcher does not live on either the top or the bottom floor
        self.assertNotIn(solution['Fletcher'], [1, 5])
        # Miller lives on a higher floor than does Cooper
        self.assertGreater(solution['Miller'], solution['Cooper'])
        # Smith does not live on a floor adjacent to Fletcher's
        smith_fletcher_distance = abs(solution['Smith'] - solution['Fletcher'])
        self.assertGreater(smith_fletcher_distance, 1)
        # Fletcher does not live on a floor adjacent to Cooper's
        fletcher_cooper_distance = abs(solution['Fletcher'] - solution['Cooper'])
        self.assertGreater(fletcher_cooper_distance, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
