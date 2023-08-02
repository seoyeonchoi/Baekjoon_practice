import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [n+1] * n
dp[0] = 0

for i in range(n):
    for j in range(1, nums[i] + 1):
        if i + j >= n:
            break
        else:
            dp[i+j] = min(dp[i+j], dp[i] + 1)

print(dp[n-1]) if dp[n-1] != n+1 else print(-1)