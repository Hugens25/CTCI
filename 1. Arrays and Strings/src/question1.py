def is_unique(str: str):
    """
    1.1 Implement an algorithm to determine 
    if a string has all unique characters
    """
    char_counts = {}
    for char in str:
        char_exists = char_counts.get(char) is not None
        if char_exists:
            return False
        char_counts[char] = 1
    return True

def is_unique_basic(str: str):
    """
    1.1 What if you cannot use additional data structures?
    """
    sorted_str = sorted(str)
    for i in range(1, len(sorted_str)):
        if sorted_str[i-1] == sorted_str[i]:
            return False
    return True
