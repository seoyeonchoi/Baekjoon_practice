import sys
from itertools import combinations

def solution(n, m, a, presents):
    presents.sort()
    count = 0
    sum_list = [0] * n
    discount_sum_list = [0] * n
    sum_list[0] = presents[0]

    # 그냥 누적합
    for i in range(1, n):
        sum_list[i] = sum_list[i-1] + presents[i]

    # 할인 적용 누적합
    for i in range(n):
        if i < a:
            discount_sum_list[i] = sum_list[i] * 0.5
        else:
            discount_sum_list[i] = sum_list[i-a] + (sum_list[i] - sum_list[i-a]) * 0.5
        if discount_sum_list[i] <= m:
            count += 1

    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m, a = map(int, input().split())
    presents = list(map(int, input().split()))
    solution(n, m, a, presents)