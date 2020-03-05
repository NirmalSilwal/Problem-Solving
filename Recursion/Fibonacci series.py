# iteratively
def fibonacci_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b

    return a


# using recursion
def fibonacci_recur(n):
    # base case
    if n == 0 or n == 1:
        return n

    return fibonacci_recur(n-1)+fibonacci_recur(n-2)


# using Memoization
n = 10
cache = [None]*(n+1)


def fibonacci_dynamic(n):
    # base case
    if n == 0 or n == 1:
        return n

    # check cache
    if cache[n] is not None:
        return cache[n]

    # keep setting cache
    cache[n] = fibonacci_dynamic(n-1) + fibonacci_dynamic(n-2)

    return cache[n]


print(fibonacci_iter(n))
print(fibonacci_recur(n))
print(fibonacci_dynamic(n))
