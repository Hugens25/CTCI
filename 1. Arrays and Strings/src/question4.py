def palindrome_permutation(str: str):
    """
    Given a string, write a function to check if it is 
    a permutation of a palin­ drome. A palindrome is a 
    word or phrase that is the same forwards and backwards. 
    A permutation is a rearrangement of letters. The palindrome 
    does not need to be limited to just dictionary words.
    """
    char_counts = {char: str.count(char) for char in str}
    
    if sum(char_counts.values()) < 3:
        return False
    
    chars_appearing_once = [k for k,v in char_counts.items() if v == 1]
    if len(chars_appearing_once) != 1:
        return False
    
    uneven_char_appearances = [k for k,v in char_counts.items() if v > 1 and v % 2 != 0]
    if uneven_char_appearances:
        return False
    
    return True