n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0

a = 0
b = n - 1

if n <= 1:
    print(0)
else:
    while a < b :
        if nums[a] + nums[b] > m:
            cnt += 1
            a += 1
            b -= 1
        else:
            a += 1
    print(cnt)  