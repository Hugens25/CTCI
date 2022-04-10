def is_substring(str1, str2):
    return str2 in str1

def string_rotation(str1, str2):
    return is_substring(str1*2, str2)
