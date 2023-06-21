def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    quadruplets = []

    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue

        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            left = b + 1
            right = n - 1

            while left < right:
                currentSum = nums[a] + nums[b] + nums[left] + nums[right]

                if currentSum == target:
                    quadruplets.append([nums[a], nums[b], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]