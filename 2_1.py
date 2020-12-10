"""
Estimated time
5 minutes

Level of difficulty
Very Easy

Objectives
becoming familiar with the the input() function;
becoming familiar with comparison operators in Python.
Scenario
Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

Test your code using the data we've provided for you.

Example input
55

Example output
False

Example input
99

Example output
False

Example input
100

Example output
True

Example input
123

Example output
True
"""

num = int(input("Enter an integer: "))
print(num >= 100)