from src import question9

def test_string_rotation_true():
    assert question9.string_rotation('erbottlewat', 'waterbottle') == True

def test_string_rotation_false():
    assert question9.string_rotation('erbottlewat', 'waterbottles') == False