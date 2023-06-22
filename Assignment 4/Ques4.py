'''Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.
Input: nums = [1,4,3,2]
Output: 4'''

def array_pair_sum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum
nums = [1, 4, 3, 2]

result = array_pair_sum(nums)
print(result)