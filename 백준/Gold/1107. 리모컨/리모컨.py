import math
import sys

input = sys.stdin.readline


def plus_check(num, broken_list):
    is_find = False
    origin_num = num
    while not is_find:
        # 100번에서 +, - 버튼 누르는 게 더 효율적인 경우 break
        if abs(num - origin_num) > abs(100 - origin_num):
            return math.inf

        for each in str(num):
            if each in broken_list:
                num += 1
                is_find = False
                break
            else:
                is_find = True
    return len(str(num)) + (num - origin_num)


def minus_check(num, broken_list):
    is_find = False
    origin_num = num
    while not is_find:
        # 더 이상 갱신이 안되는 경우 break
        if num < 0:
            return math.inf

        for each in str(num):
            if each in broken_list:
                num -= 1
                is_find = False
                break
            else:
                is_find = True
    return len(str(num)) + (origin_num - num)



n = int(input())
num_of_broken_btn = int(input())
if n == 100:  # 시작이 목적지인 경우
    print(0)
elif num_of_broken_btn > 0:
    if num_of_broken_btn == 10:  # 다 고장난 경우
        print(abs(100 - n))
    else:
        broken_btn = list(input())
        print(min(plus_check(n, broken_btn), minus_check(n, broken_btn), abs(100 - n)))
else:  # 고장난 버튼이 없는 경우
    print(min(len(str(n)), abs(100 - n)))
