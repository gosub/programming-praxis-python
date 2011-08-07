# Multiple Dwellings
# A simple logic puzzle
# Programming Praxis Exercise 7
# http://programmingpraxis.com/2009/02/20/multiple-dwellings/

from itertools import permutations, ifilter, ifilterfalse


names = 'Baker', 'Cooper', 'Fletcher', 'Miller', 'Smith'

def dwellings():
    B,C,F,M,S = names
    dwellers = permutations(names)

    # Baker does not live on the top floor
    dwellers = ifilterfalse(lambda d: d[4] == B, dwellers)
    # Cooper does not live on the bottom floor
    dwellers = ifilterfalse(lambda d: d[0] == C, dwellers)
    # Fletcher does not live on either the top or the bottom floor
    dwellers = ifilterfalse(lambda d: d[0] == F or d[4] == F, dwellers)
    # Miller lives on a higher floor than does Cooper
    dwellers = ifilter(lambda d: d.index(M) > d.index(C), dwellers)
    # Smith does not live on a floor adjacent to Fletcher's
    dwellers = ifilterfalse(lambda d: abs(d.index(S) - d.index(F)) == 1, dwellers)
    # Fletcher does not live on a floor adjacent to Cooper's
    dwellers = ifilterfalse(lambda d: abs(d.index(F) - d.index(C)) == 1, dwellers)

    solution = dwellers.next()
    return solution


def dwellings_dict():
    solution = dwellings()
    return {name: floor for floor, name in enumerate(solution, start=1)}


if __name__ == '__main__':
    solution = dwellings()
    pretty = list(enumerate(solution, start=1))
    pretty.reverse()
    for floor, name in pretty:
        print floor, name
