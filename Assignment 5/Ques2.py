'''You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.
Given the integer n, return *the number of **complete rows** of the staircase you will build*.
Input: n = 5
Output: 2'''

def calculate_complete_rows(n):
    k = 0
    while (k * (k + 1)) // 2 <= n:
        k += 1

    return k - 1
n = 5
output = calculate_complete_rows(n)
print(output)