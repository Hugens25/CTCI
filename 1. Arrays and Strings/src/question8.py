from typing import List

def zero_matrix(matrix: List[List[int]]):
    """
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0.
    """
    max_column_index = len(matrix)
    max_row_index = len(matrix[0])

    columns_to_set_zero = []
    rows_to_set_zero = []
    for i in range(max_column_index):
        for j in range(max_row_index):
            if matrix[i][j] == 0:
                rows_to_set_zero.append(i)
                columns_to_set_zero.append(j)
    for i in range(max_column_index):
        for j in range(max_row_index):
            if i in rows_to_set_zero:
                matrix[i][j] = 0
            if j in columns_to_set_zero:
                matrix[i][j] = 0
    return matrix
