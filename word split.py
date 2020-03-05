"""
Create a function called word_split() which takes in a string phrase and a set list_of_words.
The function will then determine if it is possible to split the string in a way in which words
can be made from the list of words. You can assume the phrase will only contain words found in the
dictionary if it is completely splittable.
"""


def word_split(phrase, list_of_words):

    if len(list_of_words) == len(set(list_of_words)):
        dic = {word:1 for word in list_of_words}

    else:
        dic = {}
        # if any duplicates in list_of_words
        for words in list_of_words:
            if words not in dic.keys():
                dic[words] = 1
            else:
                dic[words] += 1

    result = []
    for keys in dic.keys():
        if keys in phrase:
            result.append(keys)

    result_str = ''.join(result)

    if len(result_str) == len(phrase):
        return result
    else:
        return []


print(word_split('themanran', ['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','a','love','John']))
print(word_split('themanran',['clown','ran','man']))
