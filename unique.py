"""Implement an algorithm to determine if a string has all unique characters comparable"""


def is_unique(s):
    return len(s) == len(set(s))


s1 = "unique"
s2 = "bear"

print (is_unique(s1))
print (is_unique(s2))