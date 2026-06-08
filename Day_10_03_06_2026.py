"""
Problem Statement

Given a string containing only:

()
{}
[]

Determine if the input string is valid.

A string is valid if:
Every opening bracket has a matching closing bracket
Brackets close in the correct order

Example 1
Input:
"()"

Output:
True

Example 2
Input:
"()[]{}"

Output:
True

Example 3
Input:
"(]"

Output:
False
"""


def is_valid(s):
    stack = []

    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # Opening bracket
        if char in pairs.values():
            stack.append(char)

        # Closing bracket
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
