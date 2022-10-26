
def get_char_count(s):

    chars = {}

    for char in s:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    return chars

def most_frequent_char(s):  

    chars = get_char_count(s)

    # max(chars, key=chars.get) Get key with highest value
    best = None
    for char in s:
        if best is None or chars[char] > chars[best]:
            best = char

    return best    
