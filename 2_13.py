"""
Estimated time
5 minutes

Level of difficulty
Very Easy

Objectives
Familiarize the student with:

using basic instructions related to lists;
creating and modifying lists.
Scenario
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to 
replace the middle number in the list with an integer number entered by the user (ex. 1);

write a line of code that removes the last element from the list;
write a line of code that prints the length of the existing list.
Ready for this challenge?
"""

# an existing list of numbers hidden in the hat
hat_list = [1, 2, 3, 4, 5]

# ex. 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user
num = int(input("Enter a number: "))
hat_list[2] = num
# ex. 2: write a line of code here that removes the last element from the list
del hat_list[4]
# ex. 3: write a line of code here that prints the length of the existing list
print(len(hat_list))
# printing the list
print(hat_list)

