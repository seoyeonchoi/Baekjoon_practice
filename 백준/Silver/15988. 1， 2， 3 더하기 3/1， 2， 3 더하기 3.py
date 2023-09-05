import sys

input = sys.stdin.readline

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1_000_001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1_000_000_009

for _ in range(int(input())):
    print(dp[int(input())])