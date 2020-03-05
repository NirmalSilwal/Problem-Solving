def anagram_check1(sen1, sen2):
    sen1 = sen1.replace(' ','').lower()
    sen2 = sen2.replace(' ','').lower()

    return 'anagram' if sorted(sen1) == sorted(sen2) else 'not anagram'


def anagram_check2(sen1, sen2):
    sen1 = sen1.replace(' ','').lower()
    sen2 = sen2.replace(' ','').lower()
    dic = {}
    for character in sen1:
        if character in dic:
            dic[character] += 1
        else:
            dic[character] = 1

    for character in sen2:
        if character in dic:
            dic[character] -= 1
        else:
            dic[character] = 1

    for key in dic:
        if dic[key]>0:
            return 'not anagram'
    return 'anagram'

print(anagram_check2('dogfx`','ogd'))
