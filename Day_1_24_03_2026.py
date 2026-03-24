"""
Problem Statement:

Write a function that takes a string and returns a dictionary containing the frequency of each character in the string.
Input: "programming"
Output: {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}

"""


def character_frequency(Input):
    Output={}
    for char in Input:
        Output[char]=Output.get(char,0)+1
    return Output

print(character_frequency("programming"))
    
    

