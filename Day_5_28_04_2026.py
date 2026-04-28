"""
Problem Statement

Write a function that takes a list of integers and returns True if there are any duplicates, otherwise False.

Examples
Input:  [1, 2, 3, 4]
Output: False

Input:  [1, 2, 3, 2]
Output: True

Input:  [5, 5, 5]
Output: True
"""


def has_duplicates(lst):
    return len(lst) != len(set(lst))


print(has_duplicates([1, 2, 3, 4]))   # False
print(has_duplicates([1, 2, 3, 2]))   # True
print(has_duplicates([5, 5, 5]))      # True