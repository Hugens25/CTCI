from src import question5

def test_one_away_remove_true():
    assert question5.one_away('pale', 'ple') == True

def test_one_away_add_true():
    assert question5.one_away('pales', 'pale') == True

def test_one_away_replace_true():
    assert question5.one_away('pale', 'bale') == True

def test_one_away_false():
    assert question5.one_away('pale', 'bake') == False