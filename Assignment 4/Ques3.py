'''Given a 2D integer array matrix, return *the **transpose** of* matrix.
The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]'''

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    result = [[0] * rows for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            result[j][i] = matrix[i][j]

    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose(matrix)
print(result)