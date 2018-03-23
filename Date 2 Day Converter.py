""" DATE TO DAY CALCULATOR
Successful on 29 Feb 2012 - 1940 Hrs"""
        


def date2day(date):
    """This def converts date into flat day no. It adds leap year accordingly"""
    
    x = date.split('-')
    year = int(x[2])
    month = int(x[1])
    day = int(x[0])
    if year % 4 == 0:
        month_value = {0:0,
                       1:31,
                       2:31+29,
                       3:31+29+31,
                       4:31+29+31+30,
                       5:31+29+31+30+31,
                       6:31+29+31+30+31+30,
                       7:31+29+31+30+31+30+31,
                       8:31+29+31+30+31+30+31+31,
                       9:31+29+31+30+31+30+31+31+30,
                       10:31+29+31+30+31+30+31+31+30+31,
                       11:31+29+31+30+31+30+31+31+30+31+30,
                       12:31+29+31+30+31+30+31+31+30+31+30+31}
    else:
        month_value = {0:0,
                       1:31,
                       2:31+28,
                       3:31+28+31,
                       4:31+28+31+30,
                       5:31+28+31+30+31,
                       6:31+28+31+30+31+30,
                       7:31+28+31+30+31+30+31,
                       8:31+28+31+30+31+30+31+31,
                       9:31+28+31+30+31+30+31+31+30,
                       10:31+28+31+30+31+30+31+31+30+31,
                       11:31+28+31+30+31+30+31+31+30+31+30,
                       12:31+28+31+30+31+30+31+31+30+31+30+31}
       
    day_of_yr = day + month_value.get(month - 1)    #Get the value from dict
    return day_of_yr


def yr_value(date):
    """Each yr starting from 1980 has got a value"""
    x = date.split('-')
    year = int(x[2])
    yrs = []
    for i in range(1980, year + 1, 4):              #Here +1 is for counting the latest leapyear
        if i % 4 == 0:
            yrs.append(i)
    leap_yr = len(yrs)
    value_of_yr = leap_yr * 366 + (year - 1980 - leap_yr) * 365
    return value_of_yr


def day_of_wk(value_of_yr, day_of_yr):
    """ This function finds out the day out of year value"""
    day_value = value_of_yr + day_of_yr
    factor = day_value % 7
    if factor == 0:
        print('SUNDAY')
    elif factor == 1:
        print('MONDAY')
    elif factor == 2:
        print('TUESDAY')
    elif factor == 3:
        print('WEDNESDAY')
    elif factor == 4:
        print('THURSDAY')
    elif factor == 5:
        print('FRIDAY')
    elif factor == 6:
        print('SATURDAY')

def main():
    date = input('Enter Date: ')
    if date == 'exit':
        exit()
    elif date == 'help':
        print("""
Type 'exit' to quit.

This calculator can
show day of dates
later than 1979.
""")
    else:
        b = date2day(date)
        a = yr_value(date)
        day_of_wk(a, b)

print("""
=======================
DATE TO DAY CALCULATOR
Version: 0.1

Touhidur Rahman
http://about.me/tanimkg
=======================
Enter any Date in this
format << dd-mm-yyyy >>
It will show the Day.
Type 'help' to get help
=======================
""")

while True:
    main()


