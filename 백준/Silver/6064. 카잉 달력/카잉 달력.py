import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    max_kaing = math.lcm(m, n)  # 마지막 해는 두 수의 최소 공배수

    check = x

    # 마지막 해를 출력하는 경우
    if m == x and n == y:
        print(max_kaing)
    else:
        # 못 만들 경우 -1 출력
        ans = -1

        while True:
            if check >= max_kaing:
                break
            elif n == y and check % n == 0:
                ans = check
                break
            elif check % n == y:
                ans = check
                break
            check += m

        print(ans)

