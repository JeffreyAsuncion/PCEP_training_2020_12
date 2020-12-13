# read two numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter secondnumber: "))
number3 = int(input("Enter third number: "))

# we temporarily assume that 
# the first number is the largest one 
# we will verify it soon
max = number1

# we check if the second value is the larger 
# than current max and update max if needed
if number2 > max:
    max = number2

# we check if the third value is larger that current max 
# and update max if needed
if number3 > max:
    max = number3

# print the result
print("the largest number is", max)