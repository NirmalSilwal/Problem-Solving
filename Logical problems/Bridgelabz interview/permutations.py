def permutation(sen):

    result = []

    if len(sen) == 1:
        result = [sen]
    else:
        for i, letter in enumerate(sen):

            before_letter = sen[:i]
            after_letter = sen[i+1:]

            print(f'current letter {letter} and index {i} ')

            for permute in permutation(before_letter + after_letter):

                print('permute here: ', permute)

                result.append(letter+permute)

                print('result till now: ',result)

    return result


print('=========================== OUTPUT ========================================')
output = permutation('abc')
print(output)
