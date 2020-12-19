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


testdata = [1900, 2000, 2016, 1987]
testresults = [False, True, True, False]
for i in range(len(testdata)):
	yr = testdata[i]
	print(yr,"->",end="")
	result = IsYearLeap(yr)
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")