def urlify(str: str):
    """
    Write a method to replace all spaces in a string with '%20'. 
    You may assume that the string has sufficient space at the end 
    to hold the additional characters, and that you are given the 
    "true" length of the string.

    (Note: If implementing in Java, please use a character array 
    so that you can perform this operation in place.)
    """
    return str.strip().replace(' ', '%20')

def urlify_without_built_ins(str: str, str_len: int):
    """
    Same as urlify, but removing use of built-in methods
    """
    new_str = ''
    for i in range(str_len):
        char = str[i]
        if char == ' ':
            char = '%20'
        new_str += char
    return new_str