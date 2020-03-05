def permutation(sen):
    result = []
    # base case
    if len(sen) == 1:
        result = [sen]
    else:
        for index, letter in enumerate(sen):

            for perm in permutation(sen[:index] + sen[index+1:]):

                result.append(letter + perm)

    return result


per_str = 'abc'
output = permutation(per_str)
# print(output)
