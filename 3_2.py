"""
Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
utilizing her/his own functions.
Scenario
Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (yes, we know that only February is sensitive to the year value, but we want our function to be universal). The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

Of course, you can (to be honest: you should!) use the previously written and tested function. It may be very helpful (we cannot say anything more, sorry). We encourage you to use a list filled with the months' lengths. You can create it inside the function - this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases.
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

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"->",end="")
	result = DaysInMonth(yr,mo)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")