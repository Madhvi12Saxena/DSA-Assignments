'''Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.
The following rules define a **valid** string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
Input: s = "()"
Output:true'''

def checkValidString(s):
    stack = []

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif stack and stack[-1] == '*':
                stack.pop()
            else:
                return False

    while stack:
        if stack[-1] == '(':
            return False
        stack.pop()

    return True
s = "()"
result = checkValidString(s)
print(result)