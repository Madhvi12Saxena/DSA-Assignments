'''Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.'''

def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    diff_indices = []
    diff_chars = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_indices.append(i)
            diff_chars.append(s[i])

    if len(diff_indices) != 2:
        return False

    if s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]:
        return True

    return False
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)