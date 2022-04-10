from src import question3

def test_urlify():
    assert question3.urlify('Mr John Smith   ') == 'Mr%20John%20Smith'

def test_urlify_without_built_ins():
    assert question3.urlify_without_built_ins('Mr John Smith   ', 13) == 'Mr%20John%20Smith'