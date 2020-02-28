def rotate_arr(lst, how_much):
    tmp = lst[:how_much]
    new_lst = lst[how_much:]
    new_lst.extend(tmp)

    return new_lst

##ANOTHER APPROACH

def left_shift(lst):
    tmp = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i + 1]

    lst[-1] = tmp

    return lst

def rotate_by_shifting(lst, how_much):
    result = lst
    for rotation in range(how_much):
        result = left_shift(result)

    return result

####

lst = [1,2,3,4,5,6,7]
how_much = 2
result = rotate_by_shifting(lst,how_much)
print(result)