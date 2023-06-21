def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        current = nums[i]
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = current + nums[left] + nums[right]

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return currentSum

        while i < n - 2 and nums[i] == current:
            i += 1

    return closestSum
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)  # Output: 2