"""
Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
building a set of utility functions;
utilizing her/his own functions.
Scenario
Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

Use the previously written and tested functions. Add some test cases to the code. Our test is only a beginning.
"""
def IsYearLeap(year):
    # if the year number isn't divisible by four, it's a common year;
    if year % 4 != 0:
        return False
    # otherwise, if the year number isn't divisible by 100, it's a leap year;
    elif year % 100 != 0:
        return True
    # otherwise, if the year number isn't divisible by 400, it's a common year;
    elif year % 400:
        return False
    # otherwise, it's a leap year.
    else:
        return True


def DaysInMonth(year,month):
    months30 = [9, 4, 6, 11]
    months31 = [1, 3, 5, 7, 8, 10, 12]
    if month in months30:
        return 30
    if month in months31:
        return 31
    if month == 2 and IsYearLeap(year):
        return 29
    else :
        return 28


def DayOfYear(year,month,day):
    #
    # put your code here
    #
    ### I need to do this still LOL
    numDayOfTheYear = 10001
    return numDayOfTheYear


print(DayOfYear(2000,12,31))