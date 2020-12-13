"""
Estimated time
5 minutes

Level of difficulty
Very easy

Objectives
Familiarize the student with:

using the for loop;
reflecting real-life situations in computer code.
Scenario
Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second-longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!

However, the word Mississippi is also used for a slightly different purpose: to "count mississippily".

If you're not familiar with the phrase, we're here to explain to you: it's used to count seconds. The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately three seconds of time. It's often used by children playing hide-and-seek to make sure the seeker does an honest count.

Your task is very simple here: create a for loop that counts "mississippily" to ten (make sure your output matches the expected output below; each line doesn't need to take a real second to print, you'll learn how to do this trick later in the course), and then prints to the screen the message "Ready or not, here I come!".

Expected output
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
6 Mississippi
7 Mississippi
8 Mississippi
9 Mississippi
10 Mississippi
Ready or not, here I come!
"""

for i in range(1,11):
    print(i, "Mississippi")
print("Ready or not, here I come!")