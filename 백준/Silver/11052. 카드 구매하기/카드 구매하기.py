# 11052

n = int(input())
array = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    dp_list = [array[i]]
    
    for k in range(1, i//2+1):
        dp_list.append(dp[k]+dp[i-k])
  
    dp[i] = max(dp_list)

print(dp[n])