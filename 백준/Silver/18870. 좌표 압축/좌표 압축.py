import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sort_nums = nums.copy()
sort_nums = sorted(list(set(sort_nums)))
dic_sort_nums = {sort_nums[i]: i for i in range(len(sort_nums))}

for i in range(n):
    print(dic_sort_nums[nums[i]], end=' ')