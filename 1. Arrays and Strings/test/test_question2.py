from src import question2

def test_check_permutation_true():
    assert question2.check_permutation('abc', 'cba') == True

def test_check_permutation_false():
    assert question2.check_permutation('abc', 'dca') == False

def test_check_permutation_diff_lengths():
    assert question2.check_permutation('abc', 'cbad') == False