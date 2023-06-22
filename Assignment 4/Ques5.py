'''You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.
Given the integer n, return *the number of **complete rows** of the staircase you will build*.
**Input:** n = 5
**Output:** 2'''

def arrange_coins(n):
    rows = 0
    total_coins = 0

    i = 1
    while total_coins <= n:
        total_coins += i
        if total_coins <= n:
            rows += 1
        i += 1

    return rows
n = 5

result = arrange_coins(n)
print(result)