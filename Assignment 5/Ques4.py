'''Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*
- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.
**Note** that the integers in the lists may be returned in **any** order.
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]'''


def findDisjoint(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    distinct_nums1 = list(set1 - set2)
    distinct_nums2 = list(set2 - set1)
    
    return [distinct_nums1, distinct_nums2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
output = findDisjoint(nums1, nums2)
print(output)