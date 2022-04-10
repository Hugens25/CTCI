def check_permutation(str1: str, str2: str):
    """
    1.2 Given two strings,write a method to decide 
    if one is a permutation of the other.
    """
    if len(str1) != len(str2):
        return False
    
    str_1_chars = {char: str1.count(char) for char in str1}
    str_2_chars = {char: str2.count(char) for char in str2}
    return sorted(str_1_chars) == sorted(str_2_chars)