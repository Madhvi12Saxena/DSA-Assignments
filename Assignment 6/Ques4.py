'''Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.
Input: nums = [0,1]
Output: 2
Explanation:[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.'''

def findMaxLength(nums):
    sums = {0: -1}
    max_length = 0
    current_sum = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            current_sum -= 1
        else:
            current_sum += 1

        if current_sum in sums:
            subarray_length = i - sums[current_sum]
            max_length = max(max_length, subarray_length)
        else:
            sums[current_sum] = i

    return max_length
nums = [0, 1]
max_length = findMaxLength(nums)
print(max_length)