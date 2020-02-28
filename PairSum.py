def pair_sum(lst, total):
    item_pairs=[]
    for i in range(len(lst)):
        for j in lst[i+1:]:
            if lst[i] + j == total:
                item_pairs.append([lst[i],j])

    unique_pairs = []
    for pair in item_pairs:
        if pair not in unique_pairs:
            unique_pairs.append(pair)

    return unique_pairs


lst = [1,2,3,2,4,0,2]
total = 4
result = pair_sum(lst, total)
print(f'given input list is : {lst}')
print(f'Total unique pairs with sum {total} is {len(result)}')
print(f'unique pairs are : {result}')