# Sieve of Eratosthenes
# An acient algorithm to enumerate prime numbers
# Programming Praxis Exercise 2
# http://programmingpraxis.com/2009/02/19/sieve-of-eratosthenes/

from math import sqrt


def fast_sieve(n):
    """ Find all the primes up to n """
    # generate every odd number from 3 to n
    numbers = range(3, n + 1, 2)
    max_idx = (n - 1) / 2
    # start sifting at index 0
    idx = 0
    # sifting must stop at sqrt(n)
    limit = int(sqrt(n))
    limit_idx = limit/2 - 1
    while idx <= limit_idx:
        num = numbers[idx]
        # given a number n at index i
        # its square is at n*(i+1)+i
        num_sqr_idx = num * (idx + 1) + idx
        # multiples of number n at index i
        # are at index i + kn
        for i in xrange(num_sqr_idx, max_idx, num):
            numbers[i] = False
        # increase index till next not-false value
        while idx <= limit_idx:
            idx += 1
            if numbers[idx]:
                break
    # remove 'falses' from list
    primes = []
    for x in numbers:
        if x:
            primes.append(x)
    # must prepend 2, the only even prime number
    return [2] + primes


def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    else:
        try:
            return fast_sieve(int(n))
        except ValueError:
            return []


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        upto = sys.argv[1]
    else:
        upto = 10

    for prime in sieve_of_eratosthenes(upto):
        print prime
    
