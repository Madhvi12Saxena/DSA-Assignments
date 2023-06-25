'''Convert 1D Array Into 2D Array
You are given a **0-indexed** 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using **all** the elements from original.
The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (**inclusive**) should form the second row of the constructed 2D array, and so on.
Return *an* m x n *2D array constructed according to the above procedure, or an empty 2D array if it is impossible*.
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]'''

def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []  # Return empty 2D array if dimensions are incompatible

    result = []
    for i in range(m):
        row = original[i * n:(i + 1) * n]  # Slice the original array for each row
        result.append(row)

    return result
original = [1, 2, 3, 4]
m = 2
n = 2
output = convert_to_2d_array(original, m, n)
print(output)