# Mardi Gras
# Compute the date of Easter
# Programming Praxis Exercise 10
# http://programmingpraxis.com/2009/02/24/mardi-gras/

from datetime import date, timedelta


def computus(year):
    """ Return the date of Easter for every year in the Gregorian Calendar.
    The original algorithm was submitted to Nature in 1877 by an anonymous.
    See: http://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm"""
    # years don't float!
    assert isinstance(year, int)
    # gregorian calendar only
    assert year > 1752
    # the actual computus
    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) / 25
    g = (b - f + 1) / 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) / 451
    n = h + L - 7 * m + 114
    month, day = divmod(n, 31)
    day += 1
    return date(year, month, day)


def paschal(year):
    """ Alternative implementation for computus(year).
    Calculate the date of paschal full moon in the gregorian calendar,
    then find the following sunday, which is easter.
    See: http://www.oremus.org/liturgy/etc/ktf/app/easter.html """
    assert isinstance(year, int)
    assert year > 1752
    # Golden number
    gn = year % 19 + 1
    # Solar correction
    sc = (year - 1600) / 100 - (year - 1600) / 400
    # Lunar correction
    lc = (year - 1400) / 100 * 8 / 25
     # Paschal full moon (num of days after vernal equinox)
    pfm = (3 - 11 * gn + sc - lc) % 30
    if pfm == 29 or (pfm == 28 and gn > 11):
        pfm -= 1
    # Paschal full moon (date)
    pfmd = date(year, 3, 21) + timedelta(days=pfm)
    # Easter is the first sunday after pfmd
    day, sunday = timedelta(days=1), 6
    easter = pfmd + day
    while not easter.weekday() == sunday:
        easter += day
    return easter


def mardi_gras(year):
    easter = computus(year)
    mardi = easter - timedelta(days=47)
    return mardi


def main(years):
    for year in years:
        easter = computus(year)
        mardi = mardi_gras(year)
        print "easter in", year, "falls on", easter
        print "mardi gras in", year, "falls on", mardi


if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        years = map(int, sys.argv[1:])
    else:
        years = [2009, 1989, 2049]
    main(years)
