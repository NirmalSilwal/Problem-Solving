def rec_bin_search(arr, element):

    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2

        if arr[mid] == element:
            return True
        else:
            if element < arr[mid]:
                return rec_bin_search(arr[:mid], element)
            else:
                return rec_bin_search(arr[mid+1:], element)


lst = [1,2,3,4,5,6,7]
print(rec_bin_search(lst, 2))
print(rec_bin_search(lst, 10))