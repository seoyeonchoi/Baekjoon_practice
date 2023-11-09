import sys
from collections import defaultdict

def solution(a, b):
    check_dict = defaultdict(int)
    flow = 0
    origin_a, origin_b = a, b
    # a 수로 콜라스 추측
    check_dict[a] = 0
    while a != 1:
        flow += 1
        if a % 2:
            a = (a*3) + 1
        else:
            a = a // 2
        check_dict[int(a)] = flow

    flow = 0
    if origin_a != origin_b and b not in check_dict.keys():
        # print('flow 실행', check_dict.keys(), b)
        # b로 콜라스 추측
        while b != 1:
            flow += 1
            if b % 2:
                b = (b*3) +1
            else:
                b = b // 2
            if (check_dict[b] > 0) or b == origin_a:
                break
            else:
                continue

    print(origin_a, 'needs', check_dict[b], 'steps,', origin_b, 'needs', flow, 'steps, they meet at', int(b))


if __name__ == "__main__":
    input = sys.stdin.readline
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        else:
            solution(a, b)