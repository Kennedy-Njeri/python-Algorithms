# consonant is a letter that is not a vowel
# i.e a letter that is not a, e, i, o, u

input_str_1 = "abc de"
input_str_2 = "KennedyScOOl"

vowel = "aeiou"


def iterative_consonants(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count += 1
    return count


