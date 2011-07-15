import unittest
from bingo import BingoCard, Simulation
from random import choice, randrange

# bingo card numbers are generated at random
# so we need to repeat the tests some times
repetitions = 50


class BingoCardTestCase(unittest.TestCase):

    def test_size(self):
        for i in xrange(repetitions):
            c = BingoCard()
            column_count = len(c.card)
            # every card has 5 columns
            self.assertEqual(column_count, 5)
            for column in c.card:
                column_size = len(column)
                # every column has 5 elements (one per row)
                self.assertEqual(column_size, 5)

    def test_content(self):
        column_ranges = {0: range(1,16), 1: range(16,31),
                         2: range(31,46), 3: range(46,61),
                         4: range(61,76)}
        for i in xrange(repetitions):
            c = BingoCard()
            for column in xrange(5):
                for row in xrange(5):
                    value = c.card[column][row]
                    if row == 2 and column == 2:
                        # center position is free
                        self.assertFalse(value)
                    else:
                        # numbers distribution on card follows bingo rules
                        self.assertIn(value, column_ranges[column])

    def test_crossing_out(self):
        for i in xrange(repetitions):
            c = BingoCard()
            extraction = randrange(1,76)
            c.cross_out(extraction)
            for column in c.card:
                # when a number is crossed out
                # is not on the card anymore
                self.assertNotIn(extraction, column)

    def test_start_end_game(self):
        for i in xrange(repetitions):
            c = BingoCard()
            # a new card can't be a winner
            self.assertFalse(c.has_won())

            for extraction in xrange(76):
                c.cross_out(extraction)
            # after the extraction of every number
            # a card must be a winner
            self.assertTrue(c.has_won())

    def test_winning_by_column(self):
        for i in xrange(repetitions):
            c = BingoCard()
            winning_column = choice(c.card)
            for num in winning_column:
                c.cross_out(num)
            # when every number on a column is crossed out
            # the card is a winner
            self.assertTrue(c.has_won())

    def test_winning_by_row(self):
        for i in xrange(repetitions):
            c = BingoCard()
            random_row = randrange(5)
            winning_row = [column[random_row] for column in c.card]
            for num in winning_row:
                c.cross_out(num)
            # when every number on a row is crossed out
            # the card is a winner
            self.assertTrue(c.has_won())
    
    def test_winning_by_diagonals(self):
        for i in xrange(repetitions):
            c = BingoCard()
            backwards = choice([True, False])
            if backwards:
                winning_diagonal = [c.card[4-n][n] for n in xrange(5)]
            else:
                winning_diagonal = [c.card[n][n] for n in xrange(5)]
            for num in winning_diagonal:
                c.cross_out(num)
            # when every number on a diagonal is crossed out
            # the card is a winner
            self.assertTrue(c.has_won())



class SimulationTestCase(unittest.TestCase):
    def test_programming_praxis(self):
        # a game of bingo with one card ends, on average,
        # after 41.5 turns
        one_card_average = Simulation(1, 1000)
        self.assertTrue(40.5 < one_card_average < 42.5)

        # a game of bingo with 500 card ends, on average,
        # after 12 turns
        fivehundred_card_average = Simulation(500, 100)
        self.assertTrue(11 < fivehundred_card_average < 13)


if __name__ == '__main__':
    unittest.main(verbosity=2)
