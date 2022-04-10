def string_compression(str: str):
    """
     Implement a method to perform basic string compression using the counts
     of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. 
     If the "compressed" string would not become smaller than the original string, your 
     method should return the original string. You can assume the string has only 
     uppercase and lowercase letters (a - z).
    """
    char_counts = {char: str.count(char) for char in str}
    char_counts_above_2 = [count for count in char_counts.values() if count > 2]
    if not char_counts_above_2:
        return str
    
    current_char = str[0]
    current_count = 0
    result_str = ''
    for char in str:
        if char == current_char:
            current_count += 1
            continue
        result_str += f'{current_char}{current_count}'
        current_char = char
        current_count = 1
    result_str += f'{current_char}{current_count}'
    return result_str
