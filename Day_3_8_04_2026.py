"""

Problem Statement

Write a function that checks whether a given string is a palindrome.

A palindrome is a string that reads the same forward and backward.

Input:  "madam"
Output: True

Input:  "racecar"
Output: True

Input:  "python"
Output: False

"""


def is_palindrome(text):
    return text == text[::-1]


print(is_palindrome("madam"))    
    

