def largest_continuous_sum(lst):

    max_list = []

    for i in range(len(lst)):
        consecutive_sum = []
        total = lst[i]
        for next_element in lst[i+1:]:
            total = total + next_element
            consecutive_sum.append(total)

        max_list.append(max(consecutive_sum))

        return max(max_list)



arr = [1,2,-1,3,4,10,10,-10,-1]

print(largest_continuous_sum(arr))