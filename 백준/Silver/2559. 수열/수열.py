# 백준 2559
n, k = map(int, input().split())
nums = list(map(int, input().split()))

end = 0
first_n = 0
for i in range(k):
    first_n += nums[i]
max_n = first_n
current_n = 0

for i in range(len(nums)):
    current_n += nums[i]
    if i - end == k - 1:
        if current_n > max_n:
            max_n = current_n
        current_n -= nums[end]
        end += 1

print(max_n)