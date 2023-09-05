import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    each = list(input().rstrip())
    stack = []
    for e in each:
        if e == '(':
            stack.append(e)
        elif e == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(e)
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')