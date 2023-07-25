import math
import sys

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
INF = math.inf

max_dp = [[0, 0, 0], [0, 0, 0]]
max_dp[0] = array[0].copy()

min_dp = [[INF, INF, INF], [INF, INF, INF]]
min_dp[0] = array[0].copy()


for i in range(1, n):
    for k in range(3):
        if i%2:
            if k == 0:
                max_dp[1][k] = max(max_dp[0][0], max_dp[0][1]) + array[i][k]
                min_dp[1][k] = min(min_dp[0][0], min_dp[0][1]) + array[i][k]
            elif k == 1:
                max_dp[1][k] = max(max_dp[0]) + array[i][k]
                min_dp[1][k] = min(min_dp[0]) + array[i][k]
            else:
                max_dp[1][k] = max(max_dp[0][1], max_dp[0][2]) + array[i][k]
                min_dp[1][k] = min(min_dp[0][1], min_dp[0][2]) + array[i][k]
        else:
            if k == 0:
                max_dp[0][k] = max(max_dp[1][0], max_dp[1][1]) + array[i][k]
                min_dp[0][k] = min(min_dp[1][0], min_dp[1][1]) + array[i][k]
            elif k == 1:
                max_dp[0][k] = max(max_dp[1]) + array[i][k]
                min_dp[0][k] = min(min_dp[1]) + array[i][k]
            else:
                max_dp[0][k] = max(max_dp[1][1], max_dp[1][2]) + array[i][k]
                min_dp[0][k] = min(min_dp[1][1], min_dp[1][2]) + array[i][k]

if n%2:
    print(max(max_dp[0]))
    print(min(min_dp[0]))
else:
    print(max(max_dp[1]))
    print(min(min_dp[1]))