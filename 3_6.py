def Factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1

    # range is exclusive on the end, so we need to add 1
    for i in range(2, n+1):
        product *= i

    return product


def Factorial_recursion(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * Factorial_recursion(n-1)



for n in range(1, 6):
    print(n, Factorial_recursion(n))