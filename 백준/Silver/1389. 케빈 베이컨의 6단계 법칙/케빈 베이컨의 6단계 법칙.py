import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friend = [[math.inf for _ in range(n+1) ] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a][b] = 1
    friend[b][a] = 1

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    friend[a][a] = 0

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            friend[a][b] = min(friend[a][b], friend[a][k] + friend[k][b])

# 수행된 결과로 케빈 베이컨 거리 계산
min_kevin = math.inf
for a in range(1, n+1):
    if sum(friend[a][1:]) < min_kevin:
        min_kevin = sum(friend[a][1:])
        min_kevin_idx = a

print(min_kevin_idx)