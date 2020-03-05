def sum_digits(num):
    if len(str(num)) == 1:
        return num
    else:
        return num % 10 + sum_digits(num // 10)


print(sum_digits(4321))
