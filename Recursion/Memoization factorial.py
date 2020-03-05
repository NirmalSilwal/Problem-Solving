class Memoize(object):

    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)

        return self.memo[args]


def factorial(num):
    if num < 2:
        return 1

    return num * factorial(num - 1)


fact = Memoize(factorial)
print(fact(4))
