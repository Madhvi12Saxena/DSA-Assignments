'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".'''

def processString(s):
    stack = []
    for c in s:
        if c != '#':
            stack.append(c)
        elif stack:
            stack.pop()
    return ''.join(stack)

def backspaceCompare(s, t):
    processed_s = processString(s)
    processed_t = processString(t)
    return processed_s == processed_t
s = "ab#c"
t = "ad#c"
are_equal = backspaceCompare(s, t)

print(f"Are Equal: {are_equal}")