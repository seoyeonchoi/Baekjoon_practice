import sys
import math
from collections import deque

input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
s, e = map(int, input().split())

dp = [math.inf] * (n + 1)
queue = deque()
queue.append(s)
dp[s] = 0

while queue:
    temp = queue.popleft()
    # 왼쪽 순회
    i = 0
    while temp - (nums[temp] * i) > 0:
        dp[temp - (nums[temp] * i)] = min(dp[temp - (nums[temp] * i)], dp[temp] + 1)
        if temp - (nums[temp] * i) == e:
            print(dp[e])
            exit()
        else:
            if temp != temp - (nums[temp] * i):
                queue.append(temp - (nums[temp] * i))
            i += 1
    # 오른쪽 순회
    i = 0
    while temp + (nums[temp] * i) <= n:
        dp[temp + (nums[temp] * i)] = min(dp[temp + (nums[temp] * i)], dp[temp] + 1)
        if temp + (nums[temp] * i) == e:
            print(dp[e])
            exit()
        else:
            if temp != temp - (nums[temp] * i):
                queue.append(temp + (nums[temp] * i))
            i += 1
print(-1)

