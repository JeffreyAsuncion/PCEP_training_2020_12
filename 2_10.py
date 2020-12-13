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
print()


for i in range(100):
    print("H" * i)
print()


for i in range(10):
    print("Valve of i is currently", i)
print()



for i in range(2, 8):
    print("Valve of i is currently", i)
print()


for i in range(2, 8, 3):
    print("Valve of i is currently", i)
print("check if anything prints")

for i in range(1, 1):
    print("Valve of i is currently", i)
print("hmm...")

print("check if anything prints")

for i in range(2, 1):
    print("Valve of i is currently", i)
print("hmm...")

pow = 1
for exp in range(16):
    print("2 to the power of ", exp, "is", pow)
    pow *= 2