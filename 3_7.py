def Fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    el1 = el2 = 1
    sum = 0
    for i in range(3, n+1):
        sum = el1 + el2
        el1, el2 = el2, sum
    return sum

def Fib_recursion(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return Fib(n-1) + Fib(n-2)

for n in range(1, 10):
    print(n,'--->', Fib_recursion(n))