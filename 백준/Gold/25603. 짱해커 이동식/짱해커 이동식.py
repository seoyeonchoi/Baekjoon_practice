import sys

input = sys.stdin.readline

n, k = map(int, input().split())
costs = list(map(int, input().split()))

max_cost = 0
idx = 0

while idx + k <= n:
    # 연속된 k개의 의뢰 중 최소비용의 의뢰 택하기
    check = min(costs[idx: idx+k])

    # 택한 의뢰를 기준으로 idx 갱신
    for i in range(k-1, -1, -1):
        if costs[idx + i] == check:
            idx += i + 1
            break

    # 택한 의뢰 비용이 현재의 최대 의뢰비용보다 크면 최대 의뢰비용 갱신
    if check > max_cost:
        max_cost = check


# 동식이가 수락한 의뢰들이 가진 비용 중 가장 높은 비용 출력
print(max_cost)

