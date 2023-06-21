def minimumScore(nums, k):
    minimum = min(nums)
    maximum = max(nums)
    
    if maximum - minimum <= 2 * k:
        return 0
    
    return maximum - k - (minimum + k)
nums = [1]
k = 0
print(minimumScore(nums, k))