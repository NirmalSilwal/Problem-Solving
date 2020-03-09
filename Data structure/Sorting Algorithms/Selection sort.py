def selection_sort(lst):

    for passes in range(len(lst)-1, 0, -1):  # requires n-1 passes

        max_position = 0

        for loc in range(1, passes+1):
            # selecting position of highest element

            if lst[loc] > lst[max_position]:
                max_position = loc

        lst[passes], lst[max_position] = lst[max_position], lst[passes]

    return lst


arr = [21, 2, 45.2, 3, 65, 6]
print(selection_sort(arr))
