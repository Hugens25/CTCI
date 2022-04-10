from src import question4

def test_is_palindrome_false_one_char():
    assert question4.palindrome_permutation('a') == False

def test_is_palindrome_false_two_char():
    assert question4.palindrome_permutation('ab') == False

def test_is_palindrome_false():
    assert question4.palindrome_permutation('abcc') == False

def test_is_palindrome_true():
    assert question4.palindrome_permutation('aba') == True

def test_is_palindrome_true_9_chars():
    assert question4.palindrome_permutation('aabbcddee') == True
