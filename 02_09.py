"""
Given an N by M matrix, rotate it by 90 degrees clockwise.
"""
matrix = [[1,2],[3,4],[5,6]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix_rotated = []
temp = []
for i in range(len(matrix[1])):
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    matrix_rotated.append(temp[::-1])
    temp = []

print(matrix_rotated)
