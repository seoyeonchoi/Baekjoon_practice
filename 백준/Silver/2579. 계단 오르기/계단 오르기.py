# 2579

n = int(input())
array = []
dp = [0] * n

for i in range(n):
    a = int(input())
    array.append(a)
    
for i in range(n):
    if i == 0:
        dp[0] = array[0]
    elif i == 1:
        dp[1] = array[0] + array[1]
    elif i == 2:
        dp[2] = max(array[0]+array[2], array[1]+array[2])
    else:
        dp[i] = max(dp[i-3]+array[i-1]+array[i], dp[i-2]+array[i])

print(dp[n-1])