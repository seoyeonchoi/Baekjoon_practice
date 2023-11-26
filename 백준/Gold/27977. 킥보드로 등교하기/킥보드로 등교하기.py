import sys

def solution(l, n, k, charging_stations):
    #이분탐색
    left, right = 0, l
    while left <= right:
        mid = (left + right) // 2
        cnt, fuel, step, idx = 0, mid, 0, 0
        while fuel > 0:
            step += 1
            fuel -= 1  # 한 칸 이동, 연료 감소
            # 만약 해당 step에 충전소가 있으면
            if step == charging_stations[idx]:
                # 마지막 충전소는 충전 가능하면 하기
                if idx == (n-1):
                    if cnt < k:
                        fuel = mid
                        cnt += 1
                    else:
                        continue
                # 그 외 충전소는 현재 연료에서 다음 충전소까지 충전 없이 이동 가능하다면 pass
                elif step + fuel >= charging_stations[idx + 1]:
                    idx += 1
                else:
                    # 아닌 경우, 충전 가능하면 충전 후 이동 지속
                    if cnt < k:
                        fuel = mid
                        cnt += 1
                        idx += 1
                    # 충전 불가하면 최대 거리까지만 이동 후 break 되는 것

        if step < l:
            left = mid + 1
        else:
            right = mid - 1
    print(left)


if __name__ == "__main__":
    input = sys.stdin.readline
    l, n, k = map(int, input().split())
    charging_stations = list(map(int, input().split()))
    solution(l, n, k, charging_stations)