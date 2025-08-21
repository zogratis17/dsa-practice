def infix_to_postfix(expression):

    stack = [] 
    Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = '' 
    for c in expression:
        if c.isalnum():
            output += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()
        elif c in Priority:
            while stack and stack[-1] != '(' and Priority.get(stack[-1], 0) >= Priority[c]:
                output += stack.pop()
            stack.append(c)
    while stack:
        output += stack.pop()
    return output

s = "a+b*(c^d-e)^(f+g*h)-i"
print('Infix Notation:', s)
print('Postfix Notation:', infix_to_postfix(s))