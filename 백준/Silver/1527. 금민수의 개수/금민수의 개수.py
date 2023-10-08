import sys

input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 0
len_a = len(str(a))
len_b = len(str(b))


def backtracking(num, length):
    global cnt
    if len(num) == length:
        if a <= int(''.join(map(str, num))) <= b:
            cnt += 1
        return

    for each in [4, 7]:
        num.append(each)
        backtracking(num, length)
        num.pop()


for i in range(len_a, len_b + 1):
    backtracking([], i)

print(cnt)
