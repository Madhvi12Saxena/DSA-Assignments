'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears **once** or **twice**, return *an array of all the integers that appears **twice***.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]'''

def findDuplicates(nums):
    result = []
    
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            result.append(abs(num))
        else:
            nums[index] = -nums[index]
    
    return result
nums = [4, 3, 2, 7, 8, 2, 3, 1]
output = findDuplicates(nums)
print(output)