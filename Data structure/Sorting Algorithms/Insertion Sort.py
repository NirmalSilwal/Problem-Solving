def insertion_sort(lst):

    for passes in range(1, len(lst)):  # n-1 passes
        current_val = lst[passes]
        pos = passes

        while pos > 0 and lst[pos-1] > current_val:
            lst[pos] = lst[pos-1]
            pos = pos-1

        lst[pos] = current_val

    return lst


arr = [2, 4, 42, 6, 22, 7]
print(insertion_sort(arr))
