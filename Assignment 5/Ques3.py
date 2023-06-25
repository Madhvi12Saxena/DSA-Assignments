'''Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]'''

def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    
    result.sort()
    return result
nums = [-4, -1, 0, 3, 10]
output = sortedSquares(nums)
print(output)