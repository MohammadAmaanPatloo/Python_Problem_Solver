"""
Problem Statement

Given an integer array nums, find the contiguous subarray (containing at least one number) that has the largest sum and return that sum.

Contiguous means the elements must be next to each other.

Example 1
Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6

Example 2
Input:
nums = [1]

Output:
1

Example 3
Input:
nums = [5, 4, -1, 7, 8]

Output:
23
"""


def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(max_subarray([1]))  # 1
print(max_subarray([5, 4, -1, 7, 8]))  # 23
print(max_subarray([-5, -2, -8]))  # -2
