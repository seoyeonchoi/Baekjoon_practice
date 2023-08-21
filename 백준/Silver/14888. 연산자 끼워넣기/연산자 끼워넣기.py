import math
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
min_cal, max_cal = math.inf, -math.inf


def backtracking(pl, mi, mu, di, idx, cur_cal):
    global min_cal, max_cal

    if idx == n:  # 모든 숫자를 처리한 경우
        min_cal = min(min_cal, cur_cal)
        max_cal = max(max_cal, cur_cal)
        return

    # 가능한 모든 연산자를 시도
    if pl > 0:
        backtracking(pl - 1, mi, mu, di, idx + 1, cur_cal + nums[idx])
    if mi > 0:
        backtracking(pl, mi - 1, mu, di, idx + 1, cur_cal - nums[idx])
    if mu > 0:
        backtracking(pl, mi, mu - 1, di, idx + 1, cur_cal * nums[idx])
    if di > 0:
        backtracking(pl, mi, mu, di - 1, idx + 1, int(cur_cal / nums[idx]))


backtracking(plus, minus, multi, div, 1, nums[0])
print(max_cal)
print(min_cal)