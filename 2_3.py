"""
Estimated time
5-10 minutes

Level of difficulty
Easy

Objectives
becoming familiar with the the input() function;
becoming familiar with comparison operators in Python;
becoming familiar with the concept of conditional execution.
Scenario
Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

One programmer from the Python Institute loves these plants. Whenever she hears or sees the word Spathiphyllum, she shouts "Spathiphyllum is the best plant ever!"

Write a program that utilizes the concept of conditional execution, takes a string as input, and prints the sentence "Spathiphyllum is the best plant ever!" to the screen if the string is "Spathiphyllum" (upper-case), and prints "No, I want a real Spathiphyllum...!" otherwise.

Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

Example input
spathiphyllum

Example output
No, I want a real Spathiphyllum...!

Example input
pelargonium

Example output
No, I want a real Spathiphyllum...!

Example input
Spathiphyllum

Example output
Spathiphyllum is the best plant ever!
"""


str = input(">>> ")
if str == "Spathiphyllum":
    print("Spathiphyllum is the best plant ever!")
else:
    print("No, I want a real Spathipyllum...!")