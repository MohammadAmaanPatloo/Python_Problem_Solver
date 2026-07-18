"""
Problem Statement

Given an integer array nums, return an array answer such that:

answer[i] = product of all elements in nums except nums[i]
Rules
Do not use the division operator (/ or //).
The solution should run in O(n) time.

Example 1
Input:
nums = [1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Example 2
Input:
nums = [-1, 1, 0, -3, 3]

Output:
[0, 0, 9, 0, 0]
"""


def product_except_self(nums):
    n = len(nums)

    # Initialize answer array with 1
    answer = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


print(product_except_self([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
