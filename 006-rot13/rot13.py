# ROT13
# A simple Caesar-shift cipher
# Programming Praxis Exercise 6
# http://programmingpraxis.com/2009/02/20/rot13/

from string import ascii_letters, ascii_lowercase, \
    ascii_uppercase, maketrans, translate

def make_rot_cypher(shift = 13):
    """ Return a function that takes a string and
    returns it crypted by a caesar shift cipher """
    # the shift value is used to slice the alphabet so
    # it must be less than 26. It's taken modulo 26
    # since rot26 wraps around to rot0, rot27 to rot1, and so on...
    shift %= 26
    rot_lowercase = ascii_lowercase[shift:] + ascii_lowercase[:shift]
    rot_uppercase = ascii_uppercase[shift:] + ascii_uppercase[:shift]
    transl_table = maketrans(ascii_letters, rot_lowercase + rot_uppercase)
    return lambda text, _table = transl_table: translate(text, _table)

rot13 = make_rot_cypher(13)

if __name__ == '__main__':
    s = "Cebtenzzvat Cenkvf vf sha!"
    print s
    print rot13(s)
