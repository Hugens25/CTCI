import json
from typing import List


def rotate_metrix(matrix: List[List[int]]):
    matrix_size = len(matrix[0])
    max_index = matrix_size-1
    new_matrix = [[0] * matrix_size] * matrix_size
    
    for i in range(matrix_size):
        for j in range(matrix_size):
            new_matrix[i][j] = matrix[max_index - j][i]
    return new_matrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# """
# 0,0 -> 0,2
# 0,1 -> 1,2
# 0,2 -> 2,2
# 1,0 -> 0,1
# 1,1 -> 1,1
# 1,2 -> 2,1
# 2,0 -> 0,0
# 2,1 -> 1,0
# 2,2 -> 2,0
# """

# """
# 2,0 -> 0,0
# 1,0 -> 0,1
# 0,0 -> 0,2
# 2,1 -> 1,0
# 1,1 -> 1,1
# 0,1 -> 1,2
# 2,2 -> 2,0
# 1,2 -> 2,1
# 0,2 -> 2,2
# """

# expected = [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3],
# ]
# print(rotate_metrix(matrix))