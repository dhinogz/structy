"""
Write a function, uncompress, that takes in a string as an argument. 
The input string will be formatted into multiple groups according to 
the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string 
where each 'char' of a group is repeated 'number' times consecutively. 
You may assume that the input string is well-formed according to the 
previously mentioned pattern.

uncompress("2c3a1t") # -> 'ccaaat'
"""
# Bruteforce
def uncompress(s):
  res = ""
  num = ""
  for char in s:
    if char.isnumeric():
      num += char
    else:
      if num == "":
        res += char
      else:
        res += char * int(num)
        num = ""

  return res

# Two pointers
def uncompress(s):

    res = ""
    nums = "0123456789"
    i = 0
    j = 0

    while j != len(s):
        if s[j] in nums:
            j += 1
        else:
            num = int(s[i:j])
            res += s[j] * num
            j += 1
            i = j

    return res


