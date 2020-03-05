# 1st approach: python trick
def reverse1(sen):
    return sen[::-1]


# 2nd approach: using recursion
def reverse_recursion(sen):
    # base case
    if len(sen) == 1:
        return sen

    # recursive case
    return reverse_recursion(sen[1:]) + sen[0]


# 3rd approach: using stack
def reverse2(sen):

    stack = [char for char in sen]
    reversed_stack = [stack.pop() for _ in range(len(stack))]

    return ''.join(reversed_stack)


# 4th approach: using stack long way
def reverse3(sen):
    stack = []
    for character in sen:
        stack.append(character)

    reversed_stack = []
    for i in range(len(stack)):
        reversed_stack.append(stack.pop())

    return ''.join(reversed_stack)


my_string = 'hello world'

print(reverse1(my_string))
print(reverse2(my_string))
print(reverse3(my_string))

print('using recursion:', reverse_recursion(my_string))