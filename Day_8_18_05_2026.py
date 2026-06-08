"""
Problem Statement

You are given a list containing n distinct numbers taken from the range 0 to n.

Exactly one number is missing.

Write a function to find the missing number.

Example 1
Input:
[3, 0, 1]

Output:
2

Example 2
Input:
[0, 1]

Output:
2

"""

def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


print(missing_number([0,1,2,4,5]))              # 2
print(missing_number([3, 0, 1]))                # 2
print(missing_number([0, 1]))                   # 2
print(missing_number([9,6,4,2,3,5,7,0,1]))      # 8

