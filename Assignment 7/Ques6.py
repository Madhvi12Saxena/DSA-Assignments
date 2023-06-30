'''Given two strings s and goal, return true if and only if s can become goal after some number of **shifts* on* s.
A *shift* on s consists of moving the leftmost character of s to the rightmost position.
- For example, if s = "abcde", then it will be "bcdea" after one shift.
Input: s = "abcde", goal = "cdeab"
Output: true'''

def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s_double = s + s
    return goal in s_double
s = "abcde"
goal = "cdeab"
can_rotate = rotateString(s, goal)

print(f"Can Rotate: {can_rotate}")