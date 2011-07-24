# Flavius Josephus
# Programming a cyclical list 
# Programming Praxis Exercise 5
# http://programmingpraxis.com/2009/02/19/flavius-josephus/

from itertools import cycle, islice, ifilterfalse


def iterator_josephus(n, m):
    # make an infinitely repeating list
    cyc = cycle(range(n))
    accumulator = []
    while len(accumulator) < n:
        # drop the first m-1 elements
        cyc = islice(cyc, m-1, None)
        # pick the m-th
        element = cyc.next()
        # save it away
        accumulator.append(element)
        # generate a function that identifies the number
        # we picked (using default argument v as a closure)
        elemental_sieve = lambda x, v = element: x == v
        # filter the number from the list, using the function
        cyc = ifilterfalse(elemental_sieve, cyc)
    return accumulator


def imperative_josephus(n, m):
    assert n > 0
    assert m > 0
    initial = range(n)
    accumulator = []
    index = 0
    while initial:
        # move the index m elements ahead
        index += m - 1
        # wrap the index around if not inside the list
        index %= len(initial)
        # extract and accumate the number at index position
        accumulator.append(initial.pop(index))
    return accumulator


def josephus(n, m):
    """ Return the list of numbers from 0 to n-1,
    with the followin ordering:
        - Pick every m-th element, not counting 
          those already picked
        - If the end of the list is reached, 
          continue counting from the start
    """
    return imperative_josephus(n, m)


if __name__ == "__main__":
    print "With 40 other soldiers, killing every 3rd man, the safe position is:",
    print josephus(41,3)[-1], "(counting from 0)"
