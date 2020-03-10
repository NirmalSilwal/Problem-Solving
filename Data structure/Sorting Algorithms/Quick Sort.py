def quick_sort(arr):

    return quick_sort_help(arr, 0, len(arr)-1)


def quick_sort_help(arr, first, last):

    if first < last:
        split_point = partition(arr, first, last)

        quick_sort_help(arr, first, split_point-1)
        quick_sort_help(arr, split_point+1, last)

    return arr


def partition(arr, first, last):

    pivot = arr[first]

    left_mark = first+1
    right_mark = last

    done = False

    while not done:

        while left_mark <= right_mark and arr[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and arr[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]

    arr[first], arr[right_mark] = arr[right_mark], arr[first]
    # temp = arr[first]
    # arr[first] = arr[right_mark]
    # arr[right_mark] = temp

    return right_mark


lst = [11, 3, 2, 5, 77, 4, 8, 0]
print('original array: ', lst)
print('sorted array: ', quick_sort(lst))
