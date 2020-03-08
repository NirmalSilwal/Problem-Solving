def seq_search(lst, element):
    pos = 0
    found = False

    while pos < len(lst) and not found:

        if lst[pos] == element:
            found = True
        else:
            pos += 1

    return found


arr = [1,2,3,4,5,56]

print(seq_search(arr,3))
print(seq_search(arr,56))
print(seq_search(arr,1))
print(seq_search(arr,6))