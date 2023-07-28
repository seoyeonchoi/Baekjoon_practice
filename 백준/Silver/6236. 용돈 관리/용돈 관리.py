import sys

input = sys.stdin.readline

n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

L = max(money)
R = sum(money)

while L <= R:
    Mid = (L + R) // 2
    current = Mid
    cnt = 1
    for each in money:
        if each <= current:
            current -= each
        else:
            cnt += 1
            current = Mid - each

    if cnt > m:
        L = Mid + 1
    else:
        R = Mid - 1

print(L)
