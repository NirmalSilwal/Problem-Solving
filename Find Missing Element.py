def find_missing(arr1, arr2):
    miss = []
    for i in arr1:
        if i not in arr2:
            miss.append(i)

    return miss


##ANOTHER APPROACH

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

###


##ANOTHER APPROACH using XOR trick for optimal solution

def finder2(arr1,arr2):
    result = 0
    for item in arr1+arr2:
        result ^= item

    return result

###


arr1 = [1,2,3,4]
arr2 = [3,1,4]

# missing = find_missing(arr1, arr2)
# print(f'missing element is: {missing}')
# print('missing element is',*missing)

# print(finder(arr1, arr2))

print(finder2(arr1,arr2))