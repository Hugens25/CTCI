from src import question1

def test_is_unique_true():
    assert question1.is_unique('abc') == True

def test_is_unique_false():
    assert question1.is_unique('abcabc') == False

def test_is_unique_basic_true():
    assert question1.is_unique_basic('abc') == True

def test_is_unique_basic_false():
    assert question1.is_unique_basic('abcabc') == False