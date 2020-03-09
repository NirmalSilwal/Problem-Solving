def bubble_sort(lst):
    for passes in range(len(lst)-1, 0, -1):
        for check in range(passes):
            if lst[check] > lst[check+1]:
                lst[check], lst[check+1] = lst[check+1], lst[check]

    return lst


lst = [1,24,4,5,6,7]
print(bubble_sort(lst))