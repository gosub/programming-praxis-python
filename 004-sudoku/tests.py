import unittest
from sudoku import SudokuPuzzle, simple_norvig, hard_norvig, programming_praxis

praxis_solution = """
789135624
623947815
451286397
237418569
845693271
916752483
178524936
562379148
394861752"""

simple_norvig_solution = """
483921657
967345821
251876493
548132976
729564138
136798245
372689514
814253769
695417382
"""

hard_norvig_solution = """
417369825
632158947
958724316
825437169
791586432
346912758
289643571
573291684
164875293
"""

class SudokuPuzzleTestCase(unittest.TestCase):

    def test_parser(self):
        """ Parser must accept only puzzles of the proper length """
        self.assertRaises(Exception, SudokuPuzzle, [""])
        self.assertRaises(Exception, SudokuPuzzle, ["0" * 80])
        self.assertRaises(Exception, SudokuPuzzle, ["0" * 82])

    def test_empty_sudoku(self):
        """ An empty puzzle must be solvable """
        self.puzzle_tester("0" * 81)

    def test_unsolvable_sudoku(self):
        """ An impossible sudoku must not be solvable """
        p = SudokuPuzzle("1" * 80 + "0")
        self.assertFalse(p.solve())

    def test_norvig(self):
        """ Two puzzles from norvig solver """
        self.puzzle_tester(simple_norvig, simple_norvig_solution)
        self.puzzle_tester(hard_norvig, hard_norvig_solution)

    def test_programming_praxis(self):
        """ Puzzle from Programming Praxis """
        self.puzzle_tester(programming_praxis, praxis_solution)

    def puzzle_tester(self, puzzle, solution = None):
        """ Verify solvability of a sudoku puzzle and 
        correctness of the solution. If a solution is 
        provided, they are compared. """
        p = SudokuPuzzle(puzzle)
        self.assertTrue(p.solve())
        self.assertTrue(p.is_solved_correctly())
        if solution:
            self.assertEqual(p.as_line(), solution.replace("\n", ""))


if __name__ == '__main__':
    unittest.main(verbosity=2)
