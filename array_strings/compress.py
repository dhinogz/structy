"""
Write a function, compress, that takes in a string as an 
argument. The function should return a compressed version of 
the string where consecutive occurrences of the same characters 
are compressed into the number of occurrences followed by the 
character. Single character occurrences should not be changed.


Solution:

    Use two pointers. Po
"""

def compress(s):
    s += "!"
    res = ""
    i = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            count = j - i
            if count == 1:
                res += s[i]
            else:
                res += f"{count}{s[i]}"
            i = j

    return res

