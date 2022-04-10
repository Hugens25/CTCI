from src import question6

def test_string_compression():
    assert question6.string_compression('aabcccccaaa') == 'a2b1c5a3'

def test_string_compression_return_original():
    assert question6.string_compression('aabbccddeeff') == 'aabbccddeeff'

def test_string_compression_return_original_example_2():
    assert question6.string_compression('abcdef') == 'abcdef'
