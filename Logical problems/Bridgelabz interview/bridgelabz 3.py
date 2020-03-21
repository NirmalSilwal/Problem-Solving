my_string = input('enter any string: ')


def is_palindrome(word):
    return word == word[::-1]


def find_permutations(sen):
    result = []

    if len(sen) == 1:
        result = [sen]
    else:
        for i, letter in enumerate(sen):

            for permute in find_permutations(sen[:i] + sen[i+1:]):

                result.append(letter + permute)

    return result


def is_possible(word):
    # let's make the permutation of given string and check till any combination satisfies or all finishes
    permutation = find_permutations(word)

    counter = 0

    while counter < len(permutation):

        if is_palindrome(permutation[counter]):
            return True

        counter += 1
    else:
        return False


if __name__ == "__main__":
    if is_possible(my_string):
        print(f'palindrome possible for given string: {my_string}')
    else:
        print('palindrome not possible')
