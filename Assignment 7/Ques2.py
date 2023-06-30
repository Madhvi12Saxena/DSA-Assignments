'''Given a string num which represents an integer, return true if num is a **strobogrammatic number**.
A *strobogrammatic number* is a number that looks the same when rotated 180 degrees (looked at upside down).
Input: num = "69"
Output: true'''

def isStrobogrammatic(num):
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in mapping or num[right] != mapping[num[left]]:
            return False

        left += 1
        right -= 1

    return True
num = "69"
is_strobogrammatic = isStrobogrammatic(num)

print(f"Is Strobogrammatic: {is_strobogrammatic}")