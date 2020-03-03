def bubble_sort(lst):
    length = len(lst)
    for pass_index in range(length-1):
        for check_element in range(length - pass_index - 1):
            if lst[check_element] > lst[check_element+1]:
                #swap them
                lst[check_element], lst[check_element+1] = lst[check_element+1], lst[check_element]

    return lst


# lst = [5,1,4,2,8]
lst = [64, 34, 25, 12, 22, 11, 90]
# lst = [4,6,73,2,7,9,0,23,6,8,2]
sorted_list = bubble_sort(lst)
print(sorted_list)