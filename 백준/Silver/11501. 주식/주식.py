import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):

    n = int(input())
    nums = list(map(int, input().split()))

    max_n = 0
    profit = 0

    for each in nums[::-1]:
        if each > max_n:
            max_n = each
        else:
            profit += (max_n - each)

    print(profit)
