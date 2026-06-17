"""
Problem Statement

Given a sorted list of integers and a target value, return the index of the target.

If the target is not found, return -1.

Example 1
nums = [1, 3, 5, 7, 9]
target = 5

Output:
2

Example 2
nums = [2, 4, 6, 8, 10]
target = 7

Output:
-1

"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Example usage
print(binary_search([1, 3, 5, 7, 9], 5))   # 2
print(binary_search([2, 4, 6, 8, 10], 7))  # -1
print(binary_search([10], 10))             # 0
