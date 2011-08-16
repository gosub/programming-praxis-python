# Creation
# Cryptanalysis of a Vigenère cipher -- encoding: utf-8
# Programming Praxis Exercise 12
# http://programmingpraxis.com/2009/03/03/creation/

from collections import Counter
from itertools import izip_longest, cycle


def average(values):
    return sum(values, 0.0) / len(values)


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def read_cipher(filename):
    """ Read a list of numbers separated by spaces from filename
    and interpret them as ascii decimal values of a string,
    which is returned. """
    with open(filename) as f:
        int_list = [int(num) for num in f.read().split()]
        text = "".join(chr(c) for c in int_list)
        return text


def probable_password_lengths(encrypted, length_range=(3, 20)):
    """ Find the most probable password lengths of a xor cypher text
    (or a multiple) sorting by alphabet length for every letter in the
    password. For example, if the password is len 3, count how many
    different char are in the cipher text at position mod 1, mod 2 and
    mod 3, and average them. For the correct password length, this
    number is lower. This method works only if the length of the
    cipher text isn't too small or too large. """
    def alphabet_size(length):
        striped = zip(*grouper(length, encrypted))
        return average([len(set(c)) for c in striped])
    return sorted(range(*length_range), key=alphabet_size)


def guess_password(enc_txt, password_length, expected_common=' '):
    """ Guess the probable password of a xor cipher text, given it
    is of length password_length and the most common char in the
    unencrypted message is expected_common. """
    striped = zip(*grouper(password_length, enc_txt))
    counted = map(Counter, striped)
    most_commons = [c.most_common(1)[0][0] for c in counted]
    pwd = "".join(chr(ord(l) ^ ord(expected_common)) for l in most_commons)
    return pwd


# xor operations are symmetrical, so the same function
# can be used both for encryption and decryption.
def xor_crypt(text, passw):
    """ Return a string where every character of the text is xored
    against the corrisponding character in the password, repeated
    as necessary. Example:
    This is uncrypted text ^
    passwordpasswordpasswo =
    ----------------------
    $\t^Z^@W^F^AD^E^O^P^A^N^_^F^A^TA^G^V^O^[
    """
    txt = "".join(chr(ord(a) ^ ord(b)) for a, b in zip(text, cycle(passw)))
    return txt


def main(filename):
    """ Read filename as list of ascii decimals,
    Return guessed cipher password and relative
    decrypted text. """
    encrypted = read_cipher(filename)
    passw_lens = probable_password_lengths(encrypted)
    passw = guess_password(encrypted, passw_lens[0])
    return passw, xor_crypt(encrypted, passw)


if __name__ == '__main__':
    from sys import argv
    fn = argv[1] if len(argv) > 1 else "cipher_message.txt"
    password, decrypted = main(fn)
    print "Probable password: ", password
    print "Decrypted text:", decrypted
