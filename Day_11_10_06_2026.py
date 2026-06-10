"""
Problem Statement

Given two sorted lists, merge them into a single sorted list.

Example 1
list1 = [1, 3, 5]
list2 = [2, 4, 6]

Output:
[1, 2, 3, 4, 5, 6]
Example 2
list1 = [1, 2, 7]
list2 = [3, 4, 5]

Output:
[1, 2, 3, 4, 5, 7]
Example 3
list1 = []
list2 = [1, 2, 3]

Output:
[1, 2, 3]
"""


def merge_sorted_lists(list1, list2):
    merged = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


# Example usage
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_sorted_lists([1, 2, 7], [3, 4, 5]))
print(merge_sorted_lists([], [1, 2, 3]))
