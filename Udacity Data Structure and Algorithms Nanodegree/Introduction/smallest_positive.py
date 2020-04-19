def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    
    # edge case
    if len(in_list) == 0:
        return None
    else:
        # checking for postive element only
        newlist = [i for i in in_list if i>0]
        
        # edge case
        if len(newlist) > 0:
            
            smallest = newlist[0]
            
            for element in newlist[1:]:
                if element < smallest:
                    smallest = element
            
            return smallest
        
        return None

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None

print(smallest_positive([-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58]))