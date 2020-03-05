def sum_digits_of_integer(num):
    """
    For example: if n = 4321, return 4+3+2+1
    """

    total = 0
    while num != 0:
        last_digit = num % 10
        total += last_digit
        num //= 10

    return total


print(sum_digits_of_integer(4321))

