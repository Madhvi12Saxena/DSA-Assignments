'''Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]'''

def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    start_row = 0
    end_row = n - 1
    start_col = 0
    end_col = n - 1
    num = 1

    while num <= n * n:
        # Fill top row
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = num
            num += 1
        start_row += 1

        # Fill right column
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = num
            num += 1
        end_col -= 1

        # Fill bottom row
        for i in range(end_col, start_col - 1, -1):
            matrix[end_row][i] = num
            num += 1
        end_row -= 1

        # Fill left column
        for i in range(end_row, start_row - 1, -1):
            matrix[i][start_col] = num
            num += 1
        start_col += 1

    return matrix
n = 3
matrix = generateMatrix(n)
print(matrix)