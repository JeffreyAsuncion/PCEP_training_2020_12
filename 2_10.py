"""
looping through code

odd
"""


Number = 13

if Number % 2 == 1:
    print(Number)

if Number % 2:
    print(Number)


print("*" * 30)

counter = 5
while counter != 0:
    print("My name is Python " + "*" * counter)
    counter -= 1

print("X" * 30)

counter = 5
while counter:
    print("My name is Python " + "X" * counter)
    counter -= 1

i = 0 
while i < 100:
    print("."*i)
    i += 1


for i in range(100):
    print("H" * i)


for i in range(10):
    print("Valve of i is currently", i)

for i in range(2, 8):
    print("Valve of i is currently", i)
