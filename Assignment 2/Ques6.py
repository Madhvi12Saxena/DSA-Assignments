def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))