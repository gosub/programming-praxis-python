import unittest
from mardi_gras import mardi_gras, computus, paschal
from datetime import date


easters = [(1980, 04, 06), (1981, 04, 19), (1982, 04, 11), (1983, 04, 03),
           (1984, 04, 22), (1985, 04, 07), (1986, 03, 30), (1987, 04, 19),
           (1988, 04, 03), (1989, 03, 26), (1990, 04, 15), (1991, 03, 31),
           (1992, 04, 19), (1993, 04, 11), (1994, 04, 03), (1995, 04, 16),
           (1996, 04, 07), (1997, 03, 30), (1998, 04, 12), (1999, 04, 04),
           (2000, 04, 23)]


class MardiGrasTestCase(unittest.TestCase):
    def test_some_easter_dates(self):
        "Verify some known easter date"
        for year, month, day in easters:
            self.assertEqual(computus(year), date(year, month, day))

    def test_gregorian(self):
        "Year argument must be part of Gregorian Calendar"
        for year in [-1000, -1, 0, 1, 1000, 1752]:
            self.assertRaises(AssertionError, mardi_gras, year)
            self.assertRaises(AssertionError, computus, year)

    def test_year_type(self):
        "Year argument must be int"
        for year in [2009.0, "2009", [2009]]:
            self.assertRaises(AssertionError, mardi_gras, year)
            self.assertRaises(AssertionError, computus, year)

    def test_paschal_computus_equivalence(self):
        "Computus and Paschal moon must give same date for easter"
        for year in xrange(1753, 4999):
            self.assertEqual(paschal(year), computus(year))

    def test_programming_praxis(self):
        "Verify mardi gras dates for 2009, 1989 and 2049"
        self.assertEqual(mardi_gras(2009), date(2009, 2, 24))
        self.assertEqual(mardi_gras(1989), date(1989, 2, 7))
        self.assertEqual(mardi_gras(2049), date(2049, 3, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
