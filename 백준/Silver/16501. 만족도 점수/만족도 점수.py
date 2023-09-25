import sys
from itertools import permutations


def satisfaction(a, b, c, d):
    return 1 - abs(((a + b) / 2 - (c + d) / 2) / 10)

input = sys.stdin.readline

scores = list(map(int, input().split()))

# 가능한 모든 팀 조합을 생성
perms = list(permutations(scores))

max_satisfaction = 0

# 각 팀 조합에 대해 만족도를 계산
for perm in perms:
    team1_satisfaction = satisfaction(perm[0], perm[1], perm[2], perm[3])
    team2_satisfaction = satisfaction(perm[4], perm[5], perm[6], perm[7])

    # 두 경기에서 가장 낮은 만족도가 현재 최대 만족도보다 높으면 업데이트
    min_satisfaction = min(team1_satisfaction, team2_satisfaction)

    if min_satisfaction > max_satisfaction:
        max_satisfaction = min_satisfaction

print(round(max_satisfaction, 2))