def rec_sum(num):
    while num > 0:
        return num + (0 if rec_sum(num-1) is None else rec_sum(num-1))


# Another way of solving
def rec_sum2(num):
    if num == 0:
        return 0
    elif num < 0:
        return 'not for negative numbers'
    else:
        return num + rec_sum2(num-1)


# Another way of solving
def rec_sum3(num):
    if num == 0:
        return 0
    else:
        return num + rec_sum3(num-1)


print(rec_sum(4))
print(rec_sum2(4))
print(rec_sum3(4))


'''
Finding the cumulative sum of given number
For example, if n=4 , return 4+3+2+1+0, which is 10.
'''