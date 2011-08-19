# Class wrapper for Roman Numeral conversion

from roman_numerals import int_to_roman, roman_to_int


class Roman(object):
    def __init__(self, value=0):
        if isinstance(value, str):
            self.roman = value
            self.value = roman_to_int(value)
        else:
            self.value = int(value)
            self.roman = int_to_roman(self.value)

    def __int__(self):
        return self.value

    def __str__(self):
        return self.roman

    def __repr__(self):
        return "<Roman object %s (%d)>" % (self.roman, self.value)

    def __add__(self, other):
        return Roman(self.value + other)

    def __radd__(self, other):
        return Roman(other + self.value)

    def __sub__(self, other):
        return Roman(self.value - other)

    def __rsub__(self, other):
        return Roman(other - self.value)

    def __mul__(self, other):
        return Roman(self.value * other)

    def __rmul__(self, other):
        return Roman(other * self.value)

    def __div__(self, other):
        return Roman(self.value / other)

    def __rdiv__(self, other):
        return Roman(other / self.value)

    def __cmp__(self, other):
        return self.value - other
