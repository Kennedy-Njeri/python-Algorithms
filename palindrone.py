"""Give a string, write a function to determine if it is a palindrone"""

# race car
# madam
# Dammit I'm mad.

import string


def is_palindrone(s):
    s = s.lower()
    s = s.translate(None, string.punctuation)
    s = s.replace(" ", "")

    return s == s[::-1]


str_1 = "racecar"
str_2 = "Dammit I'm mad"
str_3 = "computer"

print (is_palindrone(str_1))
print (is_palindrone(str_2))
print (is_palindrone(str_3))
