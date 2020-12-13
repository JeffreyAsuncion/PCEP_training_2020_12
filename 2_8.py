# program reads a sequence of numbers and counts how many numbers
# are even and how many are odd
# program terminates when zero is entered

Evens = 0
Odds = 0

# read first number
Number = int(input("Enter a value or 0 to stop: "))

# 0 terminates execution
while Number != 0:
    # check if the number is odd
    if Number % 2 == 1:
        # increase "odd" counter
        Odds += 1
    else:
        # increase "even" counter
        Evens += 1

    # read next number
    Number = int(input("Enter a value or 0 to stop: "))

# print results
print("Even numbers: ", Evens)
print("Odd numbers: ", Odds)