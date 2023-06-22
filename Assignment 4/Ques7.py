'''You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return *the number of maximum integers in the matrix after performing all the operations*
**Input:** m = 3, n = 3, ops = [[2,2],[3,3]]
**Output:** 4'''

def max_count(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col
m = 3
n = 3
ops = [[2, 2], [3, 3]]

result = max_count(m, n, ops)
print(result)