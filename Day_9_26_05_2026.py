"""
Problem Statement

Write a function that finds the longest common prefix among a list of strings.

If there is no common prefix, return an empty string "".


Example 1
Input:
["flower", "flow", "flight"]

Output:
"fl"

Example 2
Input:
["dog", "racecar", "car"]

Output:
""
"""


def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
# Output: "fl"

print(longest_common_prefix(["dog", "racecar", "car"]))
# Output: ""

print(longest_common_prefix(["interview", "internet", "internal"]))
# Output: "inter"
