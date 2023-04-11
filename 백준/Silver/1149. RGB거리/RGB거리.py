# 1149
n = int(input())
array = []

for i in range(n):
    a = list(map(int, input().split()))
    array.append(a)

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = array[0]

for i in range(1, n):
    for k in range(3):
        if k == 0:
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + array[i][0]
        if k == 1:
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + array[i][1]
        if k == 2:
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + array[i][2]

print(min(dp[n-1]))