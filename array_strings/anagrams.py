"""
First solution:
    Use sorted function in python library and compare both strings result

Hash table solution:
    Create a helper function to get a dictionary with all chars count in s
    Return comparison between both char_count dictionaries
"""



def get_char_count(s):

    chars = {}

    for char in s:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    return chars

def anagrams(s1, s2):

    return get_char_count(s1) == get_char_count(s2)