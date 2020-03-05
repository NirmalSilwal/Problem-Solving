# storing known results in cache
factorial_memo = {}


def factorial(n):
    if n < 2:
        return 1

    if n not in factorial_memo:
        factorial_memo[n] = n * factorial(n-1)

    return factorial_memo[n]


print(factorial_memo)
print(factorial(5))
print(factorial_memo)
print(factorial(4))
print(factorial_memo)
print(factorial(7))
print(factorial_memo)

