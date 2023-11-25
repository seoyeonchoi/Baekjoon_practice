import math
import sys


def solution(n):
    answer = 0
    if n < 6:
        ans_list = [[math.inf, 0] for _ in range(7)]
    else:
        ans_list = [[math.inf, 0] for _ in range(n+1)]

    ans_list[2] = [1, 1]
    ans_list[3] = [2, 2]
    ans_list[4] = [2, 2]
    ans_list[5] = [3, 3]

    if n >= 6:
        for i in range(6, n+1):
            k = 2
            while k <= (i//2):
                if i % k == 0:
                    each_min = ans_list[k][0] * (i//k)
                    each_max = ans_list[k][1] * (i//k)
                else:
                    each_min = ans_list[k][0] + ans_list[i - k][0]
                    each_max = ans_list[k][1] + ans_list[i - k][1]

                ans_list[i][0] = min(ans_list[i][0], each_min)
                ans_list[i][1] = max(ans_list[i][1], each_max)
                k += 1

    print(ans_list[n][0], ans_list[n][1])


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    solution(n)