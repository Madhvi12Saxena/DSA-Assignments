def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True
    
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            isIncreasing = False
        if nums[i] < nums[i+1]:
            isDecreasing = False
        if not isIncreasing and not isDecreasing:
            return False
    
    return isIncreasing or isDecreasing
nums = [1, 2, 2, 3]
print(isMonotonic(nums))