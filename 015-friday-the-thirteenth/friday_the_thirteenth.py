# Friday, the Thirteenth
# A small calendar library, and a simple use of it
# Programming Praxis Exercise 15
# http://programmingpraxis.com/2009/03/13/friday-the-thirteenth/

import datetime

# Since there is no datetime.FRIDAY and there is no need
# to 'import calendar' just for calendar.FRIDAY
FRIDAY = 4


def day_weekday_occurrences(day, weekday, initial_date, final_date):
    """Return every 'weekday, the dayth' from initial_date to final_date."""
    starting_year = initial_date.year
    ending_year = final_date.year
    occurrences = []
    for year in range(starting_year, ending_year):
        for month in range(1, 13):
            date = datetime.date(year, month, day)
            if date.weekday() == weekday:
                if initial_date <= date <= final_date:
                    occurrences.append(date)
    return occurrences


def main():
    # start from 2009-03-14
    initial_date = datetime.date(2009, 3, 14)
    # until 2019-03-13
    ending_date = datetime.date(2019, 3, 13)
    # list the 'friday, 13th'
    fridays13 = day_weekday_occurrences(day=13,
                                        weekday=FRIDAY,
                                        initial_date=initial_date,
                                        final_date=ending_date)
    # print them all as "year month"
    for f in fridays13:
        print f.year, f.month
    # print their count
    print "From", initial_date.isoformat(), "to", ending_date.isoformat(), \
          "there are", len(fridays13), "'Friday, 13th'"


if __name__ == "__main__":
    main()
