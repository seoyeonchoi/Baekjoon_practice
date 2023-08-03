import sys

input = sys.stdin.readline

num = list(input().rstrip())

stack = []
max_ans = ''
min_ans = ''

for n in num:
    stack.append(n)
    if n == 'K':
        if len(stack) > 1:
            max_ans += '5' + ('0' * (len(stack) - 1))
            min_ans += '1' + ('0' * (len(stack) - 2)) + '5'
        else:
            max_ans += '5'
            min_ans += '5'
        stack = []

if len(stack) > 0:
    max_ans += '1' * (len(stack))
    min_ans += '1' + ('0' * (len(stack) - 1))

print(max_ans)
print(min_ans)
