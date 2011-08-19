# Roman Numerals
# A library to read and write Roman numerals
# Programming Praxis Exercise 13
# http://programmingpraxis.com/2009/03/06/roman-numerals/

from collections import OrderedDict
from operator import itemgetter as ig


_romans = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90,
               L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)


# ordered dict from numerals to decimals {'M': 1000}
roman_numerals = OrderedDict(sorted(_romans.items(), key=ig(1), reverse=True))
# ordered dict from decimals to numerals {1000: 'M'}
roman_decimals = OrderedDict((d, n) for n, d in roman_numerals.items())


def roman_to_int(roman):
    "Convert a roman numeral to decimal."
    number = 0
    while roman:
        prefixes = [p for p in roman_numerals if roman.startswith(p)]
        if prefixes:
            number += roman_numerals[prefixes[0]]
            roman = roman[len(prefixes[0]):]
        else:
            raise Exception("Invalid roman numeral")
    return number


def int_to_roman(num):
    "Convert a decimal to roman numeral."
    roman = ""
    while num > 0:
        addenda = [a for a in roman_decimals if a <= num]
        if addenda:
            roman += roman_decimals[addenda[0]]
            num -= addenda[0]
        else:
            raise Exception("Failed int_to_roman conversion")
    return roman


def add_roman(roman1, roman2):
    "Return the sum of two roman numerals as a roman numeral."
    num1 = roman_to_int(roman1)
    num2 = roman_to_int(roman2)
    return int_to_roman(num1 + num2)


if __name__ == '__main__':
    """ If the argument passed is an integer,
    print its Roman Numeral, otherwise assume
    it'a a Roman Numeral and print its integer
    value. """
    from sys import argv
    argument = argv[1] if len(argv) > 1 else ''
    try:
        print int_to_roman(int(argument))
    except ValueError:
        print roman_to_int(argument)
