"""

Problem Statement

Write a function that takes a positive integer and returns the largest digit present in that number.

Input:  42891
Output: 9

Input:  705
Output: 7


"""

def largest_digit(Input):
    return max(int(digit) for digit in str(Input))

print(largest_digit(42891))

