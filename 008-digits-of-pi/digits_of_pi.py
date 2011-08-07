# The Digits of Pi
# A spigot algorithm to calculate the digits of pi
# Programming Praxis Exercise 8
# http://programmingpraxis.com/2009/02/20/the-digits-of-pi/

from itertools import islice


def pi_spigot():
    """ Generator version of the recursive algorithm from the
    paper 'Unbounded Spigot Algorithms for the Digits of Pi'
    by Jeremy Gibbons. """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q1 = q * 10
            r1 = 10 * (r - n * t)
            n1 = (10 * (3*q+r)) / t - 10*n
            t1, k1, l1 = t, k, l
        else:
            q1 = q * k
            r1 = (2 * q + r) * l
            t1 = t * l
            k1 = k + 1
            n1 = (q * (7 * k + 2) + r * l) / (t * l)
            l1 = l + 2
        q,r,t,k,n,l = q1,r1,t1,k1,n1,l1


def digits_of_pi(n):
    "Return a list of the first n digits of pi."
    assert n > 0
    return list(islice(pi_spigot(), n))
    

def nth_digit_of_pi(n):
    "Return the nth digit of pi."
    assert n >= 0
    digits = pi_spigot()
    for i in xrange(n+1):
        digit = digits.next()
    return digit


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    print "The digit of pi at position", n, "is:", nth_digit_of_pi(n)


