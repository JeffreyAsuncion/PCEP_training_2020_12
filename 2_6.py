"""
Estimated time
10-15 minutes

Level of difficulty
Easy/Medium

Objectives
Familiarize the student with:

using the if-elif-else statement;
finding the proper implementation of verbally defined rules;
testing code using sample input and output.
Scenario
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code below - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described. The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise.

Test your code using the data we've provided.

Example input
2000

Example output
Leap year

Example input
2015

Example output
Common year

Example input
1999

Example output
Common year

Example input
1996

Example output
Leap year

Example input
1900

Example output
Common year
"""

year = int(input("Enter a year: "))
#
# put your code here
#
# if the year number isn't divisible by four, it's a common year;
if year % 4 != 0:
    print("Common Year")
# otherwise, if the year number isn't divisible by 100, it's a leap year;
elif year % 100 != 0:
    print("Leap Year")
# otherwise, if the year number isn't divisible by 400, it's a common year;
elif year % 400:
    print("Common Year")
# otherwise, it's a leap year.
else:
    print("Leap Year")