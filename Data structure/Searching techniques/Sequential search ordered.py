def ordered_seq_search(lst, item):
    """
    Input array must be sorted
    """
    pos = 0
    found = False
    stopped = False

    while pos < len(lst) and not found and not stopped:

        if lst[pos] == item:
            found = True
            return found
        else:
            if lst[pos] > item:
                stopped = True
                return found
            else:
                pos += 1
        print(lst[pos])
    return found


arr = [1,2,3,50,56,65]

print(ordered_seq_search(arr,4))
# note here that last 2 elements are not even checked

# print(ordered_seq_search(arr,56))
# print(ordered_seq_search(arr,1))
# print(ordered_seq_search(arr,6))
