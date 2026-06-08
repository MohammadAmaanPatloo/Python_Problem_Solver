"""
Problem Statement

Write a function that checks whether two strings are anagrams of each other.

Two strings are anagrams if:

They contain the same characters
With the same frequency
Order does NOT matter

Example 1
Input:
s = "listen"
t = "silent"

Output:
True
Example 2
Input:
s = "hello"
t = "world"

Output:
False

"""


def is_anagram(s, t):
    return sorted(s) == sorted(t)


print(is_anagram("listen", "silent"))    # True
print(is_anagram("hello", "world"))      # False
print(is_anagram("triangle", "integral")) # True
