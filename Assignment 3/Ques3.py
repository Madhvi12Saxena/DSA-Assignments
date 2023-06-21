def nextPermutation(nums):
    # Find the first pair of consecutive elements where nums[i] < nums[i+1]
    firstIndex = -1
    n = len(nums)
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            firstIndex = i
            break

    if firstIndex == -1:
        # If no such pair is found, reverse the entire array
        nums.reverse()
        return nums

    # Find the first element greater than nums[firstIndex]
    secondIndex = -1
    for i in range(n - 1, firstIndex, -1):
        if nums[i] > nums[firstIndex]:
            secondIndex = i
            break

    # Swap nums[firstIndex] with nums[secondIndex]
    nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]

    # Reverse the subarray starting from nums[firstIndex+1]
    left = firstIndex + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
nums = [1, 2, 3]
result = nextPermutation(nums)
print(result)  # Output: [1, 3, 2]