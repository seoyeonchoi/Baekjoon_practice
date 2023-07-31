import sys

input = sys.stdin.readline

parenthesis = list(input())
stack = []
ans = 0

for i in range(len(parenthesis)):
    if parenthesis[i] == '(':
        stack.append(parenthesis[i])
    if parenthesis[i] == ')':
        if parenthesis[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1


print(ans)
