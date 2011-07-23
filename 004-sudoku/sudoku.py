# Sudoku
# A backtracking solution to everybody's favorite puzzle
# Programming Praxis Exercise 4
# http://programmingpraxis.com/2009/02/19/sudoku/

from copy import deepcopy
from itertools import product


# A cell is a tuple of (row, column) coordinates
# cells and peers are calculated just once, and stored
# in two global variables

def calculate_peers(cells):
    """ Precalculate dictionary of peers for every cell """
    peers = {}
    subgrid = lambda coord: xrange(coord/3*3, coord/3*3 + 3)
    for row, column in cells:
        # vertical peers
        peer = [(row, c) for c in xrange(9)]
        # horizontal peers
        peer += [(r, column) for r in xrange(9)]
        # subgrid peers
        peer += [(r,c) for r in subgrid(row) for c in subgrid(column)]
        # make a set of all the peers, excluding the cell itself
        peers[(row, column)] = set(peer) - set([(row, column)])
    return peers

_cells = [(r, c) for r in xrange(9) for c in xrange(9)]
_peers = calculate_peers(_cells)



# The Depth First Search Algorithm

def dfs(starting_puzzle):
    """ Perform a Depth First Search in the graph of the possible
    branches from the initial puzzle, starting with the cells
    with less alternatives. Return a solved puzzle, or None if
    no solution is found. """
    search_stack = [starting_puzzle]
    while search_stack:
        puzzle = search_stack.pop()
        if puzzle.propagate_constraint():
            if puzzle.is_solved():
                return puzzle
            cell = min(puzzle.unset_cells(), key = puzzle.branches)
            for alternative in puzzle.content(cell):
                child = puzzle.copy()
                child.set(cell, alternative)
                search_stack.append(child)
    return None



# The class representing a Sudoku Puzzle

class SudokuPuzzle:
    """ The grid of a Sudoku puzzle is a two-dimensional array.
    Every cell contains an int if the value of the cell is fixed,
    otherwise an array of remaining alternatives for that cell. """

    # An exception used to shortcut unsolvable puzzle
    class DeadEnd(Exception):
        pass

    def __init__(self, puzzle = None):
        """ Fill the grid of the new Sudoku puzzle, parsing 
        the string passed or generating an empty puzzle """
        if puzzle:
            self.grid = self.parse(puzzle)
        else:
            self.grid = self.parse(generate_empty_puzzle())


    def parse(self, puzzle):
        puzzle = puzzle.replace("\n", "")
        if len(puzzle) == 81:
            return [map(char_to_cell_value, subseq) \
                    for subseq in split_every(puzzle, 9)]
        else:
            raise Exception("Wrong size! a puzzle must be 81 (9x9) long!")


    def show(self):
        """ Prints an ASCII drawing of the sudoku grid.
        If a cell is not sure, a dot is printed instead. """
        for row in xrange(9):
            r = map(cell_value_to_char, self.grid[row])
            print " {0} {1} {2} | {3} {4} {5} | {6} {7} {8} ".format(*r)
            if row in (2,5):
                print "+".join(["-" * 7]*3)


    def as_line(self):
        """ Return the grid as a string parsable by another SudokuPuzzle. """
        line = "".join(cell_value_to_char(self.content(cell)) \
                           for cell in _cells)
        return line


    def is_solved(self):
        """ Tell if the puzzle is solved. """
        return all(self.is_set(cell) for cell in _cells)


    def is_solved_correctly(self):
        """ Tell if a solved puzzle also has a correct solution. """
        assert self.is_solved()
        digits = set(range(1,10))
        valid_rows = all(set(row) == digits for row in self.grid)
        valid_cols = all(set(col) == digits for col in zip(*self.grid))
        subgrids =  [list(product(range(r,r+3), range(c,c+3))) \
                         for r,c in product(range(0,7,3), repeat=2)]
        subgrids_vals = [map(self.content, subgrid) for subgrid in subgrids]
        valid_subgrids = all(set(subgrid) == digits for subgrid in subgrids_vals)
        return valid_rows and valid_cols and valid_subgrids
            

    def solve(self):
        """ Solve this puzzle in place. 
        Return False if no solution is found. """
        self.propagate_constraint()
        if not self.is_solved():
            # if Constraint Propagation is not enough
            # use Depth First Search
            solution = dfs(self)
            if not solution:
                return False
            # dfs returns a different puzzle object
            # so we must get the solution into self
            self.grid = solution.grid
        return self


    def propagate_constraint(self):
        """ Apply repeteadly the propagate constraint step,
        until no further narrowing can be done.
        Return True if the grid is consistent,
        False if a contradiction emerges. """
        try:
            while not self.is_solved():
                if not self.prop_constraint_step():
                    break
            return True
        except SudokuPuzzle.DeadEnd:
            return False


    def prop_constraint_step(self):
        """ For every certain cell, remove its value from its uncertain
        peers. Return True if at least one cell's possible values
        were narrowed down. """
        changed = False
        for cell in self.set_cells():
            for peer in _peers[cell]:
                val = self.content(cell)
                peer_val = self.content(peer)

                if not self.is_set(peer):
                    changed = self.exclude(peer, val)
                    if not self.content(peer):
                        # Bad news! A cell has no alternatives left!
                        raise SudokuPuzzle.DeadEnd

                elif val == peer_val:
                    # A cell has the same value of one of its peers! No-no!
                    raise SudokuPuzzle.DeadEnd
        return changed


    def content(self, cell):
        """ Return the content of a cell. """
        r, c = cell
        return self.grid[r][c]


    def is_set(self, cell):
        """ Tell if a cell contains a definitive value. """
        return isinstance(self.content(cell), int)


    def branches(self, cell):
        """ Return the number of possible values this cell can have. """
        return len(self.content(cell))


    def unset_cells(self):
        """ Return the sequence of uncertain cells. """
        return (cell for cell in _cells if not self.is_set(cell))


    def set_cells(self):
        """ Return the sequence of certain cells. """
        return (cell for cell in _cells if self.is_set(cell))


    def set(self, cell, val):
        """ Fixate a cell with a particular value. """
        r,c = cell
        self.grid[r][c] = val


    def exclude(self, cell, val):
        """ Remove a possible value from the set in a cell.
        If only one value remains in the list of possibilities
        fixate that one value to the cell.
        Return True if the value was effectively removed. """
        if not self.is_set(cell) and val in self.content(cell):
            r,c = cell
            self.grid[r][c].remove(val)
            new_content = self.content(cell)
            if len(new_content) == 1:
                self.set(cell, new_content[0])
            return True
        else:
            return False


    def copy(self):
        """ Make a copy ot this object, duplicating its grid. """
        s = SudokuPuzzle()
        s.grid = deepcopy(self.grid)
        return s




# Some auxiliary functions
def split_every(seq, n):
    """ Split a sequence in a sequence of sequences of lenght n. """
    return [seq[i:i+n] for i in range(0, len(seq), n)]

def char_to_cell_value(ch):
    if ch in "123456789":
        return int(ch)
    else:
        # if zero or not a digit,
        # return a list of possible values
        return range(1, 10)

def cell_value_to_char(val):
    if val in range(1,10):
        return str(val)
    else:
        return "."    

def generate_empty_puzzle():
    return "0" * 81



# Some puzzles
programming_praxis = """
7..1.....
.2.....15
.....639.
2...18...
.4..9..7.
...75...3
.785.....
56.....4.
.....1..2"""

simple_norvig = """
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300"""

hard_norvig = """
4.....8.5
.3.......
...7.....
.2.....6.
....8.4..
....1....
...6.3.7.
5..2.....
1.4......"""


def main(commandline_puzzle = None):
    def show_off(puzzle):
        p = SudokuPuzzle(puzzle)
        print "Solving: "
        p.show()
        if p.solve():
            print "Solution: "
            p.show()
        else:
            print "Sorry, no solution was found!"        
        print

    if commandline_puzzle:
        # if a puzzle is provided from command line, try to solve it
        show_off(commandline_puzzle)
    else:
        print "Solving some predefined Sudoku puzzles..."
        for predefined in [programming_praxis, simple_norvig, hard_norvig]:
            show_off(predefined)



if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
