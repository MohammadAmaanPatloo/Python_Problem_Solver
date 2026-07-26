"""
Problem Statement

Given an unsorted array of integers nums, return the length of the longest consecutive sequence.

A consecutive sequence consists of numbers that follow each other with a difference of 1.

Your algorithm should run in O(n) time.

Example 1
Input:
nums = [100, 4, 200, 1, 3, 2]

Output:
4

Example 2
Input:
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

Output:
9
"""


def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:

        # Check if this is the start of a sequence
        if num - 1 not in num_set:

            current = num
            length = 1

            # Count consecutive numbers
            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))            # 4
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))             # 9
print(longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6]))         # 7