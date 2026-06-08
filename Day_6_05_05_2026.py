"""
Problem Statement

Given a list of integers and a target number, return the indices of the two numbers such that they add up to the target.

You may assume:

Exactly one valid answer exists
You cannot use the same element twice

Examples
Example 1
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Example 2
Input:
nums = [3, 2, 4]
target = 6

Output:
[1, 2]

"""



def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], index]

        seen[num] = index


print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 2, 4], 6))        # [1, 2]

