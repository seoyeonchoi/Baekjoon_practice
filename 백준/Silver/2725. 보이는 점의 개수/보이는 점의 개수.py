import sys, math

input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 3

for x in range(2, 1001):
    count = 0
    for y in range(1, x):
        if math.gcd(x, y) == 1:
            count += 1

    dp[x] = dp[x-1] + count * 2 # x, y 반대의 경우도 가능해서 그런 것으로 추정

for _ in range(int(input())):
    print(dp[int(input())])