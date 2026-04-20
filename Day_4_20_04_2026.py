"""
Problem Statement

Write a function that takes a list of integers and returns the most frequent element.

Examples:
Input:  [1, 2, 3, 2, 1, 2]
Output: 2

Input:  [4, 4, 5, 5, 5]
Output: 5
"""



def most_frequent(Input):
    freq={}
    for num in Input:
        freq[num]=freq.get(num,0)+1
    return max(freq, key=freq.get)
    
print(most_frequent(Input=[1,2,3,2,1,2]))