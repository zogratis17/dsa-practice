def isValidParenthesis(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0

s = "(()())"
print(isValidParenthesis(s))