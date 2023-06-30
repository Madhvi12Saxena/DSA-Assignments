'''Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output:[[7,0,0],[-7,0,3]]'''

def multiply_sparse_matrices(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    k2, n = len(mat2), len(mat2[0])

    # Create the resulting matrix with initial zeros
    result = [[0] * n for _ in range(m)]

    # Create dictionaries to store the non-zero values of mat1 and mat2
    mat1_dict = {}
    mat2_dict = {}

    # Populate mat1_dict with non-zero values from mat1
    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                mat1_dict[(i, j)] = mat1[i][j]

    # Populate mat2_dict with non-zero values from mat2
    for i in range(k2):
        for j in range(n):
            if mat2[i][j] != 0:
                mat2_dict[(i, j)] = mat2[i][j]

    # Perform the multiplication on non-zero entries only
    for (i, j1), val1 in mat1_dict.items():
        for (j2, k), val2 in mat2_dict.items():
            if j1 == j2:
                result[i][k] += val1 * val2

    return result
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

result = multiply_sparse_matrices(mat1, mat2)
print(result)