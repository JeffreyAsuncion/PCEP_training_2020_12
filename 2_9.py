"""
Estimated time
15 minutes

Level of difficulty
Easy

Objectives
Familiarize the student with:

using the while loop;
reflecting real-life situations in computer code.
Scenario
A junior magician has picked a secret number. 
He has hidden it in a variable named secret_number. 
He wants everyone who runs his program 
to play the "Guess the secret number" game, 
and guess what number he has picked for them. 
Those who don't guess the number will be stuck in a loop forever! 
Unfortunately, he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that when run:

it asks the user to enter an integer number;
it checks whether the number chosen by the user is equal to the number picked by the magician. 
If the number chosen by the user is different than the secret number chosen by the magician, 
the user will see the message "No, that's not the number I've picked for you. Try again!" 
and will be asked to choose another number. 

If the number entered by the user matches the number picked by the magician, 
the number should be printed to the screen, 
and the magician should say the following words: "Well done! That's the number I've chosen for you! You are free now."

The magician is counting on you! Don't let him down.
"""

secret_number = 8

print("Welcome to my game, muggle!\nEnter an integer number and guess what number I've picked for you!\nI'll give you a hint: it's an integer number from 0 to 10.")

# Write your code line that prompts the user to enter an integer number here
guess = int(input("Enter your guess: "))

# Write your while loop and the rest of your code here
while guess != secret_number:
    # it checks whether the number chosen by the user is equal to the number picked by the magician. 
    # If the number chosen by the user is different than the secret number chosen by the magician,
    if guess != secret_number: 
        # the user will see the message "No, that's not the number I've picked for you. Try again!" 
        print("No, that's not the number I've picked for you. Try again!")
        # and will be asked to choose another number. 
        guess = int(input("Enter another guess: "))
            
# If the number entered by the user matches the number picked by the magician, 
else:
    # the number should be printed to the screen,
    print(guess) 
    # and the magician should say the following words: "Well done! That's the number I've chosen for you! You are free now."
    print("Well done! That's the number I've chosen for you! You are free now.")