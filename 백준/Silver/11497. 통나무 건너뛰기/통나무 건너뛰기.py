import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    max_minus = 0
    idx = 0
    while idx < n - 1:
        # print(idx)
        if idx == n - 2:
            if max_minus < nums[idx] - nums[idx + 1]:
                max_minus = nums[idx] - nums[idx + 1]
        elif idx == 0:
            if max_minus < nums[0] - nums[1]:
                max_minus = nums[0] - nums[1]
            if max_minus < nums[0] - nums[2]:
                max_minus = nums[0] - nums[2]
        else:
            if max_minus < nums[idx] - nums[idx + 2]:
                max_minus = nums[idx] - nums[idx + 2]

        idx += 1
    print(max_minus)