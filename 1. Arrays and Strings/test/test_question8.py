from src import question8

def test_zero_matrix():
    matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
        [10,11,12]
    ]
    expected = [
        [1, 0, 3],
        [0, 0, 0],
        [7, 0, 9],
        [10,0,12]
    ]
    actual = question8.zero_matrix(matrix)
    assert expected == actual