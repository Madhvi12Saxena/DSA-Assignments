'''The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).
- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.
Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
Output: 40
Explanation:We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.'''

def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    product_sum = 0

    for num1, num2 in zip(nums1, nums2):
        product_sum += num1 * num2

    return product_sum
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
min_product_sum = minProductSum(nums1, nums2)
print(min_product_sum)