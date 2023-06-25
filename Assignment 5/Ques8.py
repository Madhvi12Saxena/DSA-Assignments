'''An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.
Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]'''

from collections import defaultdict

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # Return empty array if the length is odd

    count = defaultdict(int)
    for num in changed:
        count[num] += 1
    
    original = []
    for num in changed:
        if count[num] == 0:
            continue
        
        if count[num * 2] == 0:
            return []  # Return empty array if num * 2 is not present
        
        original.append(num)
        count[num] -= 1
        count[num * 2] -= 1
    
    return original
changed = [1, 3, 4, 2, 6, 8]
output = findOriginalArray(changed)
print(output)