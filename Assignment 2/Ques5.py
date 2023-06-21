def maximumProduct(nums):
    nums.sort()
    max_product_1 = nums[-1] * nums[-2] * nums[-3]
    max_product_2 = nums[0] * nums[1] * nums[-1]
    return max(max_product_1, max_product_2)
nums = [1, 2, 3]
print(maximumProduct(nums))