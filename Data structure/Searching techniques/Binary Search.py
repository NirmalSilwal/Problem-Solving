def binary_search(arr, element):

    first = 0
    last = len(arr)-1
    found = False

    while first < last and not found:

        mid_index = (first+last) // 2

        if arr[mid_index] == element:
            found = True
        else:
            if element < arr[mid_index]:
                last = mid_index - 1
            else:
                first = mid_index + 1

    return found


lst = [1,2,3,4,5,6,7]
print(binary_search(lst, 2))
print(binary_search(lst, 10))