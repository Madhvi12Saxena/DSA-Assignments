'''An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.
Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].'''

from collections import Counter

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # If the length is odd, it can't be a doubled array

    counts = Counter(changed)  # Count the occurrences of each element
    sorted_changed = sorted(changed)  # Sort the changed array

    original = []
    for num in sorted_changed:
        if counts[num] == 0:
            continue

        counts[num] -= 1
        counts[2 * num] -= 1

        if counts[2 * num] < 0:
            return []  

        original.append(num)

    if len(original) == len(changed) // 2:
        return original
    else:
        return [] 

# Example :
changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)