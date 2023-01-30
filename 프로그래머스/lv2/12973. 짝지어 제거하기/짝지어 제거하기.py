def solution(s):
    answer = -1
    stack = []
    
    for i in range(len(s)):
        if (len(stack)>0) and (s[i] == stack[-1]):
            stack.pop()
        else:
            stack.append(s[i])
    
    answer = 1 if (len(stack) == 0) else 0
    return answer