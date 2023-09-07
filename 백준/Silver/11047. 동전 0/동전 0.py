import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.sort(reverse=True)
ans = 0
for c in coins:
    if k == 0:
        break
    if k >= c:
        ans += (k//c)
        k = k%c

print(ans)