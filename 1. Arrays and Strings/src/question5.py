def one_away(str1, str2):
    """
    There are three types of edits that can be performed on strings: 
    insert a character, remove a character, or replace a character. 
    
    Given two strings, write a function to check if they are one edit (or zero edits) away.
    """
    if abs(len(str1) - len(str2)) > 1:
        return False
    str_1_chars = {char: str1.count(char) for char in str1}
    str_2_chars = {char: str2.count(char) for char in str2}
    
    all_chars = list(set(list(str_1_chars.keys()) + list(str_2_chars.keys())))
    diff = 0
    for char in all_chars:
        diff += abs(str_1_chars.get(char, 0) - str_2_chars.get(char, 0))
    
    return diff <= 2