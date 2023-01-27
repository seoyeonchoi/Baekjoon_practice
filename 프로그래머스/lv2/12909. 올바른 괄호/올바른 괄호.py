def solution(s):
    stack = []
    answer = True
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif (s[i] == ')') and (len(stack) > 0) and (stack[-1] == '('):
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack) > 0:
        answer = False            
    return answer