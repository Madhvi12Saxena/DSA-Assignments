'''Given two integer arrays arr1 and arr2, and the integer d, *return the distance value between the two arrays*.
The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2'''

def findDistanceValue(arr1, arr2, d):
    distance_value = 0
    
    for num1 in arr1:
        is_valid = True
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                is_valid = False
                break
        
        if is_valid:
            distance_value += 1
    
    return distance_value
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
output = findDistanceValue(arr1, arr2, d)
print(output)